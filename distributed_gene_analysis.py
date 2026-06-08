# Import necessary libraries for MPI and data processing
from mpi4py import MPI
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Initialize MPI communication
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Rank 0 loads the breast cancer dataset and broadcasts it to other nodes
if rank == 0:
    # UPDATED: Using the correct Breast Cancer dataset
    df = pd.read_csv("breast_cancer_data.csv")
    data = df.iloc[:, :-1].values
    target = df.iloc[:, -1].values
else:
    data = None
    target = None

data = comm.bcast(data, root=0)
target = comm.bcast(target, root=0)

# Divide the data into chunks for parallel processing
chunk_size = len(data) // size
start = rank * chunk_size
end = start + chunk_size if rank != size - 1 else len(data)
local_data = data[start:end]
local_target = target[start:end]

# Train the Random Forest model locally on each worker node
clf = RandomForestClassifier(n_estimators=100)
clf.fit(local_data, local_target)

# Gather accuracy scores from all workers to the master node
local_score = clf.score(local_data, local_target)
scores = comm.gather(local_score, root=0)

# Master node prints the final results
if rank == 0:
    print("Bioinformatics scores from all nodes:", scores)
    print("Average score:", np.mean(scores))

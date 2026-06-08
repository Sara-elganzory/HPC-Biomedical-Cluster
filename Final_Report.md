# Final Report: Hybrid HPC-Big Data Clusters
## Introduction
The project aimed to establish a high-performance cluster to perform distributed gene expression classification for leukemia types.

## Methodology
- **HPC Task:** Distributed Random Forest training using MPI across 3 nodes.
- **Big Data Task:** Containerized Spark deployment using Docker Swarm to process transcriptomic datasets.

## Results
- **MPI Accuracy:** 1.0 (Average across nodes).
- **Spark Accuracy:** 0.98 (Test data).

## Conclusion
The project successfully demonstrated the efficiency of distributed computing for bioinformatics workloads, contrasting traditional HPC approaches with modern containerized orchestration.

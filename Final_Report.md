# Final Report: Hybrid HPC-Big Data Clusters
## Introduction
The project aimed to establish a high-performance cluster to perform distributed gene expression classification for leukemia types.

## Methodology
- **HPC Task:** Distributed Random Forest training using MPI across 3 nodes.
- **Big Data Task:** Containerized Spark deployment using Docker Swarm to process transcriptomic datasets.

## Results
- **MPI Performance:** Achieved consistent average score of 1.0 across cluster nodes.
- **Spark Performance:** Validated accuracy of 0.98 on distributed datasets.
- **Execution Duration:** The containerized Apache Spark job successfully completed the distributed workload in 18 seconds.

## Conclusion
The project successfully demonstrated the efficiency of distributed computing for bioinformatics workloads, contrasting traditional HPC approaches with modern containerized orchestration.

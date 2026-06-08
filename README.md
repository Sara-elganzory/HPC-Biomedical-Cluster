# Project: Hybrid HPC & Big Data Cluster
**Course:** High Performance Computing

## Overview
This repository contains the configuration, documentation, and source code for a distributed bioinformatics machine learning cluster. The project demonstrates the implementation of both traditional HPC architectures and modern Big Data orchestration.

## Environment Details
- **Architecture:** 3-node cluster (1 Master, 2 Workers) running on Ubuntu Server 20.04 (VirtualBox).
- **Networking:** Static IP assignment (192.168.56.10, .11, .12) configured via Netplan.
- **Task 1 (Mini-HPC):** Traditional distributed computing setup using OpenMPI and Scikit-Learn.
- **Task 2 (Big Data):** Containerized cluster orchestration using Docker Swarm and Apache Spark.

## Repository Structure
- `distributed_gene_analysis.py`: MPI-based gene expression classifier.
- `distributed_gene_expression_analysis.py`: PySpark-based gene expression classifier.
- `hostfile`: Node configuration for MPI.
- `spark-stack.yml`: Docker Compose file for Spark deployment.
- `/bioinfo_data/`: Contains `breast_cancer_data.csv` (Dataset).
- `/screenshots/`: Evidence of network verification, MPI execution, Docker node readiness, and Spark job completion.
- `Final_Report.md`: Detailed methodology and results analysis.
- `setup_log.txt`: Comprehensive log of terminal commands and troubleshooting steps.

## Results Summary
- **MPI Performance:** Achieved consistent average score of 1.0 across cluster nodes.
- **Spark Performance:** Validated accuracy of 0.98 on distributed datasets.
- **Execution Duration:** The containerized Apache Spark job successfully completed the distributed workload in 18 seconds.

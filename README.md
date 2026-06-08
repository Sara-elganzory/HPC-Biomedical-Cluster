# Project: Hybrid HPC & Big Data Cluster
**Course:** High Performance Computing

## Overview
This repository contains the configuration, documentation, and source code for a distributed bioinformatics machine learning cluster. The project demonstrates the implementation of both traditional HPC architectures and modern Big Data orchestration.

## 🎥 Video Presentation
**[Click here to watch the Project Presentation Video](https://drive.google.com/file/d/1uUTxblFyYkb7Z91Jn6lURBxtw0iUIY91/view?usp=sharing)**
*(A comprehensive walkthrough of the cluster architecture, methodology, and performance results).*

## Environment Details
- **Architecture:** 3-node cluster (1 Master, 2 Workers) running on Ubuntu Server 20.04 (VirtualBox).
- **Networking:** Static IP assignment (192.168.56.x) configured via Netplan.
- **Task 1 (Mini-HPC):** Traditional distributed computing setup using OpenMPI and Scikit-Learn for breast cancer gene expression analysis.
- **Task 2 (Big Data):** Containerized cluster orchestration using Docker Swarm and Apache Spark for large-scale bioinformatics ML.

## Repository Structure
- `data/`: Contains the distributed breast cancer dataset (`breast_cancer_data.csv`).
- `distributed_gene_analysis.py`: MPI-based gene expression classifier.
- `distributed_gene_expression_analysis.py`: PySpark-based gene expression classifier.
- `hostfile`: Node configuration for MPI.
- `spark-stack.yml`: Docker Compose stack file for the Apache Spark cluster.
- `screenshots/`: Contains all visual evidence of network verification, MPI execution, Docker node readiness, and Spark job completion.
- `Final_Report.md`: Detailed methodology and results analysis.
- `setup_log.txt`: Comprehensive log of terminal commands and troubleshooting steps.

## Results Summary
- **MPI Performance:** Achieved a consistent average score of 1.0 across cluster nodes.
- **Spark Performance:** Validated an accuracy of 0.98 on distributed breast cancer datasets.
- **Execution Duration:** The containerized Apache Spark job successfully completed the distributed workload in exactly 18 seconds.

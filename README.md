# Project: Hybrid HPC & Big Data Cluster
**Course:** High Performance Computing

## Overview
This repository contains the configuration, documentation, and source code for a distributed bioinformatics machine learning cluster. The project demonstrates the implementation of both traditional HPC architectures and modern Big Data orchestration.

## Environment Details
- **Architecture:** 3-node cluster (1 Master, 2 Workers) running on Ubuntu Server 20.04 (VirtualBox).
- **Networking:** Static IP assignment (192.168.56.x) configured via Netplan.
- **Task 1 (Mini-HPC):** Traditional distributed computing setup using OpenMPI and Scikit-Learn for gene expression analysis.
- **Task 2 (Big Data):** Containerized cluster orchestration using Docker Swarm and Apache Spark for large-scale bioinformatics ML.

## Repository Structure
- `/scripts/`:
  - `distributed_gene_analysis.py`: MPI-based gene expression classifier.
  - `distributed_gene_expression_analysis.py`: PySpark-based gene expression classifier.
  - `hostfile`: Node configuration for MPI.
- `/screenshots/`:
  - Contains all evidence of network verification, MPI execution, Docker node readiness, and Spark job completion.
- `Final_Report.md`: Detailed methodology and results analysis.
- `setup_log.txt`: Comprehensive log of terminal commands and troubleshooting steps.

## Results Summary
- **MPI Performance:** Achieved consistent average score across cluster nodes for gene expression data.
- **Spark Performance:** Validated accuracy of 0.98 on distributed breast cancer datasets.

## Submission Checklist
- [x] MPI Cluster verified (SSH connectivity & execution).
- [x] Docker Swarm initialized & Spark stack deployed.
- [x] Bioinformatics datasets processed across distributed nodes.
- [x] All proof screenshots captured and documented.

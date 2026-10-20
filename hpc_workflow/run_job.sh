#!/bin/bash
# Simulasi sistem submission job pada HPC (seperti SLURM atau PBS)
# Perintah ini biasa digunakan oleh integrator untuk menjalankan program komputasi berat

echo "=========================================="
echo " SUBMITTING HPC JOB: PM2.5 DATA ANALYSIS"
echo "=========================================="
echo "Node     : LOCAL_SIMULATION"
echo "Cores    : 4"
echo "Date     : $(date)"
echo "=========================================="

# Mengeksekusi Python script dengan pustaka paralel
python parallel_process.py

echo "=========================================="
echo " JOB COMPLETED."
echo "=========================================="

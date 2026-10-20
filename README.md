# HPC & IoT Integrator System - PM2.5 Forecasting

Sistem ini didasarkan pada studi kasus dari sesi "Bridging Global Infrastructure to Address Local Challenge with HPC" oleh Dr. Worawan Diaz Carballo. Proyek ini mendemonstrasikan peran seorang **Integrator** yang menjembatani data masif dari perangkat IoT (seperti sensor lingkungan) dengan infrastruktur komputasi paralel (High Performance Computing).

Berdasarkan contoh nyata prediksi kualitas udara (PM2.5) di Thailand yang diproses dengan superkomputer, sistem ini menyimulasikan:
1. Pembuatan dataset IoT berskala besar.
2. Pemrosesan paralel menggunakan pustaka multiprocessing (sebagai simulasi arsitektur HPC/MPI) untuk menganalisis data secara efisien.
3. Eksekusi alur kerja menggunakan Shell Script (Linux bash), sesuai dengan keterampilan teknis yang dianjurkan untuk mahasiswa Informatika.

## Struktur Direktori
- `iot_data_generator/`: Script untuk mensimulasikan jutaan baris data PM2.5 dari sensor IoT.
- `hpc_workflow/`: Berisi kode pemrosesan paralel (Python) dan shell script (`.sh`) untuk menjalankan tugas.

## Cara Penggunaan
1. **Buat Data IoT Skala Besar:**
   `cd iot_data_generator`
   `python generate_pm25.py`
2. **Simulasikan Job HPC (Linux/Mac) atau Git Bash:**
   `cd ../hpc_workflow`
   `chmod +x run_job.sh`
   `./run_job.sh`

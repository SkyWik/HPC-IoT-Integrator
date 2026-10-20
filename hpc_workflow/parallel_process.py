import multiprocessing as mp
import csv
import time
import os
from collections import defaultdict

def process_chunk(chunk):
    # Simulasi perhitungan intensif komputasi / pemrosesan data historis
    region_stats = defaultdict(lambda: {'total_pm25': 0, 'count': 0, 'anomalies': 0})
    
    for row in chunk:
        region = row[2]
        pm25 = float(row[3])
        region_stats[region]['total_pm25'] += pm25
        region_stats[region]['count'] += 1
        if pm25 > 100: # Batas PM2.5 berbahaya
            region_stats[region]['anomalies'] += 1
            
    return dict(region_stats)

def parallel_analysis(filepath, num_workers=4):
    print(f"\nMemulai analisis paralel HPC dengan {num_workers} core/pekerja...")
    start_time = time.time()
    
    # Membaca data
    data = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip header
        data = list(reader)
        
    total_rows = len(data)
    print(f"Total baris diproses: {total_rows}")
    
    # Membagi beban kerja (chunking) ke beberapa prosesor
    chunk_size = total_rows // num_workers
    chunks = [data[i:i + chunk_size] for i in range(0, total_rows, chunk_size)]
    
    with mp.Pool(processes=num_workers) as pool:
        results = pool.map(process_chunk, chunks)
        
    # Agregasi hasil dari berbagai node/core
    final_stats = defaultdict(lambda: {'total_pm25': 0, 'count': 0, 'anomalies': 0})
    for res in results:
        for region, stats in res.items():
            final_stats[region]['total_pm25'] += stats['total_pm25']
            final_stats[region]['count'] += stats['count']
            final_stats[region]['anomalies'] += stats['anomalies']
            
    print(f"\nWaktu eksekusi komputasi paralel: {time.time() - start_time:.4f} detik\n")
    print("--- Laporan Analisis Kualitas Udara (PM2.5) ---")
    for region, stats in final_stats.items():
        avg_pm25 = stats['total_pm25'] / stats['count']
        print(f"Wilayah: {region}")
        print(f"  Rata-rata PM2.5: {avg_pm25:.2f}")
        print(f"  Insiden Berbahaya (>100): {stats['anomalies']} kali")
    
if __name__ == '__main__':
    data_path = '../iot_data_generator/sensor_data_pm25.csv'
    if not os.path.exists(data_path):
        print("Data tidak ditemukan! Jalankan generate_pm25.py terlebih dahulu.")
    else:
        # Simulasi menggunakan 4 CPU core
        parallel_analysis(data_path, num_workers=4)

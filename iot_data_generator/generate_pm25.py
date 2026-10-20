import csv
import random
import os
from datetime import datetime, timedelta

def generate_sensor_data(num_records=500000, filename='sensor_data_pm25.csv'):
    print(f"Mengumpulkan {num_records} data simulasi dari sensor IoT PM2.5...")
    regions = ['Bangkok', 'Chiang_Mai', 'Phuket', 'Khon_Kaen', 'Pattaya']
    
    start_time = datetime.now() - timedelta(days=30)
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'sensor_id', 'region', 'pm25_level', 'temperature'])
        
        for i in range(num_records):
            timestamp = start_time + timedelta(minutes=i * 5)
            region = random.choice(regions)
            # PM2.5 memburuk di daerah tertentu sebagai simulasi
            base_pm25 = 150 if region == 'Chiang_Mai' else 30
            pm25 = max(0, random.gauss(base_pm25, 40))
            temp = random.uniform(22.0, 38.0)
            
            writer.writerow([timestamp.strftime('%Y-%m-%d %H:%M:%S'), f"SENSOR_{random.randint(100,999)}", region, round(pm25, 2), round(temp, 2)])
    
    print(f"Data tersimpan di {filename} (Ukuran kasar: {os.path.getsize(filename) / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    # Menghasilkan 500k baris untuk simulasi big data/HPC
    generate_sensor_data(500000)

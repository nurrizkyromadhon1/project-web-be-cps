import requests

url = 'http://localhost:5000/add_data'

def read_sensor_data():
    data = {
        'api_key': 'kunci-api-anda',
        'temperature': 25.5,
        'moisture': 45.0,
        'pH': 6.8,
        'conductivity': 1.2,
        'nitrogen': 3.4,
        'phosphorus': 2.5,
        'potassium': 1.8,
        'tanaman': 'cabai',        # Tambahkan jenis tanaman
        'tanaman_no': 1            # Tambahkan nomor tanaman
    }
    return data

if __name__ == '__main__':
    data = read_sensor_data()
    response = requests.post(url, data=data)
    if response.status_code == 302 or response.status_code == 200:
        print('Data berhasil dikirim dan disimpan.')
    else:
        print(f'Terjadi kesalahan: {response.status_code} - {response.text}')

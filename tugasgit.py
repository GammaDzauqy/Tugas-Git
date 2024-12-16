data_panen = {
    'lokasi1' : {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }

}

print('\nseluruh data panen:')
for lokasi, data in data_panen.items():
    print(data['nama_lokasi'],data['hasil_panen'])


jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print('\njumlah hasil panen jagung lokasi2:', jagung_lokasi2)

nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print('\nnama lokasi3:',nama_lokasi3)

padi_hasil = {lokasi: hasil['hasil_panen']['padi'] for lokasi, hasil in data_panen.items()}
kedelai_hasil = {lokasi: hasil['hasil_panen']['kedelai'] for lokasi, hasil in data_panen.items()} 

print('\nhasil panen padi:')
for lokasi, hasil in padi_hasil.items():
    print(data_panen[lokasi]['nama_lokasi'], hasil)

print('\nhasil panen kedelai:')
for lokasi, hasil in kedelai_hasil.items():
    print(data_panen[lokasi]['nama_lokasi'], hasil)

print('\nkondisi lokasi:')
kondisi_lokasi = {}
for key, lokasi in data_panen.items():
    padi = lokasi['hasil_panen']['padi']
    jagung = lokasi['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        kondisi_lokasi[lokasi['nama_lokasi']] = 'Memerlukan perhatian khusus'
    else:
        kondisi_lokasi[lokasi['nama_lokasi']] = 'Kondisi baik'

for lokasi, kondisi in kondisi_lokasi.items():
    print(f'{lokasi}: {kondisi}')









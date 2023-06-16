# Bu programı kullanmak için, `pyspeedtest`, `speedtest` veya `speedtest-cli` adlı Python kütüphanelerinden birini yüklemeniz gerekiyor. Bu kütüphaneler, internet hızınızı test etmek için Speedtest.net API'sini kullanır.

import speedtest

test = speedtest.Speedtest()

print("Sunucu Listesi Yükleniyor...")
test.get_servers()
print("Sunucunuz Eşleştiriliyor...")
best = test.get_best_server()

print(f"Bilgiler: {best['host']} Lokasyon {best['country']}")

print("İndirme Hızı Test Ediliyor...")
download_result = test.download()
print("Yükleme Hızı Test Ediliyor...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"İndirme Hızı: {download_result / 1024 / 1024:.2f}Mbit/s")
print(f"Yükleme Hızı: {upload_result / 1024 / 1024:.2f}Mbit/s")
print(f"Ping: {ping_result}ms")
if(ping_result <= 18):
    print("Durum gayet iyi :)")
elif(ping_result>=20):
    print("Durumunuz biraz kötü...")
else:
    print("Normalin çok üstünde bir performans!")
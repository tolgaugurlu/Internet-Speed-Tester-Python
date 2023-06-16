## Internet Speed Tester

Bu bir Python programıdır ve internet bağlantınızın indirme ve yükleme hızını test etmenize olanak tanır.

Bu programı kullanmak için, `pyspeedtest`, `speedtest` veya `speedtest-cli` adlı Python kütüphanelerinden birini yüklemeniz gerekiyor. Bu kütüphaneler, internet hızınızı test etmek için Speedtest.net API'sini kullanır.

Programı çalıştırmak için, terminalde `./main.py` komutunu kullanın. Program, internet bağlantınızın indirme ve yükleme hızını test eder ve sonuçları ekrana yazdırır.

Bu program, internet bağlantınızın hızını test etmek için kullanışlı bir araçtır. Ancak, internet hızı testleri, birçok faktörden etkilenebilir ve sonuçlar değişkenlik gösterebilir. Bu nedenle, programın sonuçlarını yalnızca bir referans olarak kullanın ve internet hızınızı etkileyen diğer faktörleri de göz önünde bulundurun.

# Hepsini import etmek için "pip install -r requirements.txt" yazmanız yeterli olacaktır.

Eğer herhangi bir şekilde "Speedtest" hatası alırsanız aşağıda verdiğim komutları çalıştırarak düzeltebilirsiniz.

# pip uninstall speedtest

----- Ardından -------

# pip install speedtest-cli==2.1.3

Bu komutlar, `speedtest` modülünü kaldırır ve `speedtest-cli` paketinin 2.1.3 sürümünü yükler. Bu sürüm, `Speedtest` sınıfını içerir ve programın çalışmasını sağlar.

Bu işlemleri yaptıktan sonra, programı yeniden çalıştırın ve hatanın devam edip etmediğini kontrol edin.

### Requirements.txt

1. pip install pyspeedtest
2. pip install speedtest
3. pip install speedtest-cli

### MAC için

1. pip3 install pyspeedtest
2. pip3 install speedtest
3. pip3 install speedtest-cli

### Nasıl kullanılır? Başlatılır?

Tüm kütüphaneler import edildikten sonra aşağıdaki komutu main.py olan dizinin içinde terminale yazmanız yeterli olacaktır.

```
./main.py
```

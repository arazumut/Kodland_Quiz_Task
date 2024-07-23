![Ekran görüntüsü 2024-07-23 144529](https://github.com/user-attachments/assets/c753b809-628a-417d-9abf-9294cab3faa2)
![Ekran görüntüsü 2024-07-23 144523](https://github.com/user-attachments/assets/42e576de-02a5-44ac-a9bd-a44eab258bd6)
![Ekran görüntüsü 2024-07-23 144432](https://github.com/user-attachments/assets/bbc520ca-3d2b-41ce-bfc0-e739b492f78d)
![Ekran görüntüsü 2024-07-23 144421](https://github.com/user-attachments/assets/f0275327-8d6c-42d4-bca3-9837ded49f7f)

1. Sanal Ortam Oluşturma
Öncelikle, terminal veya komut istemcisinde projenizin dizinine gidin. Bu dizin, sanal ortamınızı ve diğer proje dosyalarınızı içerecek yerdir. Aşağıdaki komutla bir sanal ortam oluşturabilirsiniz:


python -m venv venv
Burada venv, sanal ortamınızın adı. İsterseniz farklı bir ad da verebilirsiniz.

2. Sanal Ortamı Etkinleştirme
Sanal ortamı etkinleştirmek, bağımlılıkları bu ortamda kurmak ve çalıştırmak için önemlidir. Çalışma sisteminize bağlı olarak sanal ortamı etkinleştirme adımları farklılık gösterebilir:

Windows:


venv\Scripts\activate
MacOS ve Linux:


source venv/bin/activate
Etkinleştirdiğinizde, terminal veya komut istemcisinin başında (venv) gibi bir gösterge görebilirsiniz. Bu, sanal ortamınızın aktif olduğunu belirtir.

3. Gerekli Paketleri Kurma
Sanal ortam aktifken, gerekli Python paketlerini kurabilirsiniz. Flask ve diğer bağımlılıkları yüklemek için aşağıdaki komutu kullanın:


pip install flask

4. Paketlerin Listelenmesi ve Kaydedilmesi
Sanal ortamda kurulu olan tüm paketleri bir dosyaya kaydetmek istiyorsanız, şu komutu kullanabilirsiniz:


pip freeze > requirements.txt
Bu requirements.txt dosyası, projenizin bağımlılıklarını içerir ve diğer geliştiricilerin aynı ortamı kurmasını sağlar.

5. Bağımlılıkları Yükleme
Başka biri (veya siz) projeyi klonladığında, bağımlılıkları yüklemek için requirements.txt dosyasını kullanabilirsiniz:


pip install -r requirements.txt
6. Sanal Ortamı Devre Dışı Bırakma
Sanal ortamı kapatmak için, terminal veya komut istemcisinde şu komutu kullanabilirsiniz:


deactivate
Bu komut, sanal ortamdan çıkmanızı sağlar ve sistem genelindeki Python yüklemesine geri dönersiniz.

Özet
Sanal ortam oluşturun:


python -m venv venv
Sanal ortamı etkinleştirin:

Windows: venv\Scripts\activate
MacOS/Linux: source venv/bin/activate
Gerekli paketleri kurun:


pip install flask
Paketleri kaydedin:


pip freeze > requirements.txt
Bağımlılıkları yükleyin (başka birinde):


pip install -r requirements.txt
Sanal ortamı kapatın:


deactivate

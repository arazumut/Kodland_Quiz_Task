  <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> 
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> 
   </a> 
   <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> 
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> 
   </a> 
   <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
    </a> 
Quiz App With Flask

Veritabanının geliştiricinin elinde olduğu flask application
    ![Ekran görüntüsü 2024-07-23 144432](https://github.com/user-attachments/assets/bbc520ca-3d2b-41ce-bfc0-e739b492f78d)
    ![Ekran görüntüsü 2024-07-23 144421](https://github.com/user-attachments/assets/f0275327-8d6c-42d4-bca3-9837ded49f7f)

1. Soru ve Cevap Yönetimi
Soruları Depolama: Uygulama, genellikle soruları ve bu sorulara karşılık gelen cevap seçeneklerini veritabanında saklar.
Cevapları Kontrol Etme: Kullanıcıların seçtiği cevapları doğru cevaplarla karşılaştırır ve sonuçları hesaplar. <br>
![Ekran görüntüsü 2024-07-23 144529](https://github.com/user-attachments/assets/c753b809-628a-417d-9abf-9294cab3faa2)
![Ekran görüntüsü 2024-07-23 144523](https://github.com/user-attachments/assets/42e576de-02a5-44ac-a9bd-a44eab258bd6)
3. Kullanıcı Etkileşimi
Soru Gösterimi: Kullanıcıya soruları ve seçenekleri sunar.
Sonuçları Gösterme: Kullanıcının doğru cevaplarını ve toplam puanını gösterir.
5. Veritabanı İşlemleri
Soru Listesi Alma: Soru ve cevapları veritabanından alır ve kullanıcıya gösterir.
Sonuçları Saklama (Opsiyonel): Kullanıcıların geçmiş sonuçlarını saklar ve daha sonra analiz edebilir.
7. Flask ile Çalışma<br>
Flask, Python ile yazılmış bir mikro web çerçevesidir ve bu tür uygulamalar için web sunucusu olarak kullanılır. Bu uygulamada Flask'ın rolü şu şekildedir:
![Ekran görüntüsü 2024-07-23 144432](https://github.com/user-attachments/assets/bbc520ca-3d2b-41ce-bfc0-e739b492f78d)
![Ekran görüntüsü 2024-07-23 144421](https://github.com/user-attachments/assets/f0275327-8d6c-42d4-bca3-9837ded49f7f)
HTTP İstekleri Yönetimi: Kullanıcının tarayıcıdan gönderdiği HTTP isteklerini alır ve yanıtlar.
Şablonlar: HTML şablonları ile kullanıcı arayüzünü dinamik olarak oluşturur.
Veritabanı ile Etkileşim: SQLAlchemy gibi bir ORM kullanarak veritabanı ile etkileşimde bulunur.

1. Sanal Ortam Oluşturma
Öncelikle, terminal veya komut istemcisinde projenizin dizinine gidin. Bu dizin, sanal ortamınızı ve diğer proje dosyalarınızı içerecek yerdir. Aşağıdaki komutla bir sanal ortam oluşturabilirsiniz:
![Ekran görüntüsü 2024-07-23 142712](https://github.com/user-attachments/assets/02b0e9c1-b7d2-4218-9d75-87eca13d3c01)


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

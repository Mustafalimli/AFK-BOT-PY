# AFK-BOT-PY
Afk bot in order to bypass mouse detection softwares.

Botun Özellikleri

Bu bot, fare imlecini ekranda rastgele yerlere taşıyarak hareket ettiriyor. Yani ekranda belirli bir alan içinde rastgele noktalara gidiyor. Özellikle belirli bir işlemi sürekli aktif göstermek veya ekran koruyucuyu engellemek gibi durumlar içindir. Hareketler x ve y koordinatlarında rastgele olarak yapılıyor ve bu döngü sürekli tekrarlanıyor.

moveTo Fonksiyonunun Amacı

`pag.moveTo(x, y, 0.5)` koduyla, fareyi (x, y) noktasına 0.5 saniyede taşıyorum. `moveTo` komutu, farenin belirlenen koordinatlara gitmesini sağlıyor. Buradaki 0.5, hareketin süresini belirliyor, yani hızını ayarlıyor.
İstenilen orana göre değiştirilebilir.

time.sleep Fonksiyonunun Amacı

`time.sleep(2)` komutu, her hareket arasında 2 saniyelik bir bekleme süresi koyuyor. Böylece fare hareketleri daha doğal oluyor ve sürekli hareket etmesini engelliyorum. Bu sayede detectionlara takılma ihtimalini azaltıyorum.

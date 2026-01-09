# Kariyer Danışmanı Discord Botu

## Proje Hakkında
Bu proje, kullanıcıların ilgi alanlarına göre kendilerine uygun kariyer ve meslek önerileri alabilmesini sağlayan bir Discord botudur. Bot, kullanıcıyla etkileşim kurarak ilgi alanlarını öğrenir ve bu bilgilere göre kişiselleştirilmiş öneriler sunar.

Proje, Kodland Level 3 mezuniyet gereksinimlerine uygun olarak geliştirilmiştir ve demo sürüm niteliğindedir.

---

## Projenin Amacı
- Kullanıcıların kariyer seçenekleri hakkında farkındalık kazanmasını sağlamak  
- Kararsız kalan kullanıcılar için farklı meslek alternatifleri sunmak  
- Basit, anlaşılır ve kullanıcı dostu bir sistem oluşturmak  

---

## Botun Çalışma Mantığı
1. Kullanıcı `/basla` komutunu kullanır  
2. Bot, kullanıcıyı Discord kimliği (ID) ile tanır  
3. Kullanıcı, butonlar aracılığıyla ilgi alanını seçer  
4. Bot, veri tabanından uygun bir meslek önerir  
5. Meslek bilgisi sade ve anlaşılır bir formatta kullanıcıya sunulur  
6. Kullanıcı bilgileri kaydedilir ve sonraki kullanımlarda hatırlanır  

---

## Kişiselleştirme
Bot, her kullanıcıyı Discord ID üzerinden tanımlar.  
Kullanıcının seçtiği ilgi alanı ve son önerilen meslek saklanır.  
Bu sayede bot, tekrar gelen kullanıcılara daha önceki tercihlerini hatırlatarak kişiselleştirilmiş bir deneyim sunar.

---

## Veri Tabanı Yapısı
Projede JSON tabanlı iki farklı veri dosyası kullanılmaktadır.

### Meslek Veri Tabanı (careers.json)
Bu dosya, ilgi alanlarına göre meslek bilgilerini iç


##kullanıcıdan girdi alan ve aldığı girdileri bir veritabanına kaydeden basit bir program. program temelde bir kişisel gelişim uygulaması olarak tasarlandı. eklenecek olan birkaç özellik var bu özellikler sırasıyla:
#1. kullanıcıların günlük içtiği su miktarını kaydedip bu su miktarını görselleştirebilmesi.
#2. kullanıcıların gün içerisindeki ruh halini kaydedip bu ruh halini görselleştirebilmesi.
#3. kullanıcıların gün içerisindeki motivasyon seviyesini kaydedip bu motivasyon seviyesini görselleştirebilmesi.
#4. kullanıcıların gün içerisinde yapmayı planladıkları aktiviteleri kaydedebilmesi.
#5. kaydedilen verileri bir llm aracı ile analiz ederek gelecekte neler yapılması gerektiğini planlayabilmesi.

water_cons_metric = int(input("bugün içtiğin su miktarını bardak cinsinden giriniz: "))

daily_metrics = {
    "water consumption" : water_cons_metric
}

print(daily_metrics["water consumption"])
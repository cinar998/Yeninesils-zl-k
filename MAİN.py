meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "CYA": "Görüşürüz!",
            "K": "Okay'in kısaltılmış hali, tamam",
            "WDYM": "Neyden bahsediyorsun? demek",
            "o7": "Asker selamı olarak da bilinir",
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("kelime bulunamamıştır")

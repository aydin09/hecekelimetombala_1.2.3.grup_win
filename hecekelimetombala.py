from tkinter import *
import os
import tkinter.ttk as ttk
import random
import time

tombala=["el","le","ele","elle",
         "al","la","ala","alla","Ela","ela","Lale","lale",
         "ek","ke","ak","ka","kek","kal","kalk","kel","kale","elek","keke","kelle","kelek","elekle","ekle","leke","kekle","akla",
         "il","li","ik","ki","elli","iki","ile","ilke","İlke","Ali","eki","keki","eli","laleli","ekli","kil","killi","lila","ilk","ilik","ilikle",
         "keklik","lekeli","kekik","ikili","elekli","kekikli","ikilik","ilkel","ilkeli","Akile",
         "en","ne","an","na","in","ni","ana","Nil","anne","nane","ninni","İnan","Nalan","elin","kan","eken","kanal","kalan","kene","Alkan",
         "anla","inle","nine","inek","nal","Kenan","İnal","ilan","ekin","neli","alan","inan","lakin","kanka","enli","kalkan","enik","nakil",
         "ol","lo","ok","ko","on","no","ona","eko","kok","kol","kon","kola","kilo","konak","koli","kokla","alo","Okan","kano","ikon","nano",
         "ekol","koni","okka","olanak",
         "em","me","ma","im","mi","om","mo","mola","mani","mal","kalem","ekmek","kelime","Melek","Melike","limon","alma","Melik","kilim","mala",
         "Emin","Emine","liman","mama","keman","kalemlik","komi","minik","lokma","iklim","Kamil","Kamile","almak","elma","kemik","ama","nem","nemli",
         "Mine","mekik","Emel","kimlik","Leman","Kemal","Alim","komik","mini","maki","makine","mil","emekli","milli",
         "ul","lu","uk","ku","un","nu","um","mu","kule","onlu","kumlu","lokum","un","unlu","kul","kilolu","ulu","kolu","kollu","konu","konuk","onluk",
         "kum","mum","kukla","oku","okul","koku","Memmune","kokulu","konum","kolum","mumluk","Numan","limonlu","limonluk","kulak","okuma","kanun","ilkokul",
         "memnun","et","te","at","ta","it","ti","ot","to","ut","tu","tak","tek","tane","ton","tok","tel","taka","atla","atlet","teke","kot","Ata","Tan","Altan",
         "tekne","tulum","tonton","tut","mont","toka","kat","kutu","tat","ten","atma","tatma","Onat","etli","taneli","kent","kilit","koltuk","alt","kanat","net",
         "itme","Umut","tilki","teneke","anlat","laka","tam","not","Atakan","olta","Talat","kutla","teke","tele","omlet","Utku","Mete","Tekin","tatil","nokta",
         "etek","ül","lü","ük","kü","ün","nü","üm","mü","üt","tü","ünlü","ülke","Ümit","ütü","küme","kül","küllük","Ülkü","tünel","tül","tüm","lüle","ünlem",
         "ünite","menü","Tülin","Ünal","küt","kütük","tüt","mülk","akü","kütle","mümkün",
         "ey","ye","ay","ya","iy","yi","oy","yo","uy","yu","üy","yü","uyan","yak","yut","kay","koy","Kaya","ayak","yatak","yaya","koyu","alay","maya","Yaman",
         "yayla","naylon","Yemen","leylak","oyun","yalan","maymun","yutmak","kamyon","oyna","Kutay","yumak","yitik","yelken","Aylin","eylül","Ayla","Oktay",
         "uyku","oyna","yanak","tüy","Leyla","koyun","kaykay","kolay","yay","Konya","Antalya","Antakya","Eymen","leylek","yeni","yemin","üye","iyi","kamyonet",
         "kimyon","yün","yük","kalay","tay","Ayten","yelek","yakma","yol","Aykut","yemek","kolye","kaymak","kuyu","kayak","Oya","Tülay",
         "öl","lö","ök","kö","ön","nö","öm","mö","öt","tö","öy","yö","yön","köy","köylü","öykü","önlük","önem","önemli","kök","Önal","öteki","kötü","önlem",
         "öyle","kötülük","yöntem","atölye","yönet","yönetmen","ölü","ötme","ölme","köle","Öktem",
         "er","re","ar","ra","ir","ri","or","ro","ur","ru","ür","rü","ör","rö","nar","Rana","türlü","kemer","rüya","Meryem","armut","tekerleme","tekerlek",
         "türkü","turna","ara","iri","örtü","kare","tür","ürkek","Türkiye","yumurta","market","mimar","ikram","Onur","mantar","atari","Ömer","erik","internet",
         "korna","tamir","Turan","traktör","erken","kömür","torun","raket","orman","ortak","kertenkele","marul","terlik","mart","İlter","örnek","roket","yer",
         "mermer","Eren","İrem","ayran","orta","Mert","tarla","kar","makarna","kor","kör","kumru","ray","tur","Ertan","yar","kir","kur","koro","mor","Nur","Nuri",
         "yor","erkek","Eray","iri","karton","kural","kuru","Murat","Ömür","tanker","tarak","arka","Emre","karne","kira","korku","kurak","lira","tere","terli",
         "tören","yürek","Atatürk","ileri","litre","yirmi","makara","kara","yara","tur","arka","mera","kura","küre","rota","ürün","Türk","renk","tart","tren",
         "aktan","marka","metre","metro","roman","irmik","kartal","kamera","numara","maraton","karakol","Nuran","Tarkan","Kerem","Erkan","rol","kart","yurt",
         "Aynur","Taner","Koray","Ankara","roka","kürek","Erol",
         "ıl","lı","ık","kı","ın","nı","ım","mı","ıt","tı","ıy","yı","ır","rı","kır","kırk","altı","ırmak","tatlı","yık","yıka","atkı","tanı","tırnak","kırık",
         "tırtıl","kıyma","yırtık","yarım","martı","arı","ayı","altın","ılık","katır","takı","tırmık","yukarı","tırman","yılan","tartı","tanıt","kına","Itır",
         "mantı","Anıl","Tarık","ayır","aylık","kıl","kıt","kıy","yıl","akıl","alın","anıt","atık","kayık","kıta","yakın","Akın","kalın","katı","yalın","aralık",
         "yaralı","yatılı","kıyı","takım","yanıt","ayrı","Namık","karın","kulaklık","yıllık","anı","atlı","aynı","artı","yakıt","tanık","Alkın","tır",
         "ed","de","ad","da","id","di","od","do","ud","du","üd","dü","öd","dö","ıd","dı","dik","dut","dur","dede","Demet","dünya","diken","Dilek","kedi","düdük",
         "dantel","dümen","dinle","dol","dayı","dam","döner","Didem","yedi","doktor","dana","doy","Damla","Döndü","dürüm","dört","dolu","duman","direk","dar","dem",
         "dil","duy","dök","dal","der","din","ada","Eda","damak","demir","delik","demlik","dolma","durak","Kadir","maden","moda","nadir","Arda","damar","dikkat",
         "dudak","mide","müdür","ördek","dondurma","kardelen","kurdele","orkide","koridor","Ender","Dilara","dert","denk","dilim","Erdem","Derya","ad","adam","dama",
         "radyo","damat","dedi","nerede","mendil","kaldırım","dün","ödül","Aydın","Duru","Adem","Erdal","Önder","darı",
         "es","se","as","sa","is","si","os","so","us","su","üs","sü","ös","sö","ıs","sı","sarı","salı","sayı","Seda","Selin","Sema","tenis","Selim","say","sulu","simit",
         "sus","soru","taksi","Suna","süs","Sinan","Selma","sanmak","süslü","salatalık","mısır","sarımsak","süt","kestane","kayısı","susam","tost","uslu","askı","ıslak",
         "üst","Sadık","eski","soda","sıkı","Seren","seksek","sert","Esin","sinema","sandalye","usta","sütlü","saksı","istasyon","Samsun","Ersin","ses","sil","san","sat",
         "sel","sor","asker","masa","Osman","sakal","Mars","sandal","Melisa","sıra","istek","maske","sokak","Sıtkı","sanat","serin","sinek","süre","lastik","seramik",
         "Soner","domates","saniye","Selami","dans","lüks","Sinem","ders","sark","Kars","kurs","sırt","Aslı","Esra","Semra","Sıla","asansör","sokak","İlyas","asla",
         "yastık","elmas","kasa","saklan","nisan","sök","insan","doksan","sandık","adres","ısrar","Kasım","sön","dost","öksürük","dirsek","sönük","salon","sökük","sakin",
         "sarma","Asya","aslan","ast","Esma","esmer","Asu","esne","esnek","ıslık","iste","İsmet","saman","Selinay","son","Sümer","kas","Sami","testere","Dursun","Melis",
         "Mersin","sık","sen","Sude","sosis","sır","Yasin","kes",
         "eb","be","ab","ba","ib","bi","ob","bo","ub","bu","üb","bü","öb","bö","ıb","bı","baba","balık","balon","bardak","bal","balkon","bebek","Banu","abla","bayrak",
         "börek","Betül","Burak","boya","ayakkabı","Birol","sabun","Bekir","Ebru","bilet","Berat","Bayram","bir","birlik","akraba","akbaba","kelebek","büyük","oba","balina",
         "leblebi","balta","bant","ban","bana","besle","büyüt","ebe","ben","bekle","birlikte","biber","bas","bel","bil","boy","bay","bayan","bık","bin","bot","böl","bakla",
         "bamya","banyo","beton","berber","bıyık","bidon","bilim","boru","sabır","Sabri","bütün","badem","bakkal","banka","baston","beyin","bırak","bulut","kabak","barbunya",
         "bataklık","basketbol","beslenme","battaniye","belediye","burs","kalabalık","Berk","boks","bor","büst","Berkay","Basri","Baran","Belma","Berna","Birkan","Bora","bülbül",
         "bak","bisiklet","araba","bale","balo","bone","bina","bere","büro","obur","kibar","subay","nöbet","Buket","tabak","bordo","biblo","tablo","tebrik","sümbül","dürbün",
         "tombul","kibrit","tablet","sembol","abaküs","otobüs","elbise","biberon","kulübe","mobilya","İstanbul","Bilal","Kübra","Sibel","Buse","beste","tabure","Belkıs","Berke",
         "basit","bayat","besin","bilye","burun","böbrek","bey","lamba","Bartın","torba","beraber","Batman","but","robot","Kubat","Tibet","Berkant","Baki","batı","bakır","balerin",
         "balet","baskül","Beril","soba"]

uzun=0
def hecele():
    
    uzunluk=len(tombala)

    label1=Label(text="Kalan\n"+str(uzunluk),fg='red',font=("TTKB DikTemel Abece" ,30))
   
    label1.place(relx = 0.81, rely = 0.6)

    label1=Label(text="                                                                                                                 ",fg='blue',font=("TTKB DikTemel Abece" ,80))
    
    label1.place(relx = 0.35, rely = 0.3)
    
    hecele = []
    kelime=""
    heceToplam=""
    if len(tombala) >0:
        for i in random.sample((tombala),1):
          
            kelime+=i
            bits = ''.join(['1' if l in 'AEIİOÖUÜaeıioöuü' else '0' for l in i])
            tombala.remove(i)
           
        seperators = (('101', 1),('1001', 2),('10001', 3))

        index, cut_start_pos = 0, 0

        while index < len(bits):
            for seperator_pattern, seperator_cut_pos in seperators:
                if bits[index:].startswith(seperator_pattern):
                    hecele.append(i[cut_start_pos:index + seperator_cut_pos])

                    index += seperator_cut_pos
                    cut_start_pos = index
                    break

            index += 1

        hecele.append(i[cut_start_pos:])

        for hece in hecele:
            heceToplam+=hece+" "
            
        label1=Label(text=heceToplam+" -----> "+kelime,fg='blue',font=("TTKB DikTemel Abece" ,60))
        label1.place(relx = 0.1, rely = 0.3)     

    else:
        label1=Label(text="                                                                                        ",fg='blue',font=("TTKB DikTemel Abece" ,80))
        label1.place(relx = 0.1, rely = 0.3)
        uyari=Toplevel()
        Label(uyari,text="BİTTİ. YENİLENMESİ İÇİN BAŞTAN AL BUTONUNA BASINIZ.").pack()
        uyari.mainloop()
        
def al():
        pencere.destroy()
        os.startfile("hecekelimetombala.exe")
             
pencere=Tk()
pencere.tk_setPalette("light blue")
pencere.attributes("-fullscreen", 1)

mainframe = ttk.Frame(pencere,padding='3 3 12 12')
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight =1)
                    
label=Label(text="1. - 2. - 3. GRUP (ELAKİN - OMUTÜY - ÖRIDSB) HECE/KELİME TOMBALASI PROGRAMI",fg="red",font=("TTKB DikTemel Abece" ,25))
label.place(relx = 0.05, rely = 0.0)

label1=Label(text="",font=("TTKB DikTemel Abece" ,60))
label1.place(relx = 0.1, rely = 0.3)

buton1=Button()
buton1.config(text="SEÇ", command=hecele,width='25',bg="red",fg="white",font=("TTKB DikTemel Abece" ,16))
buton1.place(relx = 0.08, rely = 0.85)

buton2=Button()
buton2.config(text="BAŞTAN AL", command=al,width='25',bg="red",fg="white",font=("TTKB DikTemel Abece" ,16))
buton2.place(relx = 0.40, rely = 0.85)

buton=Button()
buton.config(text="ÇIKIŞ",command=pencere.destroy,width='25',bg="red",fg="white",font=('TTKB DikTemel Abece',16))
buton.place(relx = 0.74, rely = 0.85)

pencere.mainloop()


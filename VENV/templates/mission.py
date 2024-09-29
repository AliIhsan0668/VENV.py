import random,os

def yazi_tura_at():
    num = random.randint(0,1)
    if num == 0:
        return "YAZI"
    else:
        return "TURA"
    
def sifreci():
    elements = "ABCÇDEFGĞHIİJKLMNOÖPRSUÜVYZ1234567890"
    password = ""
    for i in range(8):
        password += random.choice(elements)
    return password

def mem_bul():
    resim = random.choice(mem_list)
    return resim

tekno_list = ["Bilgisayar",
              "Telefon",
              "Tablet",
              "VR Gözlük",
              "PlayStation",
              "Xbox",
              "Televizyon"]
mem_list = ["https://i.pinimg.com/736x/6b/1f/08/6b1f08b5681c3cb64881d991d4eb23c6.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPM7yK4ECmCBz7qYZx9aqprygQt0uHYgcfGw&s",
            "https://cdn.pixabay.com/photo/2023/11/24/12/06/duck-8409886_1280.png",
            "https://www.shutterstock.com/shutterstock/photos/2399929675/display_1500/stock-vector-confused-man-meme-pinup-pop-art-retro-hand-drawn-vector-illustration-comic-book-style-imitation-2399929675.jpg"]
from flask import Flask
import random , os
from mission import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    html_code = "<h1>Hello World!</h1>"
    html_code += "<a href='/rastgele'>Rastgele Bir Teknolojik Cihaz Görüntüle</a>"
    html_code += "<br><a href='/yazi_tura'>Yazı-tura at.<a/>"
    html_code += "<br><a href='/sifre'>8 Haneli Şifre Oluştur.<a/>"
    html_code += "<br><a href='/meme'>Rastgele Meme Bul.<a/>"
    return html_code

@app.route("/rastgele")
def tekno_esya():
    html_code = "<h1>Rastgele Teknolojik Cihaz:</h1>"
    html_code += f"<p>{random.choice(tekno_list)}</p>"
    return html_code

@app.route("/yazi_tura")
def yazi_tura():
    html_code = "<h2>Yazı-tura atıldı.</h2>"
    html_code += "<h2>Sonuç:</h2>"
    html_code += f"{yazi_tura_at()}"
    return html_code

@app.route("/sifre")
def sifre_olustur():
    html_code = "<h2>Şifre Oluşturuldu.</h2>"
    html_code += "<h2>Şifreniz :</h2>"
    html_code += f'{sifreci()}'
    return html_code

@app.route("/meme")
def meme_cik():
    html_code = "<h2>Resminiz:<h2>"
    html_code += "<img><img src=https://i.pinimg.com/736x/6b/1f/08/6b1f08b5681c3cb64881d991d4eb23c6.jpg></img>"
    return html_code

app.run(debug=True)
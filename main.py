from flask import Flask
import random

fatti_di_patate = ["lo sapevi che le patate possono crescere più patate mettendole sotto terra?",
                   "le patate sono verdure, non frutti che sputano succhi di pomodoro.",
                   "le patate sono piu radioattive delle banane e a volte hanno anche un pochino di uranio (tipo pochissimo).", 
                   "le patate furono il primo cibo coltivato nello spazio.",
                   "la patata piu pesante era stata coltivata in 1974 e pesava 167 kg.",
                   "le patate contengono piu potassio delle banane.",
                   "le patate furono introdotte in europa dal sud america nel 1536.",
                   "le patate sono il quarto vegetale piu consumato al mondo dopo riso, grano e mais.",
                   "le patate possono assorbire e rimuovere i metalli pesanti dal suolo.",
                   "le patate possono essere usate per produrre plastica biodegradabile e combustibile.",
                   "le patate possono produrre elettricita, ma pochissima.",
                   "le patate possono essere usate per pulire l'argento ossidato.",
                   "le patate possono essere usate per alleviare le scottature solari, ma solo se crude e se è una scottatura leggera."]
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/patate")
def test():
    return f'<p>{random.choice(fatti_di_patate)}</p>'

@app.route("/secret")
def secret():
    return "<p>questo è molto importante lo devi vedere: https://youtu.be/dQw4w9WgXcQ</p>"

app.run(debug=True)
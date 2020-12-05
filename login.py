import requests as req
from getpass import getpass
import json

class LoginClasseviva:
    pagina: str
    password: str
    email: str

    def __init__(self, pagina, password, email):
        self.pagina = pagina
        self.password = password
        self.email = email
    # FINE COSTRUTTORE

    def login(self):#invia la request per il login a classeviva
        global r
        data = {'cid':'',
        'uid': self.email,
        'pwd': self.password,
        'pin':'',
        'target':'' }
        global s
        s = req.Session()
        r = s.post("https://web.spaggiari.eu/auth-p7/app/default/AuthApi4.php?a=aLoginPwd", data=data)
        r = s.get(self.pagina)
    #FINE FUNZIONE

    def loggato(self):
        if r.url == self.pagina:
            return True
        else:
            return False
        #FINE FUNZIONE

    def getR(self):
        return r

    def ottieniEventi(self):
        data = {'classe_id':'','gruppo_id':'','nascondi_av': '0','start': '1606690800','end': '1610319600'}
        r = s.post('https://web.spaggiari.eu/fml/app/default/agenda_studenti.php?ope=get_events', data=data)

        eventi_formattati = r.text[1:-1].replace("},{", "};;;{")
        eventi = eventi_formattati.split(";;;")

        eventi_json = []
        for evento in eventi:
            eventi_json.append(json.loads(evento))

        return eventi_json
#FINE CLASSE

passw = getpass("Password: ")
mail = input("Mail: ")
c = LoginClasseviva("https://web.spaggiari.eu/fml/app/default/agenda_studenti.php", passw, mail)
c.login()
b = c.loggato()
if b:
    print("Ci sei")

    x = c.ottieniEventi()
    for y in x:
        print("Prof " + y["autore_desc"], end = "\t")
        print("Da " + y["start"] + " a " + y["end"], end="\t")
        print(y["title"])
else:
    print("No")

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QWidget,QStackedWidget
import sqlite3

class welcome(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\qt\login.ui",self)
        self.pushButton.clicked.connect(self.giris)     #gidip designerdan obje ismine baktım
        self.hesapolustur.clicked.connect(self.hesap)
        self.pushButton_2.clicked.connect(self.exit)
    def exit(self):
        QApplication.exit()
    def giris(self):
        login = girisyap()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)     #başka bir sayfaya geçtim demek istiyor
    def hesap(self):
        hesap_olustur = hesap()
        widget.addWidget(hesap_olustur)
        widget.setCurrentIndex(widget.currentIndex()+1)
class hesap(QDialog):
    def __init__(self):
        super(hesap,self).__init__()
        loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\qt\hesap.ui",self)
        self.baglan()
        self.hesap_olus.clicked.connect(self.olustur)
        self.pushButton.clicked.connect(self.onceki)
    def onceki(self):           #önemli nokta
        onceki = welcome()
        widget.addWidget(onceki)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def baglan(self):
        self.con = sqlite3.connect(r"C:\Users\bugra\OneDrive\Masaüstü\qt\infos.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler(user TEXT,password TEXT)")
    def olustur(self):
        user = self.user.text()
        sifre = self.passwordfield.text()
        sifre_tekrar = kullanıcı = self.passwordfield_2.text()

        if len(sifre)==0 or len(sifre_tekrar)==0 or len(user)==0:
            self.label_7.setText("Doldurulmamış alanlar var !")
        elif sifre != sifre_tekrar:
            self.label_7.setText("Şifreler uyuşmuyor !")
        else:
            self.cursor.execute("INSERT into bilgiler values(?,?)",(user,sifre))
            self.con.commit()
            self.label_7.setText("Hesap oluşturuldu")
class girisyap(QDialog):
    def __init__(self):
        super(girisyap,self).__init__()     #self önemli
        loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\qt\giris.ui",self)       #burdaki self olmazsa çalışmaz
        #self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_3.clicked.connect(self.gir)
        self.pushButton.clicked.connect(self.onceki)

    def onceki(self):  # önemli nokta
        onceki = welcome()
        widget.addWidget(onceki)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gir(self):
        user = self.lineEdit.text()
        password = self.passwordfield.text()

        if user=="" or len(password) == 0:      #ikiside olur
            self.label_7.setText("Boş bırakılan alanlar var !")
        else:
            con = sqlite3.connect(r"C:\Users\bugra\OneDrive\Masaüstü\qt\infos.db")      #değiştirmeyi unutmayın
            cur = con.cursor()
            sorgu = "SELECT password from bilgiler WHERE user = \'"+user+"\'"       #"\'"  boşluk demek ne gereksiz iş
            cur.execute(sorgu)
            sonuc = cur.fetchall()
            sifre = sonuc[0]

            if sifre[0] == password:
                self.label_7.setText("Başarılı giriş")
                print("Başarılı giriş")
            else:
                print(sifre)
                self.label_7.setText("Hatalı bilgiler !")
                print("Hatalı deneme.")

app = QApplication(sys.argv)
welcome1 = welcome()
widget = QStackedWidget()       #bir çok başka ekran açılmasını çalışıyor
widget.addWidget(welcome1)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("çıkılıyor")
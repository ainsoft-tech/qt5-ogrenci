import sys
from PyQt5 import QtWidgets as qtw
from ogrenci import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem

class Uygulama(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Dogumyer.addItems(["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"])
        self.ui.Bolum.addItems(["SAYISAL", "EŞİT AĞIRLIK", "SÖZEL"])
        self.ui.Kayitekle.clicked.connect(self.kayitekle)
        self.ui.Kayitsil.clicked.connect(self.kayitsil)

    def kayitekle(self):
        ad = self.ui.Ad.text()
        soyad = self.ui.Soyad.text()
        tc = self.ui.TcNo.text()

        cinsiyetgrup = self.ui.Cinsiyet.findChildren(qtw.QRadioButton)
        for i in cinsiyetgrup:
            if i.isChecked():
                cinsiyet = i.text()

        eturgrup = self.ui.Etur.findChildren(qtw.QRadioButton)
        for i in eturgrup:
            if i.isChecked():
                etur = i.text()

        dogumyer = self.ui.Dogumyer.currentText()
        bolum = self.ui.Bolum.currentText()
        dtarih = self.ui.DogumTarihi.selectedDate()
        ydtarih = dtarih.toString("dd-MM-yyyy")

        satırsayısı = self.ui.Tablo.rowCount()-1

        self.ui.Tablo.setItem(satırsayısı,0,QTableWidgetItem(ad))
        self.ui.Tablo.setItem(satırsayısı,1,QTableWidgetItem(soyad))
        self.ui.Tablo.setItem(satırsayısı,2,QTableWidgetItem(cinsiyet))
        self.ui.Tablo.setItem(satırsayısı,3,QTableWidgetItem(tc))
        self.ui.Tablo.setItem(satırsayısı,4,QTableWidgetItem(dogumyer))
        self.ui.Tablo.setItem(satırsayısı,5,QTableWidgetItem(ydtarih))
        self.ui.Tablo.setItem(satırsayısı,6,QTableWidgetItem(bolum))
        self.ui.Tablo.setItem(satırsayısı,7,QTableWidgetItem(etur))

        self.ui.Tablo.insertRow(satırsayısı+1)

    def kayitsil(self):
        secili = self.ui.Tablo.currentRow()
        self.ui.Tablo.removeRow(secili)






def app():
    app = qtw.QApplication(sys.argv)
    win = Uygulama()
    win.show()
    sys.exit(app.exec_())

app()
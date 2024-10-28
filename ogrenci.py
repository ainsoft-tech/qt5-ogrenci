# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogrenci.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(740, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(740, 740))
        MainWindow.setMaximumSize(QtCore.QSize(740, 740))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.Tablo = QtWidgets.QTableWidget(self.centralwidget)
        self.Tablo.setGeometry(QtCore.QRect(10, 410, 711, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tablo.setFont(font)
        self.Tablo.setRowCount(20)
        self.Tablo.setColumnCount(6)
        self.Tablo.setObjectName("Tablo")
        item = QtWidgets.QTableWidgetItem()
        self.Tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablo.setHorizontalHeaderItem(5, item)
        self.Tablo.horizontalHeader().setCascadingSectionResizes(False)
        self.Tablo.horizontalHeader().setDefaultSectionSize(111)
        self.Tablo.horizontalHeader().setHighlightSections(True)
        self.Tablo.horizontalHeader().setSortIndicatorShown(False)
        self.Tablo.horizontalHeader().setStretchLastSection(False)
        self.Tablo.verticalHeader().setVisible(True)
        self.Tablo.verticalHeader().setCascadingSectionResizes(False)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(430, 60, 181, 169))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Kayitekle = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Kayitekle.setFont(font)
        self.Kayitekle.setObjectName("Kayitekle")
        self.verticalLayout_3.addWidget(self.Kayitekle)
        self.Kayitsil = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Kayitsil.setFont(font)
        self.Kayitsil.setObjectName("Kayitsil")
        self.verticalLayout_3.addWidget(self.Kayitsil)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.OgrenciInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.OgrenciInfo.setGeometry(QtCore.QRect(30, 50, 351, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OgrenciInfo.setFont(font)
        self.OgrenciInfo.setStyleSheet("color: rgb(0, 0, 0);")
        self.OgrenciInfo.setFlat(False)
        self.OgrenciInfo.setObjectName("OgrenciInfo")
        self.label_4 = QtWidgets.QLabel(self.OgrenciInfo)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.OgrenciInfo)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 43, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.OgrenciInfo)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 74, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.OgrenciInfo)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 74, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.OgrenciInfo)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 83, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.Cinsiyet = QtWidgets.QGroupBox(self.OgrenciInfo)
        self.Cinsiyet.setGeometry(QtCore.QRect(10, 190, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cinsiyet.setFont(font)
        self.Cinsiyet.setStyleSheet("color: rgb(0, 0, 0);")
        self.Cinsiyet.setFlat(False)
        self.Cinsiyet.setCheckable(False)
        self.Cinsiyet.setObjectName("Cinsiyet")
        self.Erkek = QtWidgets.QRadioButton(self.Cinsiyet)
        self.Erkek.setGeometry(QtCore.QRect(10, 20, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Erkek.setFont(font)
        self.Erkek.setObjectName("Erkek")
        self.Kadin = QtWidgets.QRadioButton(self.Cinsiyet)
        self.Kadin.setGeometry(QtCore.QRect(100, 20, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Kadin.setFont(font)
        self.Kadin.setObjectName("Kadin")
        self.Ad = QtWidgets.QLineEdit(self.OgrenciInfo)
        self.Ad.setGeometry(QtCore.QRect(130, 40, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ad.setFont(font)
        self.Ad.setStyleSheet("color: rgb(0, 0, 0);")
        self.Ad.setObjectName("Ad")
        self.Soyad = QtWidgets.QLineEdit(self.OgrenciInfo)
        self.Soyad.setGeometry(QtCore.QRect(130, 70, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Soyad.setFont(font)
        self.Soyad.setStyleSheet("color: rgb(0, 0, 0);")
        self.Soyad.setObjectName("Soyad")
        self.TcNo = QtWidgets.QLineEdit(self.OgrenciInfo)
        self.TcNo.setGeometry(QtCore.QRect(130, 100, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TcNo.setFont(font)
        self.TcNo.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.TcNo.setObjectName("TcNo")
        self.Dogumyer = QtWidgets.QComboBox(self.OgrenciInfo)
        self.Dogumyer.setGeometry(QtCore.QRect(130, 130, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dogumyer.setFont(font)
        self.Dogumyer.setStyleSheet("color: rgb(0, 0, 0);")
        self.Dogumyer.setObjectName("Dogumyer")
        self.dateEdit = QtWidgets.QDateEdit(self.OgrenciInfo)
        self.dateEdit.setGeometry(QtCore.QRect(130, 160, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.label_8 = QtWidgets.QLabel(self.OgrenciInfo)
        self.label_8.setGeometry(QtCore.QRect(30, 250, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.Bolum = QtWidgets.QComboBox(self.OgrenciInfo)
        self.Bolum.setGeometry(QtCore.QRect(130, 250, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bolum.setFont(font)
        self.Bolum.setStyleSheet("color: rgb(0, 0, 0);")
        self.Bolum.setObjectName("Bolum")
        self.label_10 = QtWidgets.QLabel(self.OgrenciInfo)
        self.label_10.setGeometry(QtCore.QRect(30, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.OgrenciInfo)
        self.label_11.setGeometry(QtCore.QRect(30, 310, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.OgrenciInfo)
        self.lineEdit.setGeometry(QtCore.QRect(130, 280, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.OgrenciInfo)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 310, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.layoutWidget.raise_()
        self.label_2.raise_()
        self.Tablo.raise_()
        self.OgrenciInfo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Öğrenci Kayıt Programı"))
        self.label_2.setText(_translate("MainWindow", "ÖĞRENCİ KAYIT/TAKİP SİSTEMi"))
        self.Tablo.setSortingEnabled(False)
        item = self.Tablo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Adı"))
        item = self.Tablo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Soyadı"))
        item = self.Tablo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TC Kimlik No"))
        item = self.Tablo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bölüm"))
        item = self.Tablo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sınıf"))
        item = self.Tablo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Okul"))
        self.Kayitekle.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.Kayitsil.setText(_translate("MainWindow", "Kayıt Sil"))
        self.pushButton.setText(_translate("MainWindow", "Sınıf Tanımla"))
        self.pushButton_2.setText(_translate("MainWindow", "Okul Tanımla"))
        self.pushButton_3.setText(_translate("MainWindow", "Bölüm Tanımla"))
        self.OgrenciInfo.setTitle(_translate("MainWindow", " Öğrencinin "))
        self.label_4.setText(_translate("MainWindow", "Adı"))
        self.label_5.setText(_translate("MainWindow", "Soyadı"))
        self.label_6.setText(_translate("MainWindow", "TC Kimlik No"))
        self.label_7.setText(_translate("MainWindow", "Doğum Yeri"))
        self.label_9.setText(_translate("MainWindow", "Doğum Tarihi"))
        self.Cinsiyet.setTitle(_translate("MainWindow", " Cinsiyet "))
        self.Erkek.setText(_translate("MainWindow", "Erkek"))
        self.Kadin.setText(_translate("MainWindow", "Kadın"))
        self.label_8.setText(_translate("MainWindow", "Bölüm"))
        self.label_10.setText(_translate("MainWindow", "Sınıf"))
        self.label_11.setText(_translate("MainWindow", "Okul"))

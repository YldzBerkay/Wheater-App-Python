from PyQt5 import QtWidgets , QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow , QToolTip , QMessageBox , QDesktopWidget ,QStyleFactory
from PyQt5.QtGui import QIcon , QFont ,QPixmap 
from PyQt5.Qt import Qt
import sys
from os import system
import requests
import json
system("cls")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("Weather App")
        self.setStyleSheet("background-color:rgb(102,178,255);")
        self.setAutoFillBackground(True)
        self.setFixedSize(700,500)
        self.setToolTip("Weather App")
        self.setWindowIcon(QIcon("icons/01d"))  
        self.initUI()
    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Enter a city")
        self.lbl_name.setFont(QFont("Corbel",20))
        self.lbl_name.setStyleSheet("color:rgb(255,255,255);")
        self.lbl_name.move(280,50)
        self.lbl_name.resize(200,50)

        self.lbl_copyright = QtWidgets.QLabel(self)
        self.lbl_copyright.setText("© Yağız Yazıcı")
        self.lbl_copyright.move(625,475)

        self.txt_city = QtWidgets.QLineEdit(self)
        self.txt_city.setFixedSize(175,25)
        self.txt_city.setFont(QFont("Corbel",14))
        self.txt_city.returnPressed.connect(self.clicked)
        self.txt_city.setStyleSheet("border :2px solid black ;"
                     "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black;"
                     "color: white"
                     )
        self.txt_city.move(252,100)

        self.weather_icon = QtWidgets.QLabel(self)
        self.weather_icon.setGeometry(450,150,300,50)

        self.weather_result = QtWidgets.QLabel(self)
        self.weather_result.setFont(QFont("Corbel",50))
        self.weather_result.setStyleSheet("color: white")
        self.weather_result.resize(425,100)
        self.weather_result.move(25,125)

        self.weather_result1 = QtWidgets.QLabel(self)
        self.weather_result1.setFont(QFont("Corbel",100))
        self.weather_result1.setStyleSheet("color: white")
        self.weather_result1.resize(275,150)
        self.weather_result1.move(25,255)

        self.weather_result2 = QtWidgets.QLabel(self)
        self.weather_result2.setFont(QFont("Corbel",50))
        self.weather_result2.setStyleSheet("color: white")
        self.weather_result2.resize(400,75)
        self.weather_result2.move(400,300)

        self.search_button = QtWidgets.QPushButton(self)
        self.search_button.setIcon(QIcon("icons/search.png"))
        self.search_button.setFixedSize(25,25)
        self.search_button.setFont(QFont("Corbel",18))
        self.search_button.setStyleSheet("border :2px solid black ;"
                     "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")
        self.search_button.move(425,100)
        self.search_button.clicked.connect(self.clicked)
        self.search_button.setAutoDefault(True)
    def clicked(self):
        self.api_key = "892e729dedd8fe1d2581e77519155f81"
        self.total_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.txt_city.text()}&appid={self.api_key}&units=metric"
        self.result = requests.get(self.total_url)
        self.result= json.loads(self.result.text)
        if self.result["cod"] == 200:
            self.city_name = self.result["name"]
            if "Province" in self.city_name:
                self.city_name = self.city_name.replace("Province","")
            self.tempt = self.result["main"]["temp"]
            self.dscrptn = self.result["weather"][0]["main"]
            self.icon = self.result["weather"][0]["icon"]
            self.weather_result.setText(f"{self.city_name}")
            self.weather_result1.setText(f"{int(self.tempt)}°c")
            self.weather_icon.setPixmap(QPixmap(f"icons/{self.icon}.png"))
            self.weather_result2.setText(f"{self.dscrptn}")
            if self.icon[2] == "n":
                self.setStyleSheet("background-color:rgb(64,64,64);")
            else:
                self.setStyleSheet("background-color:rgb(102,178,255);")
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText(f"No city found named {self.txt_city.text().upper()}!")
            self.msg.setInformativeText("Enter a valid city name")
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
    def Center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().Center()
        qp.moveCenter(cp)
        self.move(qr.topLeft())
def Window():
    app = QApplication(sys.argv)
    win = MyWindow()
    app.setStyle('Fusion')

    win.show()
    sys.exit(app.exec_())
    
Window()
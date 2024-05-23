# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1415, 631)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 230, 450, 350))
        self.imageLabel = QLabel(self.groupBox)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(20, 20, 400, 300))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(480, 230, 450, 350))
        self.horizontalLayoutWidget = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 431, 311))
        self.reconstructionLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.reconstructionLayout.setObjectName(u"reconstructionLayout")
        self.reconstructionLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(950, 230, 450, 350))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 30, 431, 311))
        self.sinogramLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.sinogramLayout.setObjectName(u"sinogramLayout")
        self.sinogramLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(200, 10, 1011, 201))
        self.filterComboBox = QComboBox(self.groupBox_4)
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.setObjectName(u"filterComboBox")
        self.filterComboBox.setGeometry(QRect(240, 120, 161, 22))
        self.reconstructioncomboBox = QComboBox(self.groupBox_4)
        self.reconstructioncomboBox.addItem("")
        self.reconstructioncomboBox.addItem("")
        self.reconstructioncomboBox.addItem("")
        self.reconstructioncomboBox.addItem("")
        self.reconstructioncomboBox.addItem("")
        self.reconstructioncomboBox.setObjectName(u"reconstructioncomboBox")
        self.reconstructioncomboBox.setGeometry(QRect(240, 80, 161, 22))
        self.maxAngleValue = QLineEdit(self.groupBox_4)
        self.maxAngleValue.setObjectName(u"maxAngleValue")
        self.maxAngleValue.setGeometry(QRect(240, 40, 161, 22))
        self.clearButton = QPushButton(self.groupBox_4)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(840, 160, 150, 40))
        self.calculateButton = QPushButton(self.groupBox_4)
        self.calculateButton.setObjectName(u"calculateButton")
        self.calculateButton.setGeometry(QRect(840, 110, 150, 40))
        self.animationButton = QPushButton(self.groupBox_4)
        self.animationButton.setObjectName(u"animationButton")
        self.animationButton.setGeometry(QRect(840, 60, 150, 40))
        self.loadButton = QPushButton(self.groupBox_4)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(840, 10, 150, 40))
        self.maxAngleLabel = QLabel(self.groupBox_4)
        self.maxAngleLabel.setObjectName(u"maxAngleLabel")
        self.maxAngleLabel.setGeometry(QRect(20, 40, 171, 21))
        font = QFont()
        font.setPointSize(10)
        self.maxAngleLabel.setFont(font)
        self.filterLabel = QLabel(self.groupBox_4)
        self.filterLabel.setObjectName(u"filterLabel")
        self.filterLabel.setGeometry(QRect(20, 120, 121, 21))
        self.filterLabel.setFont(font)
        self.reconstructionLabel = QLabel(self.groupBox_4)
        self.reconstructionLabel.setObjectName(u"reconstructionLabel")
        self.reconstructionLabel.setGeometry(QRect(20, 80, 211, 16))
        self.reconstructionLabel.setFont(font)
        self.projectionLabel = QLabel(self.groupBox_4)
        self.projectionLabel.setObjectName(u"projectionLabel")
        self.projectionLabel.setGeometry(QRect(440, 30, 181, 31))
        self.projectionLabel.setFont(font)
        self.projectionValue = QLabel(self.groupBox_4)
        self.projectionValue.setObjectName(u"projectionValue")
        self.projectionValue.setGeometry(QRect(630, 30, 51, 31))
        self.projectionValue.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1415, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Orijinal G\u00f6r\u00fcnt\u00fc", None))
        self.imageLabel.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Yeniden Yap\u0131land\u0131rma (Reconstruction)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Sinogram Grafi\u011fi", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Ayarlar", None))
        self.filterComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Filtered Back Projection", None))
        self.filterComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"SART", None))

        self.reconstructioncomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ramp", None))
        self.reconstructioncomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"shepp-logan", None))
        self.reconstructioncomboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"cosine", None))
        self.reconstructioncomboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"hamming", None))
        self.reconstructioncomboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"hann", None))

        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.calculateButton.setText(QCoreApplication.translate("MainWindow", u"Hesapla", None))
        self.animationButton.setText(QCoreApplication.translate("MainWindow", u"Animasyon", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"G\u00f6r\u00fcnt\u00fc Y\u00fckle", None))
        self.maxAngleLabel.setText(QCoreApplication.translate("MainWindow", u"Maksimum A\u00e7\u0131 De\u011feri :", None))
        self.filterLabel.setText(QCoreApplication.translate("MainWindow", u"Yeniden Yap\u0131land\u0131rma T\u00fcr\u00fc :", None))
        self.reconstructionLabel.setText(QCoreApplication.translate("MainWindow", u"Filtre Tipi :", None))
        self.projectionLabel.setText(QCoreApplication.translate("MainWindow", u"Projeksiyon Say\u0131s\u0131 :", None))
        self.projectionValue.setText("")
    # retranslateUi


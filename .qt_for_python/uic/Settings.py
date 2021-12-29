# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\adity\PycharmProjects\osu-statqt\Screens\Settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(816, 615)
        SettingsWindow.setStyleSheet("background-color:rgb(24,22,29);\n"
"color: rgb(255,255,255);\n"
"padding:0px;")
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(800, 49))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(35,31,47);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(798, 249))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setMinimumSize(QtCore.QSize(240, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";\n"
"background-color:rgb(36,35,43);\n"
"padding-left: 30px")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setStyleSheet("background-color:rgb(49,47,56);\n"
"font: 63 12pt \"Torus Pro SemiBold\";\n"
"color: rgb(148, 143, 163)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout_3.setContentsMargins(42, 30, 50, -1)
        self.formLayout_3.setHorizontalSpacing(18)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.client_id_field_3 = QtWidgets.QLineEdit(self.frame_5)
        self.client_id_field_3.setStyleSheet("QLineEdit {\n"
"background-color: rgb(61, 57, 70);\n"
"border: none;\n"
"padding: 6px;\n"
"border-radius: 4px;\n"
"color: rgb(255,255,255);\n"
"font: 63 10pt \"Torus Pro SemiBold\";\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  rgb(148, 143, 163);\n"
"}")
        self.client_id_field_3.setObjectName("client_id_field_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.client_id_field_3)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.client_secret_field_3 = QtWidgets.QLineEdit(self.frame_5)
        self.client_secret_field_3.setStyleSheet("QLineEdit {\n"
"background-color: rgb(61, 57, 70);\n"
"border: none;\n"
"padding: 6px;\n"
"border-radius: 4px;\n"
"color: rgb(255,255,255);\n"
"font: 63 10pt \"Torus Pro SemiBold\";\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  rgb(148, 143, 163);\n"
"}")
        self.client_secret_field_3.setObjectName("client_secret_field_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.client_secret_field_3)
        self.submit_credentials_3 = QtWidgets.QPushButton(self.frame_5)
        self.submit_credentials_3.setStyleSheet("QPushButton {background-color: rgb(86,57,172);\n"
"color: rgb(255, 255, 255);\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"max-width:110px;\n"
"text-align: center;}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgb(140, 102, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Users\\adity\\PycharmProjects\\osu-statqt\\Screens\\../Assets/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_credentials_3.setIcon(icon)
        self.submit_credentials_3.setObjectName("submit_credentials_3")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.submit_credentials_3)
        self.get_credentials_3 = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_credentials_3.sizePolicy().hasHeightForWidth())
        self.get_credentials_3.setSizePolicy(sizePolicy)
        self.get_credentials_3.setMinimumSize(QtCore.QSize(160, 0))
        self.get_credentials_3.setStyleSheet("QPushButton {background-color: rgb(86,57,172);\n"
"color: rgb(255, 255, 255);\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"text-align: center;}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgb(140, 102, 255);\n"
"}")
        self.get_credentials_3.setObjectName("get_credentials_3")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.get_credentials_3)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setMinimumSize(QtCore.QSize(798, 136))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setMinimumSize(QtCore.QSize(240, 0))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_10.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";\n"
"background-color:rgb(36,35,43);\n"
"padding-left: 30px")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_7.setStyleSheet("background-color:rgb(49,47,56);\n"
"font: 63 12pt \"Torus Pro SemiBold\";\n"
"color: rgb(148, 143, 163)")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_4.setContentsMargins(50, 30, 50, -1)
        self.formLayout_4.setHorizontalSpacing(18)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.client_id_field_4 = QtWidgets.QLineEdit(self.frame_7)
        self.client_id_field_4.setStyleSheet("QLineEdit {\n"
"background-color: rgb(61, 57, 70);\n"
"border: none;\n"
"padding: 6px;\n"
"border-radius: 4px;\n"
"color: rgb(255,255,255);\n"
"font: 63 10pt \"Torus Pro SemiBold\";\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  rgb(148, 143, 163);\n"
"}")
        self.client_id_field_4.setObjectName("client_id_field_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.client_id_field_4)
        self.submit_credentials_4 = QtWidgets.QPushButton(self.frame_7)
        self.submit_credentials_4.setStyleSheet("QPushButton {background-color: rgb(86,57,172);\n"
"color: rgb(255, 255, 255);\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"max-width:110px;\n"
"text-align: center;}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgb(140, 102, 255);\n"
"}\n"
"")
        self.submit_credentials_4.setIcon(icon)
        self.submit_credentials_4.setObjectName("submit_credentials_4")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.submit_credentials_4)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMinimumSize(QtCore.QSize(798, 136))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        self.label_12.setMinimumSize(QtCore.QSize(240, 0))
        self.label_12.setMaximumSize(QtCore.QSize(240, 16777215))
        self.label_12.setStyleSheet("font: 63 18pt \"Torus Pro SemiBold\";\n"
"background-color:rgb(36,35,43);\n"
"padding-left: 30px")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_9.setStyleSheet("background-color:rgb(49,47,56);\n"
"font: 63 12pt \"Torus Pro SemiBold\";\n"
"color: rgb(148, 143, 163)")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_9)
        self.formLayout_5.setContentsMargins(35, 30, 50, -1)
        self.formLayout_5.setHorizontalSpacing(18)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.save_refresh_limit = QtWidgets.QPushButton(self.frame_9)
        self.save_refresh_limit.setStyleSheet("QPushButton {background-color: rgb(86,57,172);\n"
"color: rgb(255, 255, 255);\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"max-width:110px;\n"
"text-align: center;}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgb(140, 102, 255);\n"
"}\n"
"")
        self.save_refresh_limit.setIcon(icon)
        self.save_refresh_limit.setObjectName("save_refresh_limit")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.save_refresh_limit)
        self.refresh_limit_combo = QtWidgets.QComboBox(self.frame_9)
        self.refresh_limit_combo.setStyleSheet("background-color: rgb(61, 57, 70);\n"
"border: none;\n"
"padding: 6px;\n"
"border-radius: 4px;\n"
"color: rgb(255,255,255);\n"
"font: 63 10pt \"Torus Pro SemiBold\";")
        self.refresh_limit_combo.setObjectName("refresh_limit_combo")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.refresh_limit_combo.addItem("")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.refresh_limit_combo)
        self.horizontalLayout_6.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_3)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MainWindow"))
        self.label_4.setText(_translate("SettingsWindow", "      settings"))
        self.label_7.setText(_translate("SettingsWindow", "Credentials"))
        self.label_8.setText(_translate("SettingsWindow", "client id"))
        self.label_9.setText(_translate("SettingsWindow", "client secret"))
        self.submit_credentials_3.setText(_translate("SettingsWindow", "Submit"))
        self.get_credentials_3.setText(_translate("SettingsWindow", "Get Credentials"))
        self.label_10.setText(_translate("SettingsWindow", "User"))
        self.label_11.setText(_translate("SettingsWindow", "username"))
        self.submit_credentials_4.setText(_translate("SettingsWindow", "Enter"))
        self.label_12.setText(_translate("SettingsWindow", "OsuStat"))
        self.label_13.setText(_translate("SettingsWindow", "refresh limit"))
        self.save_refresh_limit.setText(_translate("SettingsWindow", "Save"))
        self.refresh_limit_combo.setItemText(0, _translate("SettingsWindow", "No Limit"))
        self.refresh_limit_combo.setItemText(1, _translate("SettingsWindow", "Every 5 Seconds"))
        self.refresh_limit_combo.setItemText(2, _translate("SettingsWindow", "Every 10 Seconds"))
        self.refresh_limit_combo.setItemText(3, _translate("SettingsWindow", "Every 15 Seconds"))
        self.refresh_limit_combo.setItemText(4, _translate("SettingsWindow", "Every 30 Seconds"))
        self.refresh_limit_combo.setItemText(5, _translate("SettingsWindow", "Every Minute"))

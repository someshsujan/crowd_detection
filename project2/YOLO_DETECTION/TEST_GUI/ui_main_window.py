# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window_Final.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1722, 804)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(1220, 40, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1220, 110, 481, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbDirection = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.cbDirection.setFont(font)
        self.cbDirection.setObjectName("cbDirection")
        self.verticalLayout.addWidget(self.cbDirection)
        self.cbNmPeople = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.cbNmPeople.setFont(font)
        self.cbNmPeople.setObjectName("cbNmPeople")
        self.verticalLayout.addWidget(self.cbNmPeople)
        self.cbTotalNmPeople = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.cbTotalNmPeople.setFont(font)
        self.cbTotalNmPeople.setObjectName("cbTotalNmPeople")
        self.verticalLayout.addWidget(self.cbTotalNmPeople)
        self.cbSpeedPeople = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.cbSpeedPeople.setFont(font)
        self.cbSpeedPeople.setObjectName("cbSpeedPeople")
        self.verticalLayout.addWidget(self.cbSpeedPeople)
        self.cbBoundaryBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.cbBoundaryBox.setFont(font)
        self.cbBoundaryBox.setObjectName("cbBoundaryBox")
        self.verticalLayout.addWidget(self.cbBoundaryBox)
        self.cbLineCros = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.cbLineCros.setFont(font)
        self.cbLineCros.setObjectName("cbLineCros")
        self.verticalLayout.addWidget(self.cbLineCros)
        self.cbVisualCenters = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.cbVisualCenters.setFont(font)
        self.cbVisualCenters.setObjectName("cbVisualCenters")
        self.verticalLayout.addWidget(self.cbVisualCenters)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(1220, 460, 481, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tbClassDetect = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbClassDetect.setFont(font)
        self.tbClassDetect.setObjectName("tbClassDetect")
        self.verticalLayout_2.addWidget(self.tbClassDetect)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbDefault = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.rbDefault.setFont(font)
        self.rbDefault.setObjectName("rbDefault")
        self.horizontalLayout.addWidget(self.rbDefault)
        self.rbExternal = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.rbExternal.setFont(font)
        self.rbExternal.setObjectName("rbExternal")
        self.horizontalLayout.addWidget(self.rbExternal)
        self.rbSorce = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.rbSorce.setFont(font)
        self.rbSorce.setObjectName("rbSorce")
        self.horizontalLayout.addWidget(self.rbSorce)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tbVidepSorce = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbVidepSorce.setFont(font)
        self.tbVidepSorce.setObjectName("tbVidepSorce")
        self.verticalLayout_2.addWidget(self.tbVidepSorce)
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setEnabled(True)
        self.image_label.setGeometry(QtCore.QRect(10, 70, 1200, 720))
        self.image_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.image_label.setObjectName("image_label")
        self.image_label_2 = QtWidgets.QLabel(Form)
        self.image_label_2.setEnabled(True)
        self.image_label_2.setGeometry(QtCore.QRect(20, 10, 561, 61))
        self.image_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.image_label_2.setObjectName("image_label_2")
        self.btStartDetection = QtWidgets.QPushButton(Form)
        self.btStartDetection.setGeometry(QtCore.QRect(1220, 730, 485, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.btStartDetection.setFont(font)
        self.btStartDetection.setObjectName("btStartDetection")
        self.btShowVideoSource = QtWidgets.QPushButton(Form)
        self.btShowVideoSource.setEnabled(True)
        self.btShowVideoSource.setGeometry(QtCore.QRect(1220, 670, 485, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.btShowVideoSource.setFont(font)
        self.btShowVideoSource.setObjectName("btShowVideoSource")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Open Remote Object Detection"))
        self.label_3.setText(_translate("Form", "Settings"))
        self.cbDirection.setText(_translate("Form", "Show the direction"))
        self.cbNmPeople.setText(_translate("Form", "Show number of people"))
        self.cbTotalNmPeople.setText(_translate("Form", "Show total number of people"))
        self.cbSpeedPeople.setText(_translate("Form", "Show speed of the people"))
        self.cbBoundaryBox.setText(_translate("Form", "Draw boundary box"))
        self.cbLineCros.setText(_translate("Form", "Calculate line crossed"))
        self.cbVisualCenters.setText(_translate("Form", "Visualizer Centers"))
        self.label.setText(_translate("Form", "Classes to detect"))
        self.label_2.setText(_translate("Form", "Video Source"))
        self.rbDefault.setText(_translate("Form", "Default camera"))
        self.rbExternal.setText(_translate("Form", "External camera"))
        self.rbSorce.setText(_translate("Form", "Source camera"))
        self.image_label.setText(_translate("Form", "Video Source"))
        self.image_label_2.setText(_translate("Form", "Logo"))
        self.btStartDetection.setText(_translate("Form", "Start detection"))
        self.btShowVideoSource.setText(_translate("Form", "Show video source"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

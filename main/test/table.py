# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import os
import re
def partition_list():
    regex = r"([^\\s]*:)"
    driver = os.popen("wmic logicaldisk get name").read()
    drives = re.findall(regex, driver)

    partition_list = [partition.strip() for drive in drives for partition in drive.split(":") if partition.strip()]
    partition_list[0] = partition_list[0].strip("Name  \n\n")
    return partition_list


class Ui_Drive(object):
    def setupUi(self, Drive):
        Drive.setObjectName("Drive")
        Drive.resize(948, 680)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.comboBox = QtWidgets.QComboBox(parent=self.dockWidgetContents)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 591, 31))
        self.comboBox.setObjectName("comboBox")
        self.scan_button = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.scan_button.setGeometry(QtCore.QRect(610, 10, 71, 41))
        self.scan_button.setObjectName("scan_button")
        self.sellectall = QtWidgets.QCheckBox(parent=self.dockWidgetContents)
        self.sellectall.setGeometry(QtCore.QRect(0, 50, 41, 41))
        self.sellectall.setObjectName("sellectall")
        self.label = QtWidgets.QLabel(parent=self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(40, 60, 791, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(700, 600, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(690, 0, 301, 71))
        self.label_2.setObjectName("label_2")
        self.comboBox_movepath = QtWidgets.QComboBox(parent=self.dockWidgetContents)
        self.comboBox_movepath.setGeometry(QtCore.QRect(10, 610, 671, 31))
        self.comboBox_movepath.setObjectName("comboBox_movepath")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.dockWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 871, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(100)
        Drive.setWidget(self.dockWidgetContents)
        self.scan_button.clicked.connect(self.button_click)



        self.retranslateUi(Drive)
        QtCore.QMetaObject.connectSlotsByName(Drive)

        self.comboBox.addItem("Select your drive")
        list = partition_list()
        self.comboBox.addItems(list)

    def button_click(self):
        selected_drive = self.comboBox.currentText()
        print(selected_drive)
        pass

    def retranslateUi(self, Drive):
        _translate = QtCore.QCoreApplication.translate
        Drive.setWindowTitle(_translate("Drive", "DockWidget"))
        self.scan_button.setText(_translate("Drive", "scan"))
        self.sellectall.setText(_translate("Drive", "All"))
        self.label.setText(_translate("Drive", "File Name                                                                                   Size             Path"))
        self.pushButton.setText(_translate("Drive", "move"))
        self.label_2.setText(_translate("Drive", "Select Your drive which is out of storage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Drive = QtWidgets.QDockWidget()
    ui = Ui_Drive()
    ui.setupUi(Drive)
    Drive.show()
    sys.exit(app.exec())

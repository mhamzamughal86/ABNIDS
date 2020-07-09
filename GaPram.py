# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GaPram.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp,QFileDialog,QMessageBox,QDialog,QDialogButtonBox,QVBoxLayout

class Ui_Dialog(object):
    def __init__(self,parent=None):
        self.parent = parent

    def select_train_data(self):
        train_dataset, train_dataset_type = QFileDialog.getOpenFileName(self.parent, "Select Training Dataset","","All Files (*);;CSV Files (*.csv)")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(474, 302)
        self.btn_ok = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(90, 230, 361, 32))
        self.btn_ok.setOrientation(QtCore.Qt.Horizontal)
        self.btn_ok.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_test = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_test.setObjectName("edit_test")
        self.gridLayout.addWidget(self.edit_test, 1, 0, 1, 1)
        self.edit_train = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_train.setObjectName("edit_train")
        self.gridLayout.addWidget(self.edit_train, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 10, 160, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_train_data = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_train_data.setObjectName("btn_train_data")
        self.btn_train_data.clicked.connect(self.select_train_data)
        self.verticalLayout.addWidget(self.btn_train_data)
        self.btn_test_data = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_test_data.setObjectName("btn_test_data")
        self.verticalLayout.addWidget(self.btn_test_data)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 120, 91, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(110, 120, 181, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.edit_population_size = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.edit_population_size.setObjectName("edit_population_size")
        self.verticalLayout_3.addWidget(self.edit_population_size)
        self.edit_mutation_rate = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.edit_mutation_rate.setObjectName("edit_mutation_rate")
        self.verticalLayout_3.addWidget(self.edit_mutation_rate)

        self.retranslateUi(Dialog)
        self.btn_ok.accepted.connect(Dialog.accept)
        self.btn_ok.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Model Inputs"))
        self.btn_train_data.setText(_translate("Dialog", "Select Training Dataset"))
        self.btn_test_data.setText(_translate("Dialog", "Select Testing Dataset"))
        self.label.setText(_translate("Dialog", "Population Size"))
        self.label_2.setText(_translate("Dialog", "Mutation Rate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
# def resume(self):
#         self.window = QtWidgets.QDialog()
#         self.ui = Ui_Dialog(MainWindow)
#         self.ui.setupUi(self.window)
#         self.window.setFocus(True)
#         self.window.show()
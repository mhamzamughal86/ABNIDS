from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp
import sys
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class Ui_Graph(object):
    
    def __init__(self):
        print("here")
    

        
    def setupUi(self, Graph):
        Graph.setObjectName("Graph")
        Graph.resize(800, 551)
        self.centralwidget = QtWidgets.QWidget(Graph)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 470, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 100, 751, 351))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 331, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("121.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        Graph.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Graph)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        Graph.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Graph)
        self.statusbar.setObjectName("statusbar")
        Graph.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(Graph)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(Graph)
        self.actionExit.setObjectName("actionExit")
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionExit)
        self.actionExit.triggered.connect(qApp.quit)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(Graph)
        QtCore.QMetaObject.connectSlotsByName(Graph)

    def retranslateUi(self, Graph):
        _translate = QtCore.QCoreApplication.translate
        Graph.setWindowTitle(_translate("Graph", "Graph"))
        self.pushButton.setText(_translate("Graph", "OK"))
        self.menuFIle.setTitle(_translate("Graph", "FIle"))
        self.actionSave.setText(_translate("Graph", "Save"))
        self.actionExit.setText(_translate("Graph", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Graph = QtWidgets.QMainWindow()
    ui = Ui_Graph()
    ui.setupUi(Graph)
    Graph.show()
    sys.exit(app.exec_())

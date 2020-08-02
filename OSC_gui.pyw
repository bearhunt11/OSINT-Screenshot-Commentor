from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OSINT(object):
    def setupUi(self, OSINT):
        OSINT.setObjectName("OSINT")
        OSINT.resize(779, 432)
        self.txtBox = QtWidgets.QTextEdit(OSINT)
        self.txtBox.setGeometry(QtCore.QRect(10, 10, 761, 361))
        self.txtBox.setObjectName("txtBox")
        self.layoutWidget = QtWidgets.QWidget(OSINT)
        self.layoutWidget.setGeometry(QtCore.QRect(540, 390, 228, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BtnReport = QtWidgets.QPushButton(self.layoutWidget)
        self.BtnReport.setObjectName("BtnReport")
        self.horizontalLayout.addWidget(self.BtnReport)
        self.BtnSave = QtWidgets.QPushButton(self.layoutWidget)
        self.BtnSave.setObjectName("BtnSave")
        self.horizontalLayout.addWidget(self.BtnSave)

        self.retranslateUi(OSINT)
        QtCore.QMetaObject.connectSlotsByName(OSINT)

    def retranslateUi(self, OSINT):
        _translate = QtCore.QCoreApplication.translate
        OSINT.setWindowTitle(_translate("OSINT", "OSINT Screenshot comment addon"))
        self.txtBox.setHtml(_translate("OSINT", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.BtnReport.setText(_translate("OSINT", "Build Report"))
        self.BtnSave.setText(_translate("OSINT", "Save edits and close"))
        self.BtnSave.setShortcut(_translate("OSINT", "Ctrl+Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OSINT = QtWidgets.QDialog()
    ui = Ui_OSINT()
    ui.setupUi(OSINT)
    OSINT.show()
    sys.exit(app.exec_())

""""
This is the main program of OSINT Commenting Screenshot tool
From here it sends commands to build report, the gui and basic info script.
"""


import BasicInfo
import BuildReport
import sys
from PyQt5 import QtWidgets, uic
from OSC_gui import Ui_OSINT


class OSC_gui(QtWidgets.QMainWindow, Ui_OSINT):
    def __init__(self,comment_file, folder, *args, obj=None, **kwargs):
        super(OSC_gui, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.BtnReport.clicked.connect(self.report)
        self.BtnSave.clicked.connect(self.save)

        ## Open OSINT Comment file and place text in textbox
        with open(comment_file, 'r') as f:
            txt = f.read()
        self.txtBox.setPlainText(txt)


        ## Create report from .bh11 files and close file
    def report(self):
        print('Start Report builder')
        msg = self.txtBox.toPlainText()
        with open(comment_file, 'w') as f:
            f.writelines(msg)
        BuildReport.create_report(comment_file, folder)
        app.quit()


        ## Save OSINT Comment and close file
    def save(self):
        msg = self.txtBox.toPlainText()
        with open(comment_file, 'w') as f:
            f.writelines(msg)
        app.quit()


### run commands ###
url = BasicInfo.get_url()
folder, filename, dtg = BasicInfo.create_basic_info()
comment_file = BasicInfo.write_to_file(url, folder, filename, dtg)


# Import of the GUI, and running the GUI
app = QtWidgets.QApplication(sys.argv)
window = OSC_gui(comment_file, folder)
window.show()
app.exec()
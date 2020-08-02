import win32com.client
import sys
import os
import datetime
import time
from tkinter import Tk


def get_url():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate('firefox')
    time.sleep(0.1)
    shell.SendKeys("^l")
    time.sleep(0.1)
    shell.SendKeys("^c")
    time.sleep(0.1)
    #shell.SendKeys("%{TAB}")
    url = Tk().clipboard_get()
    time.sleep(0.1)
    return url


def create_basic_info():
    full_path = sys.argv[1]
    filename = os.path.basename(full_path)
    folder = os.path.dirname(full_path)
    date_time = datetime.datetime.now()
    dtg = date_time.strftime("%Y-%m-%d %H:%M")
    return folder, filename, dtg


def write_to_file(url, folder, filename, dtg):
    comment_file = os.path.join(folder, filename.replace('.png', '.bh11'))
    with open(comment_file, 'w') as f:
        f.writelines('Basic screenshot information\n')
        f.writelines(['Folder:\t', folder, '\n'])
        f.writelines(['Filename:\t', filename, '\n'])
        f.writelines(['Dtg:\t', dtg, '\n'])
        f.writelines(['URL:\t', url, '\n'])
        f.writelines('\nOSINT Comment:\n')
    return comment_file
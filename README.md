# OSINT-Screenshot-Comment
Python script for taking notes on screenshots made by an external screenshot tool like ShareX

When taking a lot of screenshots with a tool like ShareX i want to take comments on the screenshots. 
This script creates comments and creates a report with the comments and screenshots sorted out in a Microsoft Word document. 

# Installation:
pip install extra packages:
PyQt5
lxml
python-docx
pywin32

save 4 .pyw files somewhere on computer.

install ShareX screenshot tool. 

Setup ShareX

# Setup ShareX:
At the settings menu: 
select task
check save screenshot and execute action
select Action
click add action
Name: OSC tool
Location: [path to pythonw.exe]
Arguments: [path to OSC.pyw %input]

click Ok. 


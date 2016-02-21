# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Wed Apr 22 21:17:50 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
from PyQt4.QtGui import * 
from PyQt4.QtSql import * 
from PyQt4.QtCore import * 
import sys,csv
import pandas as pd


df=pd.read_csv('structureid.txt')
fd=pd.read_csv('struct.csv')
array = df['_structureId']
title = fd['structureTitle']
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('protein.png'))
		
        self.show() 
	
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)

	
	
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
	
	
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 763, 523))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 13, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.proteindictionarylabel = QtGui.QLabel(self.layoutWidget)
        self.proteindictionarylabel.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.proteindictionarylabel.setFont(font)
        self.proteindictionarylabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.proteindictionarylabel.setIndent(0)
        self.proteindictionarylabel.setObjectName(_fromUtf8("proteindictionarylabel"))
        self.verticalLayout.addWidget(self.proteindictionarylabel)
	self.proteindictionarylabel.setStyleSheet('QLabel#proteindictionarylabel {color: red}')
        self.main_frame = QtGui.QTabWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setBold(True)
        font.setWeight(75)
        self.main_frame.setFont(font)
        self.main_frame.setObjectName(_fromUtf8("main_frame"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(700, 0, 51, 471))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.exit_tab1 = QtGui.QPushButton(self.frame)
        self.exit_tab1.setGeometry(QtCore.QRect(0, 420, 49, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.exit_tab1.setFont(font)
        self.exit_tab1.setObjectName(_fromUtf8("exit_tab1"))
        self.frame_tab1 = QtGui.QFrame(self.tab)
        self.frame_tab1.setGeometry(QtCore.QRect(10, 210, 691, 241))
        self.frame_tab1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_tab1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_tab1.setObjectName(_fromUtf8("frame_tab1"))
        self.groupBox_tab1 = QtGui.QGroupBox(self.frame_tab1)
        self.groupBox_tab1.setGeometry(QtCore.QRect(10, 0, 671, 211))
        self.groupBox_tab1.setObjectName(_fromUtf8("groupBox_tab1"))
        self.table_tab1 = QtGui.QTableWidget(self.groupBox_tab1)
        self.table_tab1.setGeometry(QtCore.QRect(10, 20, 651, 181))
        self.table_tab1.setObjectName(_fromUtf8("table_tab1"))
        self.table_tab1.setColumnCount(0)
        self.table_tab1.setRowCount(0)
        self.save_tab1 = QtGui.QPushButton(self.frame_tab1)
        self.save_tab1.setGeometry(QtCore.QRect(590, 210, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.save_tab1.setFont(font)
        self.save_tab1.setObjectName(_fromUtf8("save_tab1"))
        self.search_name = QtGui.QLabel(self.tab)
        self.search_name.setGeometry(QtCore.QRect(20, 40, 261, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.search_name.setFont(font)
        self.search_name.setObjectName(_fromUtf8("search_name"))
        self.name_textbox = QtGui.QLineEdit(self.tab)
        self.name_textbox.setGeometry(QtCore.QRect(310, 30, 361, 31))
        self.name_textbox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.name_textbox.setInputMask(_fromUtf8(""))
        self.name_textbox.setText(_fromUtf8(""))
        self.name_textbox.setEchoMode(QtGui.QLineEdit.Normal)
        self.name_textbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_textbox.setObjectName(_fromUtf8("name_textbox"))
        self.enter_name = QtGui.QPushButton(self.tab)
        self.enter_name.setGeometry(QtCore.QRect(600, 70, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enter_name.setFont(font)
        self.enter_name.setObjectName(_fromUtf8("enter_name"))
        self.searchId = QtGui.QLabel(self.tab)
        self.searchId.setGeometry(QtCore.QRect(20, 130, 341, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.searchId.setFont(font)
        self.searchId.setObjectName(_fromUtf8("searchId"))
        self.id_textbox = QtGui.QLineEdit(self.tab)
        self.id_textbox.setGeometry(QtCore.QRect(380, 120, 291, 31))
        self.id_textbox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.id_textbox.setToolTip(_fromUtf8(""))
        self.id_textbox.setStatusTip(_fromUtf8(""))
        self.id_textbox.setText(_fromUtf8(""))
        self.id_textbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.id_textbox.setObjectName(_fromUtf8("id_textbox"))
        self.enter_id = QtGui.QPushButton(self.tab)
        self.enter_id.setGeometry(QtCore.QRect(600, 160, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enter_id.setFont(font)
        self.enter_id.setObjectName(_fromUtf8("enter_id"))
        self.main_frame.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.combo_id = QtGui.QComboBox(self.tab_2)
        self.combo_id.setGeometry(QtCore.QRect(280, 50, 231, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.combo_id.setFont(font)
        self.combo_id.setObjectName(_fromUtf8("combo_id"))
	
	for i in range(0,len(array)):
	    self.combo_id.addItem(_fromUtf8(array[i]))        
        
        self.frame_3 = QtGui.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(699, 0, 51, 885))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.exit_tab2 = QtGui.QPushButton(self.frame_3)
        self.exit_tab2.setGeometry(QtCore.QRect(0, 422, 49, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.exit_tab2.setFont(font)
        self.exit_tab2.setObjectName(_fromUtf8("exit_tab2"))
        self.frame_tab2 = QtGui.QFrame(self.tab_2)
        self.frame_tab2.setGeometry(QtCore.QRect(10, 180, 691, 271))
        self.frame_tab2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_tab2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_tab2.setObjectName(_fromUtf8("frame_tab2"))
        self.save_tab2 = QtGui.QPushButton(self.frame_tab2)
        self.save_tab2.setGeometry(QtCore.QRect(590, 240, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.save_tab2.setFont(font)
        self.save_tab2.setObjectName(_fromUtf8("save_tab2"))
        self.select_id = QtGui.QLabel(self.tab_2)
        self.select_id.setGeometry(QtCore.QRect(10, 50, 241, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.select_id.setFont(font)
        self.select_id.setObjectName(_fromUtf8("select_id"))
        self.groupBox_tab2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_tab2.setGeometry(QtCore.QRect(20, 180, 671, 241))
        self.groupBox_tab2.setObjectName(_fromUtf8("groupBox_tab2"))
        self.table_tab2 = QtGui.QTableWidget(self.groupBox_tab2)
        self.table_tab2.setGeometry(QtCore.QRect(10, 20, 651, 211))
        self.table_tab2.setObjectName(_fromUtf8("table_tab2"))
        self.table_tab2.setColumnCount(0)
        self.table_tab2.setRowCount(0)
        self.combo_name = QtGui.QComboBox(self.tab_2)
        self.combo_name.setGeometry(QtCore.QRect(280, 130, 411, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.combo_name.setFont(font)
        self.combo_name.setObjectName(_fromUtf8("combo_name"))
        
        for i in range(0,len(title)):
	    self.combo_name.addItem(_fromUtf8(title[i]))

        self.select_name = QtGui.QLabel(self.tab_2)
        self.select_name.setGeometry(QtCore.QRect(10, 130, 251, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.select_name.setFont(font)
        self.select_name.setObjectName(_fromUtf8("select_name"))
        self.main_frame.addTab(self.tab_2, _fromUtf8(""))
        

	self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
	
	
	self.frame_tab4 = QtGui.QFrame(self.tab_4)
        self.frame_tab4.setGeometry(QtCore.QRect(30, 50, 521, 111))
        self.frame_tab4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_tab4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_tab4.setObjectName(_fromUtf8("frame_tab4"))
        self.button1 = QtGui.QPushButton(self.frame_tab4)
        self.button1.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.button1.setObjectName(_fromUtf8("button1"))
        self.button2 = QtGui.QPushButton(self.frame_tab4)
        self.button2.setGeometry(QtCore.QRect(130, 20, 75, 23))
        self.button2.setObjectName(_fromUtf8("button2"))
        self.button3 = QtGui.QPushButton(self.frame_tab4)
        self.button3.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.button3.setObjectName(_fromUtf8("button3"))
        self.button4 = QtGui.QPushButton(self.frame_tab4)
        self.button4.setGeometry(QtCore.QRect(330, 20, 75, 23))
        self.button4.setObjectName(_fromUtf8("button4"))
        self.button5 = QtGui.QPushButton(self.frame_tab4)
        self.button5.setGeometry(QtCore.QRect(430, 20, 75, 23))
        self.button5.setObjectName(_fromUtf8("button5"))
        self.button6 = QtGui.QPushButton(self.frame_tab4)
        self.button6.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.button6.setObjectName(_fromUtf8("button6"))
        self.button7 = QtGui.QPushButton(self.frame_tab4)
        self.button7.setGeometry(QtCore.QRect(130, 70, 75, 23))
        self.button7.setObjectName(_fromUtf8("button7"))
        self.button8 = QtGui.QPushButton(self.frame_tab4)
        self.button8.setGeometry(QtCore.QRect(230, 70, 75, 23))
        self.button8.setObjectName(_fromUtf8("button8"))
        self.button9 = QtGui.QPushButton(self.frame_tab4)
        self.button9.setGeometry(QtCore.QRect(330, 70, 75, 23))
        self.button9.setObjectName(_fromUtf8("button9"))
        self.buttonreset = QtGui.QPushButton(self.frame_tab4)
        self.buttonreset.setGeometry(QtCore.QRect(430, 70, 75, 23))
        self.buttonreset.setObjectName(_fromUtf8("buttonreset"))
	
		
	self.table_tab4 = QtGui.QTableWidget(self.tab_4)
        self.table_tab4.setGeometry(QtCore.QRect(10, 180, 731, 237))
        self.table_tab4.setObjectName(_fromUtf8("table_tab4"))
        self.table_tab4.setColumnCount(0)
        self.table_tab4.setRowCount(0)	        
        
        
        self.label_tab4 = QtGui.QLabel(self.tab_4)
        self.label_tab4.setGeometry(QtCore.QRect(30, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_tab4.setFont(font)
        self.label_tab4.setObjectName(_fromUtf8("label_tab4"))
        self.label2_tab4 = QtGui.QLabel(self.tab_4)
        self.label2_tab4.setGeometry(QtCore.QRect(173, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_tab4.setFont(font)
        self.label2_tab4.setObjectName(_fromUtf8("label2_tab4"))
        self.label3_tab4 = QtGui.QLabel(self.tab_4)
        self.label3_tab4.setGeometry(QtCore.QRect(560, 150, 181, 20))
        self.label3_tab4.setObjectName(_fromUtf8("label3_tab4"))
	self.label4_tab4 = QtGui.QLabel(self.tab_4)
        self.label4_tab4.setGeometry(QtCore.QRect(370, 420, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label4_tab4.setFont(font)
        self.label4_tab4.setObjectName(_fromUtf8("label4_tab4"))	
	self.button_find = QtGui.QPushButton(self.tab_4)
        self.button_find.setGeometry(QtCore.QRect(644, 420, 101, 23))
        self.button_find.setObjectName(_fromUtf8("button_find"))	
        self.find_tab4 = QtGui.QLineEdit(self.tab_4)
        self.find_tab4.setGeometry(QtCore.QRect(460, 420, 151, 20))
        self.find_tab4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.find_tab4.setInputMask(_fromUtf8(""))
        self.find_tab4.setText(_fromUtf8(""))
        self.find_tab4.setEchoMode(QtGui.QLineEdit.Normal)
        self.find_tab4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.find_tab4.setObjectName(_fromUtf8("find_tab4"))	
	
	self.main_frame.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)	
	
	
	
	
	

	self.connect(self.enter_name, SIGNAL("clicked()"),self.find_text)
	
        self.connect(self.enter_id, SIGNAL("clicked()"),self.find_id)
	self.save_tab1.clicked.connect(self.handleSave1)
	self.save_tab2.clicked.connect(self.handleSave2)         
	self.combo_name.activated[str].connect(self.combo_text)
	self.combo_id.activated[str].connect(self.comboid)
	
	self.button1.clicked.connect(self.dictionary1)
	self.button2.clicked.connect(self.dictionary1)
	self.button3.clicked.connect(self.dictionary1)
	self.button4.clicked.connect(self.dictionary1)
	self.button5.clicked.connect(self.dictionary1)
	self.button6.clicked.connect(self.dictionary1)
	self.button7.clicked.connect(self.dictionary1)
	self.button8.clicked.connect(self.dictionary1)
	self.button9.clicked.connect(self.dictionary1)
	self.buttonreset.clicked.connect(self.clear_table)
	self.button_find.clicked.connect(self.tab4_find)
		
        self.retranslateUi(MainWindow)
        self.main_frame.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PROTEIN-DICTIONARY", None))
        self.proteindictionarylabel.setText(_translate("MainWindow", "PROTEIN DICTIONARY...", None))
        self.exit_tab1.setText(_translate("MainWindow", "EXIT", None))
	self.exit_tab1.clicked.connect(self.close)
        self.groupBox_tab1.setTitle(_translate("MainWindow", "GET YOUR INFO HERE!", None))
        self.save_tab1.setText(_translate("MainWindow", "SAVE TEXT", None))
        self.search_name.setText(_translate("MainWindow", "SEARCH BY PROTEIN NAME", None))
        self.enter_name.setText(_translate("MainWindow", "ENTER", None))
        self.searchId.setText(_translate("MainWindow", "SEARCH BY PROTEIN STRUCTURE ID", None))
        self.enter_id.setText(_translate("MainWindow", "ENTER", None))
        self.main_frame.setTabText(self.main_frame.indexOf(self.tab), _translate("MainWindow", "SEARCH BY TEXT", None))
        
        #Combo-Box id items
        for i in range(0,len(array)):
	    self.combo_id.setItemText(0, _translate("MainWindow", array[i], None))
	
		
        self.exit_tab2.setText(_translate("MainWindow", "EXIT", None))
	self.exit_tab2.clicked.connect(self.close)
        self.save_tab2.setText(_translate("MainWindow", "SAVE TEXT", None))
        self.select_id.setText(_translate("MainWindow", "SELECT THE PROTEIN ID", None))
        self.groupBox_tab2.setTitle(_translate("MainWindow", "GET YOUR INFO HERE!", None))
        
        #Combo-Box title items
        for i in range(0,len(title)):
	    self.combo_name.setItemText(0, _translate("MainWindow", title[i], None))

        self.select_name.setText(_translate("MainWindow", "SELECT THE PROTEIN NAME", None))
        self.main_frame.setTabText(self.main_frame.indexOf(self.tab_2), _translate("MainWindow", "SEARCH BY DROP-DOWN", None))
        
	self.main_frame.setTabText(self.main_frame.indexOf(self.tab_4), _translate("MainWindow", "YOUR DICTIONARY", None))
	
	
	self.button1.setText(_translate("MainWindow", "1", None))
        self.button2.setText(_translate("MainWindow", "2", None))
        self.button3.setText(_translate("MainWindow", "3", None))
        self.button4.setText(_translate("MainWindow", "4", None))
        self.button5.setText(_translate("MainWindow", "5", None))
        self.button6.setText(_translate("MainWindow", "6", None))
        self.button7.setText(_translate("MainWindow", "7", None))
        self.button8.setText(_translate("MainWindow", "8", None))
        self.button9.setText(_translate("MainWindow", "9", None))
        self.buttonreset.setText(_translate("MainWindow", "Reset", None))
        self.label_tab4.setText(_translate("MainWindow", "CLICK ANY BUTTON ", None))
        self.label2_tab4.setText(_translate("MainWindow", "TO DISPLAY THE STRUCTURE ID\'s", None))
        self.label3_tab4.setText(_translate("MainWindow", "YOU CAN FIND THE ID\'s HERE!", None))
	self.label4_tab4.setText(_translate("MainWindow", "SEARCH ID!", None))
	self.button_find.setText(_translate("MainWindow", "FIND", None))

    def comboid(self,item):
	query= QSqlQuery ("SELECT * FROM id where _structureId='"+item+"'")	
	    
	'''
	    query = QSqlQuery() 
	    query.prepare("SELECT * FROM entityinfo where _structureId = ?")
	    query.addBindValue(item)
	    query.exec_()
	'''
	i="_structureId"
	self.table1_query(query,i)    
    
    def combo_text(self,item):
	query= QSqlQuery ("SELECT * FROM title where structureTitle='"+item+"'")
	i="structureTitle"
	self.table1_query(query,i)

    def find_text(self):
	item = self.name_textbox.text()
		
	query= QSqlQuery ("SELECT * FROM title where structureTitle='"+item+"'")
	i="structureTitle"
	self.name_textbox.clear()
	self.table_query(query,i)	
	
    
    def find_id(self):
	item = self.id_textbox.text()
	query= QSqlQuery ("SELECT * FROM id where _structureId='"+item+"'")
	i="_structureId"
	self.id_textbox.clear()
	self.table_query(query,i)


    def table_query(self,query,i):
	self.table_tab1.setColumnCount(query.record().count())
	self.table_tab1.setRowCount(query.size())
	if i=='_structureId':
	    self.table_tab1.setHorizontalHeaderLabels(('Method','Entity-Chains','Structure Id', 'Bioloical Assemblies','Release Date','Resolution'))	    
	    n=6
	else:
	    self.table_tab1.setHorizontalHeaderLabels(('Structure Id', 'Structure Title','Experimental Technique'))	
	    n=3
	index=0
	while (query.next()):
	    for i in range(0,n):
		self.table_tab1.setItem(index,i,QTableWidgetItem(query.value(i).toString()))					
	    index = index+1
	self.table_tab1.resizeColumnsToContents()
	self.table_tab1.show()	

    def table1_query(self,query,i):
	self.table_tab2.setColumnCount(query.record().count())
	self.table_tab2.setRowCount(query.size())
	index=0
	if i=='_structureId':
	    self.table_tab2.setHorizontalHeaderLabels(('Method','Entity-Chains','Structure Id', 'Bioloical Assemblies','Release Date','Resolution'))		    
	    n=6
	else:
	    self.table_tab2.setHorizontalHeaderLabels(('Structure Id', 'Structure Title','Experimental Technique'))
	    n=3
	index=0	
	while (query.next()):
	    for i in range(0,n):
		self.table_tab2.setItem(index,i,QTableWidgetItem(query.value(i).toString()))					
	    index = index+1			
	self.table_tab2.resizeColumnsToContents()	
	self.table_tab2.show()    
    
    
    #Save Tablecontent to Text File    
    def handleSave1(self):
	#table='table_tab1'
	path = QtGui.QFileDialog.getSaveFileName(
		        self, 'Save File', '', 'TXT(*.txt)')
	if not path.isEmpty():
	    with open(unicode(path), 'wb') as stream:
		writer = csv.writer(stream)
		for row in range(self.table_tab1.rowCount()):
		    rowdata = []
		    for column in range(self.table_tab1.columnCount()):
			item = self.table_tab1.item(row, column)
			if item is not None:
			    rowdata.append(unicode(item.text()).encode('utf8'))
			else:
			    rowdata.append('')
		    writer.writerow(rowdata)	
    
    def handleSave2(self):
	#table='table_tab2'
	path = QtGui.QFileDialog.getSaveFileName(
		        self, 'Save File', '', 'TXT(*.txt)')
	if not path.isEmpty():
	    with open(unicode(path), 'wb') as stream:
		writer = csv.writer(stream)
		for row in range(self.table_tab2.rowCount()):
		    rowdata = []
		    for column in range(self.table_tab2.columnCount()):
			item = self.table_tab2.item(row, column)
			if item is not None:
			    rowdata.append(unicode(item.text()).encode('utf8'))
			else:
			    rowdata.append('')
		    writer.writerow(rowdata)	    
    
    
    def dictionary1(self,i):
	i = self.sender().text()
	query = QSqlQuery("SELECT structureId,structureTitle from title where structureId like '"+i+"%' ")
	#i='1'	
	self.table_dict(query)
	
    def tab4_find(self):
	item = self.find_tab4.text()
	query = QSqlQuery("SELECT structureId,structureTitle from title where structureId like '"+item+"%' ")
	self.table_dict(query)    
    
    def table_dict(self,query):
	self.table_tab4.setColumnCount(query.record().count())
	self.table_tab4.setRowCount(query.size())
	self.table_tab4.setHorizontalHeaderLabels(('Structure ID','Structure Title'))
	index=0
	
	index=0	
	while (query.next()):
	    for j in range(0,2):
		self.table_tab4.setItem(index,j,QTableWidgetItem(query.value(j).toString()))					
	    index = index+1			
	self.table_tab4.resizeColumnsToContents()	
	self.table_tab4.show()    	
    
    def clear_table(self):
	self.table_tab4.clear()
    
    def closeEvent(self,event):
                
	mesg = QtGui.QMessageBox.question(self,'Message'," Really? You sure you would wanna QUIT?... ", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                
	if mesg == QtGui.QMessageBox.Yes:
		event.accept()
	else:
	    event.ignore()


if __name__ == '__main__':    
    db 		= QSqlDatabase.addDatabase("QMYSQL")
    #table.setWindowTitle("Connect to Mysql Database Example")   
    db.setHostName("127.0.0.1")
    db.setDatabaseName("bioinformatics")
    db.setUserName("root")	
    if (db.open()==False):     
	QMessageBox.critical(None, "Database Error",
        db.lastError().text())          
    app = QtGui.QApplication(sys.argv)  
    ex = Ui_MainWindow()
    
    

    ex.show()
    sys.exit(app.exec_())
    
    
    
'''

JOIN: WORKS fine, cant load into database

insert into merge SELECT * FROM bioinfor LEFT JOIN idinfo ON bioinfor._structureId = idinfo.structureId UNION SELECT * FROM bioinfor RIGHT JOIN idinfo ON bioinfor._structureId = idinfo.structureId;



starts with : select * from idinfo where structureId like '1%';
'''
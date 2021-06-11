from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QAbstractItemView, QHeaderView, \
    QCheckBox
from DataStatistics import Ui_MainWindow
import os
import glob
from ParsingExcel import cParsingExcel


class MainWndow(QMainWindow, Ui_MainWindow):
    '主框架'
    __IsSelAllFile = True
    def __init__(self, parent=None):
        super(MainWndow, self).__init__(parent)
        self.setupUi(self)
        self.InitUi()
        self.InitConnect()

    # 初始化界面
    def InitUi(self):
        # 初始化导入数据列表头
        listHeader = [" ", "名称", "修改日期", "类型", "大小"]
        self.tableImportData.setColumnCount(len(listHeader))
        self.tableImportData.setHorizontalHeaderLabels(listHeader)
        self.tableImportData.verticalHeader().setHidden(True)
        #禁止编辑
        self.tableImportData.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #整行选中
        self.tableImportData.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableImportData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableImportData.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    # 绑定信号槽
    def InitConnect(self):
        self.btnImportData.clicked.connect(self.slotImportData)
        self.checkBoxSelFile.clicked.connect(self.slotSelFile)
        self.tableImportData.cellDoubleClicked .connect(self.slotTableImportData)

    def slotImportData(self):
        self.listAllFiles = []
        strDirPath = QFileDialog.getExistingDirectory(self, "选择文件夹")
        files = glob.glob(strDirPath + '/**',recursive=True)
        for file in files:
            if QFileInfo(file).suffix() == "xlsx" or QFileInfo(file).suffix() == "xls":
                self.listAllFiles.append(file)
                CntRow = self.tableImportData.rowCount()
                self.tableImportData.insertRow(CntRow)
                checkitem = QCheckBox()
                checkitem.setChecked(False)
                self.tableImportData.setCellWidget(CntRow, 0, checkitem)
                self.tableImportData.setItem(CntRow, 1, QTableWidgetItem(QFileInfo(file).baseName()))
                strDate = QFileInfo(file).lastModified().toString("yyyy/MM/dd hh:mm:ss")
                self.tableImportData.setItem(CntRow, 2, QTableWidgetItem(strDate))
                self.tableImportData.setItem(CntRow, 3, QTableWidgetItem("XLSX工作表"))
                fileSize = QFileInfo(file).size() / 1024
                self.tableImportData.setItem(CntRow, 4, QTableWidgetItem(str(fileSize) + "KB"))

    def slotSelFile(self):
        if self.__IsSelAllFile == True:
            CountRow = self.tableImportData.rowCount()
            for index in range(CountRow):
                curCellWidget = self.tableImportData.cellWidget(index,0)
                curCellWidget.setChecked(True)
                self.__IsSelAllFile = False
        else:
            CountRow = self.tableImportData.rowCount()
            for index in range(CountRow):
                curCellWidget = self.tableImportData.cellWidget(index,0)
                curCellWidget.setChecked(False)
                self.__IsSelAllFile = True

    def slotTableImportData(self, CurRow, curCol):
        strFileName = self.tableImportData.item(CurRow, 1).text()
        for file in self.listAllFiles:
            if QFileInfo(file).baseName() == strFileName:
                m_ParsingExcel = cParsingExcel(file)
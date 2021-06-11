from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog, QTableWidgetItem
from DlgParsingExcel import Ui_dlgParsingExcel
import openpyxl

from ReadExcelThread import cReadExcelThread

class cParsingExcel(QDialog, Ui_dlgParsingExcel):
    def __init__(self, strFile):
        super(cParsingExcel, self).__init__()
        self.m_CurRow = -1
        self.setupUi(self)
        self.m_ReadExcelThread = cReadExcelThread(strFile)
        self.m_ReadExcelThread.signalAppendItem.connect(self.slotInserItem,Qt.BlockingQueuedConnection)
        self.m_ReadExcelThread.start()
        self.Initialize()
        self.exec()

    def slotInserItem(self,listData):
        self.m_CurRow += 1
        print("行号", self.m_CurRow)
        for col in range(7):
            self.tableWidget.setItem(self.m_CurRow,col, QTableWidgetItem(str(listData[col])))
            if col == 0:
                self.m_shopName.add(listData[col])
            elif col == 1:
                self.ccbCommodityCode.add(listData[col])
            elif col == 2:
                self.ccbSpecification.add(listData[col])
            elif col == 3:
                self.ccbOrderStatusOl.add(listData[col])
            elif col == 4:
                self.ccbDetailStatus.add(listData[col])
            elif col == 5:
                self.ccbTotalRealPay.add(listData[col])
            elif col == 6:
                self.ccbNumber.add(listData[col])

    def Initialize(self):
        self.tableWidget.setRowCount(self.m_ReadExcelThread.CurFileMaxRow() - 1)
        self.cbbShopName.addItem("None")
        self.ccbCommodityCode.addItem("None")
        self.ccbSpecification.addItem("None")
        self.ccbOrderStatusOl.addItem("None")
        self.ccbDetailStatus.addItem("None")
        self.ccbTotalRealPay.addItem("None")
        self.ccbNumber.addItem("None")

        self.m_shopName = set()
        self.m_commodityCode = set()
        self.m_specification = set()
        self.m_OrderStatusOl = set()
        self.m_detailStatus = set()
        self.m_totalRealPay = set()
        self.m_number = set()
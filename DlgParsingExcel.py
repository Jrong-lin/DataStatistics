# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgParsingExcel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgParsingExcel(object):
    def setupUi(self, dlgParsingExcel):
        dlgParsingExcel.setObjectName("dlgParsingExcel")
        dlgParsingExcel.resize(1156, 662)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(dlgParsingExcel)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(dlgParsingExcel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(dlgParsingExcel)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.ccbDetailStatus = QtWidgets.QComboBox(self.groupBox)
        self.ccbDetailStatus.setObjectName("ccbDetailStatus")
        self.gridLayout.addWidget(self.ccbDetailStatus, 4, 1, 1, 1)
        self.cbbShopName = QtWidgets.QComboBox(self.groupBox)
        self.cbbShopName.setObjectName("cbbShopName")
        self.gridLayout.addWidget(self.cbbShopName, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.ccbOrderStatusOl = QtWidgets.QComboBox(self.groupBox)
        self.ccbOrderStatusOl.setObjectName("ccbOrderStatusOl")
        self.gridLayout.addWidget(self.ccbOrderStatusOl, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.ccbTotalRealPay = QtWidgets.QComboBox(self.groupBox)
        self.ccbTotalRealPay.setObjectName("ccbTotalRealPay")
        self.gridLayout.addWidget(self.ccbTotalRealPay, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.ccbCommodityCode = QtWidgets.QComboBox(self.groupBox)
        self.ccbCommodityCode.setObjectName("ccbCommodityCode")
        self.gridLayout.addWidget(self.ccbCommodityCode, 1, 1, 1, 1)
        self.ccbNumber = QtWidgets.QComboBox(self.groupBox)
        self.ccbNumber.setObjectName("ccbNumber")
        self.gridLayout.addWidget(self.ccbNumber, 6, 1, 1, 1)
        self.ccbSpecification = QtWidgets.QComboBox(self.groupBox)
        self.ccbSpecification.setObjectName("ccbSpecification")
        self.gridLayout.addWidget(self.ccbSpecification, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnStart = QtWidgets.QPushButton(self.groupBox)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(dlgParsingExcel)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 1)

        self.retranslateUi(dlgParsingExcel)
        QtCore.QMetaObject.connectSlotsByName(dlgParsingExcel)

    def retranslateUi(self, dlgParsingExcel):
        _translate = QtCore.QCoreApplication.translate
        dlgParsingExcel.setWindowTitle(_translate("dlgParsingExcel", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dlgParsingExcel", "????????????"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dlgParsingExcel", "[??????]????????????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dlgParsingExcel", "[??????]??????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("dlgParsingExcel", "??????????????????"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("dlgParsingExcel", "????????????"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("dlgParsingExcel", "????????????"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("dlgParsingExcel", "??????"))
        self.groupBox.setTitle(_translate("dlgParsingExcel", "????????????"))
        self.label_8.setText(_translate("dlgParsingExcel", "??????"))
        self.label_3.setText(_translate("dlgParsingExcel", "[??????]????????????"))
        self.label_2.setText(_translate("dlgParsingExcel", "????????????"))
        self.label_5.setText(_translate("dlgParsingExcel", "??????????????????"))
        self.label_7.setText(_translate("dlgParsingExcel", "????????????"))
        self.label_4.setText(_translate("dlgParsingExcel", "[??????]????????????"))
        self.label_6.setText(_translate("dlgParsingExcel", "????????????"))
        self.btnStart.setText(_translate("dlgParsingExcel", "????????????"))
        self.groupBox_2.setTitle(_translate("dlgParsingExcel", "??????"))

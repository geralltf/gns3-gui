# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/builtin/ui/ethernet_switch_configuration_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ethernetSwitchConfigPageWidget(object):
    def setupUi(self, ethernetSwitchConfigPageWidget):
        ethernetSwitchConfigPageWidget.setObjectName("ethernetSwitchConfigPageWidget")
        ethernetSwitchConfigPageWidget.resize(708, 653)
        self.gridLayout_2 = QtWidgets.QGridLayout(ethernetSwitchConfigPageWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiGeneralGroupBox = QtWidgets.QGroupBox(ethernetSwitchConfigPageWidget)
        self.uiGeneralGroupBox.setObjectName("uiGeneralGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.uiGeneralGroupBox)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiGeneralGroupBox)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiDefaultNameFormatLabel = QtWidgets.QLabel(self.uiGeneralGroupBox)
        self.uiDefaultNameFormatLabel.setObjectName("uiDefaultNameFormatLabel")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLabel, 1, 0, 1, 1)
        self.uiDefaultNameFormatLineEdit = QtWidgets.QLineEdit(self.uiGeneralGroupBox)
        self.uiDefaultNameFormatLineEdit.setObjectName("uiDefaultNameFormatLineEdit")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLineEdit, 1, 1, 1, 1)
        self.uiSymbolLabel = QtWidgets.QLabel(self.uiGeneralGroupBox)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.uiGeneralGroupBox)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.uiGeneralGroupBox)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.uiCategoryLabel = QtWidgets.QLabel(self.uiGeneralGroupBox)
        self.uiCategoryLabel.setObjectName("uiCategoryLabel")
        self.gridLayout.addWidget(self.uiCategoryLabel, 3, 0, 1, 1)
        self.uiCategoryComboBox = QtWidgets.QComboBox(self.uiGeneralGroupBox)
        self.uiCategoryComboBox.setObjectName("uiCategoryComboBox")
        self.gridLayout.addWidget(self.uiCategoryComboBox, 3, 1, 1, 1)
        self.uiConsoleTypeLabel = QtWidgets.QLabel(self.uiGeneralGroupBox)
        self.uiConsoleTypeLabel.setObjectName("uiConsoleTypeLabel")
        self.gridLayout.addWidget(self.uiConsoleTypeLabel, 4, 0, 1, 1)
        self.uiConsoleTypeComboBox = QtWidgets.QComboBox(self.uiGeneralGroupBox)
        self.uiConsoleTypeComboBox.setObjectName("uiConsoleTypeComboBox")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.uiConsoleTypeComboBox, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiGeneralGroupBox, 0, 0, 1, 2)
        self.uiEthernetSwitchSettingsGroupBox = QtWidgets.QGroupBox(ethernetSwitchConfigPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEthernetSwitchSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.uiEthernetSwitchSettingsGroupBox.setSizePolicy(sizePolicy)
        self.uiEthernetSwitchSettingsGroupBox.setObjectName("uiEthernetSwitchSettingsGroupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.uiEthernetSwitchSettingsGroupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(self.uiEthernetSwitchSettingsGroupBox)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.uiPortSpinBox = QtWidgets.QSpinBox(self.uiEthernetSwitchSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiPortSpinBox.setSizePolicy(sizePolicy)
        self.uiPortSpinBox.setMinimum(0)
        self.uiPortSpinBox.setMaximum(65535)
        self.uiPortSpinBox.setProperty("value", 0)
        self.uiPortSpinBox.setObjectName("uiPortSpinBox")
        self.gridlayout.addWidget(self.uiPortSpinBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.uiEthernetSwitchSettingsGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.uiVlanSpinBox = QtWidgets.QSpinBox(self.uiEthernetSwitchSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVlanSpinBox.sizePolicy().hasHeightForWidth())
        self.uiVlanSpinBox.setSizePolicy(sizePolicy)
        self.uiVlanSpinBox.setMinimum(1)
        self.uiVlanSpinBox.setMaximum(65535)
        self.uiVlanSpinBox.setProperty("value", 1)
        self.uiVlanSpinBox.setObjectName("uiVlanSpinBox")
        self.gridlayout.addWidget(self.uiVlanSpinBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.uiEthernetSwitchSettingsGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.uiEthernetSwitchSettingsGroupBox)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.uiPortTypeComboBox = QtWidgets.QComboBox(self.uiEthernetSwitchSettingsGroupBox)
        self.uiPortTypeComboBox.setObjectName("uiPortTypeComboBox")
        self.uiPortTypeComboBox.addItem("")
        self.uiPortTypeComboBox.addItem("")
        self.uiPortTypeComboBox.addItem("")
        self.gridlayout.addWidget(self.uiPortTypeComboBox, 2, 1, 1, 1)
        self.uiPortEtherTypeComboBox = QtWidgets.QComboBox(self.uiEthernetSwitchSettingsGroupBox)
        self.uiPortEtherTypeComboBox.setEnabled(False)
        self.uiPortEtherTypeComboBox.setObjectName("uiPortEtherTypeComboBox")
        self.uiPortEtherTypeComboBox.addItem("")
        self.uiPortEtherTypeComboBox.addItem("")
        self.uiPortEtherTypeComboBox.addItem("")
        self.uiPortEtherTypeComboBox.addItem("")
        self.gridlayout.addWidget(self.uiPortEtherTypeComboBox, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiEthernetSwitchSettingsGroupBox, 1, 0, 1, 1)
        self.uiEthernetSwitchPortsGroupBox = QtWidgets.QGroupBox(ethernetSwitchConfigPageWidget)
        self.uiEthernetSwitchPortsGroupBox.setObjectName("uiEthernetSwitchPortsGroupBox")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.uiEthernetSwitchPortsGroupBox)
        self.vboxlayout.setObjectName("vboxlayout")
        self.uiPortsTreeWidget = QtWidgets.QTreeWidget(self.uiEthernetSwitchPortsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiPortsTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiPortsTreeWidget.setSizePolicy(sizePolicy)
        self.uiPortsTreeWidget.setRootIsDecorated(False)
        self.uiPortsTreeWidget.setObjectName("uiPortsTreeWidget")
        self.vboxlayout.addWidget(self.uiPortsTreeWidget)
        self.gridLayout_2.addWidget(self.uiEthernetSwitchPortsGroupBox, 1, 1, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiAddPushButton = QtWidgets.QPushButton(ethernetSwitchConfigPageWidget)
        self.uiAddPushButton.setObjectName("uiAddPushButton")
        self.horizontalLayout.addWidget(self.uiAddPushButton)
        self.uiDeletePushButton = QtWidgets.QPushButton(ethernetSwitchConfigPageWidget)
        self.uiDeletePushButton.setEnabled(False)
        self.uiDeletePushButton.setObjectName("uiDeletePushButton")
        self.horizontalLayout.addWidget(self.uiDeletePushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)

        self.retranslateUi(ethernetSwitchConfigPageWidget)
        QtCore.QMetaObject.connectSlotsByName(ethernetSwitchConfigPageWidget)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiPortSpinBox, self.uiVlanSpinBox)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiVlanSpinBox, self.uiPortTypeComboBox)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiPortTypeComboBox, self.uiAddPushButton)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiAddPushButton, self.uiDeletePushButton)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiDeletePushButton, self.uiPortsTreeWidget)

    def retranslateUi(self, ethernetSwitchConfigPageWidget):
        _translate = QtCore.QCoreApplication.translate
        ethernetSwitchConfigPageWidget.setWindowTitle(_translate("ethernetSwitchConfigPageWidget", "Ethernet switch template configuration"))
        self.uiGeneralGroupBox.setTitle(_translate("ethernetSwitchConfigPageWidget", "General"))
        self.uiNameLabel.setText(_translate("ethernetSwitchConfigPageWidget", "Name:"))
        self.uiDefaultNameFormatLabel.setText(_translate("ethernetSwitchConfigPageWidget", "Default name format:"))
        self.uiSymbolLabel.setText(_translate("ethernetSwitchConfigPageWidget", "Symbol:"))
        self.uiSymbolToolButton.setText(_translate("ethernetSwitchConfigPageWidget", "&Browse..."))
        self.uiCategoryLabel.setText(_translate("ethernetSwitchConfigPageWidget", "Category:"))
        self.uiConsoleTypeLabel.setText(_translate("ethernetSwitchConfigPageWidget", "Console type:"))
        self.uiConsoleTypeComboBox.setItemText(0, _translate("ethernetSwitchConfigPageWidget", "telnet"))
        self.uiConsoleTypeComboBox.setItemText(1, _translate("ethernetSwitchConfigPageWidget", "none"))
        self.uiEthernetSwitchSettingsGroupBox.setTitle(_translate("ethernetSwitchConfigPageWidget", "Settings"))
        self.label.setText(_translate("ethernetSwitchConfigPageWidget", "Port:"))
        self.label_3.setText(_translate("ethernetSwitchConfigPageWidget", "VLAN:"))
        self.label_2.setText(_translate("ethernetSwitchConfigPageWidget", "Type:"))
        self.label_4.setText(_translate("ethernetSwitchConfigPageWidget", "QinQ EtherType:"))
        self.uiPortTypeComboBox.setItemText(0, _translate("ethernetSwitchConfigPageWidget", "access"))
        self.uiPortTypeComboBox.setItemText(1, _translate("ethernetSwitchConfigPageWidget", "dot1q"))
        self.uiPortTypeComboBox.setItemText(2, _translate("ethernetSwitchConfigPageWidget", "qinq"))
        self.uiPortEtherTypeComboBox.setItemText(0, _translate("ethernetSwitchConfigPageWidget", "0x8100"))
        self.uiPortEtherTypeComboBox.setItemText(1, _translate("ethernetSwitchConfigPageWidget", "0x88A8"))
        self.uiPortEtherTypeComboBox.setItemText(2, _translate("ethernetSwitchConfigPageWidget", "0x9100"))
        self.uiPortEtherTypeComboBox.setItemText(3, _translate("ethernetSwitchConfigPageWidget", "0x9200"))
        self.uiEthernetSwitchPortsGroupBox.setTitle(_translate("ethernetSwitchConfigPageWidget", "Ports"))
        self.uiPortsTreeWidget.headerItem().setText(0, _translate("ethernetSwitchConfigPageWidget", "Port"))
        self.uiPortsTreeWidget.headerItem().setText(1, _translate("ethernetSwitchConfigPageWidget", "VLAN"))
        self.uiPortsTreeWidget.headerItem().setText(2, _translate("ethernetSwitchConfigPageWidget", "Type"))
        self.uiPortsTreeWidget.headerItem().setText(3, _translate("ethernetSwitchConfigPageWidget", "EtherType"))
        self.uiAddPushButton.setText(_translate("ethernetSwitchConfigPageWidget", "&Add"))
        self.uiDeletePushButton.setText(_translate("ethernetSwitchConfigPageWidget", "&Delete"))


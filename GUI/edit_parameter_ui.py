# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_parameter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editParameter(object):
    def setupUi(self, editParameter):
        editParameter.setObjectName("editParameter")
        editParameter.resize(552, 274)
        self.buttonBox = QtWidgets.QDialogButtonBox(editParameter)
        self.buttonBox.setGeometry(QtCore.QRect(170, 230, 151, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(editParameter)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 518, 205))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deviceLayout = QtWidgets.QHBoxLayout()
        self.deviceLayout.setObjectName("deviceLayout")
        spacerItem = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.deviceLayout.addItem(spacerItem)
        self.deviceLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.deviceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deviceLabel.setObjectName("deviceLabel")
        self.deviceLayout.addWidget(self.deviceLabel)
        self.deviceBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.deviceBox.setObjectName("deviceBox")
        self.deviceLayout.addWidget(self.deviceBox)
        spacerItem1 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.deviceLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.deviceLayout)
        self.paramsLayout = QtWidgets.QHBoxLayout()
        self.paramsLayout.setObjectName("paramsLayout")
        self.followParamsLayout = QtWidgets.QVBoxLayout()
        self.followParamsLayout.setObjectName("followParamsLayout")
        self.followParamsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.followParamsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.followParamsLabel.setObjectName("followParamsLabel")
        self.followParamsLayout.addWidget(self.followParamsLabel)
        self.followParamsWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.followParamsWidget.setObjectName("followParamsWidget")
        self.followParamsLayout.addWidget(self.followParamsWidget)
        self.paramsLayout.addLayout(self.followParamsLayout)
        self.followButtonLayout = QtWidgets.QVBoxLayout()
        self.followButtonLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.followButtonLayout.setObjectName("followButtonLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.followButtonLayout.addItem(spacerItem2)
        self.addFollowButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addFollowButton.sizePolicy().hasHeightForWidth())
        self.addFollowButton.setSizePolicy(sizePolicy)
        self.addFollowButton.setObjectName("addFollowButton")
        self.followButtonLayout.addWidget(self.addFollowButton)
        self.delFollowButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delFollowButton.setObjectName("delFollowButton")
        self.followButtonLayout.addWidget(self.delFollowButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.followButtonLayout.addItem(spacerItem3)
        self.paramsLayout.addLayout(self.followButtonLayout)
        self.allParamsLayout = QtWidgets.QVBoxLayout()
        self.allParamsLayout.setObjectName("allParamsLayout")
        self.allParamsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.allParamsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.allParamsLabel.setObjectName("allParamsLabel")
        self.allParamsLayout.addWidget(self.allParamsLabel)
        self.allParamsWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.allParamsWidget.setObjectName("allParamsWidget")
        self.allParamsLayout.addWidget(self.allParamsWidget)
        self.paramsLayout.addLayout(self.allParamsLayout)
        self.setButtonLayout = QtWidgets.QVBoxLayout()
        self.setButtonLayout.setObjectName("setButtonLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.setButtonLayout.addItem(spacerItem4)
        self.addSetButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addSetButton.setObjectName("addSetButton")
        self.setButtonLayout.addWidget(self.addSetButton)
        self.delSetButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delSetButton.setObjectName("delSetButton")
        self.setButtonLayout.addWidget(self.delSetButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.setButtonLayout.addItem(spacerItem5)
        self.paramsLayout.addLayout(self.setButtonLayout)
        self.setParamLayout = QtWidgets.QVBoxLayout()
        self.setParamLayout.setObjectName("setParamLayout")
        self.setParamsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.setParamsLabel.setObjectName("setParamsLabel")
        self.setParamLayout.addWidget(self.setParamsLabel)
        self.setParamsWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.setParamsWidget.setObjectName("setParamsWidget")
        self.setParamLayout.addWidget(self.setParamsWidget)
        self.paramsLayout.addLayout(self.setParamLayout)
        self.verticalLayout.addLayout(self.paramsLayout)

        self.retranslateUi(editParameter)
        self.buttonBox.accepted.connect(editParameter.accept)
        self.buttonBox.rejected.connect(editParameter.reject)
        QtCore.QMetaObject.connectSlotsByName(editParameter)

    def retranslateUi(self, editParameter):
        _translate = QtCore.QCoreApplication.translate
        editParameter.setWindowTitle(_translate("editParameter", "Dialog"))
        self.deviceLabel.setText(_translate("editParameter", "Device"))
        self.followParamsLabel.setText(_translate("editParameter", "Follow Parameters"))
        self.addFollowButton.setText(_translate("editParameter", "<<"))
        self.delFollowButton.setText(_translate("editParameter", ">>"))
        self.allParamsLabel.setText(_translate("editParameter", "             All Parameters              "))
        self.addSetButton.setText(_translate("editParameter", ">>"))
        self.delSetButton.setText(_translate("editParameter", "<<"))
        self.setParamsLabel.setText(_translate("editParameter", "   Set Parameters   "))


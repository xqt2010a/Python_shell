# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python_study\Python_Study\06_PyQt5_Eric6\zdy_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        dialog.setSizeGripEnabled(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 250, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_tj = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_tj.setObjectName("pushButton_tj")
        self.horizontalLayout.addWidget(self.pushButton_tj)
        self.pushButton_2cz = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2cz.setObjectName("pushButton_2cz")
        self.horizontalLayout.addWidget(self.pushButton_2cz)
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 201, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_xm = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_xm.setObjectName("label_xm")
        self.horizontalLayout_2.addWidget(self.label_xm)
        self.lineEdit_xm = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_xm.setObjectName("lineEdit_xm")
        self.horizontalLayout_2.addWidget(self.lineEdit_xm)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2xb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2xb.setObjectName("label_2xb")
        self.horizontalLayout_8.addWidget(self.label_2xb)
        self.radioButton_2boy = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2boy.setObjectName("radioButton_2boy")
        self.horizontalLayout_8.addWidget(self.radioButton_2boy)
        self.radioButton_1girl = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_1girl.setObjectName("radioButton_1girl")
        self.horizontalLayout_8.addWidget(self.radioButton_1girl)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3nl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3nl.setObjectName("label_3nl")
        self.horizontalLayout_9.addWidget(self.label_3nl)
        self.lineEdit_7nl = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7nl.setObjectName("lineEdit_7nl")
        self.horizontalLayout_9.addWidget(self.lineEdit_7nl)
        self.toolButton_2nl = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_2nl.setObjectName("toolButton_2nl")
        self.horizontalLayout_9.addWidget(self.toolButton_2nl)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4sg = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4sg.setObjectName("label_4sg")
        self.horizontalLayout_10.addWidget(self.label_4sg)
        self.lineEdit_8sg = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_8sg.setObjectName("lineEdit_8sg")
        self.horizontalLayout_10.addWidget(self.lineEdit_8sg)
        self.toolButton_sg = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_sg.setObjectName("toolButton_sg")
        self.horizontalLayout_10.addWidget(self.toolButton_sg)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9dh = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9dh.setObjectName("label_9dh")
        self.horizontalLayout_7.addWidget(self.label_9dh)
        self.lineEdit_9dh = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_9dh.setObjectName("lineEdit_9dh")
        self.horizontalLayout_7.addWidget(self.lineEdit_9dh)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "用户信息录入"))
        self.pushButton_tj.setText(_translate("dialog", "提交"))
        self.pushButton_2cz.setText(_translate("dialog", "重置"))
        self.label_xm.setText(_translate("dialog", "姓名"))
        self.label_2xb.setText(_translate("dialog", "性别"))
        self.radioButton_2boy.setText(_translate("dialog", "男"))
        self.radioButton_1girl.setText(_translate("dialog", "女"))
        self.label_3nl.setText(_translate("dialog", "年龄"))
        self.toolButton_2nl.setText(_translate("dialog", "..."))
        self.label_4sg.setText(_translate("dialog", "身高"))
        self.toolButton_sg.setText(_translate("dialog", "..."))
        self.label_9dh.setText(_translate("dialog", "电话"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())


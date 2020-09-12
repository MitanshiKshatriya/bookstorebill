# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm6.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 324)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 371, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.book_title_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.book_title_le.setObjectName("book_title_le")
        self.horizontalLayout.addWidget(self.book_title_le)
        self.find_price_pb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.find_price_pb.setObjectName("find_price_pb")
        self.horizontalLayout.addWidget(self.find_price_pb)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 180, 371, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.quantity_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.quantity_le.setObjectName("quantity_le")
        self.horizontalLayout_2.addWidget(self.quantity_le)
        self.find_total_pb = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.find_total_pb.setObjectName("find_total_pb")
        self.horizontalLayout_2.addWidget(self.find_total_pb)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 130, 361, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.price_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.price_le.setObjectName("price_le")
        self.horizontalLayout_3.addWidget(self.price_le)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(19, 270, 371, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.total_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.total_le.setObjectName("total_le")
        self.horizontalLayout_4.addWidget(self.total_le)

        ###conecting the buttons
        self.find_price_pb.clicked.connect(self.find_book)
        self.find_total_pb.clicked.connect(self.find_total)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Book Title"))
        self.find_price_pb.setText(_translate("Form", "Find Price"))
        self.label_2.setText(_translate("Form", "Qunatity"))
        self.find_total_pb.setText(_translate("Form", "Find Total"))
        self.label_3.setText(_translate("Form", "Price"))
        self.label_4.setText(_translate("Form", "Total"))

    def find_book(self):
        bk=sqlite3.connect('booksM6.db')
        curbk=bk.cursor()
        title=self.book_title_le.text()
        curbk.execute("SELECT price FROM bookdb WHERE title=?", (title,))

        try:
            result=cur.fetchall()
            price=result[3]
            print(result)
            self.price_le.setText(str(price))
            

        except:
            self.price_le.setText("Book not found")
    ##function for findind book's price and total
    def find_total(self):
        qty=int(self.quantity_le.text())
        bk=sqlite3.connect('booksM6.db')
        curbk=bk.cursor()
        title=self.book_title_le.text()
        curbk.execute("SELECT price FROM bookdb WHERE title=?", (title,))
        result=cur.fetchone()
        price=result[3]
        self.total_le.setText(str(price*qty))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


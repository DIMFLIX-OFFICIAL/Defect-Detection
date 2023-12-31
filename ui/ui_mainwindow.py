# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(392, 596)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/logo/resources/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #9382FF;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #9382FF;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #9382FF;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: #9382FF;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add"
                        "-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #9382FF;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #9382FF;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-p"
                        "age:horizontal\n"
"{\n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.backgground = QFrame(self.centralwidget)
        self.backgground.setObjectName(u"backgground")
        self.backgground.setStyleSheet(u"QFrame {\n"
"	background-color: #3C3656;\n"
"	border-radius: 25px;\n"
"}")
        self.backgground.setFrameShape(QFrame.StyledPanel)
        self.backgground.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.backgground)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.backgground)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #3C3656;")
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_2 = QVBoxLayout(self.settings_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.drag_and_drop = QFrame(self.settings_page)
        self.drag_and_drop.setObjectName(u"drag_and_drop")
        self.drag_and_drop.setMaximumSize(QSize(16777215, 350))
        self.drag_and_drop.setStyleSheet(u"border: 5px solid #9382FF;\n"
"border-style: dashed;\n"
"")
        self.drag_and_drop.setFrameShape(QFrame.StyledPanel)
        self.drag_and_drop.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.drag_and_drop)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.drag_and_drop_title = QLabel(self.drag_and_drop)
        self.drag_and_drop_title.setObjectName(u"drag_and_drop_title")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.drag_and_drop_title.setFont(font)
        self.drag_and_drop_title.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	color: #FFFFFF;\n"
"}")

        self.verticalLayout_3.addWidget(self.drag_and_drop_title, 0, Qt.AlignHCenter)

        self.el_in_drag_and_drop = QFrame(self.drag_and_drop)
        self.el_in_drag_and_drop.setObjectName(u"el_in_drag_and_drop")
        self.el_in_drag_and_drop.setMinimumSize(QSize(80, 30))
        self.el_in_drag_and_drop.setMaximumSize(QSize(16777215, 30))
        self.el_in_drag_and_drop.setStyleSheet(u"border: none; \n"
"background-color: #564D7A; \n"
"border-radius: 15px;")
        self.el_in_drag_and_drop.setFrameShape(QFrame.StyledPanel)
        self.el_in_drag_and_drop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.el_in_drag_and_drop)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 3, 0)
        self.filename = QLabel(self.el_in_drag_and_drop)
        self.filename.setObjectName(u"filename")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.filename.setFont(font1)
        self.filename.setStyleSheet(u"color: #FFFFFF")

        self.horizontalLayout_2.addWidget(self.filename)

        self.del_element_in_drag_end_drop = QPushButton(self.el_in_drag_and_drop)
        self.del_element_in_drag_end_drop.setObjectName(u"del_element_in_drag_end_drop")
        self.del_element_in_drag_end_drop.setMinimumSize(QSize(30, 30))
        self.del_element_in_drag_end_drop.setMaximumSize(QSize(30, 30))
        self.del_element_in_drag_end_drop.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/close/resources/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.del_element_in_drag_end_drop.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.del_element_in_drag_end_drop)


        self.verticalLayout_3.addWidget(self.el_in_drag_and_drop, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.drag_and_drop)

        self.save_to_folder_checkbox = QCheckBox(self.settings_page)
        self.save_to_folder_checkbox.setObjectName(u"save_to_folder_checkbox")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.save_to_folder_checkbox.setFont(font2)
        self.save_to_folder_checkbox.setStyleSheet(u"QCheckBox {\n"
"	background: #423B5E;\n"
"	border-radius: 10px;\n"
"	padding-left: 10%;\n"
"	padding-top: 10px; \n"
"	padding-bottom: 10px; \n"
"    color: #FFFFFF;\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #564D7A;\n"
"    background: #4C446D;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid #9382FF;\n"
"    background: #9382FF;\n"
"	image: url(:/check/resources/check.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px solid #9382FF;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/check/C:/Users/dimap/Downloads/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_to_folder_checkbox.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.save_to_folder_checkbox)

        self.StartAIBtn = QPushButton(self.settings_page)
        self.StartAIBtn.setObjectName(u"StartAIBtn")
        self.StartAIBtn.setMinimumSize(QSize(0, 50))
        self.StartAIBtn.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.StartAIBtn.setFont(font3)
        self.StartAIBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #9382FF;\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.StartAIBtn)

        self.stackedWidget.addWidget(self.settings_page)
        self.results_page = QWidget()
        self.results_page.setObjectName(u"results_page")
        self.verticalLayout_4 = QVBoxLayout(self.results_page)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.DefectsFinded = QLabel(self.results_page)
        self.DefectsFinded.setObjectName(u"DefectsFinded")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.DefectsFinded.setFont(font4)
        self.DefectsFinded.setStyleSheet(u"color: #FFFFFF;")
        self.DefectsFinded.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.DefectsFinded)

        self.defectList = QListWidget(self.results_page)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        QListWidgetItem(self.defectList)
        self.defectList.setObjectName(u"defectList")
        self.defectList.setFont(font1)
        self.defectList.setFocusPolicy(Qt.NoFocus)
        self.defectList.setStyleSheet(u"QListWidget {\n"
"        background-color: transparent;\n"
"		padding: 15px 10px;	\n"
"    }\n"
"    QListWidget::item {\n"
"		background-color: #564D7A;\n"
"		padding: 10px;\n"
"		border-radius: 5px;\n"
"        color: white;\n"
"        padding: 5px;\n"
"		margin-bottom: 10px;\n"
"		margin-right: 10px;\n"
"    }\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(56, 56, 85);\n"
" }")
        self.defectList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.defectList.setProperty("showDropIndicator", False)
        self.defectList.setSelectionMode(QAbstractItemView.NoSelection)
        self.defectList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.defectList.setTextElideMode(Qt.ElideNone)
        self.defectList.setSelectionRectVisible(False)

        self.verticalLayout_4.addWidget(self.defectList)

        self.BackBtn = QPushButton(self.results_page)
        self.BackBtn.setObjectName(u"BackBtn")
        self.BackBtn.setMinimumSize(QSize(0, 50))
        self.BackBtn.setFont(font3)
        self.BackBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #9382FF;\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: #FFFFFF;\n"
"}")

        self.verticalLayout_4.addWidget(self.BackBtn)

        self.stackedWidget.addWidget(self.results_page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.header = QFrame(self.backgground)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 40))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Title = QLabel(self.header)
        self.Title.setObjectName(u"Title")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.Title.setFont(font5)
        self.Title.setStyleSheet(u"QLabel {\n"
"	color: #FFFFFF;\n"
"}")

        self.horizontalLayout.addWidget(self.Title)

        self.maximize_btn = QPushButton(self.header)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setMinimumSize(QSize(20, 20))
        self.maximize_btn.setMaximumSize(QSize(20, 20))
        self.maximize_btn.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"border-radius: 10px;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.maximize_btn)

        self.minimize_btn = QPushButton(self.header)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(20, 20))
        self.minimize_btn.setMaximumSize(QSize(20, 20))
        self.minimize_btn.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.header)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(20, 20))
        self.close_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"	border-radius: 10px;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.close_btn)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.backgground)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DEFFECT SENSE AI", None))
        self.drag_and_drop_title.setText(QCoreApplication.translate("MainWindow", u"Drop your file here!", None))
        self.filename.setText(QCoreApplication.translate("MainWindow", u"File.txt", None))
        self.del_element_in_drag_end_drop.setText("")
        self.save_to_folder_checkbox.setText(QCoreApplication.translate("MainWindow", u"Save to folder \"Results\"", None))
        self.StartAIBtn.setText(QCoreApplication.translate("MainWindow", u"Start Processing", None))
        self.DefectsFinded.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043e \u0434\u0435\u0444\u0435\u043a\u0442\u043e\u0432: ", None))

        __sortingEnabled = self.defectList.isSortingEnabled()
        self.defectList.setSortingEnabled(False)
        ___qlistwidgetitem = self.defectList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u044b\u0444\u0432", None));
        ___qlistwidgetitem1 = self.defectList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem2 = self.defectList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0444\u044b\u0432\u044b\u0444\u0432\u0444\u044b\u0432", None));
        ___qlistwidgetitem3 = self.defectList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem4 = self.defectList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem5 = self.defectList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem6 = self.defectList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem7 = self.defectList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem8 = self.defectList.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem9 = self.defectList.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem10 = self.defectList.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem11 = self.defectList.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem12 = self.defectList.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem13 = self.defectList.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem14 = self.defectList.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem15 = self.defectList.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem16 = self.defectList.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem17 = self.defectList.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem18 = self.defectList.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem19 = self.defectList.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem20 = self.defectList.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem21 = self.defectList.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem22 = self.defectList.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.defectList.setSortingEnabled(__sortingEnabled)

        self.BackBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u041d\u0430\u0437\u0430\u0434", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"<body>\n"
"<p>\n"
"DEFECT SENSE <span style=\"color: #9382FF;\">AI</span>\n"
"</p>\n"
"</body>\n"
"</html>", None))
        self.maximize_btn.setText("")
        self.minimize_btn.setText("")
        self.close_btn.setText("")
    # retranslateUi


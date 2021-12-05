from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 820)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 451, 761))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 30, 401, 621))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_12.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_12.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_12.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_12.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_12.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_12.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_12.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_12.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_12.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_12.addWidget(self.pushButton_13)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(40, 30, 361, 321))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(60, 370, 321, 111))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_14.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_14.addWidget(self.pushButton_15)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 20, 301, 71))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("height")
        self.horizontalLayout_11.addWidget(self.lineEdit_2)

        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit.setPlaceholderText("width")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_11.addWidget(self.lineEdit)

        self.pushButton_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_11.addWidget(self.pushButton_16)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 100, 301, 71))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")


        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("y1")
        self.horizontalLayout_12.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("y2")
        self.horizontalLayout_12.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText("x1")
        self.horizontalLayout_12.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setPlaceholderText("x2")
        self.horizontalLayout_12.addWidget(self.lineEdit_6)


        self.pushButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_12.addWidget(self.pushButton_17)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 175, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_5.addWidget(self.comboBox_3)
        self.pushButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_5.addWidget(self.pushButton_19)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 300, 175, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comboBox_4 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_6.addWidget(self.comboBox_4)
        self.pushButton_21 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_6.addWidget(self.pushButton_21)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 180, 175, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox_5 = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_7.addWidget(self.comboBox_5)
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_7.addWidget(self.pushButton_18)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 40, 411, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.blurLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.blurLabel.setObjectName("blurLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.blurLabel)
        self.horizontalSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider)
        self.contrastLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.contrastLabel.setObjectName("contrastLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.contrastLabel)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_2)
        self.exposure1Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.exposure1Label.setObjectName("exposure1Label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.exposure1Label)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_4)
        self.exposure2Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.exposure2Label.setObjectName("exposure2Label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.exposure2Label)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_3)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 50, 401, 621))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_22 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_16.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout_16.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_16.addWidget(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout_16.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout_16.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_16.addWidget(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_28.setObjectName("pushButton_28")
        self.verticalLayout_16.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_29.setObjectName("pushButton_29")
        self.verticalLayout_16.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_30.setObjectName("pushButton_30")
        self.verticalLayout_16.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_31.setObjectName("pushButton_31")
        self.verticalLayout_16.addWidget(self.pushButton_31)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 60, 361, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(490, 440, 361, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 400, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 770, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.canvas = FigureCanvas(Figure())
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.verticalLayout_9.addWidget(self.canvas)

        self.canvas1 = FigureCanvas(Figure())
        self.canvas1.axes = self.canvas1.figure.add_subplot(111)
        self.verticalLayout_10.addWidget(self.canvas1)

        self.canvas2 = FigureCanvas(Figure())
        self.canvas2.axes = self.canvas2.figure.add_subplot(111)
        self.verticalLayout_13.addWidget(self.canvas2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "Gaussian Filter"))
        self.pushButton_5.setText(_translate("Form", "Prewitt Filter"))
        self.pushButton_6.setText(_translate("Form", "Meijering Filter"))
        self.pushButton_7.setText(_translate("Form", "Median Filter"))
        self.pushButton_8.setText(_translate("Form", "Otsu Filter"))
        self.pushButton_9.setText(_translate("Form", "Unsharp Mask Filter"))
        self.pushButton_10.setText(_translate("Form", "Sauvola Filter"))
        self.pushButton_11.setText(_translate("Form", "Triangle Filter"))
        self.pushButton_12.setText(_translate("Form", "Yen Filter"))
        self.pushButton_13.setText(_translate("Form", "Li Filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Filters"))
        self.pushButton_14.setText(_translate("Form", "Histogram"))
        self.pushButton_15.setText(_translate("Form", "Histogram Equalization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Histogram"))
        self.pushButton_16.setText(_translate("Form", "Resize"))
        self.pushButton_17.setText(_translate("Form", "Crop"))
        self.pushButton_19.setText(_translate("Form", "Rotate"))
        self.pushButton_21.setText(_translate("Form", "Swirl"))
        self.pushButton_18.setText(_translate("Form", "Scale"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Transform"))
        self.blurLabel.setText(_translate("Form", "Gamma(1-100)"))
        self.contrastLabel.setText(_translate("Form", "Log Gain(0-1)"))
        self.exposure1Label.setText(_translate("Form", "RescaleIntensity InRange(0-100)"))
        self.exposure2Label.setText(_translate("Form", "Sigmoid Gain(10-100)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Exposure"))
        self.pushButton_22.setText(_translate("Form", "Erosion"))
        self.pushButton_23.setText(_translate("Form", "Dilation"))
        self.pushButton_24.setText(_translate("Form", "Opening"))
        self.pushButton_25.setText(_translate("Form", "Closing"))
        self.pushButton_26.setText(_translate("Form", "White Tophat"))
        self.pushButton_27.setText(_translate("Form", "Black Tophat"))
        self.pushButton_28.setText(_translate("Form", "Skeletonize"))
        self.pushButton_29.setText(_translate("Form", "Convex Hull"))
        self.pushButton_30.setText(_translate("Form", "Remove Small Holes"))
        self.pushButton_31.setText(_translate("Form", "Remove Small Object"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Morphology"))
        self.pushButton.setText(_translate("Form", "Load"))
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.pushButton_3.setText(_translate("Form", "Clear"))
        self.comboBox_5.addItem("0.25")
        self.comboBox_5.addItem("0.5")
        self.comboBox_5.addItem("0.75")
        self.comboBox_5.addItem("1")
        self.comboBox_3.addItem("90")
        self.comboBox_3.addItem("120")
        self.comboBox_3.addItem("150")
        self.comboBox_3.addItem("180")
        self.comboBox_3.addItem("270")
        self.comboBox_4.addItem("1")
        self.comboBox_4.addItem("5")
        self.comboBox_4.addItem("10")
        self.comboBox_4.addItem("100")


from skimage.util import crop

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from skimage import io, img_as_float, filters, morphology, data, img_as_ubyte,exposure
from skimage.transform import resize,rescale,rotate,swirl
from main import Ui_Form


class UI(QMainWindow):#tmp kullanırsak filtre kombalayabiliyoruz
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.loadImage)
        self.ui.pushButton_2.clicked.connect(self.savePhoto)
        self.ui.pushButton_3.clicked.connect(self.clearPhoto)
        self.ui.pushButton_4.clicked.connect(self.GaussianFilter)
        self.ui.pushButton_5.clicked.connect(self.PrewittFilter)
        self.ui.pushButton_6.clicked.connect(self.MeijeringFilter)
        self.ui.pushButton_7.clicked.connect(self.MedianFilter)
        self.ui.pushButton_8.clicked.connect(self.ThreshOldOtsuFilter)
        self.ui.pushButton_9.clicked.connect(self.UnsharpMaskFilter)
        self.ui.pushButton_10.clicked.connect(self.ThreshOldSauvolaFilter)
        self.ui.pushButton_11.clicked.connect(self.ThreshOldTriangleFilter)
        self.ui.pushButton_12.clicked.connect(self.ThreshOldYenFilter)
        self.ui.pushButton_13.clicked.connect(self.ThreshOldLiFilter)
        self.ui.pushButton_15.clicked.connect(self.HistogramEqualizationPhoto)

        self.ui.pushButton_16.clicked.connect(self.ResizedPhoto)
        self.ui.pushButton_17.clicked.connect(self.cropPhoto)
        self.ui.pushButton_18.clicked.connect(self.RescalePhoto)
        self.ui.pushButton_19.clicked.connect(self.RotatePhoto)
        self.ui.pushButton_21.clicked.connect(self.SwirlPhoto)
        self.ui.pushButton_14.clicked.connect(self.histogram)
        self.ui.pushButton_22.clicked.connect(self.ErosionPhoto)
        self.ui.pushButton_23.clicked.connect(self.DilationPhoto)
        self.ui.pushButton_24.clicked.connect(self.OpeningPhoto)
        self.ui.pushButton_25.clicked.connect(self.ClosingPhoto)
        self.ui.pushButton_26.clicked.connect(self.WhiteTophatPhoto)
        self.ui.pushButton_27.clicked.connect(self.BlackTophatPhoto)
        self.ui.pushButton_28.clicked.connect(self.SkeletonizePhoto)
        self.ui.pushButton_29.clicked.connect(self.ConvexHullPhoto)
        self.ui.pushButton_30.clicked.connect(self.SmallHolesPhoto)
        self.ui.pushButton_31.clicked.connect(self.SmallObjectPhoto)
        self.ui.horizontalSlider.valueChanged['int'].connect(self.adjustGammaPhoto)
        self.ui.horizontalSlider_2.valueChanged['int'].connect(self.RescaleIntensity)
        self.ui.horizontalSlider_3.valueChanged['int'].connect(self.adjustSigmoidPhoto)
        self.ui.horizontalSlider_4.valueChanged['int'].connect(self.adjustLogPhoto)
    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = io.imread(self.filename)
        self.loadedImage=self.image
        self.setPhoto(self.loadedImage,0)

    def setPhoto(self, image,canvasType):
        self.tmp = image
        image = img_as_float(self.tmp)
        if(canvasType==0):
            self.ui.canvas.axes.clear()
            self.ui.canvas.axes.imshow(image,cmap='gray')
            self.ui.canvas.draw()
        elif(canvasType==1):
            self.ui.canvas1.axes.clear()
            self.ui.canvas1.axes.imshow(image,cmap='gray')
            self.ui.canvas1.draw()
        else:
            self.ui.canvas2.axes.clear()
            self.ui.canvas2.axes.hist(image.ravel(), bins=256, range=(0.0, 1.0),color='black')
            self.ui.canvas2.draw()

    def histogram(self):
        image = img_as_float(self.image)
        self.setPhoto(image,canvasType=2)

    def HistogramEqualizationPhoto(self):
        equalization=exposure.equalize_hist(self.image)
        image = img_as_float(equalization)
        self.setPhoto(image,canvasType=2)
        self.setPhoto(image, canvasType=1)



    def savePhoto(self):
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        io.imsave(filename, self.tmp)

    def clearPhoto(self):
        self.setPhoto(self.loadedImage,canvasType=1)


    def GaussianFilter(self):
        filtered = filters.gaussian(self.image, sigma=1, multichannel=False)
        self.setPhoto(filtered,canvasType=1)

    def PrewittFilter(self):
        filtered = filters.prewitt(self.image)
        self.setPhoto(filtered,canvasType=1)

    def MeijeringFilter(self):
        filtered = filters.meijering(self.image, black_ridges=False, mode='mirror')
        self.setPhoto(filtered, canvasType=1)

    def MedianFilter(self):
        filtered=filters.median(self.image)
        self.setPhoto(filtered,canvasType=1)

    def ThreshOldOtsuFilter(self):
        filtered = filters.threshold_otsu(self.image)
        binary = filtered < self.image
        self.setPhoto(binary,canvasType=1)

    def UnsharpMaskFilter(self):
        filtered=filters.unsharp_mask(self.image)
        self.setPhoto(filtered,canvasType=1)

    def ThreshOldSauvolaFilter(self):
        filtered = filters.threshold_sauvola(self.image)
        binary = filtered < self.image
        self.setPhoto(binary, canvasType=1)

    def ThreshOldTriangleFilter(self):
        filtered=filters.threshold_triangle(self.image)
        binary=filtered < self.image
        self.setPhoto(binary, canvasType=1)

    def ThreshOldYenFilter(self):
        filtered = filters.threshold_yen(self.image)
        binary = filtered < self.image
        self.setPhoto(binary, canvasType=1)

    def ThreshOldLiFilter(self):
        filtered = filters.threshold_li(self.image)
        binary = filtered < self.image
        self.setPhoto(binary, canvasType=1)

    def ResizedPhoto(self):
        a = int(self.ui.lineEdit.text())
        b = int(self.ui.lineEdit_2.text())
        resized=resize(self.tmp,(b,a))
        self.setPhoto(resized,canvasType=1)

    def cropPhoto(self):
        y1=self.ui.lineEdit_3.text()
        y2 =self.ui.lineEdit_4.text()
        x1 =self.ui.lineEdit_5.text()
        x2 =self.ui.lineEdit_6.text()
        cropped = self.image[int(y1):int(y2),int(x1):int(x2)]
        self.setPhoto(cropped,canvasType=1)

    def RescalePhoto(self):
        a=float(self.ui.comboBox_5.currentText())
        rescaled = rescale(self.image,a)
        self.setPhoto(rescaled,canvasType=1)

    def RotatePhoto(self):
        a=int(self.ui.comboBox_3.currentText())
        rotated=rotate(self.tmp,a)
        self.setPhoto(rotated,canvasType=1)

    def SwirlPhoto(self):
        a=int(self.ui.comboBox_4.currentText())
        swirled=swirl(self.tmp,strength=a)
        self.setPhoto(swirled,canvasType=1)


    def ErosionPhoto(self):
        footprint = morphology.disk(6)
        filtered = morphology.erosion(self.image,footprint)
        self.setPhoto(filtered,canvasType=1)

    def DilationPhoto(self):
        footprint = morphology.disk(6)
        filtered=morphology.dilation(self.image,footprint)
        self.setPhoto(filtered,canvasType=1)

    def OpeningPhoto(self):
        footprint=morphology.disk(6)
        filtered=morphology.opening(self.image,footprint)
        self.setPhoto(filtered,canvasType=1)

    def ClosingPhoto(self):
        footprint=morphology.disk(6)
        filtered=morphology.closing(self.image,footprint)
        self.setPhoto(filtered,canvasType=1)

    def WhiteTophatPhoto(self):
        footprint = morphology.disk(6)
        filtered = morphology.white_tophat(self.image, footprint)
        self.setPhoto(filtered, canvasType=1)

    def BlackTophatPhoto(self):
        footprint = morphology.disk(6)
        filtered = morphology.black_tophat(self.image, footprint)
        self.setPhoto(filtered, canvasType=1)

    def SkeletonizePhoto(self):
        filtered = morphology.skeletonize(self.image == 0)
        self.setPhoto(filtered, canvasType=1)

    def ConvexHullPhoto(self):
        filtered = morphology.convex_hull_image(self.image == 0)
        self.setPhoto(filtered, canvasType=1)

    def SmallHolesPhoto(self):
        filtered=morphology.remove_small_holes(self.image,50)
        self.setPhoto(filtered,canvasType=1)

    def SmallObjectPhoto(self):
        filtered = morphology.remove_small_objects(self.image, 50)
        self.setPhoto(filtered, canvasType=1)

    def adjustGammaPhoto(self):
        value = self.ui.horizontalSlider.value()+1
        gamma_corrected = exposure.adjust_gamma(self.image, int(value))
        self.setPhoto(gamma_corrected,canvasType=1)

    def adjustSigmoidPhoto(self):
        value = self.ui.horizontalSlider_3.value()+10
        print(value)
        sigmoid_corrected = exposure.adjust_sigmoid(self.image, gain=int(value))
        self.setPhoto(sigmoid_corrected,canvasType=1)

    def adjustLogPhoto(self):
        value = 100-self.ui.horizontalSlider_4.value()
        log_corrected = exposure.adjust_log(self.image, int(value)/100)
        self.setPhoto(log_corrected, canvasType=1)

    def RescaleIntensity(self):
        value = self.ui.horizontalSlider_2.value()+1
        rescale_photo = exposure.rescale_intensity(self.image, in_range=(int(value),256))
        self.setPhoto(rescale_photo, canvasType=1)


uygulama=QApplication([])
pencere=UI()
pencere.show()
uygulama.exec_()


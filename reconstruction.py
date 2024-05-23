# This Python file uses the following encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.transform import radon, iradon, iradon_sart, rescale

class reconstructionn:

    def __init__(self, image, maxAngle, filterName):

        self.image = image

        if len(self.image.shape) == 3:
            self.image = color.rgb2gray(image)

        self.angle = maxAngle
        self.filter = filterName

    def processImage(self):
    #görüntü rescale ile yeniden boyutlandırılır.
        imageScaled = rescale(self.image, scale = 0.4, mode = 'reflect')#constant,edge,symmetric,wrap...
        theta = np.linspace(0.0, self.angle, max(imageScaled.shape))#radon için max açı değeri alınır
        numProjection = len(theta)*max(imageScaled.shape)#Projeksiyon sayısı hesaplanır. Projeksiyon sayısı, oluşturulan
        #açıların uzunluğu ile yeniden boyutlandırılmış görüntünün maksimum boyutunun çarpımıdır. Bu, toplam projeksiyon sayısını verir.

        return imageScaled, theta, numProjection

    def radonTransform(self):

        image, theta, __ = self.processImage()# yeniden yapılandırılan image ve theta açısı gelir.
        sinogram = radon(image, theta = theta)

        return sinogram #radon sonrası sinogram grafiği elde edilir.

    def filteredBackProjection(self):
# Bu yöntem, filtrelenmiş geri projeksiyon yöntemini kullanarak bir sinogramdan bir görüntüyü yeniden oluşturur.
#Geri projeksiyon işlemi, Radon dönüşümünün tersini alarak orijinal görüntüyü tahmin etmeye çalışır.
        __, theta, __ = self.processImage()
        sinogram = self.radonTransform()
        reconstruction = iradon(sinogram, theta = theta, filter_name = self.filter)

        return reconstruction

    def sart(self):
#Bu yöntem, Simültan İteratif Rekonstrüksiyon Tekniği (SART) kullanılarak bir sinogramdan bir görüntüyü yeniden oluşturur.
        __, theta, __ = self.processImage()
        sinogram = self.radonTransform()

        reconstructionSart = iradon_sart(sinogram, theta = theta)

        return reconstructionSart






#"ramp": Bu, Rampa filtresini kullanır. Rampa filtresi, her frekans bileşenine eşit ağırlık verir ve genellikle basit geri projeksiyon işlemlerinde kullanılır.
#"shepp-logan": Shepp-Logan filtresi, keskin kenarları korumak için tasarlanmış bir filtreleme yöntemidir. Bu filtre, düşük frekanslı bileşenleri vurgular ve genellikle tıbbi görüntüleme uygulamalarında kullanılır.
#"cosine": Kosinüs filtresi, düşük frekans bileşenlerini vurgulamak için kullanılır. Bu filtre, bazı durumlarda daha yumuşak görüntü rekonstrüksiyonu sağlayabilir.
#"hamming": Hamming filtresi, düşük frekans bileşenlerini vurgulamak için tasarlanmış bir filtreleme yöntemidir. Bu filtre, bazı durumlarda daha iyi kontrast sağlayabilir.
#"hann": Hann filtresi, düşük frekans bileşenlerini vurgulamak için kullanılır. Bu filtre, bazı durumlarda daha pürüzsüz görüntü rekonstrüksiyonu sağlayabilir.

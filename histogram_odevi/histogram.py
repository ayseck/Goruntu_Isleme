import cv2
import numpy as np
import matplotlib.pyplot as plt

foto_gray=cv2.imread(r"ev.jfif",0)
cv2.imshow("ev_gri",foto_gray)
cv2.waitKey()

# piksel değerleri ve frekanslarını saklamak için boş bir sözlük oluşturuyoruz
histogram = {}

# for döngüsü ile her piksel değeri tek tek inceleniyor
for row in foto_gray:
    for pixel in row:
        if pixel not in histogram:
            histogram[pixel] = 1
        else:
            histogram[pixel] += 1

# Histogram verilerinin grafikte gösterimi
plt.bar(histogram.keys(), histogram.values())
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')
plt.title('Görüntü Histogramı')
plt.show()
    

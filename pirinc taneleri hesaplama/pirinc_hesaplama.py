import cv2
import numpy as np

def say_pirinc_taneleri(frame):
    # Görüntüyü gri tonlama işlemi
    gri_tonlu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Görüntüyü bulanıklaştırma işlemi
    bulanik = cv2.GaussianBlur(gri_tonlu, (5, 5), 0)

    # Kenarları tespit etme 
    kenarlar = cv2.Canny(bulanik, 50, 150)

  
    kernel = np.ones((5, 5), np.uint8)
    genisletilmis = cv2.dilate(kenarlar, kernel, iterations=1)

    # Kontur tespiti yapma
    konturlar, _ = cv2.findContours(genisletilmis, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Pirinç tanelerini sayma işlemi
    pirinc_sayisi = 0
    for kontur in konturlar:
        alan = cv2.contourArea(kontur)
        if alan > 100:  # Eşik değeri ile oynayarak pirinç tanelerini belirlenebilir
            pirinc_sayisi += 1
            cv2.drawContours(frame, [kontur], -1, (0, 255, 0), 2)

    print(f"Pirinç Taneleri Sayısı: {pirinc_sayisi}")

    return frame

# Kamerayı açma
video_capture = cv2.VideoCapture(0)

while True:
    # Bir sonraki kareyi al
    ret, frame = video_capture.read()

    if not ret:
        break

    # Pirinç tanelerini sayan fonksiyonu çağır
    sonuc_frame = say_pirinc_taneleri(frame)

    # Sonucu göster
    cv2.imshow('Pirinç Sayım', sonuc_frame)

    # 'q' tuşuna basılınca döngüden çık
    tus = cv2.waitKey(1) & 0xFF
    if tus == ord('q'):
        break

# Kamerayı kapat
video_capture.release()
cv2.destroyAllWindows()


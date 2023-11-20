import cv2
import numpy as np

def process_frame(frame):
    # Görüntüyü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı rengin HSV renk aralığını belirle
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Renk aralığına uygun maske oluştur
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise AND işlemi ile orijinal görüntüde belirtilen renk aralığına uygun pikselleri göster
    result = cv2.bitwise_and(frame, frame, mask=mask)

    return result

def main():
    # Kamera girişi
    cap = cv2.VideoCapture(0)

    while True:
        # Görüntüyü oku
        ret, frame = cap.read()

        # Görüntüyü işle
        result = process_frame(frame)

        # Görüntüleri ekranda göster
        cv2.imshow('Original', frame)
        cv2.imshow('Result', result)

        # 'q' tuşuna basıldığında çıkış yap
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kaynakları serbest bırak
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

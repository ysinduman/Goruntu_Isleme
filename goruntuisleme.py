import cv2
import numpy as np
import os

# Çalışma dizinini değiştirin
os.chdir("C:/Users/Yasin/Desktop/Projeler/Python/.vscode/Goruntu_Isleme")
print("Yeni çalışma dizini:", os.getcwd())

# Görüntü yükleme
dosya_yolu = "resim.jpeg"
resim = cv2.imread(dosya_yolu)

if resim is None:
    print("Görüntü dosyası bulunamadı:", dosya_yolu)
else:
    # 1. Yeniden Boyutlandırma
    yeniden_boyut = (600, 400)
    yeniden_boyutlandirilmis_resim = cv2.resize(resim, yeniden_boyut, interpolation=cv2.INTER_AREA)

    # 2. Gri Tonlama
    gri_resim = cv2.cvtColor(yeniden_boyutlandirilmis_resim, cv2.COLOR_BGR2GRAY)

    # 3. Histogram Eşitleme
    esitleme = cv2.equalizeHist(gri_resim)

    # 4. Gaussian Gürültüsü Ekleme
    gauss = np.random.normal(0, 25, esitleme.shape).astype('uint8')
    gurultulu_resim = cv2.add(esitleme, gauss)

    # Sonuçları gösterme 
    cv2.imshow("Orijinal Görüntü", resim)
    cv2.imshow("Yeniden Boyutlandırılmış Görüntü", yeniden_boyutlandirilmis_resim)
    cv2.imshow("Gri Görüntü", gri_resim)
    cv2.imshow("Histogram Eşitleme", esitleme)
    cv2.imshow("Gaussian Gürültülü Görüntü", gurultulu_resim)
    cv2.waitKey(0)
    

    # Sonuçları kaydetme
    cv2.imwrite("yeniden_boyutlandirilmis_resim.jpeg", yeniden_boyutlandirilmis_resim)
    cv2.imwrite("gri_resim.jpeg", gri_resim)
    cv2.imwrite("esitleme_resim.jpeg", esitleme)
    cv2.imwrite("gurultulu_resim.jpeg", gurultulu_resim)

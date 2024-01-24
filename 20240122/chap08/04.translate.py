import numpy as np, cv2

def contain(p, shape):                              # 좌표(y,x)가 범위내 인지 검사
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)
    for  i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x, y = np.subtract((j,i), pt)
            if contain((y,x), img.shape):
                dst[i,j] = img[y,x]
    return dst

image = cv2.imread('./images/translate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")

x_translation = int(input("input x : "))
y_translation = int(input("input y : "))

dst1 = translate(image, (x_translation, y_translation))

cv2.imshow("image", image)
cv2.imshow(f"dst1: trans to ({x_translation}, {y_translation})", dst1)
cv2.waitKey(0)

import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('input.jpg')

# 그레이 스케일 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 블러 처리
blur = cv2.medianBlur(gray, 5)

# 경계 검출
edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 카툰화 처리
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# 결과 출력
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
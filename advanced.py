import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('input.jpg')

# gray scale 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# edge 검출
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# edge 두껍게
kernel = np.ones((5,5), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# smoothing
color = cv2.bilateralFilter(img, 9, 100, 20)

# 카툰 스타일 적용
cartoon = cv2.stylization(color, sigma_s=150, sigma_r=0.3)

# edge 적용
cartoon = cv2.bitwise_and(cartoon, cartoon, mask=dilated_edges)

# 결과 출력
cv2.imwrite('output.jpg', cartoon)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
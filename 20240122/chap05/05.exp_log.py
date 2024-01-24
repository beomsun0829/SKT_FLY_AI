import numpy as np, cv2

# numpy array 생성 예시
v1 = np.array([1, 2, 3], np.float32)          # 1차원 리스트로 생성- 행벡터
v2 = np.array([[1], [2], [3]], np.float32)      # 2차원 리스트로(3행, 1열) - 행벡터
v3 = np.array([[1, 2, 3]], np.float32)        	# 2차원 리스트로(1행, 3열) - 일반 행렬

# 

# 결과 출력
print("[v1] 형태: %s 원소: %s" % ( v1.shape, v1))
print("[v2] 형태: %s 원소:\n%s" % ( v2.shape, v2))
print("[v3] 형태: %s 원소: %s" % ( v3.shape, v3))
print()

# 행렬 정보 출력 - OpenCV 결과는 행렬로 반환됨 - 행벡터는 열벡터로 반환됨



# 열벡터를 1 행에 출력하는 예시 - 행벡터로 변환
print("[log] =", log.T)
print("[sqrt] =", np.ravel(sqrt))         
print("[pow] =", pow.flatten())


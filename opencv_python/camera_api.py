# /video 카메라 정보가 나오는 것
# flask로 서버를 열 것
""""
# 아래 코드는 카메라를 열고 120프레임을 읽어와서 화면에 보여주는 코드입니다.

cam = Util.gstrmer(width=640, height=480, fps=30, flip=0)
camera = cv2.VideoCapture(cam, cv2.CAP_GSTREAMER)

for _ in range(120):
    ret, frame = camera.read()
    if not ret:
        print(ret)
        continue
    cv2.imshow("soda", frame)
    
camera.release()

"""
#jpg 압축 60%해서 데이터 보내기 
#5000번 포트로 api열기
#쓰레드 사용
#scp camera_api.py soda@192.168.0.56
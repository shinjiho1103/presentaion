import time
import random

class GPS:
    def __init__(self, start_lat, start_lon):
        self.latitude = start_lat
        self.longitude = start_lon

    def update_position(self, target_lat, target_lon):
        # 간단하게 위치를 갱신하기 위해 가상으로 이동
        step = 0.001
        if self.latitude < target_lat:
            self.latitude += step
        elif self.latitude > target_lat:
            self.latitude -= step

        if self.longitude < target_lon:
            self.longitude += step
        elif self.longitude > target_lon:
            self.longitude -= step

        print(f"현재 위치: {self.latitude:.6f}, {self.longitude:.6f}")
        return abs(self.latitude - target_lat) < step and abs(self.longitude - target_lon) < step

# 시작 위치와 목적지 설정
start_position = GPS(37.0, 127.0)  # 초기 위치 예시
destination = (37.5, 127.5)  # 목적지 예시

# 실버택시 이동 시뮬레이션
print("실버택시가 어르신 위치로 이동 중입니다...")
while not start_position.update_position(destination[0], destination[1]):
    time.sleep(1)

print("어르신이 실버택시에 탑승하셨습니다.")
print("목적지로 이동 중입니다...")

# 목적지 도착 시뮬레이션
while not start_position.update_position(37.7, 127.7):  # 최종 목적지 예시
    time.sleep(1)

print("목적지에 도착했습니다. 전기 휠체어가 집까지 모셔다 드립니다.")

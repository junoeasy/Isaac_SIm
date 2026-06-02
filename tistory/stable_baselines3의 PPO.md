# stable_baselines3
PPO 알고리즘을 갖고 있는 라이브러리 중 하나로 PPO의 policy에는 MlpPolicy, CnnPolicy, MultiInputPolicy가 있다.

## MlpPolicy
MlpPolicy는 Multi-Layer Perceptron으로 일반적인 `fully-connected neural network` 이다.
이런 Observation에 쓰임
```
숫자 벡터
joint position
joint velocity
cart 위치
pole 각도
로봇 상태값
```


## CnnPolicy
CnnPolicy는 이미지 observation에 사용한다.
CNN은 Convolutional Neural Network이다.
이런 Observation에 쓰임
```
RGB 이미지
depth 이미지
카메라 회전
게임 화면
```

# Isaac Sim / 로봇 학습 스터디

이 워크스페이스는 Isaac Sim 기반 로봇 학습 업무를 1단계부터 순서대로 공부하기 위한 자료입니다.

최종 목표는 아래 작업들을 직접 설계하고 테스트할 수 있는 수준까지 가는 것입니다.

- Isaac Sim / MuJoCo 기반 모바일 매니퓰레이터 시뮬레이션 환경 구축
- 도메인 랜덤화
- 합성 데이터 자동 생성
- BC, ACT, Diffusion Policy 같은 모방학습
- PPO, SAC 기반 강화학습
- Sim-to-Real 전이
- VLA/RFM 스타일 정책 평가 벤치마크
- 대규모 합성 데이터 생성 및 학습 파이프라인

## 시작 순서

먼저 전체 흐름을 보고, 1단계부터 차례대로 진행합니다.

1. [전체 학습 로드맵](docs/isaac-sim-learning-roadmap.md)
2. [1단계: 기초](docs/stage-01-foundations.md)

## 단계별 문서

1. [1단계: 기초](docs/stage-01-foundations.md)
2. [2단계: MuJoCo 제어 기초](docs/stage-02-mujoco-control-basics.md)
3. [3단계: Isaac Sim 기초](docs/stage-03-isaac-sim-basics.md)
4. [4단계: Isaac Lab](docs/stage-04-isaac-lab.md)
5. [5단계: 모바일 매니퓰레이터 환경 구축](docs/stage-05-mobile-manipulator-environment.md)
6. [6단계: 도메인 랜덤화](docs/stage-06-domain-randomization.md)
7. [7단계: 합성 데이터 생성](docs/stage-07-synthetic-data-generation.md)
8. [8단계: 모방학습](docs/stage-08-imitation-learning.md)
9. [9단계: Visuomotor Transformer 정책](docs/stage-09-visuomotor-transformer.md)
10. [10단계: 강화학습](docs/stage-10-reinforcement-learning.md)
11. [11단계: Sim-to-Real 전이](docs/stage-11-sim-to-real-transfer.md)
12. [12단계: 대규모 학습 인프라](docs/stage-12-large-scale-training-infrastructure.md)
13. [13단계: VLA/RFM 평가 벤치마크](docs/stage-13-vla-rfm-evaluation-benchmarks.md)

## 1단계 실습 실행

```bash
python3 exercises/stage01_transforms_and_kinematics.py
```

실행하면 좌표 변환, 2-link 로봇팔의 순기구학/역기구학 결과가 출력되고, `outputs/stage01_2link_arm.png` 그림이 생성됩니다.

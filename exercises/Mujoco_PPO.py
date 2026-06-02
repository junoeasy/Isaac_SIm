import time
import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("InvertedPendulum-v5", render_mode="human")

model = PPO.load("ppo_inverted_pendulum")

obs, info = env.reset()

for step in range(3000):
    action, _states = model.predict(obs, deterministic=True)

    obs, reward, terminated, truncated, info = env.step(action)

    time.sleep(0.02)

    if terminated or truncated:
        obs, info = env.reset()
        time.sleep(0.5)

env.close()
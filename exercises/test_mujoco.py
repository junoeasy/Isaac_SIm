import gymnasium as gym
import time
env = gym.make("InvertedPendulum-v5", render_mode="human")

obs, info = env.reset()
print("obs:", obs)
print("obs shape:", obs.shape)
print("action space:", env.action_space)

for step in range(10000):
    if obs[1]<-0.1:
        action=[-1.0]
    elif obs[1]>0.1:
        action=[1.0]
    else:
        action=[0.0]
    obs, reward, terminated, truncated, info = env.step(action)

    print(step, reward, terminated, truncated,info,obs[0],obs[1],obs[2],obs[3])
    time.sleep(0.1)
    if terminated or truncated:
        obs, info = env.reset()
        break

env.close()
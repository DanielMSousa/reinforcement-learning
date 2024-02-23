import gymnasium as gym
import matplotlib.pyplot as plt
from helper import save_plot

# env = gym.make("LunarLander-v2", render_mode="human")
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True, render_mode='human')

rewards = []

for i in range(20):
    observation, info = env.reset(seed=123, options={})
    done = False

    while not done:
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated
        
    rewards.append(reward)

env.close()

save_plot(rewards)
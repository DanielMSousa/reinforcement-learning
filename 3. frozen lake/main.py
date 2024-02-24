import gymnasium as gym
import matplotlib.pyplot as plt
from QTable import QTable, EpsilonGreedy
import numpy as np


# from helper import save_plot

# env = gym.make("LunarLander-v2", render_mode="human")




env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False)


lr = 0.001
gamma = 0.4
actions = [0,1,2,3]
e0 = 0
policy = EpsilonGreedy(0.4)
epochs = 2000

tabela = np.zeros((4, 16))

Q = QTable(lr, gamma, actions, e0, policy)
Q.inicializaQTable(tabela)

print(Q.QTable)

rewards = []
for i in range(epochs):
    print(f'Época atual: {i}')
    observation, info = env.reset(seed=123, options={})
    Q.estado_atual = observation

    done = False

    while not done:
        action = env.action_space.sample()  # agent policy that uses the observation and info
        
        #observation é meu estado atual
        observation, reward, terminated, truncated, info = env.step(action)
        Q.atualizaPeso(action, observation, reward)

        done = terminated or truncated
        
    rewards.append(reward)

env.close()

print(Q.QTable)




env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode='human')

observation, info = env.reset(seed=123, options={})
Q.estado_atual = observation

done = False

while not done:
    action = Q.exploit()  # agent policy that uses the observation and info
    
    #observation é meu estado atual
    observation, reward, terminated, truncated, info = env.step(action)
    Q.estado_atual = observation

    done = terminated or truncated

Q.salvar('QTable.csv')

# save_plot(rewards)
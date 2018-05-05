# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:56:00 2017

@author: Chen
"""

import gym
env = gym.make('CartPole-v0')

#> array([ 2.4       ,         inf,  0.20943951,         inf])

print(env.action_space.n)
#> array([-2.4       ,        -inf, -0.20943951,        -inf])
for i_episode in range(20):
    observation = env.reset()
    for t in range(2):
        print(observation)
        action = env.action_space.sample()
        print(action)
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

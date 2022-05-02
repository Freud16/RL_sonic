import os
import retro
import gym
import cv2

env = retro.make(game='SonicTheHedgehog-Genesis', record='.')
env.reset()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
vw = cv2.VideoWriter(os.path.join('videos', 'test2.avi'), fourcc, 4, (320,224))

for _ in range(1000):
    _obs, _rew, done, _info = env.step(env.action_space.sample())
    vw.write(_obs)
    if done:
        vw.release()
        break
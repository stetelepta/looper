import pygame
import time

# initialize mixer
pygame.mixer.init()

# load sounds
pygame.mixer.music.load("wav/snare.wav")

# input
beat = {
    'kick':  [1, 0, 1, 1, 1, 0, 1, 0],
    'snare': [0, 1, 0, 1, 0, 1, 0, 1]
}


def play_sound():
    pygame.mixer.music.play()
    print "play"

starttime = time.time()
interval = 0.5

print "starttime:", starttime
for i in range(20):
    a = starttime + (i+1) * interval - time.time()
    time.sleep(a)
    play_sound()

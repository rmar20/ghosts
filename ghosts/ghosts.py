# Ryan Mar
# June 9, 2020
# Ghosts

from midiutil import MIDIFile
import random
import datetime

#degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track = 0
channel = 0
time = 0  # Current time in beats
duration = 1 # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track, time, tempo)

total_duration = 300

while total_duration > 0:
    pitch = random.randint(0, 180)

    if pitch > 127:
        time += random.uniform(0.0, 4.0)
    else:
        duration =  random.uniform(0.0, 4.0)
        MyMIDI.addNote(track, channel, pitch, time, duration, 90)
        total_duration -= duration;
        time += duration;


now = datetime.datetime.now()
fileName = "ghosts--{}-{}-{}-{}-{}-{}.mid".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

with open(fileName, "wb") as output_file:
    MyMIDI.writeFile(output_file)

import time

from classes.TonePlayer import TonePlayer


player = TonePlayer()

try:
    octave = 1

    while True:
        player.play_note("C", octave)
        time.sleep(0.4)
        player.play_note("D", octave)
        time.sleep(0.4)
        player.play_note("E", octave)
        time.sleep(0.4)
        player.play_note("F", octave)
        time.sleep(0.4)
        player.play_note("G", octave)
        time.sleep(0.4)
        player.play_note("A", octave)
        time.sleep(0.4)
        player.play_note("B", octave)
        time.sleep(0.4)

        octave += 1
        

except KeyboardInterrupt:
    print("Audio test stopped.")
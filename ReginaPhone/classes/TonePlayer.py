
import numpy as np
import sounddevice as sd

from classes.NoteSerializer import NoteSerializer


class TonePlayer:

    def __init__(self):
        self.sample_rate = 44100
        self.volume = 0.3
        self.duration = 1.0

    def generate_bell(self, frequency):
        t = np.linspace(
            0,
            self.duration,
            int(self.sample_rate * self.duration),
            endpoint=False
        )

        fundamental = np.sin(2 * np.pi * frequency * t)
        harmonic_2 = np.sin(2 * np.pi * frequency * 2.01 * t) * 0.5
        harmonic_3 = np.sin(2 * np.pi * frequency * 3.9 * t) * 0.25

        envelope = np.exp(-4 * t)

        audio = (
            fundamental +
            harmonic_2 +
            harmonic_3
        ) * envelope * self.volume

        return audio.astype(np.float32)

    def play_frequency(self, frequency):
        audio = self.generate_bell(frequency)
        sd.play(audio, self.sample_rate)

    def play_note(self, note, octave=4):
        frequency = NoteSerializer.note_to_frequency(note, octave)
        self.play_frequency(frequency)

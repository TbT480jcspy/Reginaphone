
class NoteSerializer:

    NOTES = {
        "C": 0,
        "C#": 1,
        "Db": 1,
        "D": 2,
        "D#": 3,
        "Eb": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "Gb": 6,
        "G": 7,
        "G#": 8,
        "Ab": 8,
        "A": 9,
        "A#": 10,
        "Bb": 10,
        "B": 11
    }

    @staticmethod
    def note_to_frequency(note, octave=4):
        if note not in NoteSerializer.NOTES:
            raise ValueError(f"Invalid note: {note}")

        midi_number = (octave + 1) * 12 + NoteSerializer.NOTES[note]

        frequency = 440 * (2 ** ((midi_number - 69) / 12))

        return frequency

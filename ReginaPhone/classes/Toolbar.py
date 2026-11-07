
import tkinter as tk


class Toolbar(tk.Frame):

    def __init__(self, app):
        super().__init__(app.root)

        self.app = app
        self.height = 300

        self.configure(height=self.height)
        self.pack(fill="x")
        self.pack_propagate(False)

        self.create_transport_controls()
        self.create_tempo_controls()
        self.create_metronome_control()
        self.create_time_signature_control()

    def create_transport_controls(self):
        self.transport_frame = tk.Frame(self)
        self.transport_frame.pack(
            side="left",
            padx=15,
            pady=15,
            anchor="nw"
        )

        self.play_button = tk.Button(
            self.transport_frame,
            text="Play",
            width=5,
            height=2
        )
        self.play_button.pack(side="left", padx=5)

        self.pause_button = tk.Button(
            self.transport_frame,
            text="Pause",
            width=5,
            height=2
        )
        self.pause_button.pack(side="left", padx=5)

        self.stop_button = tk.Button(
            self.transport_frame,
            text="Stop",
            width=5,
            height=2
        )
        self.stop_button.pack(side="left", padx=5)

    def create_tempo_controls(self):
        self.tempo_frame = tk.Frame(self)
        self.tempo_frame.pack(
            side="left",
            padx=20,
            pady=15,
            anchor="nw"
        )

        self.bpm_label = tk.Label(
            self.tempo_frame,
            text="BPM"
        )
        self.bpm_label.pack()

        self.bpm_value = tk.IntVar(value=120)

        self.bpm_spinbox = tk.Spinbox(
            self.tempo_frame,
            from_=40,
            to=300,
            textvariable=self.bpm_value,
            width=6
        )
        self.bpm_spinbox.pack()

    def create_metronome_control(self):
        self.metronome_frame = tk.Frame(self)
        self.metronome_frame.pack(
            side="left",
            padx=20,
            pady=15,
            anchor="nw"
        )

        self.metronome_enabled = tk.BooleanVar(value=False)

        self.metronome_button = tk.Checkbutton(
            self.metronome_frame,
            text="Metronome",
            variable=self.metronome_enabled,
            indicatoron=False,
            width=12,
            height=2,
            relief="raised",
            selectcolor="#b0b0b0"
        )
        self.metronome_button.pack()

    def create_time_signature_control(self):
        self.time_signature_frame = tk.Frame(self)
        self.time_signature_frame.pack(
            side="left",
            padx=20,
            pady=15,
            anchor="nw"
        )

        self.time_signature_label = tk.Label(
            self.time_signature_frame,
            text="Time Signature"
        )
        self.time_signature_label.pack()

        self.time_signature_top = tk.IntVar(value=4)
        self.time_signature_bottom = tk.IntVar(value=4)

        self.time_signature_top_spinbox = tk.Spinbox(
            self.time_signature_frame,
            from_=1,
            to=16,
            textvariable=self.time_signature_top,
            width=4,
            justify="center"
        )
        self.time_signature_top_spinbox.pack()

        self.time_signature_separator = tk.Frame(
            self.time_signature_frame,
            height=2,
            bg="black"
        )
        self.time_signature_separator.pack(fill="x", pady=2)

        self.time_signature_bottom_spinbox = tk.Spinbox(
            self.time_signature_frame,
            values=(1, 2, 4, 8, 16, 32),
            textvariable=self.time_signature_bottom,
            width=4,
            justify="center"
        )
        self.time_signature_bottom_spinbox.pack()

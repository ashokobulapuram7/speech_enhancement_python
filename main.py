from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
import webbrowser
import pyaudio
import wave
from kivymd.uix.snackbar import Snackbar
import winsound
from kivy.core.window import Window
from file_ns import main1
# set window size
Window.size = (350, 600)

class SpeechApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        scr = Builder.load_file("interface.kv")

        return scr

    def record_voice(self):
        Snackbar(bg_color=(0, 0, 0, 1),text="[color=#ddbb34]Voice Recorded.[/color]").open()
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "recorded_audio.wav"

        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        main1()
    def play_voice(self):
        winsound.PlaySound('out_speech.wav', winsound.SND_FILENAME)
        Snackbar(bg_color=(0, 0, 0, 1), text="[color=#ddbb34]finished playing clean voice.[/color]").open()

    def open_facebook(self):
        webbrowser.open("https://www.facebook.com/profile.php?id=100006401596507")
    def open_insta(self):
        webbrowser.open("https://www.instagram.com/invites/contact/?i=1skrh6aignrsk&utm_content=3wxkoh5")
    def open_github(self):
        webbrowser.open("https://github.com/ashokobulapuram7")
    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/venkata-ashok-kumar-obulapuram-503070218")

    class DrawerList(ThemableBehavior, MDList):
        pass


SpeechApp().run()
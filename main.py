import queue
import sounddevice as sd
import vosk
import json
import gui
from recognizer import recognize


def callback(indata, frames, time, status):
    q.put(bytes(indata))

def main():
    with sd.RawInputStream(samplerate=samplerate, blocksize=24000, device=device[0],
                            dtype="int16", channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            gui.gui_update()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())["text"]
                recognize(data)

q = queue.Queue()

model = vosk.Model("vosk-model-small")
device = sd.default.device
samplerate = int(sd.query_devices(device[0], "input")["default_samplerate"])

if __name__ == "__main__":
    main()
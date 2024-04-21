import torch
import sounddevice as sd
import time
from num_to_text import num2text
import gui

voice_mod = True

def speak(text):
    if voice_mod:
        text = text.split()
        for i in range(len(text)):
            if text[i].isdigit():
                print(text[i])
                text[i] = num2text(int(text[i]))
        text = " ".join(text)

        language = "ru"
        model_id = "ru_v3"
        sample_rate = 48000
        speaker = "xenia" # aidar, baya, kseniya, xenia, random
        put_accent = True
        put_yo = True
        device = torch.device("cpu") # cpu unu gpu

        gui.label_bot_update(text)
        gui.gui_update()

        model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                  model='silero_tts',
                                  language=language,
                                  speaker=model_id)
        model.to(device)

        audio = model.apply_tts(text=text + ". . .",
                                speaker=speaker,
                                sample_rate=sample_rate,
                                put_accent=put_accent,
                                put_yo=put_yo)

        sd.play(audio, sample_rate)
        time.sleep(len (audio) / sample_rate)
        sd.stop()
    else:
        gui.label_bot_update(text)
        gui.gui_update()

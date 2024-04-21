from tkinter import *
from tkinter import ttk
from recognizer import recognize


def test():
    recognize(text.get("1.0", "end-1c"))

def gui_update():
    root.update()

def label_voice_update(text):
    listbox.insert(END, f"Вы: {text}")

def label_bot_update(text):
    listbox.insert(END, f"Бот: {text}")


# def label_voice_update(text):
#     label_voice["text"] = text
#
# def label_bot_update(text):
#     label_bot["text"] = text

root = Tk()
root.title("AI_voice")
root.geometry("600x400")

enabled = IntVar()

label = ttk.Label(text="Поле текстового ввода:")
label.grid(row=0, column=0)

checkbutton_neuron = ttk.Checkbutton(text="Нейросеть", variable=enabled)
checkbutton_neuron.grid(row=0, column=1)

text = Text(height=5)
text.grid(row=1, column=0, columnspan=2)

button = ttk.Button(text="Отправить", command=test)
button.grid(row=2, column=0, columnspan=2)

# label = ttk.Label(text="Вы сказали", width=50)
# label.grid(row=3, column=0)
#
# label = ttk.Label(text="Бот сказал", width=50)
# label.grid(row=3, column=1)
#
# label_voice = ttk.Label(text="", wraplength=100)
# label_voice.grid(row=4, column=0, rowspan=7)
#
# label_bot = ttk.Label(text="", wraplength=100)
# label_bot.grid(row=4, column=1, rowspan=7)

phrases = []

phrases_var = StringVar(value=phrases)
listbox = Listbox(listvariable=phrases_var, width=100, height=10)
listbox.grid(row=5, column=0, columnspan=2, sticky=W)

voice_output = "Голосовой вывод"
text_output = "Текстовый вывод"

standart_input = StringVar(value=voice_output)

btn_voice_input = ttk.Radiobutton(text=voice_output, value=voice_output, variable=standart_input)
btn_voice_input.grid(row=6, column=0)

btn_text_input = ttk.Radiobutton(text=text_output, value=text_output, variable=standart_input)
btn_text_input.grid(row=6, column=1)

# java_btn = ttk.Radiobutton(text=java, value=java, variable=lang)
# java_btn.pack(**position)


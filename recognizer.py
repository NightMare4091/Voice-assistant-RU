import gui
import words
from words import data_set
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from voice_v1 import speak

def recognize(data):
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(data_set.keys()))
    clf = LogisticRegression()
    clf.fit(vectors, list(data_set.values()))

    trg = words.triggers.intersection(data.split())
    if not trg:
        return

    gui.label_voice_update(data)
    gui.gui_update()

    data.replace(list(trg)[0], "")
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    text = " ".join(answer.split()[1:])
    if len(text) > 0:
        speak(text)
    print(func_name + f"('{data}')")
    exec(func_name + f"('{data}')")




import Redditbot 
import pyttsx3

title, comment = Redditbot.reddit()
engine = pyttsx3.init()
voice_id = 'english'
engine.setProperty('voice', voice_id)
engine.runAndWait()
count = 0

for ind, titl in enumerate(title):
    engine.save_to_file(titl, f'title{ind}.wav')
    for indx in range(2):
        engine.save_to_file(comment[count], f'response{ind}{indx}.wav')
        count += 1
engine.runAndWait()


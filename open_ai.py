import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from langchain.llms import OpenAI

r = sr.Recognizer()
os.environ["OPENAI_API_KEY"] =  'XYZ'

with sr.Microphone() as source:
    print("Please start speaking")
    audio_text = r.listen(source, timeout=20)
    print(audio_text)
    print("Time over ........")
    try:
        input_text = r.recognize_google(audio_text, language = "en-US")
        print(input_text)
        llm = OpenAI(model_name="text-davinci-003")
        completion = llm(input_text)

        speech = gTTS(completion)


        speech.save('play_file.mp3')
        playsound('play_file.mp3')
        
    
    except Exception as e:
        print('Error '+ str(e))


# 

# from langchain.llms import OpenAI
# llm = OpenAI(model_name="gpt-4")


# question = "What are the important places when we drive from London to Paris ? "

# completion = llm(question)

# print(completion)

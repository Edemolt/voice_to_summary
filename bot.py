import speech_recognition as sr
import keyboard
import time
from transformers import pipeline
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

class SpeechSummaryAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def listen_for_speech(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio).lower()
                return text
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except sr.UnknownValueError:
                print("Unknown error occurred")
        return None

    def summarize_text(self, text):
        # Increase max_length and set min_length to a lower value
        summary = self.summarizer(text, max_length=300, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    def run(self):
        print("Press 'q' to quit, 's' to start listening.")
        while True:
            if keyboard.is_pressed('q'):
                print("Stopping...")
                break

            if keyboard.is_pressed('s'):
                print("Listening...")
                speech_text = self.listen_for_speech()
                if speech_text:
                    print(f"You said: {speech_text}")
                    summary = self.summarize_text(speech_text)
                    print(f"Summary: {summary}")

            time.sleep(0.1)

if __name__ == "__main__":
    assistant = SpeechSummaryAssistant()
    assistant.run()
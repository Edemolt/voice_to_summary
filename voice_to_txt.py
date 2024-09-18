import speech_recognition as sr
import pyttsx3
import keyboard
import time

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to listen for speech
def listen_for_speech():
    with sr.Microphone() as source2:
        # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source2, duration=0.2)
        
        # Listens for the user's input
        audio2 = r.listen(source2)
        
        # Using Google to recognize audio
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()
        return MyText

print("Press 'q' to quit, 's' to start listening.")
while True:
    if keyboard.is_pressed('q'):
        print("Stopping...")
        break  # Exit the loop and stop listening
    
    # Check if 's' is pressed to start listening
    if keyboard.is_pressed('s'):
        print("Listening...")
        try:
            MyText = listen_for_speech()
            print("Did you say:", MyText)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")
    
    time.sleep(0.1)  # Small delay to reduce CPU usage

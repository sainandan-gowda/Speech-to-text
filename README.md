🎙️ Voice Assistant (Speech Recognition + Text-to-Speech)

This is a simple Python-based voice assistant program that listens to user speech, converts it to text, and responds using text-to-speech. It demonstrates the integration of SpeechRecognition and pyttsx3 libraries.

* Features

1) Listens to speech input through a microphone

2) Converts speech to text using Google Speech Recognition API

3) Responds with text-to-speech using pyttsx3

4) Runs in a loop, continuously listening for commands

* Requirements

Before running the program, make sure you have the following installed:

Python 3.7+

Required Python libraries:

pip install SpeechRecognition pyttsx3 pyaudio


⚠* Note for Windows users:
If pyaudio fails to install, download the correct .whl file from PyAudio builds
 and install it manually:

pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl

▶* How to Run

Clone or download this repository.

Save the program as voice_assistant.py.

Run the script from the terminal:

python voice_assistant.py


The assistant will greet you:

Hey how may I help you


Speak into your microphone — the recognized text will be printed on the screen.

📂 Project Structure
voice_assistant/
│
├── voice_assistant.py   # Main program
├── README.md            # Project documentation

📊 Example Output
Hey how may I help you
Listening...
Recognizing.....
play music

* Known Issues

Requires a working microphone.

Accuracy may be reduced in noisy environments.

Internet connection is required for Google Speech Recognition.

 * Future Enhancements

Add specific command handling (e.g., open YouTube, play songs).

Integrate APIs (weather, news, system control).

Improve background noise filtering.

* Acknowledgments

SpeechRecognition

pyttsx3

PyAudio

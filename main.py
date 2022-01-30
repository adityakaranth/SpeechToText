################################################################
################## SPEECH RECOGNITION ##########################
################################################################
# Import library for speech recognition
# Initializing the recognizer class in order to do voice recognition.
# We аre utilizing Gооgle’s sрeeсh reсоgnitiоn API.
# The following audio formats are supported by speech recognition: wav, AIFF, AIFF-C, and FLAC.
# Google recognizer reads English by default.
# It supports a variety of languages; for further information, please refer to this documentation.

#import library
import speech_recognition as sr
r = sr.Recognizer()
# Reading Audio file as source
with sr.AudioFile('Check123.wav') as source:
    audio = r.listen(source)
    # recognize() method will call the Google audio detection API and if the API is unreachable throws an exception
    try:
        # using google speech recognition
        text = r.recognize_google(audio)
        print('Converting audio to text ...')
        print(text)
    except:
         print('Oops! Please run again..')
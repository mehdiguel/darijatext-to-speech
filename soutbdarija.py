import gtts
from playsound import playsound
import os

def darija_tts(text, output_file="output.mp3"):
    # Use 'ar' (Arabic) as the language code
    tts = gtts.gTTS(text, lang='ar')
    tts.save(output_file)
    #playsound(output_file)
    #os.remove(output_file)  # Remove the file after playing

# Example usage
darija_text = """
text_to_convert (should be written in arabic letters)
"""
darija_tts(darija_text)

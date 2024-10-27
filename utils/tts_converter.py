from gtts import gTTS

def text_to_speech(text, output_path):
    """Converts text to speech and saves it as an MP3 file."""
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)
    print(f"Text-to-speech conversion complete. Audio saved to {output_path}")

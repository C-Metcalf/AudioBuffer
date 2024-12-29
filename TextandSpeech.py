import time
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play


def transcribe_audio_with_timestamps(a_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    audio = sr.AudioFile(a_path)

    with audio as source:
        audio_data = recognizer.record(source)

    # Get full transcript with timestamps
    transcript = recognizer.recognize_google(audio_data, show_all=True)
    if 'alternative' not in transcript:
        print("No transcription available.")
        return None
    print(transcript)
    # Extract words and timestamps
    timestamps = []
    if 'words' in transcript['alternative'][0]:
        for word_info in transcript['alternative'][0]['words']:
            timestamps.append((word_info['word'], word_info['startTime']))

    return timestamps


def play_audio_and_print_words(a_path, timestamps):
    audio = AudioSegment.from_file(audio_path)
    start_time = time.time()
    for word, timestamp in timestamps:
        while time.time() - start_time < float(timestamp[:-1]):  # Wait until the correct time
            pass
        print(word)
    play(audio)


# Usage
audio_path = "audio_logs/recording_1.wav"
words_with_timestamps = transcribe_audio_with_timestamps(audio_path)
print(words_with_timestamps)
if words_with_timestamps:
    play_audio_and_print_words(audio_path, words_with_timestamps)

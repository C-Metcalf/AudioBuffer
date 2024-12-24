from pydub import AudioSegment

first_audio = AudioSegment.from_file("audio_logs/recording.wav")
second_audio = AudioSegment.from_file("audio_logs/recording_1.wav")

combined_audio = first_audio + second_audio

combined_audio.export("New_Audio.wav", format="wav")
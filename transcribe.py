import assemblyai as aai

aai.settings.api_key = "7d25acc1c0a74cbbb25fa4bc628bd5e3"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("/Users/kevinsong/Desktop/shnuckaitwo/scripts/I've Failed..mp3")

print(transcript.text)
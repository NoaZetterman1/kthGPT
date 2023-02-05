import whisper
import hashlib
import json
import os


MODEL = 'small.en'


def extract_text(mp3: str, src_url: str) -> str:
    sha = hashlib.sha256(src_url.encode()).hexdigest()
    filename = f'/tmp/{sha}.json'

    if os.path.isfile(filename):
        return filename

    model = whisper.load_model(MODEL)
    result = model.transcribe(mp3)


    with open(filename, 'w') as f:
        json.dump(result, f)

    return filename

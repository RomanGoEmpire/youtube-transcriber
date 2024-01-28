import os
import json
import whisper_timestamped as whisper

class Transcriber:
    def __init__(self,model="tiny") -> None:
        self.model = whisper.load_model(model, device="cpu")
    
    def convert(self, audio_file_path: str) -> dict:
        audio = whisper.load_audio(audio_file_path)
        result = whisper.transcribe(self.model, audio, language="en")
        return result
    
    def save(self, result: dict, file_name:str,file_path="transcriptions") -> None:
        os.makedirs(file_path, exist_ok=True)
        path = os.path.join(file_path,file_name)
        with open(path, "w") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
    
    def load(self, file_path: str) -> dict:
        with open(file_path) as file:
            result = json.load(file)
        return result

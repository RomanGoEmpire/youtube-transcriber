import json

# Load the transcription file
file_path = "transcriptions/"
with open(file_path) as file:
    result = json.load(file)

print(result.get("text"))

#FastAPI related imports
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
#bark related imports
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

#uncomment below 3 lines for smaller model
#import os
#os.environ["SUNO_OFFLOAD_CPU"] = "True"
#os.environ["SUNO_USE_SMALL_MODELS"] = "True"


app = FastAPI()

#class for processing post request
class PromptRequest(BaseModel):
	prompt: str

#preload_models
preload_models()
print("Application ready to receive Requests")


@app.get("/")
def default_case():
	return {"Send a POST request at /process-prompt with payload": "{'prompt':'text-here'}"}

#Post Method
#Returns bark Generated wav file using the prompt in the payload of POST
@app.post("/process-prompt")
def process_prompt(request: PromptRequest):
	prompt = request.prompt
	audio_array = generate_audio(text_prompt)
	file_path="bark_generation.wav"
	# save audio to disk
	write_wav(file_path, SAMPLE_RATE, audio_array)    
	return FileResponse(file_path, media_type="audio/wav")

#EXAMPLE POST:
#curl -X POST -H "Content-Type: application/json" -d {"prompt":"Hello People at Stable Diffusion API"} http://localhost:15320/process-prompt



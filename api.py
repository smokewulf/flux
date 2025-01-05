from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Directory to store images
IMAGE_DIR = 'images'

# Create the image directory if it doesn't exist
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

@app.post('/upload/')
async def upload_image(file: UploadFile = File(...)):
    file_location = os.path.join(IMAGE_DIR, file.filename)
    with open(file_location, 'wb+') as file_object:
        file_object.write(await file.read())
    return {'info': 'Image uploaded successfully', 'filename': file.filename}

@app.get('/images/{filename}')
def get_image(filename: str):
    file_path = os.path.join(IMAGE_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {'error': 'File not found'}

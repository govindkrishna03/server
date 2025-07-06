# emotion_server.py

from flask import Flask, request
from PIL import Image
import io
import random

app = Flask(__name__)

emotions = ["happy", "angry", "tired", "sad", "neutral"]

@app.route('/emotion', methods=['POST'])
def detect_emotion():
    img_bytes = request.data
    image = Image.open(io.BytesIO(img_bytes))
    # Dummy classification - randomly pick an emotion
    detected = random.choice(emotions)
    return detected

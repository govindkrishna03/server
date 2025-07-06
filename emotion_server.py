from flask import Flask, request
from PIL import Image
import io
import os
import cv2
import numpy as np
from fer import FER

app = Flask(__name__)
detector = FER(mtcnn=True)

@app.route('/emotion', methods=['POST'])
def detect_emotion():
    try:
        img_bytes = request.data
        image = Image.open(io.BytesIO(img_bytes)).convert('RGB')

        # Convert to OpenCV image
        open_cv_image = np.array(image)
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)

        # Detect emotions
        result = detector.detect_emotions(open_cv_image)

        if result:
            top_emotion = max(result[0]["emotions"], key=result[0]["emotions"].get)
            print("Detected:", top_emotion)
            return top_emotion
        else:
            return "neutral"  # default fallback
    except Exception as e:
        print("Error:", e)
        return "error"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

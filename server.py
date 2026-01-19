from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'Invalid text! Please try again!'}), 400
        result = emotion_detector(text)

        if result['dominant_emotion'] is None:
            return jsonify({
                'error': 'Invalid text!'
            }), 400

        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return jsonify({
            'processed_text': text,
            'formatted_result': formatted_response
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Emotion Detection API',
        'endpoint': '/emotionDetector',
        'method': 'POST',
        'example_input': '{"text": "I think I am having fun"}',
        'expected_format': "For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002, 'fear': 0.009, 'joy': 0.968 and 'sadness': 0.049. The dominant emotion is joy."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
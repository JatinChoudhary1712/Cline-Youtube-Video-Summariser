from flask import Flask, render_template, request, jsonify
from youtube_summarizer import extract_video_id, get_transcript, generate_summary
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        youtube_url = request.form['youtube_url']
        
        # Get API keys
        searchapi_key = os.getenv('SEARCHAPI_KEY')
        openai_api_key = os.getenv('OPENAI_API_KEY')
        
        if not searchapi_key or not openai_api_key:
            return jsonify({
                'error': 'API keys not found. Please check your .env file.'
            }), 400
        
        # Extract video ID
        video_id = extract_video_id(youtube_url)
        
        # Get transcript
        transcript = get_transcript(video_id, searchapi_key)
        
        # Generate summary
        summary = generate_summary(transcript, openai_api_key)
        
        return jsonify({
            'success': True,
            'summary': summary
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True) 
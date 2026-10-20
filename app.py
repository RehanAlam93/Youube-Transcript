from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi

# Initialize the Flask application
app = Flask(__name__)

# Define the main route handling both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    transcript_text = ""
    error = None

    # Check if the form has been submitted via POST
    if request.method == "POST":
        # Retrieve and sanitize the video ID input from the form
        video_id = request.form.get("video_id", "").strip()

        # Validate that the video ID field is not empty
        if not video_id:
            error = "Please enter a valid YouTube Video ID or URL."
        else:
            try:
                # Instantiate the YouTube Transcript API client
                ytt_api = YouTubeTranscriptApi()

                # Fetch the transcript for the given video ID in Hindi and English languages
                transcript = ytt_api.fetch(
                    video_id,
                    languages=['hi', 'en']
                )

                # Extract the raw transcript data
                transcript_data = transcript.to_raw_data()

                # Combine all individual text segments into a single continuous string
                transcript_text = "\n".join([item['text'] for item in transcript_data])

            except Exception as e:
                # Catch and store any errors encountered during transcript retrieval
                error = f"Error fetching transcript: {str(e)}"

    # Render the HTML template with the transcript text and any error messages
    return render_template("index.html", transcript=transcript_text, error=error)

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
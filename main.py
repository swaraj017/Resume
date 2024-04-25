from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return 'No file part', 400
    resume_file = request.files['resume']
    # Save the resume file or do whatever you want with it
    resume_file.save('uploads/resume.txt')
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
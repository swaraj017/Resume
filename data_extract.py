import os
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Define the directory path for uploaded files
UPLOAD_FOLDER = 'templates'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/success/<filename>')
def success(filename):
    return f'The file "{filename}" has been uploaded successfully.'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        # If the user does not select a file, the browser may submit an empty part without a filename
        if file.filename == '':
            return 'No selected file'

        # Save the file to the UPLOAD_FOLDER directory
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('success', filename=filename))

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)

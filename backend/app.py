from flask import Flask, send_from_directory
import os

# Pfad zur index.html im frontend-Ordner
frontend_folder = os.path.join(os.path.dirname(__file__), '../frontend')

app = Flask(__name__, static_folder=frontend_folder)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
    



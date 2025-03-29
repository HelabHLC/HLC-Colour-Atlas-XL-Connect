from flask import Flask, send_from_directory
import os

frontend_folder = os.path.join(os.path.dirname(__file__), '../frontend')
app = Flask(__name__, static_folder=frontend_folder)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # 👈 Heroku-Port verwenden
    app.run(host='0.0.0.0', port=port)



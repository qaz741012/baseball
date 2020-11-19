# ========== import ==========
# basic
from flask import Flask, request, abort, render_template

# ========== initialize ==========
app = Flask(__name__)
app.config.from_pyfile('config.py')

# ========== main ==========
@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()

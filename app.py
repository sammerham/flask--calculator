from flask import Flask
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """Returns a welcome message"""
    return """
        <html>
            <body>
                <h1>Welcome</h1>
            </body>
        </html>
        """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """Returns a welcome message"""
    return """
        <html>
            <body>
                <h1>This is our landing page</h1>
            </body>
        </html>
        """



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


@app.route('/welcome/home')
def home():
    """Returns a welcome message"""
    return """
        <html>
            <body>
                <h1>Welcome home</h1>
            </body>
        </html>
        """


@app.route('/welcome/back')
def back():
    """Returns a welcome message"""
    return """
        <html>
            <body>
                <h1>Welcome back</h1>
            </body>
        </html>
        """
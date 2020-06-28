from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h3>welcome to makeshifter</h3>
        <h3>site under construction...</h3>
    '''

if __name__ == "__main__":
    app.run()
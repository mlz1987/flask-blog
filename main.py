from flask import Flask
from config import Devconfig

app = Flask(__name__)


# Get the config from object of DevConfig
# use config.from_object() but not use app.config['DEBUG']
app.config.from_object(Devconfig)

# URL='/'
@app.route('/')
def home():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':

    # Entry the application
    app.run()

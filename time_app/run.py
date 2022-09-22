from flask import Flask
app = Flask(__name__)

from datetime import datetime
from pytz import timezone


@app.route('/')
def hello_world():
    return 'Hello world! This is Hsin\'s app, you could find current time by visiting http://0.0.0.0:8080/time'


@app.route('/time')
def est_time():
    now_est = datetime.now(timezone('US/Eastern'))
    return 'Current time of New York (EST) is ' + now_est.strftime("%I:%M %p") + ' and today is ' + now_est.strftime("%m/%d/%Y")
    



app.run(host='0.0.0.0',
        port=8080,
        debug=True)

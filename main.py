#!/usr/bin/env python3
from flask import Flask, render_template
import matplotlib.pyplot as plt

import base64
from io import BytesIO

app = Flask(__name__)

def get_web_plot():
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


@app.route('/')
def main():
    plt.plot(range(10))
    html_plot1 = get_web_plot()
    return render_template('home.html', html_plot1=html_plot1)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
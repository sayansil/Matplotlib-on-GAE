#!/usr/bin/env python3
from flask import Flask, render_template
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import html

import base64
from io import BytesIO

app = Flask(__name__)

def get_static_plot():
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def get_dynamic_plot():
    plot = figure()
    plot.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
    script, div = components(plot)
    return html.unescape(script), html.unescape(div)

@app.route('/')
def main():
    plt.plot(range(10))
    html_plot1 = get_static_plot()
    html_plot2 = get_dynamic_plot()
    return render_template('home.html', mplib_data=html_plot1, bokeh_script=html_plot2[0], bokeh_div=html_plot2[1])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
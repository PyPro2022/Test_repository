from flask import Flask, render_template
from webargs import fields
from webargs.flaskparser import use_kwargs
from utils import get_currency, data, get_fields_names

app = Flask(__name__)

@app.route("/rates")
@use_kwargs(
            {'currency':fields.Str(required=True)},
            location = 'query')

def bitcoin_rate(currency):
    rate = get_currency(currency)
    fields_names = get_fields_names()
    rng = len(fields_names)
    return render_template('rates/s_search_res.html', rate=rate, names=fields_names, rng=rng)




@app.route("/")
def index():
    return render_template('index.html')


# D:\PyProjects\FLASK\Lesson11\DZ_9_BitcoinRate\app.py
#D:\PyProjects\FLASK\Lesson11\app.py


@app.route('/rates/info')
def info():
    fields_names = get_fields_names()
    return render_template('rates/info.html', cur_list=data, names=fields_names)



if __name__ == '__main__':
    app.run(debug = True, port = 5000)


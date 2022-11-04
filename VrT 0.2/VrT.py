
import fasttext
import NLP
from flask import Flask, render_template, request ,jsonify , url_for , redirect
import pandas as pd
import numpy as np



m = NLP
model = fasttext.load_model('modelff.bin')



app = Flask(__name__,template_folder='template')


@app.route('/')
def man():
    return render_template('home.html'
)


@app.route('/output', methods=['POST'])
def output():

    #data1 = request.form['a']
    data1 = request.json['user_input']

    x = model.predict(m.NLP1(data1))
    y = str(x[0])
    data = str(y)
    data2 = int(x[1] * 100)
    data2 = str(data2)
    y=y[11:-3]


    #return jsonify( render_template('kkkk1.html', data=y,,data3=data1))
    return jsonify("<div id ='d3'> <table> <thead> <td> Description </td> <td>CWE</td> <td> Precision </td></thead> <tr> <td>"+data1+"</td> <td>"+y+"</td> <td> "+data2+"% </td> </tr> </table> </div> ")





if __name__ == "__main__":
    app.run(debug=True)


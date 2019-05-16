from flask import Flask, render_template, request
import unicodedata
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/', methods=['GET'])
def search(names=None, category=None, symbols=None):

    q = request.args.get('q')
    names = []
    category = []
    symbols = []

    if len(q) == 0:
        return render_template('index.html')
    else:
        for i in range (230000):
            name = unicodedata.name(chr(i), '')
            verif = str(q).upper() in name

            if verif == True:
                symbols.append(unicodedata.lookup(name))
                names.append(unicodedata.name(chr(i), ''))
                
                category.append(unicodedata.category(unicodedata.lookup(name)))


        return render_template('index.html', names=names, category=category, symbols=symbols)
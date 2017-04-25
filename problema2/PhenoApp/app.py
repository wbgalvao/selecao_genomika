from flask import abort, Flask, g, render_template, request, url_for
import sqlite3

app = Flask('PhenoApp')

DATABASE = 'local_phenodb.db'

# Conexao com banco de dados local
# ref: http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Termina conexao com banco de dados local
# ref: http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html'), 200

@app.route('/genes', methods=['POST'])
def genes():
    disease = request.form['disease']
    cur = get_db().cursor()
    cur.execute("SELECT gene FROM pheno_db WHERE disease=? COLLATE NOCASE", (disease,))
    result = cur.fetchall()
    genes = [result[0][0] for row in result]
    return render_template('genes.html', disease=disease, genes=genes), 200

app.run(debug=False, use_reloader=False)

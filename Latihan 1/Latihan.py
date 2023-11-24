from flask import Flask, render_template
# import connexion

# app = connexion.App(__name__, specification_dir='./')

# app.add_api('swagger.yml')

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/tambah')
def tambah():
    return render_template('tambah.html')


@app.route('/list')
def list():
    return render_template('list.html')

if __name__=="__main__":
    app.run(debug=True)
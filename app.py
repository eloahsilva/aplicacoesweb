from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email')
@app.route('/faleconosco')
@app.route('/contato')
def contato():
    dados={'nome': 'Eloah', 'email': 'silva.eloah@escolar.ifrn.edu.br'}
    return render_template('contato.html', dados=dados)

@app.route('/usuario', defaults={'nome': 'Desconhecido', 'sobrenome': 'Desconhecido'})
@app.route('/usuario/<nome>/<sobrenome>')
def usuario(nome, sobrenome):
    info={'nome': nome, 'sobrenome': sobrenome}
    return render_template('usuario.html', info=info)

@app.route('/semestre/<int:x>')
def semestre(x):
    dados = {}
    dados['atual'] = x
    dados['anterior'] = x-1
    return render_template('semestre.html', dados=dados)

@app.route('/perfil/<usuario>', defaults={'usuario': 'eloah'})
@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)

@app.route('/dados')
def dados():
    return render_template('dados.html')
@app.route('/recebedados', methods=['GET', 'POST'])
def recebedados():
    nome = request.form.get['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    estado = request.form.get('estado')
    escola = request.form.getlist('escola')
    return render_template('recebedados.html', nome=nome, sobrenome=sobrenome, email=email, estado=estado, escola=escola)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    usuario = request.form.get('login')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == '12345':
        return redirect(url_for('arearestrita'))
    else:
        return redirect(url_for('acessonegado'))

@app.route('/arearestrita')
def arearestrita():
    return render_template('arearestrita.html')

@app.route('/exemplolaco')
def exemplolaco():
    return render_template('exemplolaco.html')

@app.route('/acessonegado')
def acessonegado():
    return render_template('acessonegado.html')

@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('idade.html', idade=idade)

@app.route('/produtos')
def produtos():
    itens=[{'nome':'Teclado', 'preco':'200'}, 
        {'nome':'Smartphone', 'preco':'4500'},
        {'nome':'Pen-drive', 'preco':'50'}]
    qtd = len(itens)
    return render_template('produtos.html', itens=itens, qtd=qtd)

if __name__ == '__main__':
    app.run()
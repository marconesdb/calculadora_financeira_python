import os
from flask import Flask, render_template, request

template_dir = os.path.abspath('')
app = Flask(__name__, template_folder=template_dir)

# Restante do seu código aqui


def calcular_tempo_para_alcancar_meta(meta, poupanca_mensal, taxa_juros_mensal):
    poupanca_atual = 0
    meses = 0

    while poupanca_atual < meta:
        meses += 1
        poupanca_atual *= 1 + taxa_juros_mensal
        poupanca_atual += poupanca_mensal

    return meses


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        meta = float(request.form['meta'])
        poupanca_mensal = float(request.form['poupanca_mensal'])

        meses = calcular_tempo_para_alcancar_meta(meta, poupanca_mensal, 0.00875)

        anos = meses // 12
        meses = meses % 12

        return render_template('result.html', anos=anos, meses=meses)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
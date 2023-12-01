from tkinter import *
import math

calculadora = Tk()
calculadora.title('Calculadora')
calculadora.geometry('243x358+400+100')
calculadora.resizable(width=False, height=False)
calculadora.config(bg='#031626')

frame_tela = Frame(calculadora, width=275, height=60, bg='#1b1e21')
frame_tela.grid(row=0, column=0)

frame_body = Frame(calculadora, width=275, height=335, bg='#031626')
frame_body.grid(row=1, column=0)


todos_dados = ''


def entrar_dados(temp):
    global todos_dados
    todos_dados += str(temp)
    valor_texto.set(todos_dados)


def calcular():
    try:
        global todos_dados
        todos_dados = todos_dados.replace('x', '*')
        todos_dados = todos_dados.replace('÷', '/')
        if '^' in todos_dados:
            base, expoente = todos_dados.split('^')
            resultado = float(base) ** float(expoente)
            valor_texto.set(str(resultado))
        elif '**' in todos_dados or '*-+' in todos_dados or '*+-' in todos_dados:
            valor_texto.set('Equação Inválida.')
        else:
            resultado = eval(todos_dados)
            valor_texto.set(str(resultado))
    except SyntaxError:
        valor_texto.set('Equação Inválida.')
    except ZeroDivisionError:
        valor_texto.set('Impossível dividir por 0.')


def calcular_raiz_quadrada():
    global todos_dados
    try:
        resultado = math.sqrt(float(todos_dados))
        valor_texto.set(str(resultado))
    except ValueError:
        valor_texto.set('Equação Inválida.')


def calcular_porcentagem():
    global todos_dados
    if '+' in todos_dados:
        valor1, operador, valor2 = todos_dados.partition('+')
        if valor1 and operador and valor2:
            valor1 = float(valor1)
            valor2 = float(valor2)
            resultado = (valor1 * valor2) / 100
            valor_texto.set(str(resultado))
        else:
            valor_texto.set('Equação Inválida.')
    elif '-' in todos_dados:
        valor1, operador, valor2 = todos_dados.partition('-')
        if valor1 and operador and valor2:
            valor1 = float(valor1)
            valor2 = float(valor2)
            resultado = (valor1 * valor2) / 100
            valor_texto.set(str(resultado))
        else:
            valor_texto.set('Equação Inválida.')
    elif '*' in todos_dados:
        valor1, operador, valor2 = todos_dados.partition('*')
        if valor1 and operador and valor2:
            valor1 = float(valor1)
            valor2 = float(valor2)
            resultado = (valor1 * valor2) / 100
            valor_texto.set(str(resultado))
        else:
            valor_texto.set('Equação Inválida.')
    elif '/' in todos_dados:
        valor1, operador, valor2 = todos_dados.partition('/')
        if valor1 and operador and valor2:
            valor1 = float(valor1)
            valor2 = float(valor2)
            resultado = (valor1 * valor2) / 100
            valor_texto.set(str(resultado))
        else:
            valor_texto.set('Equação Inválida.')
    else:
        valor_texto.set('Equação Inválida.')


def limpar_tela():
    global todos_dados
    todos_dados = ''
    valor_texto.set('')


valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=0, relief=FLAT,
                  anchor='e', justify=RIGHT, font='Lato 19', bg='#1b1e21', fg='#d5d8db')
app_label.place(x=0, y=0)


Bt7 = Button(calculadora, command=lambda: entrar_dados('7'), text='7', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt7.place(x=2, y=120)

Bt8 = Button(calculadora, command=lambda: entrar_dados('8'), text='8', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt8.place(x=62, y=120)

Bt9 = Button(calculadora, command=lambda: entrar_dados('9'), text='9', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt9.place(x=122, y=120)

Bt4 = Button(calculadora, command=lambda: entrar_dados('4'), text='4', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt4.place(x=2, y=180)

Bt5 = Button(calculadora, command=lambda: entrar_dados('5'), text='5', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt5.place(x=62, y=180)

Bt6 = Button(calculadora, command=lambda: entrar_dados('6'), text='6', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt6.place(x=122, y=180)

Bt1 = Button(calculadora, command=lambda: entrar_dados('1'), text='1', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt1.place(x=2, y=240)

Bt2 = Button(calculadora, command=lambda: entrar_dados('2'), text='2', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt2.place(x=62, y=240)

Bt3 = Button(calculadora, command=lambda: entrar_dados('3'), text='3', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt3.place(x=122, y=240)

Bt0 = Button(calculadora, command=lambda: entrar_dados('0'), text='0', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
Bt0.place(x=62, y=300)

BtVirgula = Button(calculadora, command=lambda: entrar_dados('.'), text='.', relief=RAISED,
                   width=7, height=3, overrelief=RIDGE)
BtVirgula.place(x=2, y=300)

BtIgual = Button(calculadora, command=calcular, text='=', relief=RAISED,
                 width=7, height=3, overrelief=RIDGE)
BtIgual.place(x=122, y=300)

BtRaiz = Button(calculadora, command=calcular_raiz_quadrada, text='√', relief=RAISED,
                width=7, height=3, overrelief=RIDGE)
BtRaiz.place(x=182, y=60)

BtDivisao = Button(calculadora, command=lambda: entrar_dados('/'), text='/', relief=RAISED,
                   width=7, height=3, overrelief=RIDGE)
BtDivisao.place(x=182, y=120)

BtSubtracao = Button(calculadora, command=lambda: entrar_dados('-'), text='-', relief=RAISED,
                     width=7, height=3, overrelief=RIDGE)
BtSubtracao.place(x=182, y=240)

BtMultiplicacao = Button(calculadora, command=lambda: entrar_dados('*'), text='*',
                         relief=RAISED, width=7, height=3, overrelief=RIDGE)
BtMultiplicacao.place(x=182, y=180)

BtC = Button(calculadora, command=limpar_tela, text='C', relief=RAISED,
             width=7, height=3, overrelief=RIDGE)
BtC.place(x=2, y=60)

BtPorcentagem = Button(calculadora, command=calcular_porcentagem, text='%', relief=RAISED,
                       width=7, height=3, overrelief=RIDGE)
BtPorcentagem.place(x=122, y=60)

BtPotencia = Button(calculadora, command=lambda: entrar_dados('^'), text='^', relief=RAISED,
                    width=7, height=3, overrelief=RIDGE)
BtPotencia.place(x=62, y=60)

BtSoma = Button(calculadora, command=lambda: entrar_dados('+'), text='+', relief=RAISED,
                width=7, height=3, overrelief=RIDGE)
BtSoma.place(x=182, y=300)


calculadora.mainloop()

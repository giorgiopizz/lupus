import json
import random

giocatori=[]
figure={'lupo':0,'contadino':0,'veggente':1,'donna':1,'medium':0,'licantropo':0}
a=input('Impostazioni precedenti?(s/n)')
if a=='s':
    config=json.load(open('config.json'))
    giocatori=config['giocatori']
    figure=config['figure']
    del config
else:
    nome=input('Inserire nomi giocatori:')

    while nome!='#':
        giocatori.append(str(nome))
        nome = input('Inserire nome:')

    del nome
    a=input('Giocare con medium?(s/n)')
    if a=='s':
        figure['medium']=1
    a=input('Con quanti lupi?')
    figure['lupo'] = int(a)
    a = input('Con quanti contadini?')
    figure['contadino'] = int(a)
    a = input('Con quanti licantropi?')
    figure['licantropo'] = int(a)

    print('Controllo che il numero di figure e di giocatori combaci...')
    n=0
    for e in figure.keys():
        n+=figure[e]
    if n!=len(giocatori):
        print('I numeri non corrispondono. I giocatori sono i seguenti:')
        for e in giocatori:
            print(e)
        print('Il numero di figure è il seguente')
        for e in figure.keys():
            print(str(e)+' : '+str(figure[e]))
        print('Riprovare la configurazione')
        quit()
    else:
        config={}
        config['giocatori']=giocatori
        config['figure']=figure
        print(config)
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        print('pronti a giocare...')
        del config

#inizia il gioco
#creo una copia dei dati iniziali
giocatori_copy=giocatori.copy()
figure_copy=figure.copy()

a=input('Estrarre?(s/n)')
while a=='s':
    n=0
    for e in list(figure.keys()):
        if figure[e] <= 0:
            del figure[e]
        else:
            n += figure[e]

    for _ in range(n):
        i = random.randint(0, len(figure.keys()) - 1)
        fig = list(figure.keys())[i]
        gioc = giocatori[0]
        print('Il giocatore '+gioc+' è '+fig)
        figure[fig] -= 1
        del giocatori[0]
        for e in list(figure.keys()):
            if figure[e] <= 0:
                del figure[e]
        n -= 1
    giocatori = giocatori_copy.copy()
    figure = figure_copy.copy()
    a = input('Pronti ad estrarre?(s/n)')


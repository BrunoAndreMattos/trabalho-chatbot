# pyinstaller yourprogram.py
import random
import sys
import re
import time
import winsound
import unicodedata
from data import *

# https://stackoverflow.com/questions/6537481/python-making-a-beep-noise/18984326
duration = 100  # milliseconds
freq = 400  # Hz

# Seleciona ao aleatório um nome para o bot
nomeBot = random.choice(nomes)
tempo = 2.2

def fase1():
    # Apresentação do bot e prompt de nome do usuário
    winsound.Beep(freq, duration)
    print(nomeBot + ': Olá meu nome é ' + nomeBot + ', eu te ajudarei a escolher o filme ideal para assitir!')
    time.sleep(tempo)
    winsound.Beep(freq, duration)
    print(nomeBot + ': Qual seu nome?')

    entrada = input("Você: ")
    time.sleep(tempo)
    
    # 3 casos:
    # 1) Nome vazio: seleciona nome aleatório para usuário
    # 2) Nome muito comprido: abrevia o nome do usuário para as 2 primeiras letras
    # 3) Nome normal: elogia o nome do usuário
    if (entrada == ''): # 1)
        nomeUsuario = random.choice(nomes)

        winsound.Beep(freq, duration)
        print(nomeBot + ": " + random.choice(falasNomeNada) + nomeUsuario)
        time.sleep(tempo)
    else: # 3)
        nomeUsuario = re.findall(pegaNome, entrada)
        nomeUsuario = nomeUsuario[0]
        
        if (len(nomeUsuario) > 10): # 2)
            nomeUsuario = re.findall(pegaApelido, nomeUsuario)
            nomeUsuario = nomeUsuario[0]
            nomeUsuario = nomeUsuario + nomeUsuario

            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasNomeComprido) + nomeUsuario)
            time.sleep(tempo)
        else: # 3)
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasNomeElogio) + nomeUsuario)
            time.sleep(tempo)


    # Seleciona um gênero aleatório para caso o usuário não responda nada ou falhe em entrar um gênero válido
    auxGenero = random.choice(generos)

    # Sugere para o usuário se gosta do gênero aleatório
    winsound.Beep(freq, duration)
    print(nomeBot + ': ' + random.choice(falasSugereGenero) + auxGenero + ', sim?')

    entrada = input(nomeUsuario + ": ")
    time.sleep(tempo)
    entrada = entrada.lower()

    # 5 casos:
    # 1) Encontra positivo e não negativo na frase: interpreta que gosta do gênero sugerido e retorna o gênero
    # 2) Encontra string vazia: responde passivo agressivo, seleciona e retorna um novo gênero selecionado ao aleatório
    # 3) Se não for nem vazia nem sim: procura o nome do gênero, se houver returna se não houver
    # 4) entra num loop até perguntando qual o gênero favorito do usuário até ele entrar um gênero válido ou o bot perder a paciência
    # 5) Se o usuário entrar um gênero válido retorna o gênero, se o bot perder a paciência seleciona um gênero aleatório e retorna o gênero
    if re.search(curte, entrada) and not(re.search(naoCurte, entrada)):
        genero = auxGenero # 1)
        winsound.Beep(freq, duration)
        print(nomeBot + ': ' + random.choice(falasComentaSobreGenero) + genero)
        time.sleep(tempo)
        return (genero, nomeUsuario)
    elif entrada == '':
        genero = random.choice(generos)
        winsound.Beep(freq, duration)
        print(nomeBot + ': ' + random.choice(falasEscolheGeneroAleatorio) + genero) # 2)
        time.sleep(tempo)
        return (genero, nomeUsuario)
    else:
        if re.search(regExGeneros, entrada):
            genero = re.findall(regExGeneros, entrada)
            genero = genero[0]
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasComentaSobreGenero) + genero) # 3)
            time.sleep(tempo)
            return (genero, nomeUsuario)
        else:
            paciencia = 3
            generoValido = False
            while (generoValido == False and paciencia > 0): # 4)
                paciencia -= 1
                winsound.Beep(freq, duration)
                print(nomeBot + ': ' + 'Então qual você diria que é seu genêro de filmes favorito?')

                entrada = input(nomeUsuario + ": ")
                time.sleep(tempo)
                entrada = entrada.lower()

                if re.search(regExGeneros, entrada) and not(re.search(naoCurte, entrada)): # 5)
                    generoValido = True
                    genero = re.findall(regExGeneros, entrada)
                    genero = genero[0]
                    winsound.Beep(freq, duration)
                    print(nomeBot + ': ' + random.choice(falasComentaSobreGenero) + genero)
                    time.sleep(tempo)
                    return (genero, nomeUsuario)
                else: 
                    winsound.Beep(freq, duration)
                    print(nomeBot + ': ' + random.choice(falasNaoReconheceGenero))
                    time.sleep(tempo)
            
            if paciencia == 0: # 5)
                genero = random.choice(generos)
                winsound.Beep(freq, duration)
                print(nomeBot + ': ' + random.choice(falasEscolheGeneroAleatorio) + genero)
                time.sleep(tempo)
                return (genero, nomeUsuario)

    # Retorna o nome do usuário e o gênero estabelecido
    return (genero, nomeUsuario)

def fase2(genero, nomeUsuario):
    respostaValida = False

    # Repete a pergunta até o usuário entrar um dos 3 casos:
    # 1) vazio onde o bot escolhe se vai ser lançamento ou antigo para o usuário
    # 2) encontra lançamentos ou sinonimos e não antigos ou sinonimos
    # 3) encontra antigos ou sinoniomos e não lançamentos ou sinonimos
    # Retorna a preferência do usuário
    while respostaValida == False:
        winsound.Beep(freq, duration)
        print(nomeBot + ': Agora me diga, você prefere lançamentos ou filmes mais antigos?')

        entrada = input(nomeUsuario + ": ")
        time.sleep(tempo)
        entrada = entrada.lower()

        if entrada == '':
            aux = ('antigos', 'novos')
            data = random.choice(aux)
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasEscolheAleatorio) + data)
            time.sleep(tempo)
            respostaValida = True
        elif re.search(encontraLancamento, entrada) and not(re.search(encontraAntigo, entrada)):
            data = re.findall(encontraLancamento, entrada)
            data = data[0]
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasComentaSobreLancamento))
            time.sleep(tempo)
            respostaValida = True
        elif re.search(encontraAntigo, entrada) and not(re.search(encontraLancamento, entrada)):
            data = re.findall(encontraAntigo, entrada)
            data = data[0]
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasComentaSobreAntigo))
            time.sleep(tempo)
            respostaValida = True
        else:
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasNaoReconhece))
            time.sleep(tempo)
            respostaValida = False

    winsound.Beep(freq, duration)
    print(nomeBot + ': ' + random.choice(falasResumeSituacao) + genero + ', ' + data)
    time.sleep(tempo)
    return data

def fase3(genero, lancamento, nomeUsuario):
    respostaValida = False

    # Repete a pergunta até o usuário entrar um dos 3 casos:
    # 1) vazio onde o bot escolhe se vai ser popular ou desconhecido para o usuário
    # 2) encontra popular ou sinonimos e não desconhecido ou sinonimos
    # 3) encontra descohecido ou sinoniomos e não popular ou sinonimos
    # Retorna a preferência do usuário
    while respostaValida == False:
        winsound.Beep(freq, duration)
        print(nomeBot + ': Enfim, você prefere filmes desconhecidos ou algo mais popular?')

        entrada = input(nomeUsuario + ": ")
        time.sleep(tempo)
        entrada = entrada.lower()

        if entrada == '':
            aux = ('indie', 'conhecidos')
            conhecido = random.choice(aux)
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasEscolheAleatorio) + conhecido)
            time.sleep(tempo)
            respostaValida = True
        elif re.search(encontraConhecido, entrada) and not(re.search(encontraIndie, entrada)):
            conhecido = re.findall(encontraConhecido, entrada)
            conhecido = conhecido[0]
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasComentaSobreConhecido))
            time.sleep(tempo)
            respostaValida = True
        elif re.search(encontraIndie, entrada) and not(re.search(encontraConhecido, entrada)):
            conhecido = re.findall(encontraIndie, entrada)
            conhecido = conhecido[0]
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasComentaSobreIndie))
            time.sleep(tempo)
            respostaValida = True
        else:
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasNaoReconhece))
            time.sleep(tempo)
            respostaValida = False

    winsound.Beep(freq, duration)
    print(nomeBot + ': ' + random.choice(falasResumeSituacao) + genero + ', ' + lancamento + ' e ' + conhecido)
    time.sleep(tempo)
    return conhecido

def fase4(genero, lancamento, indie, nomeUsuario):
    
    # Concerta edge cases onde o usuário pode ter escrito abreviações ou plural diferente do gênero
    # Remove acentos para facilitar a comparação
    if re.search(r'(animações|animaçoes)', genero):
        genero = strip_accents('animação')
    elif re.search(r'(horror)', genero):
        genero = 'terror'
    elif re.search(r'(sci fi|sci-fi|ficção|ficcao)', genero):
        genero = strip_accents('ficção científica')
    elif re.search(r'(herói|heroi|super heroi)', genero):
        genero = strip_accents('super-herói')
    else:
        genero = strip_accents(genero)

    # Atribui true or false ao checador de lancamento dependendo do que o usuario respondeu na fase 2
    if re.match(encontraLancamento, lancamento):
        lancamento = 1
    else:
        lancamento = 0

    # Atribui true or false ao checador de indie dependendo do que o usuario respondeu na fase 3
    if re.match(encontraIndie, indie):
        indie = 1
    else:
        indie = 0

    # Passar por todos os filmes da lista até encontrar algum que se encaixe nas definições do usuário
    for filme in filmes:
        # Remove acento do filmes e compara todos os dados
        generoFilme = strip_accents(filme.genero)
        if filme.novo == lancamento and filme.indie == indie and generoFilme == genero:
            winsound.Beep(freq, duration)
            print(nomeBot + ': ' + random.choice(falasMostraRecomendacao) + filme.nome)
            time.sleep(tempo)
    winsound.Beep(freq, duration)
    print(nomeBot + ': ' + random.choice(falasMensagemDeTchau))
    return 0

# https://stackoverflow.com/questions/44431730/how-to-replace-accented-characters-in-python?rq=1
def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

def main():
    # Chama fase um de diálogo incial e estabelece o gênero de filme favorito do usuário
    generoENome = fase1()
    genero = generoENome[0]
    nomeUsuario = generoENome[1]
    # Chama fase dois que estabelece se o usuário prefere lançamentos ou filmes antigos
    lancamento = fase2(genero, nomeUsuario)
    # Chama fase três que estabelece se o usuário prefere filmes conhecidos ou indie
    conhecido = fase3(genero, lancamento, nomeUsuario)
    # Chama fase quatro onde pega todos os dados coletados do usuário e encontra um filme que se encaixe na descrição
    fase4(genero, lancamento, conhecido, nomeUsuario)
    input()

if __name__ == '__main__':
    main()
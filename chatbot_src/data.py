nomes = ("Alexandre", "Eduardo", "Henrique", "Murilo", "Theo",
    "André", "Enrico", "Henry", "Nathan", "Thiago",
    "Antônio", "Enzo", "Ian", "Otávio", "Thomas",
    "Augusto", "Erick", "Isaac", "Pietro", "Vicente",
    "Breno", "Felipe", "João", "Rafael", "Vinícius",
    "Bruno", "Fernando", "Kaique", "Raul", "Vitor",
    "Caio", "Francisco", "Leonardo", "Rian", "Yago",
    "Cauã", "Frederico", "Luan", "Ricardo", "Ygor",
    "Daniel", "Guilherme", "Lucas", "Rodrigo", "Yuri",
    "Danilo", "Gustavo", "Mathias", "Samuel", "Agatha",
    "Camila", "Esther", "Isis", "Maitê", "Natália",
    "Alícia", "Carolina", "Fernanda", "Joana", "Malu",
    "Nicole", "Amanda", "Catarina", "Gabriela", "Laís",
    "Maria", "Olívia", "Ana", "Cecília", "Gabrielle",
    "Lara", "Mariah", "Pietra", "Antonela", "Clara",
    "Giovanna", "Larissa", "Mariana", "Rafaela", "Aurora",
    "Clarice", "Giulia", "Lavínia", "Marina", "Rebeca",
    "Bárbara", "Eduarda", "Heloísa", "Letícia", "Maya",
    "Sara", "Beatriz", "Elisa", "Isabel", "Liz",
    "Melissa", "Sophie", "Bianca", "Emanuelly", "Isabelly",
    "Lorena", "Milena", "Stella", "Bruna", "Emilly",
    "Isadora", "Luana", "Mirella", "Vitória", "Yasmin")

generos = ("ação", "animação", "aventura",
        "comédia", "comédia romântica",
        "documentário", "drama",
        "ficção científica", "guerra", "musical",
        "policial", "romance", "super-herói",
        "suspense", "terror")

class Filme:
    def __init__(self, nome, genero, indie, novo):
        self.nome = nome        #str
        self.genero = genero    #str
        self.indie = indie      #bool
        self.novo = novo        #bool

filmes = []
# filmes novos e não-indie
filmes.append(Filme('Alita: Anjo de Combate (2019)', 'ação',                        0, 1))
filmes.append(Filme('Dumbo (2019)', 'animação',                                     0, 1))
filmes.append(Filme('Aladdin (2019)', 'aventura',                                   0, 1))
filmes.append(Filme('De Pernas pro Ar 3 (2019)', 'comédia',                         0, 1))
filmes.append(Filme('Casal Improvável (2019)', 'comédia romântica',                 0, 1))
filmes.append(Filme('Amazônia - O despertar da florestania (2019)', 'documentário', 0, 1))
filmes.append(Filme('Superação - O Milagre da Fé (2019)', 'drama',                  0, 1))
filmes.append(Filme('Capitã Marvel (2019)', 'ficção científica',                    0, 1))
filmes.append(Filme('Tolkien (2019)', 'guerra',                                     0, 1))
filmes.append(Filme('UglyDolls (2019)', 'musical',                                  0, 1))
filmes.append(Filme('Pokémon - Detetive Pikachu (2019)', 'policial',                0, 1))
filmes.append(Filme('After (2019)', 'romance',                                      0, 1))
filmes.append(Filme('Vingadores: Ultimato (2019)', 'super-herói',                   0, 1))
filmes.append(Filme('A Maldição da Chorona (2019)', 'suspense',                     0, 1))
filmes.append(Filme('Cemitério maldito (2019)', 'terror',                           0, 1))
# filmes novos e indie
filmes.append(Filme('The Offender (2019)', 'ação',                                     1, 1))
filmes.append(Filme('A Lenda dos Guardiões (2010)', 'animação',                        1, 1))
filmes.append(Filme('O Grande Hotel Budapeste (2014)', 'aventura',                     1, 1))
filmes.append(Filme('Night of Adventure (2019)', 'comédia',                            1, 1))
filmes.append(Filme('Scott Pilgrim Contra o Mundo (2010)', 'comédia romântica',        1, 1))
filmes.append(Filme('O Sushi dos Sonhos de Jiro (2011)', 'documentário',               1, 1))
filmes.append(Filme('Eu, Você e a Garota Que Vai Morrer (2015)', 'drama',              1, 1))
filmes.append(Filme('Ela (2013)', 'ficção científica',                                 1, 1))
filmes.append(Filme('Little Boy - Além do Impossível (2015)', 'guerra',                1, 1))
filmes.append(Filme('Inside Llewyn Davis: Balada de um Homem Comum (2013)', 'musical', 1, 1))
filmes.append(Filme('Um Deslize Perigoso (2015)', 'policial',                          1, 1))
filmes.append(Filme('A Garota Dinamarquesa (2015)', 'romance',                         1, 1))
filmes.append(Filme('Kick-Ass (2010)', 'super-herói',                                  1, 1))
filmes.append(Filme('Frank (2014)', 'suspense',                                        1, 1))
filmes.append(Filme('O Uivo (2015)', 'terror',                                         1, 1))
# filmes antigos e indie
filmes.append(Filme('O Profissional (1994)', 'ação',                        1, 0))
filmes.append(Filme('Planeta Fantástico (1973)', 'animação',                1, 0))
filmes.append(Filme('Pequena Miss Sunshine (2006)', 'aventura',             1, 0))
filmes.append(Filme('Barbarella (1968)', 'comédia',                         1, 0))
filmes.append(Filme('Essa Estranha Atração (1988)', 'comédia romântica',    1, 0))
filmes.append(Filme('A Enseada (2009)', 'documentário',                     1, 0))
filmes.append(Filme('O Barco: Inferno no Mar (1981)', 'drama',              1, 0))
filmes.append(Filme('Laranja Mecânica (1971)', 'ficção científica',         1, 0))
filmes.append(Filme('Vá e Veja (1985)', 'guerra',                           1, 0))
filmes.append(Filme('The Rocky Horror Picture Show (1975)', 'musical',      1, 0))
filmes.append(Filme('Taxi Driver: Motorista de Táxi (1976)', 'policial',    1, 0))
filmes.append(Filme('Maurice (1987)', 'romance',                            1, 0))
filmes.append(Filme('The Crow (1994)', 'super-herói',                       1, 0))
filmes.append(Filme('Parceiros da Noite (1980)', 'suspense',                1, 0))
filmes.append(Filme('Trilogia de Terror (1975)', 'terror',                  1, 0))
# filmes antigos e não-idie
filmes.append(Filme('Star Wars, Episódio V: O Império Contra-Ataca (1980)', 'ação', 0, 0))
filmes.append(Filme('A Viagem de Chihiro (2001)', 'animação',                       0, 0))
filmes.append(Filme('O Senhor dos Anéis: O Retorno do Rei (2003)', 'aventura',      0, 0))
filmes.append(Filme('Luzes da Cidade (1931)', 'comédia',                            0, 0))
filmes.append(Filme('A Vida é Bela (1997)', 'comédia romântica',                    0, 0))
filmes.append(Filme('Shoah (1985)', 'documentário',                                 0, 0))
filmes.append(Filme('Um Sonho de Liberdade (1994)', 'drama',                        0, 0))
filmes.append(Filme('Matrix (1999)', 'ficção científica',                           0, 0))
filmes.append(Filme('O Resgate do Soldado Ryan (1998)', 'guerra',                   0, 0))
filmes.append(Filme('O Pianista (2002)', 'musical',                                 0, 0))
filmes.append(Filme('Seven: Os Sete Crimes Capitais (1995)', 'policial',            0, 0))
filmes.append(Filme('Forrest Gump: O Contador de Histórias (1994)', 'romance',      0, 0))
filmes.append(Filme('Batman: O Cavaleiro das Trevas (2008)', 'super-herói',         0, 0))
filmes.append(Filme('Os Suspeitos (1995)', 'suspense',                              0, 0))
filmes.append(Filme('Psicose (1960)', 'terror',                                     0, 0))

# expressões regulares
pegaNome = r'\w[a-zÀ-ÿ]*$'
pegaApelido = r'^\w{2}'
regExGeneros = r'(animação|animacao|animaçao|animações|animaçoes|ação|açao|aventura|comédia romântica|comedia romântica|comedia romantica|comédia|comedia|documentario|documentário|drama|ficção científica|sci fi|sci-fi|ficçao cientifica|ficção cientifica|guerra|musical|policial|romance|super-herói|herói|heroi|super heroi|super-heroi|suspense|terror|horror)'
curte = r'(sim|gosto|curto|pode ser|aham|ok|true|tru|ye|yes|certo|adoro|amo|as vezes|sou)'
naoCurte = r'(não|nao|na verdade|nah|gosto mesmo é de|não gosto|nao gosto)'
encontraLancamento = r'(lançamentos|lançamento|lancamento|lancamentos|blockbuster|AAA|novos|novo)'
encontraAntigo = r'(antigos|clássicos|clássico|classico|classicos|antigo|datados)'
encontraIndie = r'(nao famoso|não famoso|não famosos|nao famosos|indie|indies|desconnhecido|desconhecidos|não popular|não populares|nao populares|obscuro|obscuro|cult|cults|não muito popular|não muito populares|nao muito populares|nao popular|nao muito popular|independente|independentes)'
encontraConhecido = r'(conhecidos|conhecido|popular|populares|famoso|famosos)'

# fillers
fillers = ("", "", "", "", "", "", "", "", "", "", "")

# base de dados de falas da fase 1
falasNomeNada = ("Olha... se você não quer falar eu não vou te forçar, mas de agora em diante você será ",
                "Hmmmm temos alguém que se importa com a privacidade aqui... vou te chamar de ",
                "Tá bom então, vou te chamar de ")

falasNomeComprido = ("Nossa que nome grande, vamos fazer assim vou te chamar de ",
                "Bah eu não vou escrever tudo isso, vou te chamar de ",
                "kkkkk como pronuncia tudo isso? Vou te chamar de ")

falasNomeElogio = ("Haha que nome engraçado ",
                "Gostei desse nome, vou chamar minha tartaruga de ",
                "Que nome simpático ")

falasSugereGenero = ("Bah eu chutaria que tu é uma pessoa que gosta do gênero ",
                "Olha... eu te recomendo bastante o gênero ",
                "Tu tem cara de alguém passa tardes assistindo filmes do gênero ")

falasEscolheGeneroAleatorio = ("Aff assim você não tá me ajudando, vamos fazer assim eu escolho o gênero ",
                "Hmmmm... ok então vamos com o gênero ",
                "Não to te entendendo, então vou escolher o gênero ")

falasNaoReconheceGenero = ("Perdão mas eu não entendi",
                "Não conheço esse aí não",
                "É pra você me dizer seu gênero favorito salkjdaskj")

falasComentaSobreGenero = ("Hehe já passei mais tardes do que gostaria de admitir assistindo filmes de ",
                "Ahhhh! Eu adoro filmes de ",
                "É clichê, mas são muito bom os filmes de ")

# base de dados de falas da fase 2
falasComentaSobreLancamento = ("Ah nada como ir no cinema aproveitar um filme recém lançado",
                "Bah eu também, todo mundo conversando sobre o filme recém lançado, muito bom",
                "Opa, temos alguém que gosta dos novos filmes então")

falasComentaSobreAntigo = ("Ah sim, nada como assistir os grandes clássicos",
                "Então você é do tipo que comenta sobre os filmes que assite pros seus pais e é da epoca deles",
                "Nossa eu também adoro filmes mais antigos, é uma nova vibe comparando com os lançamentos atuais")

# base de dados de falas da fase 3
falasComentaSobreConhecido = ("Ah eu também prefiro filmes conhecidos, é mais fácil pra conversar sobre com os amigos",
                "O bom de filmes conhecidos é que tem bastante review na internet!",
                "Opa eu também gosto de filmes mais conhecidos e tal")

falasComentaSobreIndie = ("Uhhhh temos alguém cult aqui, só nos filmes indie",
                "Então você é do tipo que comenta sobre os filmes que assite e seus amigos ficam ????",
                "Bah eu também adoro! Mas é dificil encontrar pessoas pra conversar sobre")

# base de dados de falas da fase 2 e 3
falasNaoReconhece = ("Perdão mas eu não entendi, pode repetir?",
                "Não entendi, repete por favor",
                "AH sim, não pera, não entendi, pode repetir?")

falasEscolheAleatorio = ("Rsrs não quer falar é, então vamos de filmes ",
                "Ah já que você não quer participar eu escolho filmes ",
                "Ok... vou escolher filmes ")

falasResumeSituacao = ("Certo então estamos procurando por filmes de ",
                "Ok estabelecemos que queremos filmes de ",
                "Tá então vamos procurar por filmes de ")

# base de dados de falas da fase 4
falasMostraRecomendacao = ("Certo, então eu minha recomendação pra você é ",
                "Feito! Então eu te recomendo o filme ",
                "Ufa terminamos, minha recomendação pra você é ")

falasMensagemDeTchau = ("É isso! Terminamos, foi um prazer recomendar um filme pra você! Tchau!",
                "Ok, meu trabalho aqui está feito, foi um prazer te recomendar um filme, adeus!",)

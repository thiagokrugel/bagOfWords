# Feito por: Thiago Krügel
'''
ENUNCIADO 
Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de 
linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função 
que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta 
url. Duas condições são importantes:  
a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
1000 palavras.  
b) O texto desta página deverá ser transformado em um array de senteças.  

Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca
Spacy.
'''
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import spacy

nlp = spacy.load("en_core_web_sm")


def definirTexto(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def pegarTexto(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(definirTexto, texts)
    return u" ".join(t.strip() for t in visible_texts)


corpus = []

html = urllib.request.urlopen('https://hbr.org/2022/04/the-power-of-natural-language-processing').read()
page = nlp(pegarTexto(html))
for sentence in page.sents:
    corpus.append(sentence.text)

html2 = urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing').read()
page = nlp(pegarTexto(html2))
for sentence in page.sents:
    corpus.append(sentence.text)

html3 = urllib.request.urlopen(
    'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/').read()
page = nlp(pegarTexto(html3))
for sentence in page.sents:
    corpus.append(sentence.text)

html4 = urllib.request.urlopen(
    'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html').read()
page = nlp(pegarTexto(html4))
for sentence in page.sents:
    corpus.append(sentence.text)

html5 = urllib.request.urlopen('https://monkeylearn.com/natural-language-processing/').read()
page = nlp(pegarTexto(html5))
for sentence in page.sents:
    corpus.append(sentence.text)


def criarVocabulario(corpus):
    vocabulario = set()

    for sentenca in corpus:
        for palavra in sentenca.split():
            vocabulario.add(palavra)

    return sorted(vocabulario)


def criarMatriz(corpus):
    vocabulario = criarVocabulario(corpus)
    bagOfWords = []

    for sentenca in corpus:
        vetor = [0] * len(vocabulario)
        for palavra in sentenca.split():
            vetor[vocabulario.index(palavra)] += 1
        bagOfWords.append(vetor)

    return bagOfWords


vocabulario = criarVocabulario(corpus)
print(vocabulario)

matriz = criarMatriz(corpus)

for linha in matriz:
    print(linha)

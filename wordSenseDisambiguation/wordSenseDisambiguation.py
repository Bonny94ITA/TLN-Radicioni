import nltk
import metrics
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import semcor as sc
from nltk.corpus import wordnet as wn
import random

stop_words = set(stopwords.words('english'))
stop_words.add(',')
stop_words.add('.')
stop_words.add(';')
stop_words.add(':')
stop_words.add('etc')
#stop_words.add('\'\'')


# Lettura file
def read_file():
    array = []
    with open("./asset/sentences.txt", "r") as tsv:
        for line in tsv:
            array.append(line)
    array.pop(0)
    return array


# Estrazione delle parole e delle posizioni delle parole tra '**'. Viene estratta anche la parte rimanente della frase
def extract_word(sentences):
    word_sent = []
    for sentence in sentences:
        item = []
        word_tokens = word_tokenize(sentence)
        for i, word in enumerate(word_tokens):
            if len(word) > 4 and word[0] == '*' and word[1] == '*':  # 4 è il numero minimo di '*'
                item.append(word[2:len(word) - 2])  # Parola tra gli '**' [0]
                item.append(i)  # La posizione della parola nella frase [1]
        word_tokens.pop(item[1])
        item.append(word_tokens)  # Il resto della frase [2]
        word_sent.append(item)
    return word_sent


# Eliminazione delle stop word (es. and, at, etc...)
def delete_stop_words(word_tokens):
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return filtered_sentence


# Part of speech tagging e lemmatizzazione
def pos_tagging_and_lemming(word_tokens):
    word_pos_tag = nltk.pos_tag(word_tokens)  # Il pos tagging è da gestire ancora meglio per il lemmatizer

    lemmatizer = WordNetLemmatizer()
    lemming_pos = []
    for words, pos in word_pos_tag:
        lemming_pos.append(lemmatizer.lemmatize(words))  # Lemmatizzazione
        lemming_pos.append(pos)
    return lemming_pos


# Definizione del contesto
def get_context(sentence_tokens):
    return pos_tagging_and_lemming(delete_stop_words(sentence_tokens))


# Ritorna un esempio e la glossa del senso
def get_examples(sense):
    example = sense.examples()
    gloss = sense.definition()
    if len(example) > 0:
        return example[0] + gloss
    else:
        return gloss


def overlap(context1, context2, size):  # valutare se fare intersezione o confronto elemento per elemento
    olp = 0
    for elem1, elem2 in zip(context1[:size], context2[:size]):
        if elem1 == elem2:
            olp += 1
    return olp


def overlap_intersection(context1, context2, size):  # valutare se fare intersezione o confronto elemento per elemento
    set1 = set(context1[:size])
    set2 = set(context2[:size])
    return len(set1.intersection(set2))


def max_overlap(context1, context2):
    len1 = len(context1)
    len2 = len(context2)
    olp = 0
    if len1 <= len2:
        olp = overlap(context1, context2, len1)
    else:
        olp = overlap(context1, context2, len2)
    return olp


# Algoritmo di Lesk
def Lesk_algorithm(word, sentence_tokens):
    synset = wn.synsets(word)
    best_sense = synset[0]
    max_olp = 0
    sentence_context = get_context(sentence_tokens)

    for sense in synset[1:]:
        sense_examples = get_examples(sense)
        sense_context = get_context(word_tokenize(sense_examples))
        olp = max_overlap(sentence_context, sense_context)
        if max_olp < olp:
            max_olp = olp
            best_sense = sense
    return best_sense


# Estrazione di sinonimi random
def get_synonym(sense):
    return random.choice(sense.lemmas()).name()


def rebuild_sentence(sense, sentence_tokens, index):
    synonym = get_synonym(sense)
    sentence = ""
    for i, token in enumerate(sentence_tokens):
        if i < index or i > index:
            sentence += token + " "
        else:
            sentence += synonym + " " + token + " "
    return sentence


def main():

    sentences = read_file()
    """
    word_sentences = extract_word(sentences)
    for word_sent in word_sentences:
        best_sense = Lesk_algorithm(word_sent[0], word_sent[2])
        sent = rebuild_sentence(best_sense, word_sent[2], word_sent[1])
        print("Sentence: {}\n sense: {} definition: {}\n\n".format(sent, best_sense, best_sense.definition()))
    """

    semcor_sentences, semcor_extracted = metrics.semcor_extraction()
    tmp = []

    sentence = ""
    for elem in enumerate(semcor_sentences):

      print(delete_stop_words(list(elem)))
    #print(sentence)



    for i, x in zip(semcor_sentences, semcor_extracted):
        print(i)
        print(x)



if __name__ == '__main__':
    main()

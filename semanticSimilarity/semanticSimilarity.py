import utils
import sem_eval_mapper
from nltk import word_tokenize
from nltk.corpus import wordnet as wn


def main():
    # print(sem_eval_mapper.map_2_hundred(2))

    array = utils.read_file()
    print(array)
    array = utils.extract_word(array)
    print(array)
    print(len(array))


if __name__ == '__main__':
    main()

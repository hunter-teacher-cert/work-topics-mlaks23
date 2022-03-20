# hat-tip to Liam Baum and Andrew Healey, a British software engineer, who have both implemented Markov Chains in ways that proved invaluable to our group!
# You can find Liam's (super awesome) lyric generator here on his repo: https://github.com/hunter-teacher-cert/work_csci70900-mrbombmusic/tree/master/ds/markov
# And Healey Codes version here: https://github.com/healeycodes/markov-chain-generator

import random

# This function handles input by opening a file and returning it as a string
def input(text):
    with open(text) as f:
        corpus = f.read()
    return corpus

# This function takes as inputs your corpus (a string of text) and the state size and returns a dictionary that is a Markov model of the corpus

    # Here, state size is another way of saying the "n" in "n-gram":

        # If state size is 1, the model will build a dictionary in which each word in the corpus
        # is a key, and the words that follows a given word--anywhere in the corpus--are the values.

        # If state size is 2, the model will build a dictionary in which each pair of words in the corpus
        # is a key, and the words that follows that pair are the keys.

def build_markov(corpus, state_size):
    corpus = corpus.split()#split the string input into a list of words
    
    markov = {}#create an empty dictionary to hold the model - keys and values are words
    for i in range(state_size, len(corpus)):
        current_word = corpus[i]
        previous_words = ' '.join(corpus[i-state_size:i])
        if previous_words in markov:
            markov[previous_words].append(current_word)
        else:
            markov[previous_words] = [current_word]
    return markov


# This function takes as input a Markov model (in the form of a dictionary), the state size, and the maximum number of words you want to generate.
# It returns a string that (hopefully) sounds like the text input into the model!
def generate_text(model, state_size, max_length):

    # This function picks a new starting word or phrase, by picking a random capitalized word
    # Obviously, this assumes that lines start with capital letters, which is not always the case
    def get_new_starter():
        return random.choice([s.split(' ') for s in model.keys() if s[0].isupper()])
    text = get_new_starter()

    i = state_size
    while True:
        key = ' '.join(text[i-state_size:i])
        if key not in model:
            text += get_new_starter()
            i += 1
            continue

        next_word = random.choice(model[key])
        if next_word == "[Chorus]":
           next_word = random.choice(model[key])
           text.append(next_word)
           i += 1
           if i == max_length:
              break
        else:
            text.append(next_word)
            i += 1
            if i == max_length:
                break
    return ' '.join(text)

# This is like "main" in java - here is where we run the program by calling the functions

if __name__ == "__main__":
    body1 = input('dr_seuss.txt')
    #print(body1)
    model1 = build_markov(body1,2)
    #print(model1)
    
    
    body2 = input('beatles.txt')
    #print(body2)
    model2 = build_markov(body2,2)
    #print(model2)
    
    
    body3 = input('nirvana.txt')
    #print(body3)
    model3 = build_markov(body3,2)
    # print(model3)
    
    
    body4 = input('missy-elliott.txt')
    #print(body4)
    model4 = build_markov(body4,2)
   # print(model4)
   
    for i in range(3):
        print(generate_text(model1,2,5))
        print(generate_text(model2,2,10))
        print(generate_text(model3,2,10))
        print(generate_text(model4,2,10))
        print(generate_text(model1,2,5))
        print(generate_text(model2,2,10))
        print(generate_text(model3,2,10))
        print(generate_text(model4,2,10))
        print(generate_text(model1,2,5))
        
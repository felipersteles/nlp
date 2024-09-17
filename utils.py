from nltk.corpus import stopwords

def print_tokens_count(tokens):
    print("--------------------------------")
    print(f'Total of tokens: %s' % len(tokens))

def print_all_tokens(tokens):
    print_tokens_count(tokens)
    print("--------------------------------\nAll tokens:")
    
    text = ""
    for token in tokens:
        text += token
        text += " "

    print(text)

def list_all_tokens(tokens):
    print_tokens_count(tokens)
    print("--------------------------------\nAll tokens:")
    
    for token in tokens:
        print(token)

def print_words_frequency(frequent_words):
    print("--------------------------------")
    print("Frequency of words:")
    for word in frequent_words:
        print(word[0] + " - " + str(word[1]))

def print_bar():
    print("--------------------------------")

def only_words(tokens):
    words = []
    for token in tokens:
        if(token.isalpha()):
            words.append(token)

    return words

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_words = []
    
    for token in tokens:
        if(not token in stop_words):
            filtered_words.append(token)

    return filtered_words
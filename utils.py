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
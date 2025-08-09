def check_word(word):
    wordcount=len(word)
    if wordcount%2==0:
        result="even"
    else:
        result="odd"
    return result    


if __name__=="__main__":
    print(check_word("acde"))
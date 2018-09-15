import requests as rq
def read_text():
    quotes = open('./movie_qoutes.txt')
    contents = quotes.read()
    # print(contents)
    quotes.close()
    return contents

def check_profanity(text):
    "Google Curse word checker"
    url = 'http://www.wdylike.appspot.com/?q='+text
    r = rq.get(url)
    return (r.text)

if __name__ == '__main__':
    contents = read_text()
    result = check_profanity(contents)
    
    if result == 'true':
        print("Profanity Alert!")
    elif result == 'false':
        print("This document has no curse words!")
    else:
        print('Could not scan the document propertly.')

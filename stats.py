def sort_on(items):
    return items["num"]

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    alphabet = dict()
    for c in text:
        c = c.lower()
        if c not in alphabet:
            alphabet[c] = 0
        alphabet[c] += 1
    return alphabet

def sort_report(raw_report):
    sorted_report = list()
    alpha_report = list()
    for c in raw_report:
        if c.isalpha():
            alpha_report.append({
                                "char" : c,
                                "num" : raw_report[c]
            })
    alpha_report.sort(reverse=True, key=sort_on)

    return alpha_report

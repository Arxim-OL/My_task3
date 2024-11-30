# Задача "Однокоренные"
def single_root_words (root_word, *other_words):
    same_words = []
    for x in other_words:
        y = x.lower ()
        z = root_word.lower ()
        if y.count(z) or z.count(y):
            same_words.append(x)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
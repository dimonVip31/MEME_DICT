meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            'ПОН': "понятно или ясно",
            "РОФЛ":"шутка",
            "КРИПОВЫЙ":"страшный или пугающий"
            }
word = input('enter unknown word')
if word.upper() in meme_dict:
    print(meme_dict[word.upper()])
else:
    print('not understand')

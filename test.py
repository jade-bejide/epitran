import epitran

translator = epitran.Epitran('vie-Latn', tones=True)
print(translator.transliterate("iã"))
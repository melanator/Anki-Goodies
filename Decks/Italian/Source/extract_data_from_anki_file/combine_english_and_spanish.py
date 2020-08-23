from regex_definitions import SPLIT_FIELDS_REGEX

EN_file = r'../Ultimate Italian Conjugation.4anki'
SP_file = r'../Domina la Conjugación Italiana.4anki'
new_deck_file = r'out/English_to_Spanish.4anki'

english = []
spanish = []

# Fill english table with (english_field, tag_field) tuples
with open(EN_file, encoding="utf8") as fin:
    for line in fin:
        match = SPLIT_FIELDS_REGEX.search(line)
        if match:
            english_field = match.group(1)
            tags_field = match.group(2)
            english.append((english_field, tags_field))

# Fill spanish table with spanish_field
with open(SP_file, encoding="utf8") as fin:
    for line in fin:
        match = SPLIT_FIELDS_REGEX.search(line)
        if match:
            spanish_field = match.group(1)
            spanish.append(spanish_field)

english_total = len(english)
spanish_total = len(spanish)

if english_total == spanish_total:
    with open(new_deck_file, 'w', encoding="utf8") as fout:
        for i in range(english_total):
            line = english[i][0] + ";" + spanish[i] + ";" + english[i][1] + "\n"
            fout.write(line)

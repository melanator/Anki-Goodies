import re
from regex_definitions import VERB_EXTRACT_REGEX, TAGS_REGEX, NOT_WORD_CHAR_REGEX

anki_file = r'../Ultimate Italian Conjugation.4anki'
verb_forms_file = r'out/conjugated_verb_forms.txt'
track_names_file = r'out/track_names.txt'
unique_track_names_file = r'out/unique_track_names.txt'
unique_track_names = set()

with open(anki_file, encoding="utf8") as fin:
    with open(verb_forms_file, 'w', encoding="utf8") as fout:
        with open(track_names_file, 'w', encoding="utf8") as fout2:
            for line in fin:
                match = re.search(VERB_EXTRACT_REGEX, line)
                if match:
                    detagged_verb = TAGS_REGEX.sub("", match.group(1))
                    clean_verb = detagged_verb.lower().replace(" /", ",")
                    underscore_name = clean_verb.replace(" ", "_")
                    track_name = NOT_WORD_CHAR_REGEX.sub("", underscore_name) + ".ogg"
                    unique_track_names.add(track_name)
                    fout.write("{}\n".format(clean_verb))
                    fout2.write("{}\n".format(track_name))
fin.close()
fout.close()
fout2.close()

with open(unique_track_names_file, 'w', encoding="utf8") as fout3:
    for track_name in sorted(list(unique_track_names)):
        fout3.write("{}\n".format(track_name))
fout3.close()

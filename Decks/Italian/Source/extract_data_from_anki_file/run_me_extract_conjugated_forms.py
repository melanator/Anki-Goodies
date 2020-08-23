import re
from regex_definitions import VERB_EXTRACT_REGEX, TAGS_REGEX

in_file = r'../Ultimate Italian Conjugation.4anki'
out_file = r'out/conjugated_verb_forms.txt'

with open(in_file, encoding="utf8") as fin:
    with open(out_file, 'w', encoding="utf8") as fout:
        for line in fin:
            match = re.search(VERB_EXTRACT_REGEX, line)
            if match:
                detagged_verb = TAGS_REGEX.sub("", match.group(1))
                clean_verb = detagged_verb.lower().replace(" /", ",")
                fout.write("{}\n".format(clean_verb))
fin.close()
fout.close()

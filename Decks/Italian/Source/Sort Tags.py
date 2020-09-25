import re

anki_file = "Domina la Conjugación Italiana.4anki"
sorted_tags_file = f"[sorted] {anki_file}"

ANKI_LINE = re.compile(r"""(?m)^(?!#)((?:[^;\r\n]*;){2})([^;\r\n]*)([\r\n]+)""")

with open(anki_file, "r", encoding="utf8") as fin:
    fout = open(sorted_tags_file, "w", encoding="utf8")
    for line in fin:
        match = ANKI_LINE.search(line)
        if match:
            sorted_tags =' '.join(sorted([tag.strip() for tag in match.group(2).split()]))
            fout.write(f"{match.group(1)}{sorted_tags}{match.group(3)}")
        else:
            fout.write(line)
    fout.close()

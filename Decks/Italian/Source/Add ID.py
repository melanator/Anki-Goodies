import re

anki_file_path = "C:/path-to-file/"
anki_file = "my_file.4anki"
original_file = f"{anki_file_path}{anki_file}"
id_file = f"{anki_file_path}[ID] {anki_file}3"
id_back_file = f"{anki_file_path}[ID_back] {anki_file}3"

ANKI_LINE = re.compile(r"""(?m)^(?!#)((?:[^;\r\n]*;){2})([^;\r\n]*[\r\n]+)""")

with open(original_file, "r", encoding="utf8") as fin:
    fid = open(id_file, "w", encoding="utf8")
    fid_back = open(id_back_file, "w", encoding="utf8")
    count = 0
    for line in fin:
        match = ANKI_LINE.search(line)
        if match:
            count += 1
            count_str = str(count).zfill(5)
            fid.write(f"{count_str};{match.group(0)}")
            fid_back.write(f"{match.group(1)}{count_str};{match.group(2)}")
        else:
            fid.write(line)
            fid_back.write(line)
    fid.close()
    fid_back.close()

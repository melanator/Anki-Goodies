import re
import fileinput


class Card:
    """
    Simple class with fields
    """
    def __init__(self, uuid, prompt, similar, notes, tags, audio):
        self.uuid = uuid
        self.prompt = prompt
        self.similar = similar
        self.notes = notes
        self.tags = tags
        self.audio = audio

    def __str__(self):
        return f"{self.uuid};{self.prompt};{self.similar};{self.notes};{self.audio};{self.tags}"


def parse_line(line):
    fields = line.split(";")
    audio = re.findall(r"{{c1::.+::", fields[1])

    # if regex found pattern, delete symbols. If multiple words, split
    if len(audio) > 0:
        audio = audio[0][6:-2].replace(" | ", ", ")
    else:
        audio = re.findall(r"{{c1::.+}}", fields[1])[0][6:-2]

    return Card(*fields, audio)


new_deck = open("Decks/Spanish/source/Ultimate Spanish Conjugation {{Cloze_wAudio}}.4anki", "w")

for line in fileinput.input('Decks/Spanish/source/Ultimate Spanish Conjugation {{Cloze}}.4anki'):
    new_line = str(parse_line(line))
    new_deck.write(new_line)

new_deck.close()

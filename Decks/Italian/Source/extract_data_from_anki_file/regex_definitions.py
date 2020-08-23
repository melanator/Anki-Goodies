import re

TAGS_REGEX = re.compile(r"<[^>]*>")
ONE_WORD_LINE_REGEX = re.compile(r"^\w+$")
NOT_WORD_CHAR_REGEX = re.compile(r"\W+")

SPLIT_FIELDS_REGEX = re.compile(r"""(?m)^(?!#)([^;]+);[^;]+;(.*)""")

VERB_EXTRACT_REGEX = re.compile(r'''(?mx) # anchors match on each line, free-spacing
^ # Beg line
[^#;\r\n]+; # consume the first field: any chars that are neither a hash nor a semi-colon or a linebreak, plus a semi-colon
# skip the irrelevant part
(?: # this group is optional and non-capturing
  (?!Avere[ ]perso) # if what immediately follows is "Avere perso" (special case), don't skip
  (?: # skip any number of characters that match the following rules
     (?!  # IF what immediately follows is neither
        ; # a semi-comma
        |(?<!lui)[ ]/[ ] # or " / " that is not preceded by "lui"
        |<br # or an html linebreak
     )  # ENDIF
     . # then skip one character
  )+ 
  [ ] # and a space
)? # end irrelevant optional part to skip
# \K # throw away the match so far (Perl/PCRE-specific, otherwise remove and use Group 1 below)
# Now match the conjugated verb
( # Group 1: Either match:
    Avere[ ]perso[ ]/[ ]avere[ ]perduto # "Avere perso / avere perduto"
    | # or
    # 
    (?: # match one or more chars matching the following rule
      (?![; ]|<br) # IF what immediately follows is neither a semi-colon, space or html br
      . # match one character
    )+  # match as many of those as you want
    (?: # optionally, also match one or more groups that look like:
      [ ]/[ ] # space-slash-space
      (?:(?![; ]|<br).)+ # and the same kind of group already matched above
    )* # end of optional part of the match
)   # End match, captured to Group 1
# The match must be followed by
(?=
  ; # a semi-colon
  |<br # or an html linebreak
  |[ ]\[(?:lit|rare) # or "[lit" or "[rare"
) # End of post-match check
            ''')

import re

s = "123"
matcher = re.match('\d{3}\Z',s)

if matcher:
    print("True")
else:
    print("False")

'''
Re Grammar rules

\d 	Matches a decimal digit; equivalent to the set [0-9].
\D 	The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
\s 	Matches any whitespace character; equivalent to [ \t\n\r\f\v].
\S 	The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
\w 	Matches any alphanumeric character; equivalent to [a-zA-Z0-9_].
\W 	Matches the complement of \w.
\b 	Matches the empty string, but only at the start or end of a word.
\B 	Matches the empty string, but not at the start or end of a word.
\\ 	Matches a literal backslash.
'''
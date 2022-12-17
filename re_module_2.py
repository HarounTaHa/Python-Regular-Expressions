import re

# sub
text = """Hello my Number is 791-808-8102 and my friend's number is 428-562-2152 
        """
# replace all slash - to space from text
replace = re.sub(r"\d{3}-\d{3}-\d{4}", "415 555 1011", text, 1)
print(replace)

text = "I am a student at Hasoub Academy"
replace = re.sub(r"\s", "-", text)
print(replace)

# split
txt = "I am a student at Hasoub Academy"
words = re.split(r'\s', txt)
print(words)
words = re.split(r'\s', txt, 4)
print(words)

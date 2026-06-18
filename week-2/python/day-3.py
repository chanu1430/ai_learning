# Longest Word

text = "I want to become a generative ai engineer"
text=text.split(" ")
lw=""
for i in text:
    if len(i)>len(lw):
        lw=i

print(lw)
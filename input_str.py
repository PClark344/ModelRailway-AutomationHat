# to get no. from ADC

nochars = 5

s = "{'three': 0.03, 'two': 0.03, 'one': 8.53}"

l = len(s)

maxchar = max(s)
maxpos = s.find(maxchar)
startpos = maxpos - nochars
eos = s[startpos:nochars]

print(s)
print('startpos = ' + str(startpos))
print('maxchar = ' + str(maxchar))
print('maxpos = ' + str(maxpos))
print('eos = ' + str(eos))

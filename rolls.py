import random

dice = 2
num = 4

rolls = []
totalResult = 0
count = 0
while(count < dice):
    result = random.randint(1, num)
    totalResult += result
    rolls.append(result)
    count += 1
formatRoll = 'You have rolled '
if(len(rolls) == 1):
    formatRoll += '1 die. \nRoll = {'
elif(len(rolls) == 0):
    formatRoll += 'NOTHING!'
else:
    formatRoll += str(len(rolls)) + " dice. \nRolls = {"
for r in rolls:
    formatRoll += str(r)
    if count != 1:
        formatRoll += ', '
    count -= 1
formatRoll += "}"

print(formatRoll)
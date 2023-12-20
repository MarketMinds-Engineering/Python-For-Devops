import re

test = "hey my name is prakash"
chkFor = "prakaaaash"

val = re.search(chkFor, test)

if val:
    print("val is: " + val.group())
else:
    print(val)




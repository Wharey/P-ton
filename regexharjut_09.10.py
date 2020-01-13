

"""
scannib teksti ning paneb clipboardi leitud maskiga numbrid ja
www.aadressid.
"""

import re, pyperclip

text=[]

text.append(pyperclip.paste())

reg=re.compile(r"\d\d\d-\d\d\d-\d\d\d")
reg2=re.compile(r"\www.\w+\.com")

mo=reg.findall(str(text))
mo2=reg2.findall(str(text))

print(mo)
print(mo2)

pyperclip.copy(str(mo+mo2))




"""
www.neti.com
www.net2.com
regex=re.compile(r"-?\d{3}")
mo=regex.findall("415-444-555")
print(mo)


* - zero or all (same "www") preceding
? - non or one (one optional"w") preceding
. - any character but newline (.  .ot= hot, tot, jot jne)
.* - Accepts as many sequence as available. Greedy approach.
.*?- Accepts the first matched sequence and stops. Non-Greedy approach
.findall() ja .search()

regex=re.compile(r"(4){3}")
mo=regex.findall("415-444")
print(mo.group())

"""

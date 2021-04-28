iA={"蘋果", "香蕉","鳳梨","芭樂"}
iB={"鳳梨","蘋果","水梨","蓮霧"}

a = input()
A = input()
iA.add(a)
iA.add(A)
iA.remove("蘋果")


b = input()
B = input()
iB.add(b)
iB.add(B)
iB.remove("蓮霧")

lstiA = list(iA)
lstiB = list(iB)
lstiA.sort()
lstiB.sort()

print("iA:",lstiA)
print("iB:",lstiB)

both = iA.union(iB)
lstboth=list(both)
lstboth.sort()
print("union:",lstboth)

tgt=iA.intersection(iB)
lsttgt = list(tgt)
lsttgt.sort()
print("intersection:", lsttgt)

iaspe = both-iB
lstiaspe = list(iaspe)
lstiaspe.sort()
print("A diff B:",lstiaspe)

ibspe = both-iA
lstibspe = list(ibspe)
lstibspe.sort()
print("B diff A:",lstibspe)


ans= both-tgt
lst= list(ans)
lst.sort()
print("A xor B:", lst)

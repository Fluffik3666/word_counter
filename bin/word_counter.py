

wtc = input("enter a word or sentence \nto count.\n(word counter)\n")


print("the program is working but this isn't the result. \nthe result will say when it's it.")
#print("Length of wtc is:",len(wtc))
#print("wtc index position 1 is:",wtc[1])
#
#ll
length = len(wtc)
for x in range(0,length):
    print(wtc[x:length])

print("this is your result",length,)
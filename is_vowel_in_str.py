k=["a","e","i","o","u","A","E","I","O","U"]
S=input()
for i in range(len(S)):
    if S[i] in k:
        print("yes")
        break
    elif i==len(S)-1:
        print("no")

import sys

W1=str(sys.argv[1])
L=str(sys.argv[2]).split(',')
W=[]
W2=[]
for i in W1 :
    W2.append(i)
W.extend(W2)

l=['_']*len(W)

guessed_words_in=[]
guessed_words_out=[]

guessC=5
mod=["IN","OUT"]
print("you have 5 guesses left")
print(l)


for i in L:
    if (guessC>0) and L.index(i)<len(L)   :
        if mod[0]=="IN":
            if (i in W2) and (not i in guessed_words_in) :
                guessed_word=i
                print("guessed word:",i,"You are IN mood")
                print("You have",guessC,"gusses left")
                mod[0]="IN"
                guessed_words_in.append(i)
                if W2.count(i)>1:
                    for j in range(W2.count(i)):
                        l[W2.index(i)]=i
                        W2[W2.index(i)]=""
                        if  guessC<0:
                            break
                    print(l)
                    print("- "*22)
                else:
                    l[W.index(i)]=i
                    print(l)
                    print("- "*22)
            elif(i in guessed_words_in):
                guessC-=1
                print("Guessed word: "+i+" is used in IN mode.The game turned into OUT mode")
                print("You have",guessC, "guesses left")
                print(l)
                print("- "*22)
                mod[0]=mod[1]
            else:
                guessC-=1
                print("guessed word:",i,"The game turned into OUT mode")
                print("You have",guessC,"guess left")
                print(l)
                print("- "*22)
                mod[0]=mod[1]
                guessed_words_in.append(i)
        else:
            if i in W:
                guessed_word=i
                guessC-=1
                print("guessed word:",i,"You are in OUT mode")
                print("You have",guessC,"guess left")

                print(l)
                print("- "*22)
                mod[0]=mod[1]
                guessed_words_out.append(i)
            elif (i in guessed_words_out):
                guessC-=1
                print("guessed word:",i,"is used before You are in OUT mode")
                print("You have",guessC,"guess left")
                print(l)
                print("- "*22)
                mod[0]=mod[1]
            else :
                guessed_word=i
                print("guessed word:",i,"The game turned into IN mode")
                print("You have",guessC,"guess left")
                print(l)
                print("- "*22)
                mod[0]="IN"
                guessed_words_out.append(i)

if (guessC>0) and (W==l):
    print("you won the game")
else:
    print("you have no letters or you have no right")
    print("you lost the game")


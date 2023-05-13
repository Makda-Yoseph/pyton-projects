import random
word_list=["aardvark","baboon","camel"]
chosen_word=random.choice(word_list)
guess= input(str("guess a leter.")).lower()
display=[]
n=0
for i in chosen_word:
    if guess== i:
        display.insert(n,i)
        n +=1
    else:
        display.insert(n,"_")
        n +=1
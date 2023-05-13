import random
word_list=["aardvark","baboon","camel"]
chosen_word=random.choice(word_list)
guess= input(str("guess a leter.")).lower()
for i in chosen_word:
    if guess== i:
        print("Right")
    else:
        print("Wrong")
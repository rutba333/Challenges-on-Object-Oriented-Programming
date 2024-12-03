class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning

    def __str__(Self):
        #we will return a string
        return self.word'('+self.meaning')'

flash=[]
print("welcome to flash card application")
#the following loop will repeat until
#user stop to using flash cards
while(True):
    word=input("Please input the name you want to add in flash card:")
    meaning=input("please enter the meaning of the word")

    flash.append(flashcard(word,meaning))
    option=int(input("enter 0, if want another flash card then otherwise enter 1"))
     if(option):
            break

#print all the flash cards
print("\nYour flash cards")
for i in flash:
    print(">",i)
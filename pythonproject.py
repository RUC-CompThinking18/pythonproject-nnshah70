print u"    \U0001F407                \U0001F407"#Unicodes for the ears, bunny and lipsticks for animal testing
print u"   \U0001F484\U0001F484\U0001F484              \U0001F484\U0001F484\U0001F484"#these lines are to add a visual component to compliment the facts that will change underneath
print u"   \U0001F407\U0001F407\U0001F407\U0001F407             \U0001F407\U0001F407\U0001F407\U0001F407"#the point of these ears made up of the unicodes are to draw the audiences attention to the issue
print u"   \U0001F484\U0001F484\U0001F484\U0001F484             \U0001F484\U0001F484\U0001F484\U0001F484"
print u"   \U0001F407\U0001F407\U0001F407\U0001F407             \U0001F407\U0001F407\U0001F407\U0001F407"
print u"   \U0001F484\U0001F484\U0001F484\U0001F484             \U0001F484\U0001F484\U0001F484\U0001F484"
#Import the text file so it will randomize facts into the shape of the bunny above in order to show the impact of animal cruelty in regards to animal testing
import random
f = open('makeup.txt','r')#to open the text file to read
file  = f.read().split('\n')#splits the facts line by line
#Every time someone runs the code, each time the facts will change but the shape will stay the same
random.shuffle(file)#So that the facts will change each time the funtion is run so that the audience can walk away with multiple astonishing facts that show the impact of cosmetic testing
facts = file[0].split(' ')#splits the text file
#To join the facts in the shape of the bunny by going line by line
print (str(' '.join(facts[:4]))+'\n'+str(' '.join(facts[4:9]))+'\n'+str(' '.join(facts[9:12]))+'\n'+str(' '.join(facts[12:15])))
fname = open ("makeup.txt")
k = 0
for line in f:#counting the spaces in order to write another function that will actually put spaces before the facts so they create the oval/half circle shape of the head
    words = line.split()
    for i in words:
        for letter in i:
            if(letter.isspace):
                k=k+1
print(k)#counting the characters in order to dictate line by line how many chracters should show up in order to make the shape
characters = 0
for n in facts:
    for m in n:
        characters+=1
print(characters)#hopefully so that it will print the characters so i can take the first line and the second line and count the space

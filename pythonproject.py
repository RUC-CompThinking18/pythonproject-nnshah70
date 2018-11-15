print u"    \U0001F407                         \U0001F407"#Unicodes for the ears, bunny and lipsticks for animal testing
print u"   \U0001F484\U0001F484\U0001F484                       \U0001F484\U0001F484\U0001F484"
print u"   \U0001F407\U0001F407\U0001F407\U0001F407                      \U0001F407\U0001F407\U0001F407\U0001F407"
print u"   \U0001F484\U0001F484\U0001F484\U0001F484                      \U0001F484\U0001F484\U0001F484\U0001F484"
print u"   \U0001F407\U0001F407\U0001F407\U0001F407                      \U0001F407\U0001F407\U0001F407\U0001F407"
print u"   \U0001F484\U0001F484\U0001F484\U0001F484                      \U0001F484\U0001F484\U0001F484\U0001F484"
print "    RRR RRRRRRRRRRRRRRRRRRRR RRR"
print "    RRRRRRRRRRRRRRRRRRRRRRRRRRRR "
print "   RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
print "  RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
print "  RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
print "  RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
print "  RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
print "   RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
print "    RRRRRRRRRRRRRRRRRRRRRRRRRRRR"
print "     RRRRRRRRRRRRRRRRRRRRRRRRRR"
print "      RRRRRRRRRRRRRRRRRRRRRRRR"
print "       RRRRRRRRRRRRRRRRRRRRRR"
print "        RRRRRRRRRRRRRRRRRRRR"
print "            RRRRRRRRRRRR"
#Import the text file so it will randomize facts into the shape of the bunny above in order to show the impact of animal cruelty in regards to animal testing
import random
f = open('makeup.txt','r')#to open the text file and the next line is to read it and split the lines
file  = f.read().split('\n')
#Every time someone runs the code, each time the facts will change but the shape will stay the same
random.shuffle(file)#So that the facts will change
facts = file[0].split(' ')
#To join the facts in the shape of the bunny
print (str(' '.join(facts[:3]))+'\n'+str(' '.join(facts[3:7]))+'\n'+str(' '.join(facts[7:12]))+'\n'+str(' '.join(facts[12:15])))

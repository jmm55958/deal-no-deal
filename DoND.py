from case import Case
import board
import random
import time

def removeCase(caseList, moneyDisplay, caseNo, first):

    case = caseList[caseNo-1]

    #removing the case from the board
    if(case.number>9):
        case.face = 'XX'
    else:
        case.face = 'X'
    if(first==False):
        index = moneyDisplay.index(case.value)
        moneyDisplay[index] = '---------'


#opening statements
print("Welcome to Deal of No Deal!")
print ("Ladies please...") 

#grab username
name = input("What's your name: ")

#create arrray for cases
caseList = []
moneyList = ['      .01',   '        1',   '        5',   '       10',   '       25',   '       50',   '       75',  '      100',   '      200',   '      300',   '      400',   '      500',   '      750', '    1,000','    5,000','   10,000','   25,000','   50,000','   75,000','  100,000','  200,000','  300,000','  400,000','  500,000','  750,000','1,000,000']
moneyDisplay = moneyList.copy()

#shuffle money array
random.shuffle(moneyList)

#create cases and add to the array
for num in range(1, 27):
    case = Case(num, moneyList[num-1])
    caseList.append(case)

#print the board
board.printScreen(caseList, moneyDisplay, name, '??')

#picking your case
caseNo = int(input("Pick your case: "))
userCase = caseList[caseNo-1]
userCase.frontFace = userCase.face

#call remove case
removeCase(caseList, moneyDisplay, caseNo, True)

#game variables
game = True
rounds = [6, 5, 4, 3, 3, 2, 1, 1]
cases = 25
#simple banker approximation banker's offer = average value * turn number / 10


#testing 
# counter =0
# for x in caseList:
#     print(x.face),
#     print(' for '+str(counter))
#     counter +=1
# print(caseList[25].face)
# exit()


#main game loop
while(game):

    #loops the rounds of the game 
    for turn in rounds:

        #loops through the cases before the banker
        counter = 0
        while(turn!=0):
            board.printScreen(caseList, moneyDisplay, name, userCase.frontFace)
            if(counter ==0):
                print("You have "+str(cases)+" cases left to open!")
                print("This round please open "+ str(turn)+" cases.")

            #choosing a case to open
            caseNo = input("Please choose a case to open: ")

            print('You have chosen case number '+ str(caseNo)+ "!")
            print('Lets see whats inside'),
            print('.'),
            time.sleep(.5)
            print('.'),
            time.sleep(.5)
            print('.'),
            time.sleep(.5)
            print(str(caseList[int(caseNo)-1].value)+"!")
            

            #remove the case from the lists
            removeCase(caseList, moneyDisplay, int(caseNo), False)

            #increment the counter
            counter = counter +1
            turn = turn -1
            
            time.sleep(1.5)
            if(turn!=0):
                print('Let\'s open another!')
            time.sleep(1.5)

            


            
        

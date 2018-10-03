import random

class Case(object):
    number =0
    value =0


def newCase(num):
    case = Case()
    case.number=num
    case.face= str(num)
    # case.value=money
    return case

def printScreen(caseList, moneyList):
    print()
    print('-----------------------------------------------------')
    print(' Cases                         | Values    ')
    print('-----------------------------------------------------')
    print('                               | '+moneyList[0]+'  '+moneyList[13]+' ')
    print('  '+caseList[20].face+'   '+caseList[21].face+'   '+caseList[22].face+'   '+caseList[23].face+'   '+caseList[24].face+'   '+caseList[25].face+'  | '+moneyList[1]+'  '+moneyList[14]+' ')
    print('                               | '+moneyList[2]+'  '+moneyList[15]+' ')
    print('  '+caseList[13].face+'  '+caseList[14].face+'  '+caseList[15].face+'  '+caseList[16].face+'  '+caseList[17].face+'  '+caseList[18].face+'  '+caseList[19].face+'   | '+moneyList[3]+'  '+moneyList[16]+' ')
    print('                               | '+moneyList[4]+'  '+moneyList[17]+' ')
    print('  '+caseList[6].face+'   '+caseList[7].face+'   '+caseList[8].face+'   '+caseList[9].face+'   '+caseList[10].face+'   '+caseList[11].face+'  '+caseList[12].face+' | '+moneyList[5]+'  '+moneyList[18]+' ')
    print('                               | '+moneyList[6]+'  '+moneyList[19]+' ')
    print('   '+caseList[0].face+'   '+caseList[1].face+'   '+caseList[2].face+'   '+caseList[3].face+'   '+caseList[4].face+'   '+caseList[5].face+'       | '+moneyList[7]+'  '+moneyList[20]+' ')
    print('                               | '+moneyList[8]+'  '+moneyList[21]+' ')
    print('-------------------------------| '+moneyList[9]+'  '+moneyList[22]+' ')
    print('  NAME  ,                      | '+moneyList[10]+'  '+moneyList[23]+' ')
    print('       Your Case: ??           | '+moneyList[11]+'  '+moneyList[24]+' ')
    print('                               | '+moneyList[12]+'  '+moneyList[25]+' ')
    print('-----------------------------------------------------')
    print()

#opening statements
print("Welcome to Deal of No Deal!")
print ("Ladies please...") 

name = input("What's your name?: ")



#create 5 cases
case1 = newCase(1)
case2 = newCase(2)
case3 = newCase(3)
case4 = newCase(4)
case5 = newCase(5)
case6 = newCase(6)
case7 = newCase(7)
case8 = newCase(8)
case9 = newCase(9)
case10 = newCase(10)
case11 = newCase(11)
case12 = newCase(12)
case13 = newCase(13)
case14 = newCase(14)
case15 = newCase(15)
case16 = newCase(16)
case17 = newCase(17)
case18 = newCase(18)
case19 = newCase(19)
case20 = newCase(20)
case21 = newCase(21)
case22 = newCase(22)
case23 = newCase(23)
case24 = newCase(24)
case25 = newCase(25)
case26 = newCase(26)

#create arrays
moneyList = ['      .01',   '        1',   '        5',   '       10',   '       25',   '       50',   '       75',  '      100',   '      200',   '      300',   '      400',   '      500',   '      750', '    1,000','    5,000','   10,000','   25,000','   50,000','   75,000','  100,000','  200,000','  300,000','  400,000','  500,000','  750,000','1,000,000']
moneyCopy = moneyList.copy()

caseList = [case1, case2, case3, case4, case5, case6 , case7 , case8 , case9 , case10, case11, case12, case13, case14, case15, case16, case17, case18, case19, case20, case21, case22, case23, case24, case25, case26]

#shuffle money array
random.shuffle(moneyList)

#hardcoded could do this in a loop
case1.value=moneyList[0]
case2.value=moneyList[1]
case3.value=moneyList[2]
case4.value=moneyList[3]
case5.value=moneyList[4]
case6.value=moneyList[5]
case7.value=moneyList[6]
case8.value=moneyList[7]
case9.value=moneyList[8]
case10.value=moneyList[9]
case11.value=moneyList[10]
case12.value=moneyList[11]
case13.value=moneyList[12]
case14.value=moneyList[13]
case15.value=moneyList[14]
case16.value=moneyList[15]
case17.value=moneyList[16]
case18.value=moneyList[17]
case19.value=moneyList[18]
case20.value=moneyList[19]
case21.value=moneyList[20]
case22.value=moneyList[21]
case23.value=moneyList[22]
case24.value=moneyList[23]
case25.value=moneyList[24]
case26.value=moneyList[25]

printScreen(caseList, moneyCopy)


#picking a case
caseNo = int(input("Pick your case!: "))
userCase = caseList[caseNo-1]

if(userCase.number>9):
    userCase.face = 'XX'
else:
    userCase.face = 'X'

printScreen(caseList, moneyCopy)

#takes out user case from case list
caseList.pop(caseNo-1)




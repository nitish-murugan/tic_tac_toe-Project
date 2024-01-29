a11 = "-"
a12 = "-"
a13 = "-"
a21 = "-"
a22 = "-"
a23 = "-"
a31 = "-"
a32 = "-"
a33 = "-"
loop = True
moves = []
def printxo():
    print(a11,a12,a13)
    print(a21,a22,a23)
    print(a31,a32,a33)

def player1():
    playing = int(input("Player1   : Enter the row and colomn number => "))
    if(playing in moves):
        print("\nChoose a different location")
        player1()
    else:
        moves.append(playing)
        if(playing == 11):
            global a11
            a11 = "X"
        elif(playing == 12):
            global a12
            a12 = "X"
        elif(playing == 13):
            global a13
            a13 = "X"
        elif(playing == 21):
            global a21
            a21 = "X"
        elif(playing == 22):
            global a22
            a22 = "X"
        elif(playing == 23):
            global a23
            a23 = "X"
        elif(playing == 31):
            global a31
            a31 = "X"
        elif(playing == 32):
            global a32
            a32 = "X"
        elif(playing == 33):
            global a33
            a33 = "X"
        printxo()

def player2():
    playing = int(input("Player2   : Enter the row and colomn number => "))
    if(playing in moves):
        print("\nChoose a different location")
        player2()
    else:
        moves.append(playing)
        if(playing == 11):
            global a11
            a11 = "O"
        elif(playing == 12):
            global a12
            a12 = "O"
        elif(playing == 13):
            global a13
            a13 = "O"
        elif(playing == 21):
            global a21
            a21 = "O"
        elif(playing == 22):
            global a22
            a22 = "O"
        elif(playing == 23):
            global a23
            a23 = "O"
        elif(playing == 31):
            global a31
            a31 = "O"
        elif(playing == 32):
            global a32
            a32 = "O"
        elif(playing == 33):
            global a33
            a33 = "O"
        printxo()

def checking():
    global loop
    if(a11!="-" and a12!="-" and a13!="-"):
        if(a11==a12==a13):
            
            print("\n-------------------------------------------")
            print(a11," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a21!="-" and a22!="-" and a23!="-"):
        if(a21==a22==a23):
            
            print("\n-------------------------------------------")
            print(a21," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a31!="-" and a32!="-" and a33!="-"):
        if(a31==a32==a33):
            
            print("\n-------------------------------------------")
            print(a31," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a11!="-" and a21!="-" and a31!="-"):
        if(a11==a21==a31):
            
            print("\n-------------------------------------------")
            print(a11," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a12!="-" and a22!="-" and a32!="-"):
        if(a12==a22==a32):
            
            print("\n-------------------------------------------")
            print(a12," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a13!="-" and a23!="-" and a33!="-"):
        if(a13==a23==a33):
            
            print("\n-------------------------------------------")
            print(a13," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a11!="-" and a22!="-" and a33!="-"):
        if(a11==a22==a33):
            print("\n-------------------------------------------")
            print(a11," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a13!="-" and a22!="-" and a31!="-"):
        if(a13==a22==a31):
            
            print("\n-------------------------------------------")
            print(a13," wins")
            print("------------------------------------------- \n\n")
            loop = False
 
printxo()
flag = 0
while(loop):
    player1()
    flag+=1
    checking()
    if(loop == False):
        break
    if(flag == 9):
        print("\n-------------------------------------------")
        print("Match Draw")
        print("------------------------------------------- \n\n")
        break
    player2()
    flag+=1
    checking()
    if(loop == False):
        break
    if(flag == 9):
        break
ii= input("Press any key to exit...")

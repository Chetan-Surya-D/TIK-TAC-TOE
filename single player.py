import random

p=["X","O"]
pn = ["",""]
start = 0
pn[0] = input("Enter Player 1 name: ")
pn[1] = "Computer"
print("Welcome to TIC TAC TOE Game")
print(pn[0],"'s symbol is 'X' and ", pn[1],"'s symbol is 'O'")

while 1:

    g = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    unocc=[1,2,3,4,5,6,7,8,9]
    stat = -1 # initially tie
    turn = start
    count = 1 #No of moves

    print("GRID NUMBERS:\n")
    print(" ", g[0], "| ", g[1], "| ", g[2], " ")
    print("===============")
    print(" ", g[3], "| ", g[4], "| ", g[5], " ")
    print("===============")
    print(" ", g[6], "| ", g[7], "| ", g[8], " ")

    print(pn[start],"goes first")

    while stat == -1:
        if(turn == 0):
            while 1:
                print(pn[turn], end=" ")
                x = input("choose an unoccupied grid:\n")
                if(x.isdigit()):
                    x = int(x)
                    if(x>=0 and x<=9 and g[x-1]!="X" and g[x-1]!="O"):
                        g[x-1]=p[turn]
                        break
                    else:
                        print("Invalid choice")
                else:
                    print("Invalid input")
            x=int(x)-1

        else:
            c=0
            for i in range(9):
                if(g[i-1].isdigit()):
                    unocc[c]=int(g[i-1])
                    c+=1

            choice=random.randrange(0,10-count)
            g[unocc[choice]-1]=p[turn]



        print("PRESENT GRID:\n")
        print(" ", g[0], "| ", g[1], "| ", g[2], " ")
        print("===============")
        print(" ", g[3], "| ", g[4], "| ", g[5], " ")
        print("===============")
        print(" ", g[6], "| ", g[7], "| ", g[8], " ")

        #Row Check

        if(x==0 or x==1 or x==2):
          if(g[0]==g[1] and g[1]==g[2]):
            stat = turn

        if (x == 3 or x == 4 or x == 5):
            if (g[3] == g[4] and g[4] == g[5]):
                stat = turn

        if (x == 6 or x == 7 or x == 8):
            if (g[6] == g[7] and g[7] == g[8]):
                stat = turn

        # Column Check

        if (x == 0 or x == 3 or x == 6):
            if (g[0] == g[3] and g[3] == g[6]):
                stat = turn

        if (x == 1 or x == 4 or x == 7):
            if (g[1] == g[4] and g[4] == g[7]):
                stat = turn

        if (x == 2 or x == 5 or x == 8):
            if (g[2] == g[5] and g[5] == g[8]):
                stat = turn

        #Diag Check

        if (x == 0 or x == 4 or x == 8):
            if (g[0] == g[4] and g[4] == g[8]):
                stat = turn

        if (x == 2 or x == 4 or x == 6):
            if (g[2] == g[4] and g[4] == g[6]):
                stat = turn

        if(stat != -1):
            print(pn[stat],"WINS")


            break
        elif(count == 9):
            print("It's a TIE")
            break
        else:
            pass
        turn = (turn+1)%2
        count+=1

    start = (start+1)%2
    while 1:
        ch=input("Do you want to play again?\nAnswer yes or no\n")
        ch=ch.lower()
        if(ch=='yes' or ch=='no'):
            break
        else:
            print("Invalid Input")
            continue

    if(ch == 'yes'):
        continue
    else:
        break
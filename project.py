import sys,random
from time import sleep #To add pauses in the game for a bit of loading time
class TicTacToe:
    def __init__(self,q,l,m):
        self.q=q
        self.l=l
        self.m=m

    #To check if the user is placing an 'O' in an already filled place    
    def check(self,n):
        for i in range(3):
            for j in range(3):
                if(l[i][j]==n):
                    #If user places his 'O' at an already filles position then he loses
                    if((m[i][j]=='O')or(m[i][j]=='X')):
                       print('Invalid Input',q,'lost')
                       sleep(1)
                       sys.exit()
                    m[i][j]='O'

    #To check if the computer is placing a 'X' in an already filled place  
    def chec(self,n):
        for i in range(3):
            for j in range(3):
                if(l[i][j]==n):
                    #If the computer places its 'X' at an already filles position then it loses
                    if((m[i][j]=='O')or(m[i][j]=='O')):
                       print('Invalid Input,System Lost')
                       sleep(1)
                       sys.exit()
                    m[i][j]='X'

    #To print the board                
    def prints(self):
        sleep(1)
        for i in range(3):
            print('     |     |     ')
            for j in range(3):
                if(m[i][j]!='1'):
                    print(" ",m[i][j]," ",end='')
                else:
                    print("     ",end='')
                if(j!=2):
                    print("|",end='')
                if(j==2):
                    print("",end='')
            print()
            if(i!=2):
                print("_____|_____|_____")
        print("     |     |     ")
        print()

    #To check if the user won or not  
    def win(self):
        sleep(1)
        if(((m[0][0]=='O')&(m[0][1]=='O')&(m[0][2]=='O'))|
           ((m[1][0]=='O')&(m[1][1]=='O')&(m[1][2]=='O'))|
           ((m[2][0]=='O')&(m[2][1]=='O')&(m[2][2]=='O'))|
           ((m[0][0]=='O')&(m[1][0]=='O')&(m[2][0]=='O'))|
           ((m[0][1]=='O')&(m[1][1]=='O')&(m[2][1]=='O'))|
           ((m[0][2]=='O')&(m[1][2]=='O')&(m[2][2]=='O'))|
           ((m[0][0]=='O')&(m[1][1]=='O')&(m[2][2]=='O'))|
           ((m[0][2]=='O')&(m[1][1]=='O')&(m[2][0]=='O'))):
            
            print()
            print(q+" won")
            sys.exit()

    #To check if the computer won or not         
    def loss(self):
        sleep(1)
        if(((m[0][0]=='X')&(m[0][1]=='X')&(m[0][2]=='X'))|
           ((m[1][0]=='X')&(m[1][1]=='X')&(m[1][2]=='X'))|
           ((m[2][0]=='X')&(m[2][1]=='X')&(m[2][2]=='X'))|
           ((m[0][0]=='X')&(m[1][0]=='X')&(m[2][0]=='X'))|
           ((m[0][1]=='X')&(m[1][1]=='X')&(m[2][1]=='X'))|
           ((m[0][2]=='X')&(m[1][2]=='X')&(m[2][2]=='X'))|
           ((m[0][0]=='X')&(m[1][1]=='X')&(m[2][2]=='X'))|
           ((m[0][2]=='X')&(m[1][1]=='X')&(m[2][0]=='X'))):
            print()
            print(q+" lost")   
            sys.exit()
            

    #Program that has all the working         
    def MAIN(self):
        sleep(1)
        for j in range(4):
            print(q,'enter the number where you want your circle')
            n=int(input())
            #If number is not in the range of 1-9 then the user loses
            if ((n>9)|(n<1)):
                sleep(1)
                print('Invalid Input',q,'lost')
                sys.exit()
            else:
                self.check(n)
                self.prints()
                self.win()

            sleep(1)
            print('The Computer chose this : ')
            print()
            self.compMove()
            self.prints()
            self.loss()
        print(q,' enter the number where you want your circle')
        n=int(input())
        if ((n>9)|(n<1)):
            print('Invalid Input',q,'lost')
            sys.exit()
        else:
            self.check(n)
            self.prints()
            self.win()
        print()
        print('Draw')

    #Deciding the computer move
    def compMove(self):            
        #row1
        if(((m[0][0]=='X')&(m[0][1]=='X')&(m[0][2]=='1'))or
           ((m[0][0]=='O')&(m[0][1]=='O')&(m[0][2]=='1'))):
           m[0][2]='X'    
        elif(((m[0][0]=='X')&(m[0][1]=='1')&(m[0][2]=='X'))or
             ((m[0][0]=='O')&(m[0][1]=='1')&(m[0][2]=='O'))):
           m[0][1]='X'
        elif(((m[0][0]=='1')&(m[0][1]=='X')&(m[0][2]=='X'))or
             ((m[0][0]=='1')&(m[0][1]=='O')&(m[0][2]=='O'))):
           m[0][0]='X'
        #row2
        elif(((m[1][0]=='X')&(m[1][1]=='X')&(m[1][2]=='1'))or
             ((m[1][0]=='O')&(m[1][1]=='O')&(m[1][2]=='1'))):
           m[1][2]='X'
        elif(((m[1][0]=='X')&(m[1][1]=='1')&(m[1][2]=='X'))or
             ((m[1][0]=='O')&(m[1][1]=='1')&(m[1][2]=='O'))):
           m[1][1]='X'
        elif(((m[1][0]=='X')&(m[1][1]=='1')&(m[1][2]=='X'))or
             ((m[1][0]=='1')&(m[1][1]=='O')&(m[1][2]=='O'))):
           m[1][0]='X'
        #row3  
        elif(((m[2][0]=='O')&(m[2][1]=='O')&(m[2][2]=='1'))or
             ((m[2][0]=='O')&(m[2][1]=='O')&(m[2][2]=='1'))):
           m[2][2]='X'
        elif(((m[2][0]=='O')&(m[2][1]=='1')&(m[2][2]=='O'))or
             ((m[2][0]=='O')&(m[2][1]=='1')&(m[2][2]=='O'))):
           m[2][1]='X'
        elif(((m[2][0]=='1')&(m[2][1]=='O')&(m[2][2]=='O'))or
             ((m[2][0]=='1')&(m[2][1]=='O')&(m[2][2]=='O'))):
           m[2][0]='X'
        #column1
        elif(((m[0][0]=='X')&(m[1][0]=='X')&(m[2][0]=='1'))or
             ((m[0][0]=='O')&(m[1][0]=='O')&(m[2][0]=='1'))):
           m[2][0]='X'
        elif(((m[0][0]=='X')&(m[1][0]=='1')&(m[2][0]=='X'))or
             ((m[0][0]=='O')&(m[1][0]=='1')&(m[2][0]=='O'))):
           m[1][0]='X'
        elif(((m[0][0]=='1')&(m[1][0]=='X')&(m[2][0]=='X'))or
             ((m[0][0]=='1')&(m[1][0]=='O')&(m[2][0]=='O'))):
           m[0][0]='X'
        #column2   
        elif(((m[0][1]=='X')&(m[1][1]=='X')&(m[2][1]=='1'))or
             ((m[0][1]=='O')&(m[1][1]=='O')&(m[2][1]=='1'))):
           m[2][1]='X'
        elif(((m[0][1]=='X')&(m[1][1]=='1')&(m[2][1]=='X'))or
             ((m[0][1]=='O')&(m[1][1]=='1')&(m[2][1]=='O'))):
           m[1][1]='X'
        elif(((m[0][1]=='1')&(m[1][1]=='X')&(m[2][1]=='X'))or
             ((m[0][1]=='1')&(m[1][1]=='O')&(m[2][1]=='O'))):
           m[0][1]='X'
        #column3   
        elif(((m[0][2]=='X')&(m[1][2]=='X')&(m[2][2]=='1'))or
             ((m[0][2]=='O')&(m[1][2]=='O')&(m[2][2]=='1'))):
           m[2][2]='X'
        elif(((m[0][2]=='X')&(m[1][2]=='1')&(m[2][2]=='X'))or
             ((m[0][2]=='O')&(m[1][2]=='1')&(m[2][2]=='O'))):
           m[1][2]='X'
        elif(((m[0][2]=='1')&(m[1][2]=='X')&(m[2][2]=='X'))or
             ((m[0][2]=='1')&(m[1][2]=='O')&(m[2][2]=='O'))):
           m[0][2]='X'
        #digonal left 
        elif(((m[0][0]=='X')&(m[1][1]=='X')&(m[2][2]=='1'))or
             ((m[0][0]=='O')&(m[1][1]=='O')&(m[2][2]=='1'))):
           m[2][2]='X'
        elif(((m[0][0]=='X')&(m[1][1]=='1')&(m[2][2]=='X'))or
             ((m[0][0]=='O')&(m[1][1]=='1')&(m[2][2]=='O'))):
           m[1][1]='X'
        elif(((m[0][0]=='1')&(m[1][1]=='X')&(m[2][2]=='X'))or
             ((m[0][0]=='1')&(m[1][1]=='O')&(m[2][2]=='O'))):
           m[0][0]='X'
        #digonal right   
        elif(((m[0][2]=='X')&(m[1][1]=='X')&(m[2][0]=='1'))or
             ((m[0][2]=='O')&(m[1][1]=='O')&(m[2][0]=='1'))):
            m[2][0]='X'
        elif(((m[0][2]=='X')&(m[1][1]=='1')&(m[2][0]=='X'))or
             ((m[0][2]=='O')&(m[1][1]=='1')&(m[2][0]=='O'))):
            m[1][1]='X'
        elif(((m[0][2]=='1')&(m[1][1]=='X')&(m[2][0]=='X'))or
             ((m[0][2]=='1')&(m[1][1]=='O')&(m[2][0]=='O'))):
            m[0][2]='X'
        
        else:
            if(m[1][1]=='1'):
                m[1][1]='X'
            elif(m[0][0]=='1'):
                m[0][0]='X'
            elif(m[1][2]=='1'):
                m[1][2]='X'
            elif(m[2][0]=='1'):
                m[2][0]='X'
            elif(m[2][2]=='1'):
                m[2][2]='X'
            else:
                for x in range(10):
                    a=random.randint(0,2)
                    b=random.randint(0,2)
                    
                    if(m[a][b]=='1'):
                        m[a][b]='X'
                        break
                    else:
                        continue
                    

    #Starting point of the tictactoe program     
    def main(self):
        sleep(1)
        print("Let's begin")
        sleep(1)
        print()
        print("This is your board ; Remember the position of numbers")
        sleep(2)
        print()
        print("     |     |     ")
        print("  1  |  2  |  3  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  4  |  5  |  6  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  7  |  8  |  9  ")
        print("     |     |     ")
        print()
        sleep(8)
        self.MAIN()

#A list to remember the index of values
l=[[1,2,3],[4,5,6],[7,8,9]]
#A list to the position of 'X' and 'O'
m=[['1','1','1'],['1','1','1'],['1','1','1']]                   
q=input('Enter the name of player : ')
print()
ob=TicTacToe(q,l,m)
ob.main()

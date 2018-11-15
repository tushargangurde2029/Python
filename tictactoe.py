#Creating the game of tic tac toe using the concepts of python=Lists,Definations,Adding list item using append and index method,functions,while and for loops,if else statements and the many more.(First mini project in my life)
def display(a):
   print('~~~~~~~~~~~~~')
   print('|',a[0],'|',a[1],'|',a[2],'|')
   print('~~~~~~~~~~~~~')
   print('|',a[3],'|',a[4],'|',a[5],'|')
   print('~~~~~~~~~~~~~')
   print('|',a[6],'|',a[7],'|',a[8],'|')
   print('~~~~~~~~~~~~~')
a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
win1=int(0)
win2=int(0)
flag=int(1)
print('********The TIC TAC TOE game********')
print('Three Rules you should know')
print('1.The Tic Tac Toe board look like this if you want to add then enter the number=')
print('      |1|2|3|')
print('      |4|5|6|')
print('      |7|8|9|')
print('2.After every game the players changed that means first chance of first player goes to second')
print('3.Enjoy')
while True:
   print('First Player wins=',win1)
   print('Second Player wins=',win2)
   check=input('You want to play?(y/n)=')
   a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
   if(check=='y'):
      display(a)
      positions=[]
      for i in range(1,10):
         if(i%2!=0):
            while True:
               player1=int(input('Enter the Box Position='))
               if(player1<=0 or player1>=10):
                  print('You enter the wrong choice')
                  continue
               elif(a[player1-1]=='O' or a[player1-1]=='X'):
                  print('The position is already taken')
                  continue
               else:
                  a.insert((player1-1),'O')
                  del a[player1]
                  display(a)
                  break
         elif(i%2==0):
            while True:
               player2=int(input('Enter the Box Position='))
               if(player2<=0 or player2>=10):
                  print('You enter the wrong choice')
                  continue
               elif(a[player2-1]=='O' or a[player2-1]=='X'):
                  print('The position is already taken')
                  continue
               else:
                  a.insert((player2-1),'X')
                  del a[player2]
                  display(a)
                  break
         if(a[0]==a[1] and a[0]==a[2] and a[0]=='O'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break
         elif(a[0]==a[1] and a[0]==a[2] and a[0]=='X'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break    
         elif(a[3]==a[4] and a[3]==a[5] and a[3]=='O'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break
         elif(a[3]==a[4] and a[3]==a[5] and a[3]=='X'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break 
         elif(a[6]==a[7] and a[6]==a[8] and a[6]=='O'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break
         elif(a[6]==a[7] and a[6]==a[8] and a[6]=='X'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break 
         elif(a[0]==a[3] and a[0]==a[6] and a[0]=='O'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break
         elif(a[0]==a[3] and a[0]==a[6] and a[0]=='X'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break 
         elif(a[1]==a[4] and a[1]==a[7] and a[1]=='O'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break
         elif(a[1]==a[4] and a[1]==a[7] and a[1]=='X'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break 
         elif(a[2]==a[5] and a[2]==a[3] and a[2]=='O'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break
         elif(a[2]==a[5] and a[2]==a[8] and a[2]=='X'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break 
         elif(a[0]==a[4] and a[0]==a[8] and a[0]=='O'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break
         elif(a[0]==a[4] and a[0]==a[8] and a[0]=='X'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break 
         elif(a[2]==a[4] and a[2]==a[6] and a[2]=='O'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break
         elif(a[2]==a[4] and a[2]==a[6] and a[2]=='X'):
            flag=flag+1
            if(flag%2==0):
               win1=win1+1
               print('First Player Wins')
            else:
               win2=win2+1
               print('Second Player Wins')
            break              
   else:
      if(win1>win2):
         print('The First player Wins')
      elif(win2>win1):
         print('The Second player wins')
      elif(win2==win1):
         print('No one wins')
      print('Thanks for playing')
      break

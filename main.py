import random   #allows me to use the random function

#function that goes through the player name letter by letter making sure that it doesn't contain any numbers or special characters
def isValidated(playerName):
  val = True
  for x in range(1, len(playerName)):
    if playerName[x] not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'v', 'w', 'x', 'y', 'z'):
      val = False

  return val

#function that allows the player to roll the dice and according to the rules calculates the corresponding score. has the argument score so that the program can add to the score depending on what they roll and what the rules are. has the argument player so that the function knows the name of the player and correctly prints their name on the console. has the argument player ends with s so that if the name ends with s, the correct grammatical formatting is used. has the argument winner so that if the player's score goes below 0, it automatically assigns the winner as player2. 
def roll(score, player):
  #rolls two dice and prints the numbers as well as the total rolled
  roll1 = random.randrange(1, 6)
  print(player, "rolled a", roll1)
  roll2 = random.randrange(1, 6)
  print(player, "rolled a", roll2)
  print("In total", player, "rolled", str(roll1 + roll2))

  #adds each of the rolls to the score
  score = score + roll1 + roll2
  
  #checks if the player rolled an odd or even number and either adds 10 or takes away 5
  if ((roll1 + roll2) % 2) == 0:
    score = score + 10
    print(player + "'s total is even so 10 additional points were awarded!")
  else:
    score = score - 5
    print(player + "'s total is odd so 5 points were deducted!")

  #checks if the player rolled a double and allows them to roll again and adds that to the total score
  if roll1 == roll2:
    print(player, "rolled a double so they get an extra roll!")
    roll = random.randrange(1, 6)
    print(player, "rolled a", roll)
    score =  score + roll

  #prints the total score onto the screen using the correct grammar depending on if their name ends with an s
  print(player + "'s total score is", score)
  
  #returns the total score of the player so that the main program can change the variable of the correct player's score
  return score

#the login function that asks both users to enter their usernames and password. you can only make 3 mistakes each otherwise the program will lock you out. it takes in the parameter player number so that it can print the correct statements
def login(playerNumber):
  wrong = 0
  allow = False
  users = []

  #dumping the entire database of all the users and passwords to a list/dynamic array
  with open("users.txt") as usersFile:
    users = usersFile.readlines()

  while wrong < 3 and allow == False:
    
    #asks the user to enter the username and stores it in the user1 variable
    user = input("Player " + playerNumber + "'s username: ")
    user = user + '\n'

    #checks if the username exists in the list. if not then tells the user that it doesn't exist and asks again. if the username exists then the program proceeds to ask for the password. if they get it right then the program sets allow1 to true but if they get it wrong then the variable wrong is incremented and the process repeats. the variable wrong can't go above 4. if it does then the program doesn't let the user play the game
    if user in users:
      password = input("Player " + playerNumber + "'s password: ")
      password = password + '\n'
      if users[users.index(user)+1] == password:
        allow = True
      else:
        print('Wrong password')
        allow = False
        wrong = wrong + 1
        print()
        print(str(3-wrong), 'tries left...')
    else:
      print('Username does not exist')
      allow = False 
      wrong = wrong + 1 
      print()
      print(str(3-wrong), 'tries left...')

  #prints a success message is the username and password was correct
  if allow == True:
    return True

#assigning variables that will be used later in the program
again = 'y'
alreadyPlayed = False
masterAllow = False

#the function call for the login. it calls the function twice for both players and if one of them returns false then the variable masterAllow doesn't change to true, an error message is displayed and they can't play the game. If both function calls return true then masterAllow is set to true and they are allowed to play the game
if login('1') == True:
  print()
  print('Login successful for player 1')
  print()
  if login('2') == True:
    print()
    print('Login successful for player 2')
    print()
    masterAllow = True
  else:
    print('Login unsuccessful for player 2')
    print('You are not allowed to play')
else:
  print('Login unsuccessful for player 1')
  print('You are not allowed to play')

#will repeat the game if they want to play it again and they are allowed to play
while (again == 'y') and masterAllow == True:
  
  #if the user hasn't played the game before then it will print the rules
  if alreadyPlayed == False:
    print('Welcome to the dice game by Amogh')
    print('Here are the rules:')
    print('1) Two dice are rolled and added to their score')
    print('2) If the total is an even number, 10 additional points are added to their score')
    print('3) If the total is an odd number, 5 points are subtracted from their score')
    print('4) If they roll a double, they get to roll one extra die and get the number of points rolled added to their score')
    print('5) The score of a player cannot go below 0 at any point')
    print('6) The person with the highest score at the end of the 5 rounds wins')
    print('7) If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins)')
    print('')

  #asks the user to enter their names for player 1 and 2. they will automatically be capitalised
  print()
  player1 = input("Player 1's Name: ").capitalize()
  player2 = input("Player 2's Name: ").capitalize()

  #if the names don't follow the validation rules then they will be asked to write their names again until it is validated.  
  while isValidated(player1) == False or isValidated(player2) == False or player1 == player2:
    print()
    print("Invalid name")
    print("Check if the names are the same and if they only contain letters")
    player1 = input("Player 1's Name: ").capitalize()
    player2 = input("Player 2's Name: ").capitalize()

  #variables that I will use later in my program
  roundNum = 1
  cont = 'y'

  score1 = 0
  score2 = 0
  
  winner = ''

  #the rolling loop. while the number of rounds is less than or equal to 5 and they want to continue and there isn't a winner yet, roll the dice
  while cont == 'y' and roundNum <= 5 and winner == '':

    #prints the round number onto the console
    print()
    print("Round", str(roundNum) + ":")

    #rolls the dice for both players and checks whether the other player has already won as their score went below 0
    score1 = roll(score1, player1)
    print()
    if score1 < 0:
      winner = player2
    score2 = roll(score2, player2)
    if score2 < 0:
      winner = player1

    print()
    
    #if player 1's score is bigger then it will print to the console that they are in the lead by x amount of points where it will calculate what x is. 
    if score1 > score2:
      print(player1, "is in the lead by", str(score1 - score2), "points!")
    elif score2 > score1:
      print(player2, "is in the lead by", str(score2 -score1), "points!")


    #increments the round number
    roundNum = roundNum + 1

    #if the round number is smaller or equal to 5 and there isn't a winner yet then it asks the user if they want to continue to the next round. validates their input and repeatedly asks them again if it is invalid. if the round number is bigger than or equal to 5 and there isn't a winner yet then it prints 'max rounds reached' as you can only play 5 rounds max. 
    if roundNum <= 5 and winner == '':
      cont = input("Do you want to continue to the next round? (y/n): ")
      while cont != 'y' and cont != 'n':
        print()
        print("Invalid answer try again")
        cont = input("Do you want to continue to the next round? (y/n): ")
    elif roundNum >= 5 and winner == '':
      print("Max rounds reached")
      break
    
    #if there already is a winner due to a player's score going below 0, it prints that they won 'as the other player's score went below 0'
    if winner != '':
      print(winner, "won as the other player's score went below 0")

    #if they don't want to continue to the next round then it will break out of the main while loop
    if cont == "n":
      break

  print()

  #if the both the scores are the same then it will play another round and make sure that the scores are different and their is a winner
  while (score1 == score2):
    
    print(player1, "and", player2, "are drawing so another round is being played:")

    score1 = roll(score1, player1)
    if score1 < 0:
      winner = player2
    print()
    score2 = roll(score2, player2)
    if score2 < 0:
      winner = player1

  #if there isn't already a winner then this will calculate who the winner is by seeing who has the most points
  if winner == '':
    if score1 > score2:
      winner = player1
    else:
      winner = player2

  #if the winner is player 1 then it will open the file for append and append the name of the winner and their score and close the file. else it will do the same but for the other player. also if the points that they won with is smaller than or equal to 9 then it will add a 0 in front of it, for example 7 will become 07
  if winner == player1:
    print("The winner is", player1, "with", str(score1), "points!")
    winFile = open("winner.txt", "a")
    if score1 <= 9:
      winFile.write("0" + str(score1) + " " + player1)
    else:
      winFile.write(str(score1) + " " + player1)
    winFile.write('\n')
    winFile.close()
    print()
  else:
    print("The winner is", player2, "with", str(score2), "points!")
    winFile = open("winner.txt", "a")
    if score2 <= 9:
      winFile.write("0" + str(score2) + " " + player2)
    else: 
      winFile.write(str(score2) + " " + player2)
    winFile.write("\n")
    winFile.close()
    print()

  #allows me to use the list scores to store the contents of the winner.txt file
  scores = []

  #opens the file winner.txt for read and dumps the entire contents of the file to the list scores
  with open("winner.txt", "r") as winFile:
    scores = winFile.readlines()


  #sorts the list scores by the score in each record of the file. sorts it in reverse to the highest score is at the top of the file
  scores = sorted(scores, reverse = True)
  
  #rewrites the contents of the winner.txt file as the contents of the array as it is sorted
  with open("winner.txt", "w") as winFile:
    winFile.writelines(scores)

  #trims the scores list and only keeps the first 5 as they are the top 5 scores
  scores = scores[0:5]

  #prints 'Top 5 Scores'
  print("Top 5 Scores: ")

  #prints the top 5 scores in order with their rank and brackets to separate them
  x = 1
  for count in scores:
    print(str(x) + ")", count)
    x = x + 1

  #asks the user if they want to play again. validates the input and repeatedly asks them if it isn't 'y' or 'n'
  again = input('Do you want to play again?(y/n): ')
  while again != 'y' and again != 'n':
    print('Invaid answer please try again')
    again = input('Do you want to play again?(y/n): ')

  #sets the variable alreadyPlayed to true so that the rules aren't printed again
  alreadyPlayed = True

#if they don't want to play again but they are still allowed to play then it will print 'thank you for playing' onto the console
if again == 'n' and masterAllow == True:
  print('Thank you for playing')

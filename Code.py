# start of the game
import random
player1_score=0
player2_score=0
player1_wins=0
player2_wins=0
ties=0
print("to exit the whole game just enter F")
while True:
	choice=input("Enter F if you want to end the league,to continue give any other character:")
	if choice=='F':
		break
	while True:
		player1=input("Enter the choice of player1(R=rock,P=paper,S=scissor):")
		if player1=='E':
			break
		a=random.randint(1,3)
		b=int(a)
		if b==1:
			player2='R'
		elif b==2:
			player2='S'
		else:
			player2='P'
		print("choice entered by computer(R=rock,P=paper,S=scissor):",player2)
		if player2=='E':
			break
		if player1=='R':
			if player2=='R':
				print("make a turn again")
			if player2=='S':
				player1_score=player1_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
			if player2=='P':
				player2_score=player2_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
		elif player1=='P':
			if player2=='P':
				print("make a turn again")
			if player2=='S':
				player2_score=player2_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
			if player2=='R':
				player1_score=player1_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
		elif player1=='S':
			if player2=='S':
				print("make a turn again")
			if player2=='R':
				player2_score=player2_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)	
			if player2=='P':
				player1_score=player1_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
		elif player2=='R':
			if player2=='R':
				print("make a turn again")
			if player1=='S':
				player2_score=player2_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
			if player1=='P':
				player1_score=player1_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
		elif player2=='P':
			if player2=='P':
				print("make a turn again")
			if player1=='S':
				player1_score=player1_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
			if player1=='R':
				player2_score=player2_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
		elif player2=='S':
			if player2=='S':
				print("make a turn again")
			if player1=='R':
				player1_score=player1_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)	
			if player1=='P':
				player2_score=player2_score+1
				print("player 1 score is:",player1_score)
				print("player 2 score is:",player2_score)
							
		else:
			print("input is invalid, Please give the input again")	
			player1=input("Enter the choice of player1(R=rock,P=paper,S=scissor):")
			player2=input("Enter the choice of player2(R=rock,P=paper,S=scissor):")
	
	if player1_score>player2_score:
		print("player1 wins by a margin of ",player1_score-player2_score)
		player1_wins=player1_wins+1
		
	elif player1_score==player2_score:
		print("The game has been tied")
		ties=ties+1
		
		
	else:
		print("player2 wins by a margin of ",player2_score-player1_score)
		player2_wins=player2_wins+1
	
	player1_score=0;
	player2_score=0;	
print("player1 wins",player1_wins)	
print("player2 wins",player2_wins)
print("total ties",ties)
	
# end of the game
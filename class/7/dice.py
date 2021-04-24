import random

def roll_dice(n):
    dice=[]
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice
def who_is_winner(usr_list, cmp_list):
	cmp_score=sum(cmp_list)
	usr_score=sum(usr_list)
	print("user score %d" % usr_score)
	print("computer score %d" %cmp_score)
	if (usr_score > cmp_score):
		print('user is winner')
	elif(usr_score < cmp_score):
		print('computer is winner')
	else:
		print('tie')

num_dice = int(input('n'))
user = roll_dice(num_dice)
print('user result = %s'  % user) #格式化 and show user list
comp = roll_dice(num_dice)
print('computer result = %s' % comp) #格式化 and show computer list
who_is_winner(user,comp)
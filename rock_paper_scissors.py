import random

def play():
    user_win = 0
    comp_win = 0
    
     
    while user_win != 2 or comp_win != 2:
        user = input("First one to 2 wins! What\'s your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            print('Great minds think alike, try again!')
            pass 
        
        elif is_win(user, computer):
            user_win += 1
            print(f'You won {user_win} times!')
        else:    
            comp_win += 1
            print(f'I won {comp_win} times!')
        
        if user_win == 2:
            print(f'You win! You beat me {user_win} times!')
            return user_win
        elif comp_win == 2:
            print(f'I won {comp_win} times, Better luck next time!!')
            return comp_win
                        
    
def is_win(player, opponent):
    # r > s, s > p, p > r
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player ==  's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True


play()

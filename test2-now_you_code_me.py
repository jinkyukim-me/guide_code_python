import random

def draw_card(userCard, trump):
    n = random.randrange(0,52)
    if trump[n]==userCard:
        return True
    else:
        return False
        
trump = ['SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK','DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK','CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK']

userCard = input()

for i in range(len(trump)):
    trump[i] = userCard

print(draw_card(userCard, trump))

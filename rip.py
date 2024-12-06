import random

def game():
    
    n=int(input('enter the limit'))
    print("you are playing ")
   
    score=random.randint(1,n)
    with open("Newscore") as f:
        Newscore=f.read()

        if(Newscore !=""):
              Newscore=int(Newscore)
        else:
            Newscore=0
       
    print(f"your score is {score}")

    if(score>Newscore) or (score<=Newscore):
        with open("Newscore","w") as f:
            f.write(str(score))




    return score
game()

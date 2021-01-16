class RockPaperScissors:

    def CheckWinner(self,player1,player2):
        if player1==player2:
            return "Tie"

        elif player1=="Rock":
                if player2=="Scissors":
                    return "Player1"
                else:
                    return "Player2"

        elif player1=="Scissors":
                if player2=="Rock":
                    return "Player2"
                else:
                    return "Player1"
        
        else: 
                if player2=="Rock":
                    return "Player1"
                else:
                    return "Player2"
    
    def Checkroundwinner(self,array_input): 
        
        player1count=0
        player2count=0

        for x in array_input:
            y=x      
            player1,player2=y.split("-")

            result=RockPaperScissors.CheckWinner(self,player1 , player2)
            if result=="Player1":
                player1count=player1count+1
            elif result=="Player2":
                player2count=player2count+1

        if player1count>player2count: 
            return "player1 is winner"

        elif player2count>player1count:
            return "player2 is winner"
        else:
            return "Tie"
        

             
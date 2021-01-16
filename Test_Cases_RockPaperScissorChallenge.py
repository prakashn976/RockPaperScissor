import unittest
from RockPaperScissorChallenge import RockPaperScissors

class TestRockPaperScissors(unittest.TestCase):   
    
    def test_Tie(self):
        arrayinput=["Scissors-Scissors" ,"Paper-Paper","Rock-Rock"]
        result=RockPaperScissors.Checkroundwinner(self,arrayinput)
        self.assertEqual("Tie",result)

    def test_Player1IsWinner_IfAllGamesWonByPlayer1(self):
        arrayinput=["Rock-Scissors" ,"Scissors-Paper","Paper-Rock"]
        result=RockPaperScissors.Checkroundwinner(self,arrayinput)
        self.assertEqual("player1 is winner",result)

    def test_Player2IsWinner_IfAllGamesWonByPlayer2(self):
        arrayinput=["Scissors-Rock" ,"Paper-Scissors","Rock-Paper"]
        result=RockPaperScissors.Checkroundwinner(self,arrayinput)
        self.assertEqual("player2 is winner",result)

    def test_Player1IsWinner_IfPlayer1WinsTwoGames(self):
        arrayinput=["Rock-Scissors" ,"Scissors-Paper","Rock-Paper"]
        result=RockPaperScissors.Checkroundwinner(self,arrayinput)
        self.assertEqual("player1 is winner",result)

    def test_Player1IsWinner_IfPlayer1WinsOneGameOtherTwoTie(self):
        arrayinput=["Rock-Scissors" ,"Paper-Paper","Rock-Rock"]
        result=RockPaperScissors.Checkroundwinner(self,arrayinput)
        self.assertEqual("player1 is winner",result)
    
    def test_Player2IsWinner_IfPlayer2WinsTwoGames(self):
        arrayinput=["Scissors-Rock" ,"Paper-Scissors","Rock-Scissors"]
        result=RockPaperScissors.Checkroundwinner(self,arrayinput)
        self.assertEqual("player2 is winner",result)

    def test_Player2IsWinner_IfPlayer2WinsOneGameOtherTwoTie(self):
        arrayinput=["Rock-Paper" ,"Paper-Paper","Rock-Rock"]
        result=RockPaperScissors.Checkroundwinner(self,arrayinput)
        self.assertEqual("player2 is winner",result)
    
    

if __name__ == '__main__':
    unittest.main()

import unittest
import Game

class testBolwingGame(unittest.TestCase):

    def testGutterGame(self):
        g = Game.Game()
        for i in xrange(20):
            g.roll(0)
        assert g.score() == 0

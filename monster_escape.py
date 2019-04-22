import random


class EasterEggHunt():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def displayInfo(self, player, monster, door):
        print(
            f'Player Coords: {player.getCoords()}\t Monster Coords: {monster.getCoords()}\t Door Coords: {door.getCoords()}')
        print(f'Player Lives: {player.getLives()}')

    def makeGrid(self, player, monster, door):
        self.displayInfo(player, monster, door)

        for row in range(self.rows):
            print('+---' * self.cols + '+')
            for col in range(self.cols):
                if [col, row] == player.getCoords() and [col, row] == player.getCoords():
                    if col == 0:
                        print('|m&p|', end='')
                    else:
                        print('m&p|', end='')
                elif [col, row] == door.getCoords():
                    if col == 0:
                        print('| d |', end='')
                    else:
                        print(' d |', end='')
                elif [col, row] == player.getCoords():
                    if col == 0:
                        print('| p |', end='')
                    else:
                        print(' p |', end='')
                elif [col, row] == door.getCoords():
                    if col == 0:
                        print('| d |', end='')
                    else:
                        print(' d |', end='')
                elif [col, row] == monster.getCoords():
                    if col == 0:
                        print('| m |', end='')
                    else:
                        print(' m |', end='')
                elif col == 0:
                    print('|   |', end='')
                else:
                    print('   |', end='')
            print('')
        print('+---' * self.cols + '+')

    def checkMonsterCollision(self, player, monster):
        if player.getCoords() == monster.getCoords():
            if player.isCheating():
                player.setLives(-1)
                print("The monster hit you. You lost a life")
                print(f'You have {player.getLives()} lives left')
            else:
                print('YOU AND YOUR CHEATCODES LAUGH IN THE FACE OF DANGER!')

    def checkWinCondition(self, player, door):
        if player.getCoords() == door.getCoords():
            if player.isCheating():
                print('You win... dirty cheater')
                return True
            else:
                print('You win!!!')
                return True

    def checkGameOver(self, player):
        return player.getLives() <= 0


class GamePiece():
    def __init__(self, coords):
        self.coords = coords

    # get coords
    def getCoords(self):
        return self.coords

    def startRandomCoords(self, cols, rows):
        self.coords = [random.randint(
            1, cols - 1), random.randint(1, rows - 1)]


class Player(GamePiece):
    def __init__(self, name, lives=3, coords=[0, 0], cheating=False):
        super().__init__(coords)
        self.name = name
        self.lives = lives
        self.cheating = cheating

    def movePlayer(self, move):
        if move == 'up' and (self.coords[1] - 1) >= 0:
            self.coords[1] -= 1
        elif move == 'down' and (self.coords[1] + 1) < rows:
            self.coords[1] += 1
        elif move == 'left' and (self.coords[0] - 1) >= 0:
            self.coords[0] -= 1
        elif move == 'right' and (self.coords[0] + 1) < rows:
            self.coords[0] += 1
        else:
            print("Sorry that is not a valid move")
            return False
        return True

    def setLives(self, num):
        self.lives += num

    def getLives(self):
        return self.lives

    def resetPlayer(self):
        self.lives = 3
        self.coords = [0, 0]
        self.cheating == False

    def isCheating(self):
        return self.cheating


class Monster(Player):
    def __init__(self, name, lives=999, coords=[4, 4]):
        super().__init__(name, lives, coords)

    def moveMonster(self, cols, rows):
        self.coords = [random.randint(
            1, cols - 1), random.randint(1, rows - 1)]


# variable to check exit game
playing = True
# main loop for creating and playing game
while playing:
    # instantiate objects for game
    rows = 5
    cols = 5
    game = EasterEggHunt(rows, cols)
    player = Player('Steve')
    monster = Monster('Mr. Angry')
    door = GamePiece('door')
    monster.startRandomCoords(cols, rows)
    player.startRandomCoords(cols, rows)
    door.startRandomCoords(cols, rows)

    # making sure things don't spawn on each other
    while player.getCoords() == monster.getCoords() or player.getCoords() == door.getCoords() or monster.getCoords() == door.getCoords():
        player.startRandomCoords(cols, rows)
        monster.startRandomCoords(cols, rows)
        door.startRandomCoords(cols, rows)

    game_over = False

    # start game loop
    while not game_over:
        # create the grid
        game.makeGrid(player, monster, door)

        # ask user for input see if they quit or move
        ans = input(
            'Would you like to quit or move up/down/left/right? ').lower()

        # base case
        if ans == 'quit':
            print('Thanks for playing!')
            break

        elif ans == 'stronk':
            print("!!! - INVINCIBILITY ACTIVATED - !!!")
            player.setLives(99999999999)

        elif ans == 'up' or ans == 'down' or ans == 'left' or ans == 'right':
            # move player and monster
            player.movePlayer(ans)
            monster.moveMonster(cols, rows)

            # making sure the monster isn't covering the door
            while door.getCoords() == monster.getCoords():
                monster.moveMonster(cols, rows)

            # check win condition
            if game.checkWinCondition(player, door):
                game_over == True
                break

            else:
                # check collisions
                game.checkMonsterCollision(player, monster)

                if game.checkGameOver(player):
                    print('You lost all your lives! Better luck next time.')
                    game_over = True
        else:
            print('Please choose quit or move up/down/left/right')

    # ask if the user would like to play again
    ans = input('Would you like to play again? (Y/N) ').lower()

    if ans == 'n':
        playing = False
    else:
        player.resetPlayer()

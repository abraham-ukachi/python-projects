##############################
# Name: Job01 - Le Pendu
# Script: pendu.py
# Author: Abraham Ukachi <abraham.ukachi@laplateforme.io>
# version: 0.0.1 (alpha)
#
# Usage:
#   1-|> python3 pendu.py
#
#   2-|> from pendu import PenduGame
#    -|>
#    -|> pendu = PenduGame('en')
#    -|> pendu.requestPlayerLevel()
#    -|> pendu.startGame()
#
##############################
# IMPORTANT: This code is a work in progress and subject to major changes until version 0.1
##############################

#========== Job 01 ===========
#     >>> DESCRIPTION <<<
#~~~~~~~~~ (French) ~~~~~~~~~~
#
# - Écrivez un programme pendu.py, qui permet à l’utilisateur de faire une partie 
#   du célèbre jeu le pendu dans le terminal.
# - Le programme devra dans un premier temps demander aujoueur le niveau avec lequel 
#   il souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi 
#   (exemple débutant 10, intermédiaire 7, expert 4). 
# - Vous êtes libres de choisir le nombre de vies par niveau.
# - Le programme devra donc choisir aléatoirement un mot dans le dictionnaire 
#   disponible ici, et afficher :
#   - Le nombre de vies restantes au joueur
#   - Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
#     En expert, la liste n’apparaîtra pas)
#   - Des “_” pour remplacer les lettres non trouvées
#   - Les lettres proposées qui se trouvent dans le mot 
#
# - La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.
#
# - Dans l’exemple ci dessous, le mot est “Plateforme”. 
# - Le joueur joue en débutant comme il l’a dit au premier input. 
# - Il propose la lettre X, qui ne se trouve pas dans le mot recherché. 
# - Il perd donc une vie, la lettre s’ajoute à la liste des lettres proposées. 
# - Il propose ensuite le E. Toutes les lettres E du mot sont donc affichées, 
#   et le E est ajouté à la liste de lettres proposées.
#
#~~~~~~~~~ (English) ~~~~~~~~~
#
# - Write a pendu.py program, which allows the user to make part of the famous 
#   game the pendu in the terminal.
# - The program will first have to ask the player what level he wants to play with.
# - It will have a number of lives depending on the level chosen (example beginner 10, 
#   intermediate 7, expert 4). You are free to choose the number of lives per level.
# - The program will have to randomly choose a word in the dictionary available here, 
#   and display:
#   - The number of lives left to the player
#   - Letters already proposed by the player (in the beginner and intermediate mode. 
#     As an expert, the list will not appear)
#   - “_” to replace letters not found
#   - The proposed letters in the word
#
# - The game ends when the player has found the word, or has no life.
#
# - In the example below, the word is “Platform”. 
# - The player plays starting as he said at the first input. 
# - He proposes the letter X, which is not in the search word. 
# - So he loses a life, the letter is added to the list of proposed letters. 
# - He then proposes the E. All the letters E of the word are thus displayed,
# - and the E is added to the list of proposed letters.
#
#=============================

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOTTO: I'll always do more 😜!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Importing the 'good-stuff'...
import time # <- python's built-in time module: This stuff can make you 'sleep' ;)
import random


# Let's define some constants, shall we? ;)

# Prompt Sign constants
PROMPT_SIGN_DEFAULT = "\x1b[1m\x1b[34m?\x1b[0m " # <- (bold + blue)
PROMPT_SIGN_IN = "\x1b[1m\x1b[32m>>\x1b[0m " # <- (bold + green)
PROMPT_SIGN_OUT = "\x1b[1m\x1b[34m<<\x1b[0m " # <- (bold + blue)
PROMPT_SIGN_ERR = "\x1b[1m\x1b[31m<<\x1b[0m " # <- (bold + red)

# Emoji constants
EMOJI_THUMBS_UP = "\U0001F44D"
EMOJI_THUMBS_DOWN = "\U0001F44E"
EMOJI_CHECK_MARK = "\U00002714"

# - language constant
LANG = "fr" # <- default language set to "english", duh! Use 'fr' for french


# TODO: Create a parent class named `Game`
# TODO: Rename `PenduGame` class to `Pendu`
# TODO: Inherit the `Game` class from `Pendu` class


# Creating a `PenduGame` class...

# ======= START OF PENDUGAME CLASS ========

class PenduGame:
    """
    Pendu is the one of the most fun games in France. :) 
    """
    
    # Defining some attributes...
    
    name = "Pendu"
    version = "0.0.1"
    
    author = {} # <- Shemless plug, ikr ;) 
    author["name"] = "Abraham Ukachi"
    author["email"] = "abraham.ukachi@laplateforme.io"
    
    
    # assigning values to `Pendu` with the `__init__()` function
    def __init__(self, lang):
        """
        A function that is called automatically every time `Pendu` is 
        being used to create a new object

        :param { obj } self: A parameter to access variables
        :param { str } lang: Language of the game
        :param { dict } strings
        """
        
        # Initializing some variables for `PenduGame`...
        
        ## ==== PUBLIC VARIABLES

        self.lang = lang # <- the game's current language (eg. 'en' for english)
        self.words = [] # <- a list of words to be used by this game
        self.randomWord = "" # <- a randomly generated word the player has to guess/found.
        self.playerLetters = [] # <- a list of letters that the player guessed
        self.found = False # <- If `True` the player has found the word
        self.currentLivesCount = 0 # <- the number of lives left of the player
        self.tries = 0 # <- The number of attempts or tries made by the player
        self.levels = (("beginner", "intermediate", "advanced", "expert"))
        self.lives = {"beginner": 15, "intermediate": 12, "advanced": 6, "expert": 3}
        # set the default level to beginner
        self.defaultLevel = "beginner"
        self.caseSensitive = False
         



        # Create a `strings` dictionary/object for game localization
        # NOTE: The optimal way would be to create this outside the main file.
        self.strings = { "en": {}, "fr": {} }

        # EN - strings in english
        self.strings["en"]["welcome"] = "Welcome to Pendu"
        self.strings["en"]["chooseLevel"] = "Choose your level:"
        self.strings["en"]["beginner"] = "Beginner"
        self.strings["en"]["intermediate"] = "Intermediate"
        self.strings["en"]["advanced"] = "Advanced"
        self.strings["en"]["expert"] = "Expert"
        self.strings["en"]["chooseLevelAgain"] = "Please enter a number from {} to {}:"
        self.strings["en"]["startingGame"] = "Starting the game..."
        self.strings["en"]["gameInfo1"] = "Hello, one word out of \x1b[4m%s french words\x1b[0m has been selected randomly."
        self.strings["en"]["gameInfo2"] = "To win this game, you've got to guess all letters correctly"
        self.strings["en"]["livesLeft"] = "You've got \x1b[36m{} live{}\x1b[0m left"
        self.strings["en"]["lettersGiven"] = "Letters previously given: \x1b[36m{}\x1b[0m"
        self.strings["en"]["chooseLetter"] = "What's your letter?"
        self.strings["en"]["good"] = "Good"
        self.strings["en"]["bad"] = "Nope"
        self.strings["en"]["congratulations"] = "Congratulations! You've won !!!"
        self.strings["en"]["youLost"] = "Oops! You've lost !!!"
        self.strings["en"]["results"] = "Results"
        self.strings["en"]["resultLevel"] = "Level"
        self.strings["en"]["resultTries"] = "Attempts"
        self.strings["en"]["resultWord"] = "Word"
        self.strings["en"]["resultLives"] = "Lives remaining"



        # FR - strings in french
        self.strings["fr"]["welcome"] = "Bienvenu au Pendu"
        self.strings["fr"]["chooseLevel"] = "Choisissez votre niveau :"
        self.strings["fr"]["beginner"] = "Débutant"
        self.strings["fr"]["intermediate"] = "Intermediare"
        self.strings["fr"]["advanced"] = "Supérieure"
        self.strings["fr"]["expert"] = "Expert"
        self.strings["fr"]["chooseLevelAgain"] = "Veuillez entrer un nombre de {} à {} :"
        self.strings["fr"]["startingGame"] = "Démarrage du jeu..."
        self.strings["fr"]["gameInfo1"] = "Bonjour, un mot sur \x1b[4m%s mots\x1b[0m a été choisi au hasard"
        self.strings["fr"]["gameInfo2"] = "Pour gagner ce jeu, vous devez deviner toutes les lettres correctement"
        self.strings["fr"]["livesLeft"] = "Il vous reste \x1b[36m{} vie{}\x1b[0m"
        self.strings["fr"]["lettersGiven"] = "Lettres proposées : \x1b[36m{}\x1b[0m"
        self.strings["fr"]["chooseLetter"] = "Quelle lettre proposes tu ?"
        self.strings["fr"]["good"] = "Bon"
        self.strings["fr"]["bad"] = "Mince"
        self.strings["fr"]["congratulations"] = "Félicitations! Vous avez gagné !!!"
        self.strings["fr"]["results"] = "Resultats"
        self.strings["fr"]["youLost"] = "C'est domage! Vous avez perdu !!!"
        self.strings["fr"]["resultLevel"] = "Niveau"
        self.strings["fr"]["resultTries"] = "Tentatives"
        self.strings["fr"]["resultWord"] = "Mot"
        self.strings["fr"]["resultLives"] = "Nombre de vie(s) restant(s)"

        

        ## ==== PRIVATE VARIABLES
        
        self._playerLevel = ""
        self._hiddenLetters = []

        # self._playerLevelChanged = False
        # self.__livesLeft__ = -1
    
    
    
    # PRIVATE METHODS
    
    def _loadWords(self, filename = "dico_france.txt", enc = "cp1250"):
        """
        Loads all the words from the given `filename`
        This method extracts all the words to Pendu's `words` list

        :param { str } filename
        :param { str } encoding
        """

        
        # DEBUG [4dbsmaster]: tell me about it 
        # print("[_loadWords](1): About to load words from %s ..." % filename)

        # Let's try to open the file
        try:
            # open the file
            file = open(filename, encoding=enc)
            # get the words from the `file`
            words = file.read()
            # Remove all the '\n' from the `words` and 
            # update the game's words (i.e self.words)
            self.words = words.split('\n')
            # close the file
            file.close()
        except Exception:
            # Do something if a problem occurs - maybe?
            pass

        # DEBUG [4dbsmaster]: tell me about it 
        # print("[_loadWords](2): %d words were loaded successfully" % len(self.words))

        # Tell the world how many words were loaded
        print(self.getString("gameInfo1") % len(self.words))
        print(self.getString("gameInfo2"))
    
    

    def _checkLetter(self, letter):
        """
        Method used to check or verify that the player's given `letter` is valid

        :parm { str } letter
        :return { bool } result
        """
        
        # Initialize the `result` variable
        result = False
        
        # lowercase the `letter`
        letter = letter.lower()
        # lowercae the randomWord too
        randomWord = self.randomWord.lower()
        
        # if the given `letter` exists in the `randomWord` and hasn't been guessed yet
        if (letter in randomWord) and (letter not in self.playerLetters):
            # ...set the `result` to `True`
            result = True 
        


        # DEBUG: [4dbsmaster]: tell me about it :)
        # print("[_checkLetter](1): randomWord => ", self.randomWord)
        # print("[_checkLetter](2): letter => ", letter)
        # print("[_checkLetter](3): ~ in randomWord? => ", letter in self.randomWord)
        # print("[_checkLetter](4): ~ not in playerLetters => ", \
        #        letter not in self.playerLetters)

        # return the result
        return result


    def _notifyHiddenLetters(self):
        """
        Method used to notify or update the `_hiddenLetters` list.
        """
        
        # Get the random word as `randomWord`
        rw = self.randomWord
        # Define the separator 
        separator = '_'
        
        # Initialize a `newHiddenLetters` list by populating it 
        # with '_' for each letter in the `randomWord` 
        # eg. if `randomWord` is "love", newHiddenLetters will be ['_','_','_','_']
        newHiddenLetters = [separator for letter in rw]
        

        # For each index or letter position in `randomWord`...
        for i in range(len(rw)):
            # ...at each `newHiddenLetter`'s position;
            # - substitute the separator with its corresponding letter from `randomWord`;
            # - Only if that `randomWord` letter can be found in `playerLetters`
            newHiddenLetters[i] = rw[i] if (rw[i] in self.playerLetters) else separator


        # Update the `_hiddenLetters` list with `newHiddenLetters`
        self._hiddenLetters = newHiddenLetters


    ## --- private handlers

    def _playerLevelHandler(self, playerLevel):
        """
        Handler that is called whenever the player's level gets updated
        """

        # get the player level (eg. 'beginner')
        # playerLevel = self.getPlayerLevel()
        
        # update the current lives count
        self.currentLivesCount = self._getLivesOfLevel(playerLevel)

        # get the locale name of the level (eg. 'Debutant' in french)
        playerLevelName = self.getString(playerLevel)
        
        # TODO: Inform the player in plain text of his/her level change
        # print("{}".format(PROMPT_SIGN_OUT))
        
        # print out the selected player level name in green
        print(PROMPT_SIGN_OUT + "\x1b[32m{}\x1b[0m".format(playerLevelName))
        
        
        
        # DEBUG [4dbsmater]: tell me about it :)
        # print("[_playerLevelHandler]: playerLevel => %s" % playerLevel)
    
    
    def _letterGoodHandler(self, letter):
        """
        Handler that is called whenever the player's given `letter` is good or correct

        :param { str } letter
        """
        
        # NOTE: Do not reduce the player's lives, 'cause he got a letter right

        # Update the `playerLetters` list with the given `letter`
        self._updatePlayerLetters(letter)
        
        # Get the player's word from `hiddenLetters` list
        playerWord = ''.join(self._hiddenLetters)

        # DEBUG [4dbsmaster]: tell me about it :)
        # print("[_letterGoodHandler]: playerWord => ", playerWord)

        # If lowercased `playerWord` is the same as lowercased `randomeWord`...
        if playerWord.lower() == self.randomWord.lower():
            # ...PLAYER HAS WON THE GAME !!!
    
            # Congratulate the player in green
            print("\n\x1b[32m{}\x1b[0m".format(self.getString("congratulations")))

            # show a star
            self.showStar()
            
            # show the results of the game
            self.showGameResults()

            # stop the game
            self.stopGame(True)

            # reset the game
            self.resetGame()

        else:
            # The player still got some lives left, and guessed a letter correctly
            # wait for half a second
            time.sleep(0.5)
            # Inform the player in green
            print("\x1b[32m{} {} {}\x1b[0m".format(EMOJI_CHECK_MARK, \
                    self.getString("good"), EMOJI_THUMBS_UP))

            # wait for 1 second before proceeding
            time.sleep(1)

    
    def _letterBadHandler(self, letter):
        """
        Handler that is called whenever the player's given `letter` is bad or incorrect
        
        :param { str } letter
        """
        
        # If the game is still active and the current lives count is more than 0...
        if self.active and self.currentLivesCount > 0: 
            # ...TAKE A LIFE!!! - Reduce the player's remaining lives by 1
            self.currentLivesCount -= 1
        
        

        # DEBUG [4dbsmaster]: tell me about it :)
        # print("[_letterBadHandler]: letter => ", letter)
        
        # Update the `playerLetters` list with the given `letter`
        self._updatePlayerLetters(letter) 

        # If the playeer has no more lives left ...
        if self.currentLivesCount == 0:
            # ...PLAYER HAS LOST THE GAME !!!

            # Inform the plyaer in red
            print("\n\x1b[31m{}\x1b[0m".format(self.getString("youLost")))

            # show a sad face
            self.showSadFace()

            # show the resuls of the game
            self.showGameResults()

            # stop the game
            self.stopGame(False)

            # reset the game
            self.resetGame()

        else:
            # The player still got some lives left, but didn't guess a letter correctly

            # wait for half a second
            time.sleep(0.5)
            # Inform the player in red
            print("\x1b[31m{} {} {}\x1b[0m".format("X", \
                    self.getString("bad"), EMOJI_THUMBS_DOWN))

            # wait for 1 second before proceeding
            time.sleep(1)


    def _updatePlayerLetters(self, letter):
        """
        Updates the `playerLetters` list with the given `letter`

        :param { str } letter
        """
        
        # Add the given `letter` to the `playerLetters` list
        self.playerLetters.append(letter)
        # Notify the hidden letters of this recent change
        self._notifyHiddenLetters()


    ## --- private getters

    def _getLivesOfLevel(self, level):
        """
        Returns the lives of the given `level`

        :param { str } level
        :return { int } lives
        """

        # TODO: make sure the given `level` is valid before proceeding

        return self.lives[level]
    
    
    

    # PUBLIC METHODS
    
    def showWelcomeMessage(self):
        """
        Displays a welcome message for the current job
        
        :param { str } msg: the message to be displayed
        """
        print("\x1b[2m") # <- everything should be in gray color
        print("=" * 33) # <- top/open style
        #print("#")
        print("# \t  ✺◟(•‿•)◞✺" + "\t\t#")
        print("# \t" + self.getString("welcome") + "\t#")
        # print("#")
        print("=" * 33) # <- bottom/close style
        print("\x1b[0m") # <- stop coloring
      
    
    def showCurrentStatus(self, playerLevel):
        """
        Displays the current status of the player.
        The status will show the number of lives left, letters guessed, and hidden letters.

        :param { str } playerLevel
        """
        # Get the total lives of a player's level as `totalLives`
        # totalLives = self._getLivesOfLevel(playerLevel);

        # Get the current number of lives left as `livesCount`
        livesCount = self.currentLivesCount

        # Get the letters guessed or entered by the player as `letters`
        letters = ' '.join(self.playerLetters)

        # Get the hidden letters as `hiddenLetters`
        hiddenLetters = ' '.join(self._hiddenLetters)

        # Okay, now that we've got all three values...:

        # HACK: adding s to the word "live" if the player has more than one live
        s = 's' if livesCount > 1 else ''
        
        # 1. Tell the player how many lives he/she's got left
        print(PROMPT_SIGN_OUT + self.getString("livesLeft").format(livesCount, s))
        
        # 2. Show the player his/her chosen/guessed letters,
        # However if the player is an 'expert', he/she doesn't need to see this.
        if playerLevel != "expert":
            print(PROMPT_SIGN_OUT + self.getString("lettersGiven").format(letters))
        
        # 3. Show the hidden letters if `playerLevel`
        print("\n" + hiddenLetters + "\n")

        
    def showStar(self):
        """
        Displays a star in ASCII
        """

        # Create an a star
        star = """
              ,
           \  :  /
        `. __/ \__ .'
        _ _\     /_ _
           /_   _\ 
         .'  \ /  `.
           /  :  \  
              '
        """

        # ^^^^^^ Thanks to "Hayley Jane Wakenshaw" - an ascii artist \
        #       from [ASCII ART](https://www.asciiart.eu/ascii-artists)

        # Show the star in green
        print("\x1b[32m%s\x1b[0m" % star)
    
    def showSadFace(self):
        """
        Displays an emoji-like sad face in ASCII
        """

        # Create a sad face
        sadFace = """

             .--------.
           .'          '.
          /   O      O   \ 
         :           `    :
         |           `    | 
         :    .------.    :
          \  '        '  /
           '.          .'
             '-......-'
        
        """ 
        # ^^^^^^^^^ Thanks to "Joan Stark" - an ascii artist \
        #           from [ASCII ART](https://www.asciiart.eu/computers/smileys)

        # Show the sad face in red
        print("\x1b[31m%s\x1b[0m" % sadFace)


    def showGameResults(self, delay = 0.4):
        """
        Displays the game results (i.e. level, tries, word and lives remaining)

        :param { float } delay
        """
        # Create a tuple of the result keys
        resultKeys = (('resultLevel', 'resultTries', 'resultWord', 'resultLives'))
        
        results = {}

        # get the plyers level as `resultLevel`
        results['resultLevel'] = self.getString(self.getPlayerLevel())
        # get the number of attempts as `resultTries`
        results['resultTries'] = self.tries
        # get the random word as `resultWord`
        results['resultWord'] = self.randomWord
        # get the number of lives remaining as `resutLives`
        results['resultLives'] = self.currentLivesCount
        
        print("\x1b[2m+++++ %s +++++\x1b[0m" % self.getString('results'))

        # For each key in `resultKeys`
        for key in resultKeys:
            # get the result
            # result = results[key]
            # if (key == 'level'):
            #    result = self.getString(result)
            # ...print the corresponding result using the `key`
            print("\x1b[2m+ {} --> {}\x1b[0m".format(self.getString(key), results[key]))
            # but wait for 
            time.sleep(delay)
 

    def updatePlayerLevel(self, playerLevel):
        """
        Method used to update the player's level

        :param { str } playerLevel
        """

        # Do nothing if the given `playerLevel` doesn't exist
        if playerLevel not in self.levels:
            return
        
        # set the private `_playerLevel` variable to the given `playerLevel`
        self._playerLevel = playerLevel

        # call the player level handler
        self._playerLevelHandler(playerLevel)



    def requestPlayerLevel(self, speed = 10):
        """
        Prints all currently available levels of the game,
        and prompts the player to pick his/her level from a list.
        
        :param { int } speed
        :return { int } playerLevel
        """
        
        # Initialize the `playerLevel` variable
        playerLevel = 0
         
        # For each level..
        for level in self.levels: 
            # DEBUG [4dbsmaster]: tell me  about it :)
            # print("[requestPlayerLevel]: level => " + level)
            
            # ...get the current level's index
            index = self.levels.index(level)
            # calculate the current level's number by offsetting `index`
            levelIndex = index + 1
            # get the 'real' name of the level in either french or english
            levelName = self.getString(level)
            
            # print the level's `num` & `name` at a given `speed`
            print("\x1b[32m{}\x1b[0m - {}\n".format(levelIndex, levelName))
            
            # compute the delay in milliseconds
            delay = speed / 100 
            time.sleep(delay)
        
        
        # Create a gray-colored hint like [1-3] 
        hint = "\x1b[2m[1-{}]\x1b[0m".format(len(self.levels))
        # Ask the player to pick a level
        playerInput = input("{}{} {} "\
                .format(PROMPT_SIGN_DEFAULT, self.getString("chooseLevel"), hint))
 
        # TODO: Make sure the level picked (i.e. `playerInput`) 
        #       is a number, otherwise handle it!
        
        # DEBUG [4dbsmaster]: tell me about it :)
        # print("[requestPlayerLevel]: playerLevelIndex => " + playerLevelIndex)

        # get the `playerLevel` using the index the player picked
        playerLevel = self.levels[int(playerInput) - 1]

        # Update the player's level
        self.updatePlayerLevel(playerLevel)
        
        # return `playerLevel`
        return playerLevel
    
    
    def startGame(self, defaultLevel = 'beginner', speed = 0.6):
        """
        Method used to start this game
        
        :param { str } defaultLevel: the default player's level
        :param { float } speed
        """
        
        # Get the player's level
        playerLevel = self.getPlayerLevel()

        # Use the `defaultLevel` as `currentLevel` if the `playerLevel` has not been set
        currentLevel = defaultLevel if len(playerLevel) == 0 else playerLevel
        
        # Set the `active` attribute to True
        self.active = True
        
        # Tell the world that the game is about to start, Hooray!!!
        print(self.getString("startingGame"))
        
        # ...print out 50 forward slashes in gray (i.e. "/")
        print("\x1b[2m{}\x1b[0m".format("/" * 50))

        # Load the words
        self._loadWords()
        
        # Update the random word
        self.randomWord = self.getRandomWord(self.caseSensitive)
        
        # Notify the hidden letters
        self._notifyHiddenLetters()

        # Wait for just 50 milliseconds 
        # NOTE: this is not necessary but, "It's a game!!" 
        time.sleep(speed)

        # Now, it's time to use the famous `while` loop 
        # So... while the game is active and the player hasn't found the random word yet
        # Or if the player ain't got no more lives...
        while (self.active and not self.found) or (self.currentLivesCount > 0):
            # ...print out 50 plus signs in gray (i.e. "+")
            print("\x1b[2m{}\x1b[0m".format("+" * 50))

            # then, show the current status of the player
            # TODO: Define a `showCurrentStatus` method
            self.showCurrentStatus(currentLevel)

            # Request a letter from the player as `letter`
            letter = input(PROMPT_SIGN_IN + "%s " % self.getString("chooseLetter"))
           
            # if the game is not case sensitive...
            if self.caseSensitive == False:
                # ...uppercase the `letter`
                letter = letter.upper() # <- NOTE: Not the best-looking code but it works.

            # Update the number of tries
            self.tries += 1

            # Check the letter
            letterIsGood = self._checkLetter(letter)

            # If the letter is good...
            if letterIsGood:
                # ...call the letterGood handler :)
                self._letterGoodHandler(letter)
            else:
                # if not, call the letterBad handler :(
                self._letterBadHandler(letter)
            
            # DEBUG [4dbsmaster]: tell me about it :)
            # print("[startGame](1): letter => %s & tries => %s" % (letter, self.tries))
            # print("[startGame](2): letterIsGood? => ", letterIsGood)

    
    def stopGame(self, found = False):
        """
        Method used to stop this game

        :param { bool } found
        """
        
        # Update the game's `self.found` attribute with the given `found`
        self.found = found
        
        # Stop the game by setting `active` to `False`
        self.active = False

        # TODO: Add a replay feature (e.g. of msg: "Do you wanna play again? (y/N))

    def resetGame(self):
        """
        Method used to reset all the values of the game
        """
        
        # public values
        self.words = []
        self.randomWord = ""
        self.tries = 0
        self.currentLivesCount = 0
        
        
        # private values
        self._playerLevel = ""
        self._hiddenLetters = []


    ## --- public getters

    def getString(self, value):
        """
        Returns the locale string of the given `value`.
        This method is used for localization of the game.
        
        :param { str } value
        :return { str } string
        """
        
        return self.strings[self.lang][value]


    def getPlayerLevel(self):
        """
        Returns the current player's level

        :return { str } playerLevel
        """

        # IDEA: Do something here before returning the `_playerLevel` variable ?

        # return the `_playerLevel`
        return self._playerLevel
   

    def getRandomWord(self, caseSensitive = False):
        """
        Returns a random word

        :param { bool } caseSensitive
        """
        
        # Get the random word from the given `self.words` list only if that 
        # list is not empty; if the `words` list is empty however, 
        # just use an empty string (i.e. '')
        randomWord = random.choice(self.words) if len(self.words) > 0 else ''
        
        # If the game is not case-sensitive and ther's actually a random word...
        if caseSensitive == False and len(randomWord) > 0:
            # ...uppercase all the letters in `randomWord`
            randomWord = randomWord.upper()
        
        # Return the random word
        return randomWord




# ====== END OF PENDUGAME CLASS ===========



# Define our main function
def main():
    """
    The main function of Job01 - Le Pendu
    """

    # Create an object named `pendu` of our `PenduGame`
    pendu = PenduGame(LANG)
    
    # Show a welcome message
    pendu.showWelcomeMessage()
    
    # Request a player level
    pendu.requestPlayerLevel()
    
    # Start the Pendu game
    pendu.startGame()


# if `pendu.py` is being run directly...
if __name__ == "__main__":
    # ...call our main function
    main()
else:
    # do something else :)
    pass


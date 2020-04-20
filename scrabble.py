letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key:value for key,value in (zip(letters, points))}

letters_to_points[" "] = 0

def score_word(word):
    point_total = 0
    for word_letter in word:
        point_total += letters_to_points.get(word_letter.upper(), 0)
    return point_total

brownie_points = score_word("BROWNIE")

player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        print(player)
        for word in words:
            player_points += score_word(word)
        print(player_points)
        player_to_points[player] = player_points

def play_word(player_input, word_input):
    for player in player_to_words.keys():
        if player == player_input:
            player_to_words[player].append(word_input)
    update_point_totals()
    return

play_word('player1','quiz')

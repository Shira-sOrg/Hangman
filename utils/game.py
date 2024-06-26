import typer

def take_guess(player: int, guessed_letters: set) -> str:
    """
    Handle player guess input
    """
    is_valid_guess = False
    guess = ""
    while not is_valid_guess:
        guess = input(f"Player {player + 1}, guess a letter: ").lower()
        if guess in guessed_letters:
            typer.echo("You already guessed that letter!")
        elif len(guess) != 1 or not guess.isalpha():
            typer.echo("Incorrect input, Please guess an alphabetic letter")
        else:
            is_valid_guess = True
    return guess

def enter_num_of_players()->int:
    """
    Handle num of players input
    """
    is_valid_num = False
    num_of_players = 0
    while not is_valid_num:
        try:
            num_of_players = int(input(f"How many players will be playing?"))
            is_valid_num = True
        except:
              typer.echo("Incorrect input, Please enter the number of players that will be playing")
              
    return num_of_players            

def handle_guess(player: int, guessed_letters: set, players: list[int:dict[str:str|int]], word_indices: dict[str:list[int]], guess: str, guessed_word: list[str]) -> str:
    """
    Determine if player guess is correct or not
    """
    guessed_letters.add(guess)
    if word_indices.get(guess):
        players[player]["score"] += len(word_indices[guess])
        for i in word_indices[guess]:
            guessed_word[i] = guess
        typer.echo("Correct guess!")
    else:
        typer.echo("Incorrect guess!")
    return guessed_word

def display_score(players: list[int:dict[str:str|int]]):
    """
    Display the final score of the game
    """
    winner_score = max(player["score"] for player in players)
    winner_names = []
    for player in players:
        if player["score"] == winner_score:
            winner_names.append(player["name"])
        typer.echo(f"{player["name"]}: {player["score"]} points")
    
    for winner in winner_names:
        typer.echo(f"{winner} Won!")
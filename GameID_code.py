# Function to search for a deal by game ID
def search_by_game_id(game_id, deals):
    for deal in deals:
        # Searching whether the game ID matches the ID entered by the user
        if str(deal["gameID"]) == game_id:
            return deal  # Returns this particular deal
    return None  # Returns nothing if the game ID was not found in the deals

        elif choice == '3':
            print("Random Games with Game ID:")
            random.shuffle(deals)  # Displays random examples for Game IDs
            for _ in range(5): # Five game examples are given
                deal = random.choice(deals)  # Selects a random deal
                print("Game ID:", deal["gameID"])
            
            game_id = input("Enter the game ID: ")
            game = search_by_game_id(game_id, deals)
            
            if game:
                print("Game Title:", game["title"])
                print("Deal ID:", game["dealID"])
                print("Game ID:", game["gameID"])
                print("Normal Price:", game["normalPrice"])
                print("Deal Price:", game["salePrice"])
                print("-" * 30)
            else:
                print("Game not found.")
        
import requests
import random

def game_deals():                   #API GET code
    url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        deals = response.json()[:5]  # Get the first 5 deals
        for deal in deals:
            title = deal["title"]
            normal_price = deal["normalPrice"]
            deal_price = deal["salePrice"]

            print("Game Title:", title)  # Sorting Json file to receive only relevant info
            print("Normal Price:", normal_price)
            print("Deal Price:", deal_price)
            print("-" * 30)
    else:
        print("Failed to retrieve game deals. Status code:", response.status_code)

# Function to search for matching deals by game name
def search_by_name(game_name, deals):
    matching_deals = []
    for deal in deals:
        #If the game name provided by the user (ignoring uppercase/lowercase because the next line code will convert any typed text in lower text and it will compare with the game in the deals) is in the deal's title
        if game_name.lower() in deal["title"].lower():
            matching_deals.append(deal)  # This will add to the list of matching deals
    return matching_deals  # Return the list of matching deals

# Function to search for a deal by game ID
def search_by_game_id(game_id, deals):
    for deal in deals:
        # Searching whether the game ID matches the ID entered by the user
        if str(deal["gameID"]) == game_id:
            return deal  # Returns this particular deal
    return None  # Returns nothing if the game ID was not found in the deals
        

# This function allows to search for a deal between a chosen price range
def search_by_cost(min_price, max_price, deals):
    while True:
        min_price_input = input("Enter the minimum price: ") # Gives search tab for minimum price
        max_price_input = input("Enter the maximum price: ") # Gives search tab for maximum price
        
        try:
            min_price = float(min_price_input)  
            max_price = float(max_price_input)  
            break  # Exit the loop if conversion was successful
        except ValueError:
            print("Invalid input. Please enter valid numeric prices.") # This makes sure that the user enters a number in both search tabs
    
    matching_deals = []
    for deal in deals:
        normal_price = float(deal["salePrice"])  # Gives the sale price of the deal
        if min_price <= normal_price <= max_price:  # Equation to give products only in the user's specified price range
            matching_deals.append(deal)  # This adds the given deal to the output (Terminal)
    return matching_deals  # This gets the user back to all the possible products in the specified price range
    

def main():                 #Options for the user to choose from
    while True:
        print("Please choose one from the following:")
        print("1. Game deals")
        print("2. Search by name")
        print("3. Search by game ID")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            game_deals()
        elif choice == '2':
            print("Random Games with Game Name:")
            random.shuffle(deals)  # Gives some examples for random games
            for _ in range(5): #The maximun number of games that will show will be 5.
                deal = random.choice(deals)  # Select a random deal
                print("Game Name:", deal["title"])
            
            game_name = input("Enter the game name: ") #game_name will catch the name typed by the user.
            matching_deals = search_by_name(game_name, deals) #The game_name will be passed as a parameter to the function search_by_name to see the matching results.
            
            if len(matching_deals) == 0:
                print("No matching deals found.") #This will come out if any matching games was found
            else:
                for deal in matching_deals:
                    print("Game Title:", deal["title"])
                    print("Deal ID:", deal["dealID"])
                    print("Game ID:", deal["gameID"])
                    print("Normal Price:", deal["normalPrice"])
                    print("Deal Price:", deal["salePrice"])
                    print("-" * 30)
                    
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

        
        elif choice == '4': # The specified choice
            deals = fetch_game_deals() # Fetches game deals
            min_price = None 
            max_price = None
            
            while min_price is None or max_price is None:
                matching_deals = search_by_cost(min_price, max_price, deals)
                if len(matching_deals) == 0: # Looks if there are actual deals, corresponding to the specified price range
                    print("No matching deals found.")
                else:
                    for deal in matching_deals:
                        print("Game Title:", deal["title"])
                        print("Deal ID:", deal["dealID"])
                        print("Game ID:", deal["gameID"])
                        print("Normal Price:", deal["normalPrice"])
                        print("Deal Price:", deal["salePrice"])
                        print("-" * 30)
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

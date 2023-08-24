import requests

def game_deals():                   #API GET code
    url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        deals = response.json()[:3]  # Get the first 3 deals
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

        elif choice == '2':
            print("Random Games with Game Name:")
            random.shuffle(deals)  # Gives some examples for random games
            for _ in range(5): #The maximun number of games that will show will be 5.
                deal = random.choice(deals)  # Select a random deal
                print("Game Name:", deal["title"])
            
            game_name = input("Enter the game name: ")
            matching_deals = search_by_name(game_name, deals)
            
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

def search_by_game_id():
    game_id = input("Enter the game ID: ")
    

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
            search_by_name()
        elif choice == '3':
            search_by_game_id()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

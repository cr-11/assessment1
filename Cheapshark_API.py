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

def search_by_name():
    name = input("Enter the game name: ")
   

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

#!/opt/homebrew/bin/python3
from cards import create_deck
import time

def pick_and_display_card():
    deck = create_deck()
    
    try:
        card_index = int(input("Pick a card number (1-52): "))
        if card_index < 1 or card_index > 52:
            raise ValueError("Card number must be between 1 and 52.")
        
        selected_card = deck[card_index - 1]  # Subtract 1 to match zero-based indexing
        print(f"The selected card is: {selected_card}")
        time.sleep(5)  # Display the card for 5 seconds
        print("\nCard display finished!")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    pick_and_display_card()

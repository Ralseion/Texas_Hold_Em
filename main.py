import random

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
symbols = ["♣", "♦", "♥", "♠"]
deck_dict = {}
deck = []


def create_deck():
    for card, value in cards.items():
        for symbol in symbols:
            deck_dict[card + symbol] = value
            deck.append(card + symbol)
    random.shuffle(deck)


def start_game():
    user.start_hand()
    player_2.start_hand()
    player_3.start_hand()
    player_4.start_hand()
    dealer.start_hand()
    dealer.draw_card()


def show_the_board():
    user.reveal_hand()
    player_2.reveal_hand()
    player_3.reveal_hand()
    player_4.reveal_hand()
    dealer.reveal_hand()
    draw_line()


def hand_change():
    user.change_cards(user_choice)
    player_2.change_cards("3")
    rand_choice = random.randint(1, 4)
    player_3.change_cards(str(rand_choice))
    player_4.change_cards("4")


def draw_line():
    print("===================================")


def reset():
    global deck
    deck = []
    user.clear_hand()
    player_2.clear_hand()
    player_3.clear_hand()
    player_4.clear_hand()
    dealer.clear_hand()


def type_of_hand(score, high_card, name):
    if score == 1:
        print(f"{name}'s high card is {high_card}.")
    elif score == 2:
        print(f"{name} got one pair.")
    elif score == 3:
        print(f"{name} got two pairs.")
    elif score == 4:
        print(f"{name} got a three of a kind.")
    elif score == 5:
        print(f"{name} got a straight!")
    elif score == 6:
        print(f"{name} got a flush!")
    elif score == 7:
        print(f"{name} got a full house!")
    elif score == 8:
        print(f"{name} got a four of a kind!")
    elif score == 9:
        print(f"{name} got a straight flush!")
    elif score == 10:
        print(f"{name} got a royal flush!!!!!")


def show_all_scores():
    draw_line()
    type_of_hand(user.score, user.high_card, user.name)
    type_of_hand(player_2.score, player_2.high_card, player_2.name)
    type_of_hand(player_3.score, player_3.high_card, player_3.name)
    type_of_hand(player_4.score, player_4.high_card, player_4.name)


def compare_scores(p1, p2, p3, p4):
    lst = [p1, p2, p3, p4]
    big_num = max(lst)
    if lst.count(big_num) == 1:
        if p1 == big_num:
            print(f"{user.name} is the winner!")
        elif p2 == big_num:
            print(f"{player_2.name} is the winner!")
        elif p3 == big_num:
            print(f"{player_3.name} is the winner!")
        else:
            print(f"{player_4.name} is the winner!")
    else:
        print("It's a draw.")


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.final_hand = []
        self.high_card = ""

    def __repr__(self):
        return f"""Name: {self.name}
Hand: {self.hand}
Final Hand: {self.final_hand}"""

    def draw_card(self):
        self.hand.append(deck.pop(0))

    def start_hand(self):
        self.draw_card()
        self.draw_card()

    def reveal_hand(self):
        if self.name != "Dealer":
            print(f"{self.name}'s hand: [{self.hand[0]}] [{self.hand[1]}]")
        else:
            if len(self.hand) == 3:
                print(f"Cards dealt out so far: [{self.hand[0]}] [{self.hand[1]}] [{self.hand[2]}]")
            elif len(self.hand) == 4:
                print(f"Cards dealt out so far: [{self.hand[0]}] [{self.hand[1]}] [{self.hand[2]}] [{self.hand[3]}]")
            elif len(self.hand) == 5:
                print(f"Final cards: [{self.hand[0]}] [{self.hand[1]}] [{self.hand[2]}] [{self.hand[3]}] "
                      f"[{self.hand[4]}]")

    def clear_hand(self):
        self.hand = []

    def change_cards(self, choice):
        if choice == "1":
            self.hand.pop(0)
            self.draw_card()
        elif choice == "2":
            self.hand.pop(1)
            self.draw_card()
        elif choice == "3":
            self.clear_hand()
            self.start_hand()
        else:
            pass

    def get_score(self, dealer_hand):
        self.score = 0
        temp_hand = self.hand + dealer_hand
        temp_hand.sort()
        main_hand = []
        extra_hand = []
        suit = []
        value = []
        counter = []
        index = []

        # Hand is now sorted by 10, 2-9, A, K, J, Q, so adding some custom sorting, I have not figured out
        # quite how to do this without a bunch of for loops yet
        for card in temp_hand:
            if card[0] == "1":
                extra_hand.append(card)
        for card in temp_hand:
            if card[0] == "J":
                extra_hand.append(card)
        for card in temp_hand:
            if card[0] == "Q":
                extra_hand.append(card)
        for card in temp_hand:
            if card[0] == "K":
                extra_hand.append(card)
        for card in temp_hand:
            if card[0] == "A":
                extra_hand.append(card)
        for card in temp_hand:
            if card not in extra_hand:
                main_hand.append(card)
        self.final_hand = main_hand + extra_hand
        for card in self.final_hand:
            if card[0] == 1:
                value.append("10")
            else:
                value.append(deck_dict[card])
                suit.append(card[-1])
        flush_check = sorted(suit)
        self.high_card = self.final_hand[-1]
        # check for straight
        counter.append(value[0])
        index.append(suit[0])
        for i in range(len(value)):
            if value[i] == counter[-1] + 1:
                counter.append(value[i])
                index.append(suit[i])
            elif value[i] == counter[-1] or len(counter) == 5:
                pass
            else:
                counter = [value[i]]
                index = [suit[i]]
        # check for straight flush
        if len(counter) == 5:
            self.score = 5
            check = ""
            for suit in flush_check:
                if len(check) == 5:
                    pass
                elif suit not in check:
                    check += suit
                else:
                    check = suit
            if len(check) == 5:
                self.score = 9
                # check for royal
                if 14 in value and 13 in value and 12 in value and 11 in value and 10 in value:
                    self.score = 10
        # check for normal flush
        check = ""
        for suit in flush_check:
            if len(check) == 5:
                pass
            elif suit not in check:
                check = suit
            else:
                check += suit
        if len(check) == 5 and 6 > self.score:
            self.score = 6
        # check for card pairings
        count_dict = {}
        for num in cards.values():
            if num in value:
                count_dict[num] = value.count(num)
        # Four of a kind
        if 4 in count_dict.values() and self.score < 8:
            self.score = 8
        # Full house
        if 3 in count_dict.values() and 2 in count_dict.values() and self.score < 7:
            self.score = 7
        # Three of a kind
        if 3 in count_dict.values() and self.score < 4:
            self.score = 4
        # Two pair and less
        pair = 0
        for i in count_dict.values():
            if i == 2:
                pair += 1
        if pair >= 2 and self.score < 3:
            self.score = 3
        elif pair == 1 and self.score < 2:
            self.score = 2
        if self.score < 2:
            self.score = 1


user_name = input("Welcome to Texas Hold Em. Please enter your name: ")
user = Player(user_name)
player_2 = Player("Stinky Pete")
player_3 = Player("Dirty Dan")
player_4 = Player("Pinhead Larry")
dealer = Player("Dealer")
game = True

while game:
    create_deck()
    start_game()
    show_the_board()
    user_choice = input("Type 1 to change your 1st card, 2 to change your 2nd, 3 to change both, or anything else "
                        "to keep: ")
    hand_change()
    dealer.draw_card()
    show_the_board()
    dealer.draw_card()
    show_the_board()
    user.get_score(dealer.hand)
    player_2.get_score(dealer.hand)
    player_3.get_score(dealer.hand)
    player_4.get_score(dealer.hand)
    show_all_scores()
    compare_scores(user.score, player_2.score, player_3.score, player_4.score)
    draw_line()
    go_again = input("Would you like to play again? 1 for yes, anything else for no: ")
    if go_again == "1":
        game = True
        reset()
        draw_line()
        draw_line()
    else:
        game = False
        draw_line()
        print("Thank you for playing!")





import random
suits = ('Hearts', 'Diamonds', 'Spade', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight','Nine', 'jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'jack':10, 'Queen':11, 'King':11, 'Ace':11}

playing = True

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	
	def __str__(self):
		return self.rank + ' Of ' +  self.suit


class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' + card.__str__()
			return "The Deck has: "+ deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card


class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0
	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]
	
	def adjust_for_ace(self):
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -= 1

class Chips:
	def __init__(self, total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many Chips would you like to bet ??:::"))
		except:
			print("Sorry, a bet must be  an integer")	
		else:
			if chips.bet > chips.total:
				print("Sorry, You dont have too much chips. You have{}".format(chips.total))
			else:
				break


def hit(deck, hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()


def hit_or_stand(deck, hand):
	global playing
	while True:
		x = input("Hit or Stand? Enter h or s !!!!")
		if x[0].lower() =='h':
			hit(deck, hand)
		elif x[0].lower() == 's':
			print("Player Stand !! Now Dealers's Turn !")
			playing = False
		else:
			print('Sorry, I did no undestand that, Please enter h or s !!! ')
			continue
		break


def show_some(player, dealer):
	print("Dealer Hand!! One card Hidden")
	print(dealer.cards[1])
	print('\n')
	print("Player Hand")
	for card in player.cards:
		print(card)

	
def show_all(player,dealer):
	print('\n')
	print("Dealers's Hand!! ")
	for card in dealer.cards:
		print(card)
	print('\n')
	print("Player Hand")
	for card in player.cards:
		print(card)
	print('\n')


def player_busts(player, dealer, chips):
    print("Bust PLayer!!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins!!!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer Bust Player Wins !!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!!!")
    chips.lose_bet()

def push(player, dealer):
    print("Match Tie!!!")


while True:
	print("Welcome to Black Jack Game !!")
	# Creat and Shuffle the deck, deal two cards to each Player
	deck = Deck()
	deck.shuffle()
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Set up Player's Chips
	player_chips = Chips()
	
	# Prompt the player for their bet
	take_bet(player_chips)
	# Show cards (but keep on dealer card hidden)
	show_some(player_hand, dealer_hand)

	while playing:
		hit_or_stand(deck, player_hand)
		# Show cards (but keep on dealer card hidden)
		show_some(player_hand, dealer_hand)
	  # If Plyaer hasn't excees 21, run player_butst()

		if player_hand.value > 21:
			player_busts(player_hand, dealer_hand, player_chips)
			break
		# if Player hsn't busted dealterd rached 17
		if player_hand.value <= 21:
			while dealer_hand.value < player_hand.value:
				hit_or_stand(deck, dealer_hand)
				# Show all cards
				show_all(player_hand, dealer_hand)

				# Run different winning scenerios
				if player_hand.value > 21:
					dealer_busts(player_hand, dealer_hand, player_chips)
				elif dealer_hand.value > player_hand.value:
					dealer_wins(player_hand, dealer_hand, player_chips)
				elif dealer_hand.value < player_hand.value:
					player_wins(player_hand, dealer_hand, player_chips)
				else:
					push(player_hand, dealer_hand)
	# inform Player of their chips total
	print("\nPlayer Total chips are :{}".format(player_chips.total))
	# Ask to Play again
	new_game = input("would you like to play agian: ")
	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thanks for Particapting in GAme!!!")
		break


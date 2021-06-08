# init blockchain list
blockchain = []


def get_last_blockchain_value():
	"""Returns last value of the blockchain"""
	return blockchain[-1]


def add_Value(transaction_amount, last_transaction_value=[1]):
	"""Appends a new value into the blockchain and prints the current
       values of the blockchain
	"""
	blockchain.append([last_transaction_value, transaction_amount])
	print(blockchain)


def get_user_input():
	"""User adds a number to add to the blockchain"""
	return float(input("Enter your transaction amount here: "))


tx_amount = get_user_input()
add_Value(tx_amount)

tx_amount = get_user_input()
add_Value(tx_amount)

tx_amount = get_user_input()
add_Value(tx_amount)


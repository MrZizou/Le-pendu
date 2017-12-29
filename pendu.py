# -*- coding:utf-8 -*-

# The game language is in french !
# Author: Zizou
# Created on 22 December 2017, at 10:20pm.

import os
import sys
import time
import logging as lg

from random import randrange

def main():
	# Store the random word in a variable.
	word_to_find = get_random_word_in(load_file('words.txt'))

	print('Bienvenue au jeu du Pendu !')

	startedTime = time.time()
	play_game(word_to_find)

	totalTime = round(time.time() - startedTime, 2)

	print('Il vous a fallut %s secondes pour trouver le mot secret.'\
		% totalTime)

def load_file(path_to_file) -> list:
	""" Give a text file and return a list.

	Open the file that contains the words and add 
	each word to the list and return it at the end.
	"""
	if not os.path.exists(path_to_file):
		lg.critical('The file %s doesn\'t exist !' % path_to_file)
		sys.exit()

	file = open(path_to_file, 'r')
	words = [word for word in file.read().split('\n') if len(word) > 1]
	file.close()

	return words

# Return a random word from a list.
def get_random_word_in(words_list) -> str:
	rand_num = randrange(len(words_list))
	rand_word = words_list[rand_num]

	return rand_word

def play_game(word_to_find, chances = 10):
	score = chances
	string_hidden = hide_string(word_to_find)

	while score != 0:
		print('\nQuel est le mot ? %s' % string_hidden)
		print('Proposez une lettre:', end = ' ')
		user_char = str(input()).upper()

		if len(user_char) > 1:
			print('\nVeuillez saisir seulement un caractère.')
			continue

		# Convert the string into list.
		string_hidden_list = list(string_hidden)

		if user_char in word_to_find:
			char_indexes = []

			for i in range(len(word_to_find)):
				# Create an empty list and add each index one by one.
				if user_char == word_to_find[i]:
					char_indexes.append(i)
					
			for j in char_indexes:
				string_hidden_list[j] = user_char
		else:
			score -= 1
			print('\nIl vous reste %s essais.' % score)
			
		# Convert the list of characters into a string.
		string_hidden = ''.join(string_hidden_list)

		if string_hidden == word_to_find:
			print('\nBravo ! Le mot caché était bien: %s'\
				% word_to_find)
			break

	if score == 0:
		print('\nPerdu ! Le mot caché était: %s' % word_to_find)
		sys.exit()

	print('Votre score: <%s/%s>' % (score, chances))

# Get the hidden word.
def hide_string(word_to_find) -> str:
	return '*' * len(word_to_find)

if __name__ == '__main__':
	main()

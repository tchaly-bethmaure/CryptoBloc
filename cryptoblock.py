#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import hashlib

# NOTE :
# 1) Ce script peu peut-être marcher avec du texte UNICODE
# 2) l'encryption par bloc n'a pas été faite par flemme mais elle est faisable
# facilement.
# 3) je n'ai pas bien compris l'encryption par bloque donc je ne sait pas si la 
# clef doit être découpée elle aussi en fonction des blocs ou s'il faut en générer
# une par bloc. La seconde proposition d'après mes connaissances sur le sujet m'a 
# l'air meilleurs en terme de sécuritée mais moins optimale en terme de perf.

def encrypt_bloc(text, key):
	# On prépare notre encryption pour qu'elle soit faite octet par octet
	tab_of_char = []
	for c in text:
		tab_of_char.append(c)
	tab_of_key_char = []
	for c in key:
		tab_of_key_char.append(c)
	# On encrypte
	tab_encrypte = []
	for i in range(len(tab_of_char)):
		tab_encrypte.append(chr(ord(tab_of_char[i])^ord(tab_of_key_char[i])))
	return ''.join(tab_encrypte)
	


mon_text_a_encrypter = u"MonSuperTextSupraLongavecdeséééééetdesààààà"
ma_super_clef = random.getrandbits(2048)

sha = hashlib.sha512()
sha.update(str(ma_super_clef))
ma_clef = sha.digest()

text_crypte = encrypt_bloc(mon_text_a_encrypter, ma_clef)
text_decrypte = encrypt_bloc(text_crypte, ma_clef)
print(text_decrypte)
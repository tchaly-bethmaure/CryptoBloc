#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import hashlib
import math

# NOTE :
# 1) il reste à développer le cipher et faire marcher le tout.

def xor(bloc_text, iv):
	# On prépare notre encryption pour qu'elle soit faite octet par octet
	tab_of_char = []
	for c in bloc_text:
		tab_of_char.append(c)
	tab_of_key_char = []
	for c in iv:
		tab_of_key_char.append(c)
	# On encrypte
	tab_encrypte = []
	for i in range(len(tab_of_char)):
		tab_encrypte.append(chr(ord(tab_of_char[i])^ord(tab_of_key_char[i])))
	return ''.join(tab_encrypte)
	
def decoupage_par_bloc(text, taille_bloc):
	if(taille_bloc > len(text)):
		print("Le découpage n'est pas possible sans rajout de bloc fictif (option à rajouter si amélioration demandée).")
		exit()
	else:
		bloc_de_text = []
		nombre_de_bloc = int(math.floor(len(text)/taille_bloc))
		curseur_debut_bloc = 0
		curseur_fin_bloc = taille_bloc
		for index_bloc in range(nombre_de_bloc):
			bloc_de_text.append(text[curseur_debut_bloc:curseur_fin_bloc])
			temp = curseur_fin_bloc
			curseur_debut_bloc = curseur_fin_bloc
			curseur_fin_bloc += taille_bloc
		return bloc_de_text


def decoupage_par_bloc_de_n_bit(text, taille_bloc_en_bit):
	newText = "";
	for c in text:
		newText += bin(ord(c))
	text = newText
	if(taille_bloc_en_bit > len(text)):
		print("Le découpage n'est pas possible sans rajout de bloc fictif (option à rajouter si amélioration demandée).")
		exit()
	else:
		bloc_de_text = []
		nombre_de_bloc = int(math.floor(len(text)/taille_bloc_en_bit))
		curseur_debut_bloc = 0
		curseur_fin_bloc = taille_bloc_en_bit
		for index_bloc in range(nombre_de_bloc):
			bloc_de_text.append(text[curseur_debut_bloc:curseur_fin_bloc])
			temp = curseur_fin_bloc
			curseur_debut_bloc = curseur_fin_bloc
			curseur_fin_bloc += taille_bloc_en_bit
		return bloc_de_text

mon_text_a_encrypter = u"MonSuperTextSupraLongavecdeséééééetdesààààà"
#decoupage_par_bloc(mon_text_a_encrypter, 4)
print(decoupage_par_bloc_de_n_bit(mon_text_a_encrypter, 8))
# iv = random.getrandbits(2048)

# sha = hashlib.sha512()
# sha.update(str(ma_super_clef))
# ma_clef = sha.digest()

# text_crypte = encrypt_bloc(mon_text_a_encrypter, ma_clef)
# text_decrypte = encrypt_bloc(text_crypte, ma_clef)
# print(text_decrypte)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import hashlib
import math
from Crypto.Cipher import AES
import os

def encryption(text, clef, iv):
	mon_objet_d_encryption = AES.new(clef, AES.MODE_CBC, iv)
	return mon_objet_d_encryption.encrypt(text)

def decryption(text, clef, iv):
	mon_object_de_decryption = AES.new(clef, AES.MODE_CBC, iv)
	return mon_object_de_decryption.decrypt(text)

def xor(bloc_text, vecteur):
	# On prépare notre encryption pour qu'elle soit faite octet par octet
	tab_of_char = []
	for c in bloc_text:
		tab_of_char.append(c)
	# On xor
	tab_encrypte = []
	for i in range(len(tab_of_char)):
		tab_encrypte.append(chr(ord(tab_of_char[i])^vecteur))
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

mon_text_a_encrypter = u"MonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongueMonSuperTextSupraLongue"
ma_clef_dencryption = os.urandom(32)
ma_clef_de_decriptage = os.urandom(32)
iv = os.urandom(16)

print("############################# ENCRYPT ################################")

mes_blocs = decoupage_par_bloc(mon_text_a_encrypter, len(ma_clef_dencryption))
mes_blocs_encryptes = []
# On encrypte par bloc :
for bloc in mes_blocs:
	cipher_text = encryption(bloc, ma_clef_dencryption, iv)
	mes_blocs_encryptes.append(cipher_text)
print(''.join(mes_blocs_encryptes))

print("############################# DECRYPT ################################")

mes_blocs_decryptes = []
for bloc in mes_blocs_encryptes:
	cipher_text = decryption(bloc, ma_clef_dencryption, iv)
	mes_blocs_decryptes.append(cipher_text)
print(''.join(mes_blocs_decryptes))
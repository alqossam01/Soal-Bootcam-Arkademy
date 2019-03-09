#Soal Nomor 2 By Izzuddin Adam M.A @Arkademy
import re  #Memasukan function regular expression 
pola = "^(?=.*[a-z])(?=.*\d)[a-z\d]{8,}$" 	#pattern atau syarat untuk menginput password
password = raw_input("Masukan Password : ") #input password
result = re.findall(pola, password)			#mengumpulkan hasil dari sebuah inputan
if (result):
    print "Password Anda Valid"				#kondisi benar jika password sesuai syarat
else:
    print "Password Anda Tidak Valid !"		#kondisi salah jika password tidak sesuai syarat

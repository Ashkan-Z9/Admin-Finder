import urllib.request
import platform
import sys
from datetime import datetime
import os

systemOS = platform.system()
systemName = platform.node()

def ex():
  ex = input("\n\nPress [ENTER] to Exit...")
  if ex == "":
    sys.exit()

def time():
	hour = datetime.now() .hour
	minute = datetime.now() .minute
	second = datetime.now() .second
	print("STARTED IN " + str(hour) + ':' + str(minute) + ':' + str(second) + '\n')

words = [
	'admin/',
	'administrator/',
	'admin1/',
	'admin3/',
	'admin4/',
	'admin5/',
	'usuarios',
	'usuario/',
	'moderator',
	'webadmin/',
	'adminarea/',
	'bb-admin/',
	'cpanel',
	'adminLogin/',
	'admin_area/',
	'panel-administracion/',
	'instadmin/',
	'memberadmin/',
	'administratorlogin/',
	'adm/',
	'admin/account.php',
	'admin/index.php',
	'admin/login.php',
	'admin/admin.php',
	'admin_area/admin.php',
	'admin_area/login.php',
	'siteadmin/login.php',
	'siteadmin/index.php',
	'siteadmin/login.html',
	'admin/account.html',
	'admin/index.html',
	'admin/login.html',
	'admin/admin.html',
	'admin_area/index.php',
	'bb-admin/index.php',
	'bb-admin/login.php',
	'bb-admin/admin.php',
	'admin/home.php',
	'admin_area/login.html',
	'admin_area/index.html',
	'admin/controlpanel.php',
	'admin.php',
	'admincp/index.asp',
	'admincp/login.asp',
	'admincp/index.html',
	'adminpanel.html',
	'webadmin.html',
	'webadmin/index.html',
	'webadmin/admin.html',
	'webadmin/login.html',
	'admin/admin_login.html',
	'admin_login.html',
	'panel-administracion/login.html',
	'admin/cp.php',
	'cp.php',
	'administrator/index.php',
	'administrator/login.php',
	'nsw/admin/login.php',
	'webadmin/login.php',
	'admin/admin_login.php',
	'admin/admin_login.php',
	'administrator/account.php',
	'administrator.php',
	'admin_area/admin.html',
	'pages/admin/admin-login.php',
	'admin-login.php',
	'bb-admin/index.html',
	'bb-admin/login.html',
	'acceso.php',
	'bb-admin/admin.html',
	'admin/home.html',
	'login.php',
	'modelsearch/login.php',
	'moderator.php',
	'moderator/login.php',
	'moderator/admin.php',
	'account.php',
	'pages/admin/admin-login.html',
	'admin/admin-login.html',
	'admin-login.html',
	'controlpanel.php',
	'admincontrol.php',
	'admin/adminLogin.html',
	'adminLogin.html',
	'home.html',
	'rcjakar/admin/login.php',
	'moderator/admin.php',
	'account.php',
	'pages/admin/admin-login.html',
	'admin/admin-login.html',
	'admin-login.html',
	'controlpanel.php',
	'admincontrol.php',
	'admin/adminLogin.html',
	'admin-login.html',
	'controlpanel.php',
	'admincontrol.php',
	'admin/adminLogin.html',
	'adminLogin.html',
	'administrator/index.html',
	'administrator/login.html',
	'user.html',
	'administrator/account.html',
	'administrator.html',
	'login.html',
	'modelsearch/login.html',
	'moderator/login.html',
	'adminarea/login.html',
	'panel-administracion/index.html',
	'panel-administracion/admin.html',
	'modelsearch/index.html',		
	'modelsearch/admin.html',
	'admincontrol/login.html',
	'adm/index.html',
	'adm.html',
	'moderator/admin.html',
	'user.php',
	'account.html',
	'controlpanel.html',		
	'admincontrol.html',
	'panel-administracion/login.php',
	'wp-login.php',
	'adminLogin.php',
	'admin/adminLogin.php',
	'home.php',
	'adminarea/index.php',
	'adminarea/admin.php',
	'adminarea/login.php',
	'panel-administracion/index.php',
	'panel-administracion/admin.php',
	'modelsearch/index.php',
	'modelsearch/admin.php',
	'admincontrol/login.php',
	'adm/admloginuser.php',
	'admloginuser.php',
	'admin2.php',
	'admin2/login.php',
	'admin2/index.php',
	'usuarios/login.php',
	'adm/index.php',
	'adm.php',
	'affiliate.php',
	'adm_auth.php',
	'memberadmin.php',
	'administratorlogin.php',
	'account.asp',
	'admin/account.asp',
	'admin/index.asp',
	'admin/login.asp',
	'admin/admin.asp',
	'admin_area/admin.asp',
	'admin_area/login.asp',
	'admin_area/index.asp',
	'bb-admin/index.asp',
	'bb-admin/login.asp',
	'bb-admin/admin.asp',
	'admin/home.asp',
	'admin/controlpanel.asp',
	'admin.asp',
	'pages/admin/admin-login.asp',
	'admin/admin-login.asp',
	'admin-login.asp',
	'admin/cp.asp',
	'cp.asp',
	'administrator/account.asp',
	'administrator.asp',
	'acceso.asp',
	'login.asp',
	'modelsearch/login.asp',
	'moderator.asp',
	'moderator/login.asp',
	'administrator/login.asp',
	'moderator/admin.asp',
	'controlpanel.asp',
	'user.asp',
	'admincontrol.asp',
	'adminpanel.asp',
	'webadmin.asp',
	'webadmin/index.asp',
	'webadmin/admin.asp',
	'webadmin/login.asp',
	'admin/admin_login.asp',
	'admin_login.asp',
	'panel-administracion/login.asp',
	'adminLogin.asp',
	'admin/adminLogin.asp',
	'home.asp',
	'adminarea/index.asp',
	'adminarea/admin.asp',
	'adminarea/login.asp',
	'panel-administracion/index.asp',
	'panel-administracion/admin.asp',
	'modelsearch/index.asp',
	'modelsearch/admin.asp',
	'administrator/index.asp',
	'admincontrol/login.asp',
	'adm/admloginuser.asp',
	'admloginuser.asp',
	'admin2.asp',
	'admin2/login.asp',
	'admin2/index.asp',
	'adm/index.asp',
	'adm.asp',
	'affiliate.asp',
	'adm_auth.asp',
	'memberadmin.asp',
	'administratorlogin.asp',
	'siteadmin/login.asp',
	'siteadmin/index.asp',
	'admin/account.cfm',
	'admin/index.cfm',
	'admin/login.cfm',
	'admin/admin.cfm',
	'admin_area/admin.cfm',
	'admin_area/login.cfm',
	'siteadmin/login.cfm',
	'siteadmin/index.cfm',
	'admin_area/index.cfm',
	'bb-admin/index.cfm',
	'bb-admin/login.cfm',
	'bb-admin/admin.cfm',
	'admin/home.cfm',
	'admin/controlpanel.cfm',
	'admin.cfm',
	'admin/cp.cfm',
	'cp.cfm',
	'administrator/index.cfm',
	'administrator/login.cfm',
	'nsw/admin/login.cfm',
	'webadmin/login.cfm',
	'admin/admin_login.cfm',
	'admin_login.cfm',
	'administrator/account.cfm',
	'administrator.cfm',
	'pages/admin/admin-login.cfm',
	'admin/admin-login.cfm',
	'admin-login.cfm',
	'login.cfm',
	'modelsearch/login.cfm',
	'moderator.cfm',
	'moderator/login.cfm',
	'moderator/admin.cfm',
	'account.cfm',
	'controlpanel.cfm',
	'admincontrol.cfm',
	'acceso.cfm',
	'rcjakar/admin/login.cfm',
	'webadmin.cfm',
	'webadmin/index.cfm',
	'webadmin/admin.cfm',
	'adminpanel.cfm',
	'user.cfm',
	'panel-administracion/login.cfm',
	'wp-login.cfm',
	'adminLogin.cfm',
	'admin/adminLogin.cfm',
	'home.cfm',
	'adminarea/index.cfm',
	'adminarea/admin.cfm',
	'adminarea/login.cfm',
	'panel-administracion/index.cfm',
	'panel-administracion/admin.cfm',
	'modelsearch/index.cfm',
	'modelsearch/admin.cfm',
	'admincontrol/login.cfm',
	'adm/admloginuser.cfm',
	'admloginuser.cfm',
	'admin2.cfm',
	'admin2/login.cfm',
	'admin2/index.cfm',
	'usuarios/login.cfm',
	'adm/index.cfm',
	'adm.cfm',
	'affiliate.cfm',
	'adm_auth.cfm',
	'memberadmin.cfm',
	'administratorlogin.cfm',
	'admin/account.js',
	'admin/index.js',
	'admin/admin.js',
	'admin_area/admin.js',
	'admin_area/login.js',
	'siteadmin/login.js',
	'siteadmin/index.js',
	'admin_area/index.js',
	'bb-admin/index.js',
	'bb-admin/login.js',
	'bb-admin/admin.js',
	'admin/home.js',
	'admin/controlpanel.js',
	'admin.js',
	'admin/cp.js',
	'cp.js',
	'administrator/index.js',
	'administrator/login.js',
	'nsw/admin/login.js',
	'webadmin/login.js',
	'admin/admin_login.js',
	'admin_login.js',
	'administrator/account.js',
	'administrator.js',
	'pages/admin/admin-login.js',
	'admin/admin-login.js',
	'admin-login.js',
	'login.js',
	'modelsearch/login.js',
	'moderator.js',
	'moderator/login.js',
	'moderator/admin.js',
	'account.js',
	'controlpanel.js',
	'admincontrol.js',
	'rcjakar/admin/login.js',
	'webadmin.js',
	'webadmin/index.js',
	'acceso.js',
	'webadmin/admin.js',
	'adminpanel.js',
	'user.js',
	'panel-administracion/login.js',
	'wp-login.js',
	'adminLogin.js',
	'admin/adminLogin.js',
	'home.js',
	'adminarea/index.js',
	'adminarea/admin.js',
	'adminarea/login.js',
	'panel-administracion/index.js',
	'panel-administracion/admin.js',
	'modelsearch/index.js',
	'modelsearch/admin.js',
	'admincontrol/login.js',
	'adm/admloginuser.js',
	'admloginuser.js',
	'admin2.js',
	'admin2/login.js',
	'admin2/index.js',
	'usuarios/login.js',
	'adm/index.js',
	'adm.js',
	'affiliate.js',
	'adm_auth.js',
	'memberadmin.js',
	'administratorlogin.js',
	'admin/account.cgi',
	'admin/index.cgi',
	'admin/login.cgi',
	'admin/admin.cgi',
	'admin_area/admin.cgi',
	'admin_area/login.cgi',
	'siteadmin/login.cgi',
	'siteadmin/index.cgi',
	'admin_area/index.cgi',
	'bb-admin/index.cgi',
	'bb-admin/login.cgi',
	'bb-admin/admin.cgi',
	'admin/home.cgi',
	'admin/controlpanel.cgi',
	'admin.cgi',
	'admin/cp.cgi',
	'cp.cgi',
	'administrator/index.cgi',
	'administrator/login.cgi',
	'nsw/admin/login.cgi',
	'webadmin/login.cgi',
	'admin/admin_login.cgi',
	'admin_login.cgi',
	'administrator/account.cgi',
	'administrator.cgi',
	'pages/admin/admin-login.cgi',
	'admin/admin-login.cgi',
	'admin-login.cgi',
	'login.cgi',
	'modelsearch/login.cgi',
	'moderator.cgi',
	'moderator/login.cgi',
	'moderator/admin.cgi',
	'account.cgi',
	'controlpanel.cgi',
	'admincontrol.cgi',
	'rcjakar/admin/login.cgi',
	'webadmin.cgi',
	'webadmin/index.cgi',
	'acceso.cgi',
	'webadmin/admin.cgi',
	'adminpanel.cgi',
	'user.cgi',
	'panel-administracion/login.cgi',
	'wp-login.cgi',
	'adminLogin.cgi',
	'admin/adminLogin.cgi',
	'home.cgi',
	'adminarea/index.cgi',
	'adminarea/admin.cgi',
	'adminarea/login.cgi',
	'panel-administracion/index.cgi',
	'panel-administracion/admin.cgi',
	'modelsearch/index.cgi',
	'modelsearch/admin.cgi',
	'admincontrol/login.cgi',
	'adm/admloginuser.cgi',
	'admloginuser.cgi',
	'admin2.cgi',
	'admin2/login.cgi',
	'admin2/index.cgi',
	'usuarios/login.cgi',
	'adm/index.cgi',
	'adm.cgi',
	'affiliate.cgi',
	'adm_auth.cgi',
	'memberadmin.cgi',
	'administratorlogin.cgi',
	'admin_panel/',
	'admin_panel.html',
	'adm_cp/'
	]

# -- LINUX --
def linux():
	print('''
 	 \033[92m_____________________________________
	|                                     |
	|          Admin Panel Finder         |
	|_____________________________________|
	|                                     |
	|          ->  Ashkan_Z9  <-          |
	|_____________________________________| 
	|                                     |
	|         Telegram: @Ashkan_Z9        |     
	|_____________________________________|\033[0m
	''')
	print('\n\n' + '\033[33m--> Hello ' + systemName + '!')
	print('--> ENTER YOUR TARGET,')
	print('--> EXAMPLE: http & https://wwww.site.com/\n')
	url = input("URL: ")
	
	panelCounter = 0
	panels = []
	print("\n===================================================================\n")
	time()
	for x in words:
		try:
			urlOpen = urllib.request.urlopen(url + x)
			print('\n\033[92m----------------------------------------------')
			print("\033[92mFOUND -- " + url + x)
			print('\033[92m----------------------------------------------\n')
			panelCounter+=1
			panels.append(url + x)
		except urllib.error.URLError:
			print("\033[31mNOT FOUND -- " + url + x)
	print('\n' + '\033[33m--> ' +  str(panelCounter) + " PANEL FOUND!")
	if panelCounter > 0:
		seePanels = input("\033[33m--> DO YOU WANT TO SEE THEM?(y/n) ")
		if seePanels == 'y' or seePanels == 'Y':
			print('\n\033[92m===========================================')
			for ps in panels:
				print(ps)
			print('\n\033[92m===========================================\n')
			print("\033[33mTHANKS FOR USING ASHKAN_Z9 ADMIN PANEL FINDER!")

		elif seePanels == 'n' or seePanels == 'N':
			print("\n\033[33m--> THANKS FOR USING ASHKAN_Z9 ADMIN PANEL FINDER!")

		else:
			print('\033[31mUNKNOWN COMMAND!')
	else:
		print("\n\033[33m--> THANKS FOR USING ASHKAN_Z9 ADMIN PANEL FINDER!")
	ex()

# -- WINDOWS --

def windows():
	os.system('color a')
	print('''
 	 _____________________________________
	|                                     |
	|          Admin Panel Finder         |
	|_____________________________________|
	|                                     |
	|          ->  Ashkan_Z9  <-          |
	|_____________________________________| 
	|                                     |
	|         Telegram: @Ashkan_Z9        |     
	|_____________________________________|
	''')
	print('\n\n' + '--> Hello ' + systemName + '!')
	print('--> ENTER YOUR TARGET,')
	print('--> EXAMPLE: http & https://www.site.com/\n')
	url = input("URL: ")
	
	panelCounter = 0
	print("\n===================================================================\n")
	time()
	for x in words:
		try:
			urlOpen = urllib.request.urlopen(url + x)
			print('\n----------------------------------------------')
			print("FOUND -- " + url + x)
			print('----------------------------------------------\n')
			panelCounter+=1
		except urllib.error.URLError:
			print("NOT FOUND -- " + url + x)
	print('\n=============================================')
	print('\n--> ' +  str(panelCounter) + " PANEL FOUND!")
	print('\n=============================================\n')
	print("--> THANKS FOR USING ASHKAN_Z9 ADMIN PANEL FINDER!")
	ex()	

if systemOS == 'Linux':
	os.system('clear')
elif systemOS == 'Windows':
	os.system('cls')
print('''
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWWNXXK0OOkkkxxxxkkOO0KXNWMMMMMMMMMMMMM
MMMMMMNKkdl:;,'....              ...,:lx0NMMMMMMMM
MMMMXd,.                                .,o0WMMMMM
MMMK:                                      .dNMMMM
MMNl                                        .oNMMM
MM0'                                         .kMMM
MWd.     .,;:::,.                .';;;,'.     cNMM
MNc   'clokOkddk0Oo'          'lkOkxxkxdll:.  ,KMM
MX;  .,'. 'clllccoOKo.      .d0Oxxxdc;.  .,;. .OMM
MK,          .':oolc:.      'loxkd:.          .OMM
MK,             .:Ok,        ,lc.             .kMM
M0'    .;ldddolc;.:0Xc       .. ..:ldxxdl'    .kMM
M0' .'l0WMMMMMMMWXodNO.       'd0NWMMMMMMXd,. .OMM
M0' 'dkOO0000Okxoc'cX0,       .:cccccccc:::,..'OMM
M0,                ;XK,                       '0MM
MNo.               :X0'                       :XMM
MMNo.             .dWO.                      .dWMM
MMWKd'          .;kNMk.                     'dNMMM
MMWkdOkol;''.. .dKOKWo       .'.    ....,,ckOXMMMM
MMMXcl0XNx.    .xl.xX:         .    ..;OKoxKOXMMMM
MMMMO,;dk0x;.   . .o0;              .;OKl:dd0MMMMM
MMMMWd..clxK0dc,..'oXOc;;:lkx;.  .,lOXOccl:kWMMMMM
MMMMMNl .;ccoONNXXNWMNx:oOXMMN0kOKNXklcdl,dNMMMMMM
MMMMMMXc  :xl,,:oxO0Oo'...:OXXK0kd:..;x:.oNMMMMMMM
MMMMMMMXc  :KKd,.     ..........    ':'.oNMMMMMMMM
MMMMMMMMXc  cX0;... .';;;;;.       .,..dNMMMMMMMMM
MMMMMMMMMNo. :d.    .cXWWWK:      .. 'kWMMMMMMMMMM
MMMMMMMMMMWk' ..     :XMMMk.        :0MMMMMMMMMMMM
MMMMMMMMMMMW0:.     'OMMMMX:      .dNMMMMMMMMMMMMM
MMMMMMMMMMMMMNx'    '0MMMMNl    .:0WMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMXd,   oNMMMO'  .:OWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNkc';0MWWx';dKWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNKNMMWNXWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
''')

if systemOS == "Linux":
	linux()

elif systemOS == 'Windows':
	windows()


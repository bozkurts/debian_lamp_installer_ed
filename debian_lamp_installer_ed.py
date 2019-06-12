import os
import sys
import pymsgbox 

print "\n\
    __________  \n\
   / ____/ __ \ \n\
  / __/ / / / / \n\
 / /___/ /_/ /  \n\
/_____/_____/   \n\
                \n\
   debian_lamp_installer_ed.py programı Eyüp Durak tarafından Python programlama dili ile programlanmıştır. \n\
   debain_lamp_installer_ed.py Genel Kamu Lisansı ile korunmaktadır. \n\
   Bizi tercih ettiğiniz için teşekkürler.\n\
   
os.system("sudo apt-get update")
os.system("sudo apt-get upgrade")
os.system("sudo apt-get install apache2")
os.system("sudo apt-get install mysql-server")
os.system("sudo apt-get install php php-fpm php-mysql")
os.system("exit")

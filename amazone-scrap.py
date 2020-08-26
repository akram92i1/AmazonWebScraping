import  requests as re
import  matplotlib.pyplot as plt
#  for sending an email  we have to import this following libary
import  smtplib
from  email.message  import EmailMessage
from locale import *
from bs4 import BeautifulSoup
from colorama import  Fore , Style
from colorama import  Fore

# the method  to send an email if case was confirmed 
def send_email( price ) :
    if price < 140.00 :
        # NOW WE HAVE TO MAKE CONNECTION TO THE GMAIL
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('akramkhelili1996@gmail.com','kckuftwevsfzsjak')

        Subject  =" Hey the price fall down houra !! "
        Body =" Please check the link   https://www.amazon.fr/XFX-RX-570P4DFD6-graphique-Radeon-Express/dp/B06Y64PV2X/ref=sr_1_1_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=7L16SKOQ0JTH&keywords=amd+rx+570&qid=1565372176&s=gateway&sprefix=amd+rx+%2Caps%2C555&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUzVQNUZKNkRENUo0JmVuY3J5cHRlZElkPUEwOTc5MDE0U0lSNFBPVkhaMUJaJmVuY3J5cHRlZEFkSWQ9QTA1MTkwMDZQT1k3VlU5WVdRV0Emd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl  "
        message = f"Subject : {Subject} \n\n {Body}"
        server.sendmail("akramkhelili1996@gmail.com","johnnyakram32@gmail.com",message)
        print("HEY THE EMAIL HAS BEEN SUCESSFULLY SENT  YOUPI !! ")
    else :
        print("the price still not what you want ")


setlocale(LC_NUMERIC,'')
atof('12341,13131')
URL = 'https://www.amazon.fr/ukYukiko-dissipateurs-Thermiques-Raspberry-Mod%C3%A8le/dp/B07Y775WWL/ref=sr_1_4?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=23WAHN45B75WN&dchild=1&keywords=raspberry+pi+4&qid=1597017043&sprefix=ras%2Caps%2C500&sr=8-4'
headers = {"user-agent ":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
def get_Name_of_product(URL , headers ):
    page = re.get(URL , headers= headers)
    soup = BeautifulSoup(page.content,'html.parser')
    type(soup)




def check_prices( URL , headers ):

    page = re.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    ################################
    # HERE WE GONNA FIND SOME PRICE#
    price = str
    price = soup.find(id='priceblock_ourprice')
    print(Fore.BLUE,"------------------------------------------" ,Style.RESET_ALL)
    print(type(price))
    print(Fore.BLUE,"------------------------------------------" ,Style.RESET_ALL)
    # PRICE = PRICE WITH EURO
    price_without_euro = str
    price_with_euro  = price.split()
    for elem in price_with_euro :
        if elem != '€':
            price_without_euro = elem
    price_number = atof(price_without_euro)

    return price_number

price = check_prices(URL,headers)

print("THE PRICE OF YOUR PRODUCT IS : ",price)
send_email(price)
################################



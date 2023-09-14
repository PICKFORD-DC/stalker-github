# AUTHOR : PICKFORD
# WA : 083806211924

###-----[ IMPORT MODULE ]-----###
import requests
import rich
import json
import os

###-----[ MODULE RICH ]-----###
from rich.panel import Panel as panel
from rich import print as rprint
from rich.text import Text as text
H = "[bold green]"
M = "[bold red]"
P = "[bold white]"
def logo():
    index = """
    ╔═╗╔╦╗╔═╗╦  ╦╔═╔═╗╦═╗  ╔═╗╦╔╦╗╦ ╦╦ ╦╔╗   
    ╚═╗ ║ ╠═╣║  ╠╩╗║╣ ╠╦╝  ║ ╦║ ║ ╠═╣║ ║╠╩╗  
    ╚═╝ ╩ ╩ ╩╩═╝╩ ╩╚═╝╩╚═  ╚═╝╩ ╩ ╩ ╩╚═╝╚═╝  
    """
    rprint(panel(text(index,justify='center',style='bold white'),title=f'{H}[ {P}WELCOME TO MY PROJECT {H}]',style='bold white'))
    return

def main():
    logo()
    user = input('* Masukan User Name : ')
    data = requests.get(f'http://api.github.com/users/{user}')
    data2 = requests.get(f'https://api.github.com/users/{user}/followers')
    try:
        nama = json.loads(data.text)['name']
        user_name = json.loads(data.text)['login']
        id = json.loads(data.text)['id']
        bio = json.loads(data.text)['bio']
        pp = json.loads(data.text)['avatar_url']
        followers = json.loads(data.text)['followers']
        following = json.loads(data.text)['following']
        repo_publik = json.loads(data.text)['public_repos']
        Create = json.loads(data.text)['created_at']
        Update = json.loads(data.text)['updated_at']
        print(f'* Nama : {nama}')
        print(f'* User Name : {user_name}')
        print(f'* Id : {id}')
        print(f'* Bio : {bio}')
        print(f'* Foto Profile : {pp}')
        print(f'* Followers : {followers}')
        print(f'* Following : {following}')
        print(f'* Repository Publik : {repo_publik}')
        print(f'* Akun Di Buat Pada {Create}')
        print(f'* Akun Di Update {Update}')
        response = requests.get(pp)
        if response.status_code == 200:
           with open(f"/sdcard/avatar/{user}.jpg", "wb") as data:
                data.write(response.content)
                print("Avatar Berhasil Tersimpan In /sdcard/avatar")
        else:
             print("Avatar Gagal Tersimpan")
    except KeyError:
           print('* Pengguna Tidak Di Temukan')

if __name__ == '__main__':
  try:
       open('/sdcard/avatar','r').read()
  except Exception:
         os.system('mkdir /sdcard/avatar')
  os.system('clear')
  main()

from urllib.request import Request, urlopen

def ipgrab():
    ip = 'None'
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

ip = ipgrab()

print(f'Current IP: {ip}')

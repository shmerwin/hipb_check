import sys
import hashlib
import getpass
import requests

def sha1_upper(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest().upper()

def query_range(prefix):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(
        url,
        headers={"User-Agent": "hibp-checkk"},
        timeout=5
    )
    return response.text  

def find_count(suffix, body):
    
    for line in body.splitlines():
        hash_suffix, count = line.split(":", 1)
        if hash_suffix == suffix:    
            return int(count)
            
    return 0 

def main():

    pw = getpass.getpass("Gib das zu testende Passwort ein: ")
    
    hash = sha1_upper(pw)
    prefix = hash[:5]
    suffix = hash[5:]

    body = query_range(prefix)
    
    count = find_count(suffix, body)
    if count > 0:
        print(f" Das Passwort kam {count} Mal vor.")
        
    else:
        print("Passwort nicht gefunden.")

if __name__ == "__main__":
    main()

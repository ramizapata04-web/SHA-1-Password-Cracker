import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = [line.strip() for line in f]
    if use_salts:
        with open('known-salts.txt', 'r') as f:
            salts = [line.strip() for line in f]
    else:
        salts = [""]

    for password in passwords:
        for salt in salts:
            if use_salts:
                combinations = [
                    salt + password,
                    password + salt,
                    salt + password + salt 
                ]
            else:
                combinations = [password]
            
            for combo in combinations:
                hash_obj = hashlib.sha1(combo.encode())
                hashed_password = hash_obj.hexdigest()
                if hashed_password == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
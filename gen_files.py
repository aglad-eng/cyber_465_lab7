import pandas as pd
import crypt

df = pd.read_csv('plain_user_pswd.txt')
# my_salt = "MYSALT349HJD334"
def create_shadow():
    f = open("shadow_ex", "w")
    for i in range(len(df['username']) - 1):
        group = 1000
        hashed_password = crypt.crpyt(df['password'][i], crypt.METHOD_MD5)
        days_passed = 18920
        f.write(f"{df['username'][i]}:{hashed_password}:{days_passed}:{0}:{99999}:7:::\n")
    f.close()
    print("Finished creating shadow_ex")

def create_passwd():
    f = open("passwd_ex", "w")
    for i in range(len(df['username']) - 1):
        group = 1000
        f.write(f"{df['username'][i]}:{df['password'][i]}:{group + i}:{group}:{Nothing}:/:/bin/bash\n")
    f.close()
    print("Finished creating passwd_ex")
    

# print(f"df: \n{df}\n")

# print(f"df.dtypes: \n{df.dtypes}\n")
# print(f"df[username]: \n{df['username']}\n")
# print(df['username'][0])

create_passwd()
create_shadow()
print("Finished script")
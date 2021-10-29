import pandas as pd
import crypt

df = pd.read_csv('plain_user_pswd.txt')
# my_salt = "MYSALT349HJD334"
def create_shadow(file_name, start_index=0, num_entries=3):
    f = open(file_name, "w")
    for i in range(num_entries):
        group = 1000
        hashed_password = crypt.crypt(df['password'][start_index + i], crypt.METHOD_MD5)
        days_passed = 18920
        f.write(f"{df['username'][start_index + i]}:{hashed_password}:{days_passed}:{0}:{99999}:7:::\n")
    f.close()
    print("Finished creating shadow_ex")

def create_passwd(file_name, start_index=0, num_entries=3):
    f = open(file_name, "w")
    for i in range(num_entries):
        group = 1000
        f.write(f"{df['username'][start_index + i]}:{df['password'][start_index + i]}:{group + start_index+ i}:{group}:GECOS:/:/bin/bash\n")
    f.close()
    print("Finished creating passwd_ex")
    

# print(f"df: \n{df}\n")

# print(f"df.dtypes: \n{df.dtypes}\n")
# print(f"df[username]: \n{df['username']}\n")
# print(df['username'][0])

create_passwd("veryweak_passwd", 0)
create_passwd("weak_passwd", 3)
create_passwd("good_passwd", 6)
create_passwd("strong_passwd", 9)
create_passwd("verystrong_passwd", 12)

create_shadow("veryweak_shadow", 0)
create_shadow("weak_shadow", 3)
create_shadow("good_shadow", 6)
create_shadow("strong_shadow", 9)
create_shadow("verystrong_shadow", 12)
print("Finished script")
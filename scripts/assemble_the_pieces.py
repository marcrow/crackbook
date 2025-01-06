import re
#Edit this variable
ntds_csv_file='/home/kali/user_accounts_4_cracking.csv'

# do locate hashcat.potfile if the script doesn't find f1 file

with open('/home/kali/.local/share/hashcat/hashcat.potfile') as f1, open(ntds_csv_file) as f2:
    f2_lines = f2.readlines()
    for lines in f1:
        hash = lines.split(':')[0]
        password = lines.split(':')[1]
        for match in f2_lines:
            if hash in match:
                tmatch=match.split(":")
                user = tmatch[0]
                print(f"{user}:{password.strip()}")
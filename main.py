import subprocess as sp

data = sp.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = data.decode('utf-8').split('\n')

for lines in data:
    print(lines)

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]




for i in profiles:
    results = sp.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')

    for lines in results:
        if 'Key Content' in lines:
            print(i,'\t', end=' ')
            print('\t',lines)
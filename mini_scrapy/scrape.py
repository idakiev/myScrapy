import subprocess

ans = subprocess.call(['scrapy', 'crawl', 'shoes', '-o data.json'])
if ans == 0:
    print('Command executed.')
    subprocess.call(['python', 'clean_data.py'])
else:
    print('Command failed.')

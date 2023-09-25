import requests
from bs4 import BeautifulSoup

url = "https://sekolahloka.com/data/smk-n-4-bandar-lampung/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', class_='table table-striped')
    
    if table:
        for row in table.find_all('tr'):
            header = row.find('th')
            data = row.find('td')
            
            if header and data:
                header_text = header.get_text(strip=True)
                data_text = data.get_text(strip=True)
                print(f"{header_text}: {data_text}")

    else:
        print("Tabel Tidak Ditemukan.")
else:
    print("URL Tidak Ditemukan.")

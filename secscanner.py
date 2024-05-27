import os
import shodan
import logging
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('SHODAN_API_KEY')
SEARCH_FOR = 'SonarQube'

logging.basicConfig(filename='secscanner.log', level=logging.INFO)

def shodan_search(api_key, query):
    api = shodan.Shodan(api_key)
    results = api.search(query)
    return results['matches']

def check_default_credentials(ip, port):
    # Burada SonarQube varsayılan kimlik bilgilerini kontrol eden kod olacak
    pass

def main():
    results = shodan_search(API_KEY, SEARCH_FOR)
    for result in results:
        ip = result['ip_str']
        port = result['port']
        if check_default_credentials(ip, port):
            message = f'Varsayılan kimlik bilgileri ile erişim sağlanabilen {ip}:{port} bulundu!'
            print(message)
            logging.info(message)

if __name__ == '__main__':
    main()

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os, re, pprint, json

# example url
# https://www.ouedkniss.com/annonces/index.php?c=automobiles&prix=1&prix_min=5&prix_max=1000&p=1

class Scraper:
    def __init__(self, url, **kwargs):
        self.url_ = url
        self.root_url_ = '{}://{}'.format(urlparse(url).scheme, urlparse(url).netloc)
        self.params_ = dict()
        self.init_params_(**kwargs)
        self.items_ = []

    def init_params_(self, **kwargs):
        if 'c' in kwargs:
            self.params_['c'] = kwargs['c']
        else:
            self.params_['c'] = 'automobiles'

        if 'prix' in kwargs:
            self.params_['prix'] = kwargs['prix']
        else:
            self.params_['prix'] = '1'

        if 'prix_min' in kwargs:
            self.params_['prix_min'] = kwargs['prix_min']
        else:
            self.params_['prix_min'] = '5'

        if 'prix_max' in kwargs:
            self.params_['prix_max'] = kwargs['prix_max']
        else:
            self.params_['prix_max'] = '1000'

    def update_params_(self, **kwargs):
        if 'c' in kwargs:
            self.params_['c'] = kwargs['c']

        if 'prix' in kwargs:
            self.params_['prix'] = kwargs['prix']

        if 'prix_min' in kwargs:
            self.params_['prix_min'] = kwargs['prix_min']

        if 'prix_max' in kwargs:
            self.params_['prix_max'] = kwargs['prix_max']

    def get_search_page(self, p = '1', **kwargs):
        self.update_params_(**kwargs)
        params = dict(self.params_)
        params['p'] = p
        try:
            req = requests.get(self.url_, params)
        except Exception as e:
            print(e)
            return None
        else:
            return BeautifulSoup(req.text, 'html.parser')

    def get_item_page(self, item_url):
        req = requests.get(item_url)
        return BeautifulSoup(req.text, 'html.parser')

    def scrape_search_page(self, p = '1'):
        bs = self.get_search_page(p)
        if bs is None:
            return False

        try:
            items = bs.find_all('div', {'class': 'annonce'})
            for item_ in items:
                try:
                    title = item_.find('h2', {'itemprop': 'name'})
                    item_url = item_.find('a', {'itemprop': 'url'})
                    print('# ' + title.text)
                    print('> ' + self.root_url_ + '/' + item_url['href'])
                    self.scrape_item(self.root_url_ + '/' + item_url['href'])
                    print('-' * 20)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        return True
    
    def scrape_item(self, item_url):
        bs = self.get_item_page(item_url)
        try:
            annonce = bs.find('div', {'id': 'annonce'})
            self.scrape_item_description(annonce)
        except Exception as e:
            print(e)

    def scrape_item_description(self, annonce):
        props = dict()

        description = annonce.find('div', {'id': 'Description'})
        if description is None:
            return None

        try:
            props['id'] = description.find('span', {'itemprop': 'productID'}).text
        except Exception as e:
            print(e, 'id')

        try:
            #props['date'] = description.find('p', {'id': 'Catégorie'}).previous_siblings[1] .find('span', {'class': 'description_span'}).text
            props['date'] = description.find('p', {'id': 'Catégorie'}).previous_sibling.previous_sibling.previous_sibling.previous_sibling .find('span', {'class': 'description_span'}).text
        except Exception as e:
            print(e, 'date')

        try: 
            props['category'] = description.find('p', {'id': 'Catégorie'}).span.text
        except Exception as e:
            print(e, 'category')

        try:
            props['energy'] = description.find('p', {'id': 'Energie'}).span.text
        except Exception as e:
            print(e, 'energy')

        try:
            props['engine'] = description.find('p', {'id': 'Moteur'}).span.text
        except Exception as e:
            print(e, 'engine')
                
        try:
            props['range'] = description.find('p', {'id': 'Kilométrage'}).span.text
        except Exception as e:
            print(e, 'range')

        try:
            props['color'] = description.find('p', {'id': 'Couleur'}).span.text
        except Exception as e:
            print(e, 'color')

        try:
            props['papers'] = description.find('p', {'id': 'Papiers'}).span.text
        except Exception as e:
            print(e, 'papers')

        try:
            props['options'] = description.find('p', {'id': 'Options'}).span.text
        except Exception as e:
            print(e, 'options')

        try:
            props['transmission'] = description.find('p', {'id': 'Transmission'}).span.text
        except Exception as e:
            print(e, 'transmission')

        try:
            props['price'] = annonce.find('span', {'itemprop': 'price'}).text
        except Exception as e:
            print(e, 'price')
        
        try:
            props['title'] = annonce.find('h1', {'id': 'Title'}).text
        except Exception as e:
            print(e, 'title')

        try:
            props['address'] = annonce.find('div', {'id': 'Annonceur'}).find('p', {'class': 'Adresse'}).text
        except Exception as e:
            print(e, 'address')

        self.items_.append(props)
        pprint.pprint(props)

    def scrape_pages(self, max_pages = 10):
        i = 1
        while i <= max_pages and self.scrape_search_page(p = str(i)):
            print(str(i) + '\n')
            i = i + 1
        with open(os.path.abspath('dataset/cars.json'), 'w', encoding = 'utf-8') as file:
            json.dump(self.items_, file, indent = 2)

scraper = Scraper(url = 'https://www.ouedkniss.com/annonces/index.php')
scraper.scrape_pages(max_pages = 300)


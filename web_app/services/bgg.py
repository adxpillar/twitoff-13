import requests
import bs4
import json
import os


game_id = 13
url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, features='lxml')
print(soup.find('name').text)


@APP.shell_context_processor
def make_shell_context():
    return {'DB': DB, 'Record': Record}
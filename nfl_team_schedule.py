import requests, os, bs4
import pandas as pd

teams = ['Bills', 'Dolphins', 'Patriots', 'Jets', 'Ravens', 'Bengals', 'Browns', 'Steelers', 'Texans', 'Colts', 'Jaguars', 'Titans',
         'Broncos', 'Chiefs', 'Raiders', 'Chargers', 'Cowboys', 'Giants', 'Eagles', 'Commanders', 'Bears', 'Lions', 'Packers', 'Vikings',
         'Falcons', 'Panthers', 'Saints', 'Buccaneers', 'Cardinals', 'Rams', '49ers', 'Seahawks']

url_dict = {'Bills': 'buf/buffalo-bills', 'Dolphins': 'mia/miami-dolphins', 'Patriots': 'ne/new-england-patriots',
            'Jets': 'nyj/new-york-jets', 'Ravens': 'bal/baltimore-ravens', 'Bengals': 'cin/cincinnati-bengals', 'Browns': 'cle/cleveland-browns',
            'Steelers': 'pit/pittsburgh-steelers', 'Texans': 'hou/houston-texans', 'Colts': 'ind/indianapolis-colts', 'Jaguars': 'jax/jacksonville-jaguars',
            'Titans': 'ten/tennessee-titans', 'Broncos': 'den/denver-broncos', 'Chiefs': 'kc/kansas-city-chiefs', 'Raiders': 'lv/las-vegas-raiders',
            'Chargers': 'lac/los-angeles-chargers', 'Cowboys': 'dal/dallas-cowboys', 'Giants': 'nyg/new-york-giants', 'Eagles': 'phi/philadelphia-eagles',
            'Commanders': 'wsh/washington-commanders', 'Bears': 'chi/chicago-bears', 'Lions': 'det/detroit-lions', 'Packers': 'gb/green-bay-packers',
            'Vikings': 'min/minnesota-vikings', 'Falcons': 'atl/atlanta-falcons', 'Panthers': 'car/carolina-panthers', 'Saints': 'no/new-orleans-saints',
            'Buccaneers': 'tb/tampa-bay-buccaneers', 'Cardinals': 'ari/arizona-cardinals', 'Rams': 'lar/los-angeles-rams', '49Ers': 'sf/san-francisco-49ers',
            'Seahawks': 'sea/seattle-seahawks'}

url = 'https://www.espn.com/nfl/team/schedule/_/name/'
team = input("Which team's schedule do you want to see? ").title()
team_url = url + url_dict[team]

res = requests.get(team_url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

rows = []

#for i in range(0, 21):
 #   schedule = soup.find("tr", {"data-idx": i})
  #  for row in schedule:
   #     data = row.select('td, span')
    #    for a in data:
     #       print(a.getText())

for tr in soup.find_all('tr'):
    rows.append([td.text for td in tr.select('td span')])

for row in rows:
    if ' ' in row:
        row[2:5] = [''.join(row[2:5])]

rows = list(filter(None, rows))
df = pd.DataFrame(rows, columns = rows[1])
print(df)
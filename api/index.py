from flaskr import create_app
from flaskr.transformer import LogTransformer
from joblib import load
import os

app = create_app(load(os.path.abspath('flaskr/price_estimator.joblib')))

if __name__ == "__main__":
  app.run(debug=True)



# Eg:
# data['range'] = 36000
# data['volume'] = 1.6
# data['horses'] = 110
# data['year'] = 2017

# data['phares antibrouillard'] = 1
# data['toit ouvrant'] = 0
# data['phares xénon'] = 0
# data['climatisation'] = 1
# data['retroviseurs électriques'] = 0
# data['abs'] = 1
# data['alarme'] = 1
# data['vitres éléctriques'] = 1
# data['direction assisstée'] = 1
# data['esp'] = 1
# data['feux du jour'] = 1
# data['jantes alliage'] = 1
# data['radar de recul'] = 1

# data['category'] = 'Citadine'
# data['energy'] = 'Essence'
# data['color'] = 'noir'
# data['papers'] = 'Carte Grise (safia)'
# data['transmission'] = 'Manuelle'
# data['offer'] = 'Fixe'
# data['wilaya'] = 'alger'
# data['town'] = 'bab ezzouar'
# data['brand'] = 'seat'
# data['model'] = 'ibiza'


#['range', 'volume', 'horses', 'year', 'phares antibrouillard', 'toit ouvrant', 'phares xénon', 'climatisation', 'retroviseurs électriques', 'abs', 'alarme', 'vitres éléctriques', 'direction assisstée', 'esp', 'feux du jour', 'jantes alliage', 'radar de recul', 'category', 'energy', 'color', 'papers', 'transmission', 'offer', 'wilaya', 'town', 'brand', 'model']

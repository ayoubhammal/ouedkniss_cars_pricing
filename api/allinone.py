from flask import Flask
from flask import request
from joblib import load
import os
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class LogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return np.log(X)

model = load(os.path.abspath('flaskr/price_estimator.bz2'))

app = Flask(__name__) 

app.model = model
@app.route('/', methods = ['POST', 'GET'])
def predict():
  if request.method == 'POST':
    try:
      features = request.get_json()
      df = pd.DataFrame(data = features, columns = ['range', 'volume', 'horses', 'year', 
                                                    'phares antibrouillard', 'toit ouvrant', 
                                                    'phares xénon', 'climatisation', 'retroviseurs électriques', 
                                                    'abs', 'alarme', 'vitres éléctriques', 'direction assisstée', 
                                                    'esp', 'feux du jour', 'jantes alliage', 'radar de recul', 
                                                    'category', 'energy', 'color', 'papers', 'transmission', 
                                                    'offer', 'wilaya', 'town', 'brand', 'model'], 
                                          index = [0])
      prediction = app.model.predict(df)
      return {'price' : prediction[0]}
    except Exception as e:
      print(e)
      return {'error': 'Something went wrong'}
  elif request.method == 'GET':
    return {"attributes" : {
              'range' : 'int',
              'volume' : 'float',
              'horses' : 'int',
              'year' : 'int',
              'phares antibrouillard' : '0 or 1',
              'toit ouvrant' : '0 or 1',
              'phares xénon' : '0 or 1', 
              'climatisation' : '0 or 1', 
              'retroviseurs électriques' : '0 or 1', 
              'abs' : '0 or 1', 
              'alarme' : '0 or 1', 
              'vitres éléctriques' : '0 or 1', 
              'direction assisstée' : '0 or 1', 
              'esp' : '0 or 1', 
              'feux du jour' : '0 or 1', 
              'jantes alliage' : '0 or 1', 
              'radar de recul' : '0 or 1', 
              'category' : ['berline', 'break - familiale', 'cabriolet - coupé', 'camionnette', 'citadine', 'commerciale', 'fourgonnette', 'grande berline', 'mini citadine', 'moyenne berline', 'pickup', 'tout terrain - suv'], 
              'energy' : ['diesel', 'essence', 'gpl'], 
              'color' : ['aubergine', 'beige', 'blanc', 'bleu', 'grenat', 'gris', 'jaune', 'maron', 'marron', 'mauve', 'miel', 'noir', 'orange', 'rose', 'rouge', 'vert', 'violet'], 
          'papers' : ['carte grise (safia)', 'carte jaune (safia)', 'licence moudjahid / délai'], 
              'transmission' : ['automatique', 'manuelle', 'semi automatique'], 
              'offer' : ['fixe', 'négociable', 'offert'], 
              'wilaya' : ['adrar', 'ain defla', 'ain temouchent', 'alger', 'annaba', 'batna', 'bechar', 'bejaia', 'biskra', 'blida', 'bordj bou arreridj', 'bouira', 'boumerdes', 'chlef', 'constantine', 'djelfa', 'el bayadh', 'el oued', 'el taref', 'ghardaia', 'guelma', 'illizi', 'jijel', 'khenchela', 'laghouat', 'mascara', 'medea', 'mila', 'mostaganem', 'msila', 'naama', 'oran', 'ouargla', 'oum el bouaghi', 'relizane', 'saida', 'setif', 'sidi bel abbes', 'skikda', 'souk ahras', 'tamanrasset', 'tebessa',  'tiaret', 'tindouf', 'tipaza', 'tissemsilt', 'tizi ouzou', 'tlemcen'], 
              'town' : 'any', 
              'brand' : ['audi', 'baic', 'bmw', 'brilliance', 'bugatti', 'byd', 'chana', 'changan', 'chery', 'chevrolet', 'citroen', 'dacia', 'daewoo', 'daihatsu', 'dfm', 'dfsk', 'ds', 'emgrand', 'faw', 'fiat', 'ford', 'foton', 'geely', 'gonow', 'great wall', 'hafei motors', 'haima', 'honda', 'hyundai', 'isuzu', 'jac', 'jaguar', 'jeep', 'jmc', 'kia', 'lada', 'land rover', 'lifan', 'mahindra', 'mazda', 'mercedes benz', 'mg', 'mini', 'mitsubishi', 'nissan', 'opel', 'peugeot', 'porsche', 'renault', 'rover', 'saipa', 'seat', 'skoda', 'ssangyong', 'subaru', 'suzuki', 'tata', 'toyota', 'volkswagen', 'zotye'], 
              'model' : 'any'
            }
          }

if __name__ == "__main__":
  app.run(debug=True)


# {    
#   "abs": 1,
#   "alarme": 1,
#   "brand": "seat",
#   "category": "citadine",
#   "climatisation": 1,
#   "color": "noir",
#   "direction assisstée": 1,
#   "energy": "essence",
#   "esp": 1,
#   "feux du jour": 1,
#   "horses": 110,
#   "jantes alliage": 1,
#   "model": "ibiza",
#   "offer": "offert",
#   "papers": "carte grise (safia)",
#   "phares antibrouillard": 1,
#   "phares xénon": 0,
#   "radar de recul": 1,
#   "range": 36000,
#   "retroviseurs électriques": 0,
#   "toit ouvrant": 0,
#   "town": "bab ezzouar",
#   "transmission": "manuelle",
#   "vitres éléctriques": 1,
#   "volume": 1.6,
#   "wilaya": "alger",
#   "year": 2017
# }
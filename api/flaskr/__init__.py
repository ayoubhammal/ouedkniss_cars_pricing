from flask import Flask
from flask import request

import pandas as pd

def create_app(model):
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
        prediction = model.predict(df)
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

  return app

if __name__ == "__main__":
  print("hello")
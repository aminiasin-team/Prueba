# -*- coding: utf-8 -*-
# Creado por Alberto Valencia el 22 de Enero de 2020   
# Para cualquier consulta escribe a aminiasin@gmail.com

import csv
import json
import pandas as pd

csvfile = open('costs.csv', 'r')
jsonfile = open('resultado.json', 'w')

#convierte el fichero de csv a json

fieldnames = ("Service","EC2-Otros(USD)","EC2-Instancias(USD)","Plesk Obsidian on CentOS 7 - WordPress & Website Hosting Environment(USD)","Config(USD)","CloudWatch(USD)","EC2 Container Registry (ECR)(USD)","S3(USD)","Key Management Service(USD)","SNS(USD)","Costo total (USD)")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
    
jsonfile.close()

#eliminamos las dos primeras lineas y la ultima

df = pd.read_json (r"C:\Users\avalencia\Downloads\resultado.json", lines=True)
df.drop(df.index[[0,1,-1]], inplace=True)

#crea un fichero csv desde el dataframe creado 

df.to_csv(r'C:\Users\avalencia\Downloads\final.csv', sep=',', encoding='utf-8', index=False)

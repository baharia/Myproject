from databas import loadDbase
db = loadDbase()
for key in db:
    print(key, '=>\n  ', db[key])
    print(db['sue']['name'])

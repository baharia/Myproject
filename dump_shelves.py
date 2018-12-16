import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n  ', db[key])
    for ki in db[key]:
        print(ki,'=>',db[key][ki])
print(db['sue']['name'])
db.close()

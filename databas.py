"""Save in-memory database object to a file with custom formatting;
assume 'endrec.', 'enddb.', and '=>' are not used in the data;
assume db is dict of dict;  warning: eval can be dangerous - it runs strings as code;
could also eval() record dict all at once;
could also dbfile.write(key + '\n') vs print(key, file=dbfile); """

"""bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
#bob {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
db = {}
db['bob'] = bob                      # reference in a dict of dicts >>>
db['sue'] = sue
db['bob']['name']                    # fetch bob's name 'Bob Smith' >>>
db['sue']['pay'] = 50000   """          # change sue's pay >>>
#db['sue']['pay']                     # fetch sue's pay 50000
"""print(db)
import pprint
pprint.pprint(db)
for key in db:
    print(key, '=>', db[key]['name'])
    for (name,value) in db[key].items():
        print(name)"""



dbfilename = 'people-file'
ENDDB  = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

"""dbfile = open(dbfilename, 'w')
for key in db:
    print(key, '=>', db[key]['name'])
    for (name,value) in db[key].items():
        print(name + RECSEP + repr(value), file=dbfile)
print(ENDDB, file=dbfile)
"""
def storeDbase(db, dbfilename=dbfilename):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename, 'w')
    for key in db:
            print(key, file=dbfile)
            for (name,value) in db[key].items():
                print(name + RECSEP + repr(value), file=dbfile)
                print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()
    
def loadDbase(dbfilename=dbfilename):
    "parse data to reconstruct database"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
"""for line in open('people-file'):
     print(line, end='') """

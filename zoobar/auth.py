from zoodb import *
from debug import *
import auth_client

import hashlib
import random

def newtoken(db, person):
    hashinput = "%s%.10f" % (person.password, random.random())
    person.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return person.token

def login(username, password):
    return auth_client.login(username, password);

def register(username, password):
    db = person_setup()
    person = db.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newperson.username = username
    db.add(newperson)
    db.commit()
    return auth_client.register(username, password);

def check_token(username, token):
    return auth_client.check_token(username, token)
    if person and person.token == token:
        return True
    else:
        return False


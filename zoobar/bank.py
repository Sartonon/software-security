from zoodb import *
from debug import *
import bank_client

import time

def transfer(sender, recipient, zoobars, token):
    return bank_client.transfer(sender, recipient, zoobars, token)

def balance(username):
    return bank_client.balance(username)

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))


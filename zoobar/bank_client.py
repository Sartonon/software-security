from debug import *
from zoodb import *
import rpclib

def transfer(sender, recipient, zoobars, token):
    log(token)
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars, token=token)
        return ret

def balance(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('balance', username=username)
        return ret

def get_log(username):
     with rpclib.client_connect('/banksvc/sock') as c:
        log(username)
        ret = c.call('get_log', username=username)
        return ret

def add_bank(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('add_bank', username=username)
        return ret

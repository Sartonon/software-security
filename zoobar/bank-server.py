#!/usr/bin/python

import rpclib
import sys
import auth
from zoodb import *
from debug import *

import time

class AuthRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, sender, recipient, zoobars, token):
        #persondb = person_setup()
        
        check = auth.check_token(sender, token)
        log(check)
        if auth.check_token(sender, token) == False:
            return None

        bankdb = bank_setup()
        senderp = bankdb.query(Bank).get(sender)
        recipientp = bankdb.query(Bank).get(recipient)

        sender_balance = senderp.zoobars - zoobars
        recipient_balance = recipientp.zoobars + zoobars

        if sender_balance < 0 or recipient_balance < 0:
            raise ValueError()

        senderp.zoobars = sender_balance
        recipientp.zoobars = recipient_balance
        bankdb.commit()

        transfer = Transfer()
        transfer.sender = sender
        transfer.recipient = recipient
        transfer.amount = zoobars
        transfer.time = time.asctime()

        transferdb = transfer_setup()
        transferdb.add(transfer)
        transferdb.commit()

    def rpc_balance(self, username):
        db = bank_setup()
        bank = db.query(Bank).get(username)
        return bank.zoobars

    def rpc_get_log(self, username):
        db = transfer_setup()
        log(username)
        logsList = db.query(Transfer).filter(or_(Transfer.sender==username, Transfer.recipient==username))
        log(logsList)
        return logsList

    def rpc_add_bank(self, username):
        bank = Bank()
        bank.username = username
        bankdb = bank_setup()
        bankdb.add(bank)
        bankdb.commit()
        

(_, dummy_zookld_fd, sockpath) = sys.argv

s = AuthRpcServer()
s.run_sockpath_fork(sockpath)

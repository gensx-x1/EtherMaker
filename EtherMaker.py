import datetime
import time
from eth_account import Account
import secrets


def generatePair():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    return acct


loop_count = 0
start_time = datetime.datetime.now()
with open('wallets', 'a') as file:
    while True:
        account = generatePair()
        file.write(f'{account.address}|{account.key.hex()}\n')
        loop_count += 1
        rate = loop_count/(datetime.datetime.now()-start_time).seconds
        print(f'loop: {loop_count}', end='\r')
        if loop_count == 10000:
            print(f'10k: {(datetime.datetime.now()-start_time).seconds} seconds')
        if loop_count == 100000:
            print(f'100k: {(datetime.datetime.now()-start_time).seconds} seconds')
        if loop_count == 1000000:
            print(f'1m: {(datetime.datetime.now()-start_time).seconds} seconds')


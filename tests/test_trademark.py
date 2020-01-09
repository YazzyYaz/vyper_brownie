from brownie import accounts
import logging


INITIAL_PHRASE = 'ETCVyper'
INITIAL_AUTHOR = 'Satoshi Nakamoto'

def test_trademark_deployment(trademark):
    t = accounts[0].deploy(trademark)
    logging.info(dir(t))
    assert t.address != None

def test_trademark_balance(trademark):
    assert trademark[0].balance != 0 

def test_trademark_is_none(trademark):
    logging.info(dir(trademark[0]))
    check = trademark[0].checkTrademark(INITIAL_PHRASE)
    assert check == False 

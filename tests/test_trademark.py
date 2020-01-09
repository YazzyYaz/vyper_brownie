from brownie import accounts
import logging


INITIAL_PHRASE = 'ETC&Vyper'
INITIAL_AUTHOR = 'Satoshi Nakamoto'

def test_trademark_deployment(trademark):
    t = accounts[0].deploy(trademark)
    assert t.address != None
    logging.info("Trademark Smart Contract Deployed")

def test_trademark_balance(trademark):
    assert trademark[0].balance != 0 
    logging.info("Trademark Smart Contract Has Balance")

def test_trademark_is_not_registered(trademark):
    check = trademark[0].checkTrademark(INITIAL_PHRASE)
    assert check == False
    logging.info(f"Trademark {INITIAL_PHRASE} NOT Registered Check Complete")

def test_register_trademark(trademark):
    register_tx = trademark[0].registerTrademark(INITIAL_PHRASE, INITIAL_AUTHOR)
    assert register_tx.return_value == True
    logging.info(f"Trademark {INITIAL_PHRASE} Registration By {INITIAL_AUTHOR} Has Been Submitted")
    assert register_tx.txid is not None
    logging.info(f"Trademark Registration Transaction ID is {register_tx.txid}")

def test_trademark_is_registered(trademark):
    check = trademark[0].checkTrademark(INITIAL_PHRASE)
    assert check == True
    logging.info(f"Trademarked Phrase {INITIAL_PHRASE} Has Been Registered")

def test_get_trademark_data(trademark):
    data = trademark[0].getTrademarkData(INITIAL_PHRASE)
    logging.info("Trademark Registration Data Found")
    logging.info(f"Trademark Phrase: {data[0]}")
    logging.info(f"Trademark Author: {data[1]}")
    logging.info(f"Trademark Registration Time: {data[2]}")
    logging.info(f"Trademark Registration Proof: {data[3]}")
    assert data[1] == INITIAL_AUTHOR

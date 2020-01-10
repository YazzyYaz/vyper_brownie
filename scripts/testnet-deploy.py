from brownie import *


def main():
    accounts.load('kotti-account')
    t = accounts[-1].deploy(trademark)
    t.balance()
    t.registerTrademark("Hakuna Matata", "Simon and Pumba")
    print(t.getTrademarkData("Hakuna Matata"))

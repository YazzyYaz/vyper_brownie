#!/usr/bin/env python
# -*- coding: utf-8 -*-
from brownie import *

def main():
    accounts[0].deploy(trademark)

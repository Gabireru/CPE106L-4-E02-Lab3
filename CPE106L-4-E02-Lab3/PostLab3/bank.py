#PostLab3

"""
The str method of the Bank class (in the file bank.py) returns a string containing the accounts in random order.
Design and implement a change that causes the accounts to be placed in the string by order of name.
(Hint: You will also have to define some methods in the SavingsAccount class, in the file savingsaccount.py.) (LO: 10.1, 10.2)
"""

"""
File: bank.py
This module defines the Bank class.
"""
import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savings accounts.
    An optional file name is also associated with the bank, to allow 
    transfer of accounts to and from permanent file storage."""

    def __init__(self, fileName=None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts."""
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            with open(fileName, 'rb') as fileObj:
                while True:
                    try:
                        account = pickle.load(fileObj)
                        self.add(account)
                    except EOFError:
                        break

    def __str__(self):
        """Returns the string representation of the bank."""
        sorted_accounts = sorted(self.accounts.values(), key=lambda account: account.getName())
        return "\n".join(map(str, sorted_accounts))

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank and returns it, or None if the account does not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank, or returns None if the account does not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the interest on all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def save(self, fileName=None):
        """Saves pickled accounts to a file. The parameter allows the user to change file names."""
        if fileName is not None:
            self.fileName = fileName
        elif self.fileName is None:
            return
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)

# Functions for testing remain unchanged.


   

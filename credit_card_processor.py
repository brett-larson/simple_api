"""
    Author: Brett Larson
    Date: 2020/10/07

    Description:
        This Python file represents the credit card processing vendor that the credit card app
        server calls to receive an approval or declined message. In this case, approval is based
        on the amount of the purchase.
"""

# Required imports
import random
import string


def approve_deny_transaction(data_dict):
    """
    This function approves transactions with a purchase value of less than 200 and greater than 0.
    :param data_dict: JSON PUT data stored in a dictionary
    :return: string "approve" or "decline"
    """
    approval = 'approve'

    amount = int(data_dict.get('purchase_amt'))

    if amount >= 200 or amount <= 0:
        approval = 'decline'

    return approval


def get_authorization_code():
    """
    Create an authorization code through the creation of a string of random letters and numbers
    :return: string authorization code
    """
    letters_numbers = string.ascii_letters + string.digits
    authorization_code = ''.join((random.choice(letters_numbers) for i in range(10)))

    return authorization_code

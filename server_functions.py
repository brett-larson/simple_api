"""
    Author: Brett Larson
    Date: 2020/10/07

    Description:
        This Python file acts as the back-end server of the credit card processing application. It
        receives data from the API server, sends it to the processing vendor for approval, and then
        returns the appropriate data to the API server.
"""

# required imports
from credit_card_processor import *


def get_authorization(data_dict):
    """
    This function calls other functions in this file to create a dictionary based on whether the
    transaction was approved or declined.
    :param data_dict: JSON data received from a POST request stored as a dictionary
    :return: Dictionary with appropriate information based on decision
    """

    approval = approve_deny_transaction(data_dict)
    masked_card_number = mask_credit_card(data_dict)
    if approval == 'approve':
        auth_code = get_authorization_code()
        decision_dict = build_approval_dict(approval, auth_code, masked_card_number)
    elif approval == 'decline':
        decision_dict = build_decline_dict(approval, masked_card_number)

    return decision_dict


def build_approval_dict(approval, auth_code, card_num):
    """
    Function that builds the dictionary when a card is approved.
    :param approval: approval status (should always be "approved" for this function)
    :param auth_code: generated authorization code
    :param card_num: Last four digits of the credit card number
    :return: dictionary with approval data
    """

    approval_dict = {"approval_status": approval,
                     "authorization_code": auth_code,
                     "last_four_card_number": card_num}

    return approval_dict


def build_decline_dict(approval, card_num):
    """
    Function that builds the dictionary when a card is approved.
    :param approval: approval status (should always be "decline" for this function)
    :param card_num: Last four digits of the credit card number
    :return: dictionary with decline data
    """

    decline_dict = {"approval_status": approval,
                    "last_four_card_number": card_num}

    return decline_dict


def mask_credit_card(data_dict):
    """
    Take the credit card number provided by the user, and truncate it to the last four numbers.
    :param data_dict: Dictionary provided by the customer
    :return: String containing the last four digits of the credit card number
    """

    credit_card_num = data_dict.get('card_number')
    last_four_num = credit_card_num[-4:]

    return last_four_num

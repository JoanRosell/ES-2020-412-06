from src.Validator import Validator
from src.User import User
from src.PaymentData import PaymentData
from .test_constants import *
import pytest


def test_validate_payment_info():
    """ Test case to check all the private functions of Validator with correct conditions


    EXPECTED BEHAVIOUR:
        The given variables match the checked regular expressions and return True
    """

    name = 'This Is a Good Test'
    dni = '12345678A'
    email = 'good_email@test.uab'
    mobile_number = '123456789'
    card_number = '1234 3456 5678 7890'
    security_code = '123'
    credit_card_type = ['VISA', 'MASTERCARD']

    assert Validator._validate_full_name(name) is not None
    assert Validator._validate_full_name(name) is True
    assert Validator._validate_dni(dni) is not None
    assert Validator._validate_dni(dni) is True
    assert Validator._validate_email(email) is not None
    assert Validator._validate_email(email) is True
    assert Validator._validate_mobile_number(mobile_number) is not None
    assert Validator._validate_mobile_number(mobile_number) is True
    assert Validator._validate_credit_card_number(card_number) is not None
    assert Validator._validate_credit_card_number(card_number) is True
    assert Validator._validate_credit_security_code(security_code) is not None
    assert Validator._validate_credit_security_code(security_code) is True
    assert Validator.validate_credit_card_type(credit_card_type[0]) is True
    assert Validator.validate_credit_card_type(credit_card_type[1]) is True


def test_validate_payment_info_error():
    """ Test case to check all the private functions of Validator with error conditions


    EXPECTED BEHAVIOUR:
        The given variables don't match the checked regular expressions and return False
    """

    name = "7his_1s-a Bad 7est"
    dni = '2EFC678A9'
    email = 'bad@e/mail@test uab'
    mobile_number = '123a56aa'
    card_number = '4568 98761 234 5698'
    security_code = 'a56'
    credit_card_type = 'EXPRESS'

    assert Validator._validate_full_name(name) is not None
    assert Validator._validate_full_name(name) is False
    assert Validator._validate_dni(dni) is not None
    assert Validator._validate_dni(dni) is False
    assert Validator._validate_email(email) is not None
    assert Validator._validate_email(email) is False
    assert Validator._validate_mobile_number(mobile_number) is not None
    assert Validator._validate_mobile_number(mobile_number) is False
    assert Validator._validate_credit_card_number(card_number) is not None
    assert Validator._validate_credit_card_number(card_number) is False
    assert Validator._validate_credit_security_code(security_code) is not None
    assert Validator._validate_credit_security_code(security_code) is False
    assert Validator.validate_credit_card_type(credit_card_type[0]) is False


def test_validate_billing_data_correct(default_user: User):
    """ Test case to check the validate_billing_data function with correct conditions


    EXPECTED BEHAVIOUR:
        Variables in given User instance match the checked regular expressions and return True
    """
    assert Validator.validate_billing_data(default_user) is True


def test_validate_billing_data_error(default_user: User):
    """ Test case to check the validate_billing_data function with error conditions


    EXPECTED BEHAVIOUR:
        Variables in given User instance don't match the checked regular expressions and return False
    """

    default_user.dni = '123A'
    assert Validator.validate_billing_data(default_user) is False


def test_validate_payment_data(default_payment_data):
    """ Test case to check the validate_payment_data function


    EXPECTED BEHAVIOUR:
        Variables in given PaymentData instance match the checked regular expressions and return False
    """

    assert Validator.validate_payment_data(default_payment_data.user_name, default_payment_data.card_number,
                                           default_payment_data.security_code) is True

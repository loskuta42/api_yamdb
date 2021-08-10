import datetime as dt

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def my_year_validator(value):
    if value > dt.datetime.now().year:
        raise ValidationError(('%(value)s is not a correct year!'),
                              params={'value': value},)


def email_validator(email):
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError(
            {'email': 'Введите корректный email.'}
        )

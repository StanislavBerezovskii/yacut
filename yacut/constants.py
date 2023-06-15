import string

SYMBOLS = string.ascii_letters + string.digits
LENGTH = 6
LINK_REGULAR = r'^[a-zA-Z\d]{1,16}$'
FIELD_NAMES = {'original': 'url', 'short': 'custom_id'}

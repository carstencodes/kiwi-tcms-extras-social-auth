#
# Copyright (c) 2022 Carsten Igel.
#
# This file is part of Social Auth Provider for Kiwi TCMS 
# (see https://github.com/carstencodes/kiwi-tcms-extras-social-auth).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

# This implementation is based on the excellent work of
# Alexander Todorov (atodorov).
# See original implementation at 
# https://github.com/kiwitcms/enterprise/blob/ff306f3e6578f3a3fd416aa957ec212d7f8e19eb/tcms_enterprise/pipeline.py

from typing import TYPE_CHECKING, Final

import string
import secrets
from io import StringIO

if TYPE_CHECKING:
    from social_core.backends.base import BaseAuth
    from social_core.strategy import BaseStrategy
    from django.contrib.auth.models import User

def set_random(
        strategy: 'BaseStrategy', # NOSONAR
        details: dict, # NOSONAR
        backend: 'BaseAuth', # NOSONAR 
        user: 'User' = None,
        *args: tuple[str, ...], # NOSONAR
        **kwargs, # NOSONAR
    ) -> None:
    if user is not None and 'is_new' in kwargs and bool(kwargs['is_new']):
        password: str = _get_random_password()
        user.set_password(password)
        user.save()

def _get_random_password() -> str:
    PASSWORD_LEN: Final[int] = 63
    ALPHABET: Final[str] = \
        string.ascii_letters \
        + string.digits \
        + string.punctuation
    with StringIO() as buffer:
        for _ in range(PASSWORD_LEN):
            c: str = secrets.choice(ALPHABET)
            buffer.write(c)
    
    return buffer.getvalue()

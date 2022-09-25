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

from typing import TYPE_CHECKING

from tcms.utils.permissions import initiate_user_with_default_setups

if TYPE_CHECKING:
    from social_core.backends.base import BaseAuth
    from social_core.strategy import BaseStrategy
    from django.contrib.auth.models import User

# This implementation is based on the excellent work of
# Alexander Todorov (atodorov).
# See original implementation at 
# https://github.com/kiwitcms/enterprise/blob/ff306f3e6578f3a3fd416aa957ec212d7f8e19eb/tcms_enterprise/pipeline.py

def init_defaults(
        strategy: 'BaseStrategy', # NOSONAR
        details: dict, # NOSONAR
        backend: 'BaseAuth', # NOSONAR
        user: 'User' = None, 
        *args: tuple[str, ...], # NOSONAR
        **kwargs) -> None:
    if user is not None and 'is_new' in kwargs and bool(kwargs.get('is_new')):
        initiate_user_with_default_setups(user)


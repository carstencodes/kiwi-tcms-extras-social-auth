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

from typing import Final, FrozenSet

from simpleicons.all import icons
from social_core import backends 
from django.template import Library

supported_providers: Final[FrozenSet[str]] = frozenset([
  mod.lower() for mod in dir(backends) if mod is not None and "__" not in mod
])
register: Library = Library()

# Icon: User.svg Provided by 
# Feather Icons
# Copyright (c) 2013-2017 Cole Bemis
# Published under MIT License
# SRC: https://github.com/feathericons/feather/tree/f81cd40fdcdd5e94f3f97eb670a5058e3aac528d
_USER_ICON="""
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
>
  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
  <circle cx="12" cy="7" r="4" />
</svg>
"""

@register.filter
def get_social_icon(backend: str) -> str:
    if backend in supported_providers:
        icon = icons.get(backend)
        if icon is not None:
            return icon.svg
    return _USER_ICON

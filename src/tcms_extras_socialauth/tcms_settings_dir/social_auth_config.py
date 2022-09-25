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

from tcms.settings.common import INSTALLED_APPS as COMMON_INSTALLED_APPS
from tcms.settings.common import TEMPLATES, DATABASES
from social_core.pipeline import DEFAULT_AUTH_PIPELINE

try:
    from tcms.settings.common import DEBUG
except ImportError:
    DEBUG = False

try:
    from tcms.settings.common import RAISE_EXCEPTIONS
except ImportError:
    RAISE_EXCEPTIONS = False

# Configuration according to https://python-social-auth.readthedocs.io/en/latest/configuration/django.html

_context_processors = []

if len(TEMPLATES) > 0:
    if 'OPTIONS' in TEMPLATES[0]:
        if 'context_processors' in TEMPLATES[0]['OPTIONS']:
            _context_processors = TEMPLATES[0]['OPTIONS']['context_processors']
        else:
            TEMPLATES[0]['OPTIONS']['context_processors'] = _context_processors
    else:
        TEMPLATES[0]['OPTIONS'] = { 'context_processors': _context_processors }
else:
    TEMPLATES = [ { 'OPTIONS': { 'context_processors': _context_processors } } ]
    
if 'social_django.context_processors.backends' not in \
        _context_processors:     
    _context_processors.append(  
        'social_django.context_processors.backends')

if 'social_django.context_processors.login_redirect' not in \
        _context_processors:     
    _context_processors.append(  
        'social_django.context_processors.login_redirect')

INSTALLED_APPS = COMMON_INSTALLED_APPS + [
    'social_django',
]

if 'default' in DATABASES \
        and 'ENGINE' in DATABASES['default'] \
        and DATABASES['default']['ENGINE'].endswith('postgresql'): 
    SOCIAL_AUTH_JSONFIELD_ENABLED = True
            
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_PIPELINE = list(DEFAULT_AUTH_PIPELINE)
SOCIAL_AUTH_PIPELINE.insert(
    1, 
    'tcms_plugin_social_auth.pipelines.mail.is_required',
)
SOCIAL_AUTH_PIPELINE.extend(
    (
        'tcms_plugin_social_auth.pipelines.password.set_random',
        'tcms_plugin_social_auth.pipelines.user.init_defaults',
    )
)

if RAISE_EXCEPTIONS and DEBUG:
    SOCIAL_AUTH_RAISE_EXCEPTIONS = True

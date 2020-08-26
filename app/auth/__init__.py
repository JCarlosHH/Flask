from flask import Blueprint


#url_prefix indica que todas las rutas que incien con /auth serán dirigidas a este blueprint
auth = Blueprint('auth',__name__,url_prefix='/auth')

from . import views
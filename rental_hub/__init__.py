from flask import Blueprint

rental_hub = Blueprint('rental_hub',__name__)

from . import views,forms
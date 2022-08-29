from ctypes.wintypes import VARIANT_BOOL
from statistics import variance
from wsgiref.validate import validator
from ..models import Variable

def get_variables():
    variables = Variable.objects.all()
    return variables
    
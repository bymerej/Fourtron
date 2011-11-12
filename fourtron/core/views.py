# Create your views here
from django.http import HttpResponse
from django.template import Context, loader
from fourtron.core.models import User

def index(request):
  t = loader.get_template('fourtron/index.html')
  c = Context({})  
  return HttpResponse(t.render(c))

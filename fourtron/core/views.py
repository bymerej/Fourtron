import oauth2 as oauth
import urlparse
import time
import simplejson

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import get_messages

from social_auth import __version__ as version

@login_required
def index(request):
	t = loader.get_template('fourtron/index.html')
	c = Context({'version': version, 'last_login': request.session.get('social_auth_last_login_backend')})
	return HttpResponse(t.render(c))

def oauth(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('index')
	else:
		return render_to_response('registration/login.html', {'version': version }, RequestContext(request))

def oauth_error(request):
    messages = get_messages(request)
    return render_to_response('registration/error.html', {'version': version, 'messages': messages}, RequestContext(request))

@login_required
def oauth_logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
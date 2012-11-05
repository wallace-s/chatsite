from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from chatbox.models import MessageForm, Message

def index(request):
	message = MessageForm()
	messages = Message.objects.all()
	if request.method == "POST":
		message = MessageForm(request.POST)
		if message.is_valid():
			message.save()
			return HttpResponseRedirect(".")
		else:
			return render_to_response('chatbox/index.html', {'message':message, 'messages': messages, 'error_message':"try again"}, context_instance=RequestContext(request))
	else:
		return render_to_response('chatbox/index.html', {'message':message, 'messages': messages}, context_instance=RequestContext(request))
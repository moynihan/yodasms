from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from mashup.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_PHONE_NUMBER, X_MASHAPE_KEY
from twilio.rest import TwilioRestClient
import unirest

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = request.POST
        # if phone exists, the send message
        if 'phone' in data:
            try:
                client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                sms = client.sms.messages.create(body=data['message'],
                    to='+1' + data['phone'],
                    from_="+1" + TWILIO_FROM_PHONE_NUMBER)
                print sms.sid
                context = RequestContext(request, {
                    'title': 'test title',
                })
                return HttpResponseRedirect('/sent/')
            except Exception as e:
                return HttpResponse(e)
        # else if phone doesn't exist, but still a post, then translate the message
        else:
            try:

                response = unirest.get("https://yoda.p.mashape.com/yoda?sentence=" + data['message'],
                                       headers={"X-Mashape-Key": X_MASHAPE_KEY}
                )
                context = RequestContext(request, {
                    'title': 'test title',
                    'response': response,
                })
                template = loader.get_template('yodasms/send.html')
                return HttpResponse(template.render(context))
            except Exception as e:
                return HttpResponse(e)
    # if method not post, then
    else:
        #return HttpResponseRedirect('/')
        template = loader.get_template('yodasms/index.html')
        context = RequestContext(request, {
            'title': 'Send a Message',
        })
        return HttpResponse(template.render(context))

def sent(request):
    template = loader.get_template('yodasms/sent.html')
    context = RequestContext(request, {
        # No context
    })
    return HttpResponse(template.render(context))
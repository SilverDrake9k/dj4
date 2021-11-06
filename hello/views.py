from django.shortcuts import HttpResponse
from django.template.response import TemplateResponse
# Create your views here.


def main(request):
    resp =TemplateResponse(request, 'home/main.html', {})
    resp.set_cookie('dj4e_cookie', '05d6a571', max_age=1000)
    return resp

def hello(request):
    num_count =request.session.get('num_count',0)+1
    request.session['num_count'] = num_count
    resp = HttpResponse('<body>view count={}</body>'.format(num_count))
    resp.set_cookie('dj4e_cookie', '05d6a571', max_age=1000)
    return resp
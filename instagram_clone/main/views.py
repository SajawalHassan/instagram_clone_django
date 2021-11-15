from django.shortcuts import render

def header(req):
    return render(req, 'header.html', {})

#I have created this file
from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('About Page')

def analyze(request):

    punc = string.punctuation
    dj_text = request.POST.get('text',  'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    analyzed = ''
    if removepunc == "on":
        for char in dj_text:
            if char not in punc:
                analyzed += char
        params = {
            'purpose': 'Removed Punctuations',
            'analyze_text': analyzed
        }
        dj_text = analyzed
    if(fullcaps == 'on'):
        analyzed = ''
        for char in dj_text:
            analyzed += char.upper()
            params = {
                'purpose': 'Change to Uppercase',
                'analyze_text': analyzed
            }
        dj_text = analyzed

    if(newlineremover == 'on'):
        analyzed = ''
        for char in dj_text:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {
                    'purpose': 'Remove the new line',
                    'analyze_text': analyzed
                }
        dj_text = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(dj_text):
            if not(dj_text[index] == " " and dj_text[index+1] == " "):
                analyzed += char
        params = {
            'purpose': 'Remove Extra Spacing',
            'analyze_text': analyzed
        }
        dj_text = analyzed

    if (charcount == 'on'):
        count = int()
        for char in range(len(dj_text)):
            count = char
        params = {
            'purpose': 'Character Count',
            'analyze_text': count
        }

    if removepunc == "on" or fullcaps == 'on' or newlineremover == 'on' or extraspaceremover == 'on' or charcount == 'on':
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Please check the box to remove the punctuations..<a href="/">Go Back</a>')

'''
def removepunc(request):
    return HttpResponse('Remove Punc')

def capfirst(request):
    return HttpResponse('Capitalize First')

def newlineremove(request):
    return HttpResponse('Remove New Line')

def spaceremove(request):
    return HttpResponse('Remove Space')

def charcount(request):
    return HttpResponse(' Character Count ')
'''



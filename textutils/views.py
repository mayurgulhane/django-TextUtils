from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    text=request.POST.get('text')
    removepunc=request.POST.get('removepunc','off')
    fullCap=request.POST.get('fullCap','off')
    linermv=request.POST.get('linermv','off')
    spacermv=request.POST.get('spacermv','off')
    charCount=request.POST.get('charCount','off')
    params={}

    if removepunc == 'on':
        punc= '''!()-[]{}; +:'"\,<>./?@#$%^&*_~'''
        analyzed=" "
        for char in text:
            if char not in punc:
                analyzed = analyzed  +  char

        params={'purpose': 'Remove Punctuations', 'analyzed':analyzed }
        text = analyzed
     
       
    if (fullCap == 'on'):
        analyzed=" "
        for char in text:
            analyzed=analyzed + char.upper()
        params={ 'purpose': 'Changed to Uppercase', 'analyzed':analyzed }
        text = analyzed
        

    if (linermv == 'on'):
        analyzed=""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params={'purpose': 'Removed New Lines', 'analyzed':analyzed }
        text = analyzed
        

    if(spacermv=="on"):
        analyzed=""
        for index, char in enumerate(text):
            print(text)
            if not(text[index] == " " and text[index + 1]== " "):
                analyzed = analyzed + char
        params={'purpose': 'Removed New Lines', 'analyzed':analyzed }
        text = analyzed
        
    
    if (charCount == 'on'):
        analyzed=" "
        for char in text:
                analyzed= len(text)
        params={'purpose': 'Chatracter Count', 'analyzed':analyzed }
        
        
    if (removepunc != 'on' and fullCap !=  'on' and linermv !=  'on' and spacermv != 'on' and charCount !=  'on'):
        return HttpResponse('''<h1>please select any operation and try again</h1>''')


    return render(request,"analyze.html",params)


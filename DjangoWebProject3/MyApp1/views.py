from django.shortcuts import render   # Added for this step
from datetime import datetime
def about(request):
    return render(
        request,
        "MyApp1/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )
def index(request):
    now = datetime.now()

    return render(
        request,
        "MyApp1/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
             'title' : "cipa",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")        }
    )

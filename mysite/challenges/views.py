from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Learn Django for at least 20 minutes every day!",
    "may": "Learn Django for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Learn Django for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Learn Django for at least 20 minutes every day!",
    "december": None

}

def index(request):
     list_items =""
     months = list(monthly_challenges.keys())




     for month in months:
          capitalized_month = month.capitalize()
          month_path = reverse("month-challenge", args=[month])
          list_items+= f"<li> <a href=\"{month_path}\">{capitalized_month}</a></li>"
          

     response_data= f"<ul>{list_items}</ul>"
     return HttpResponse(response_data)

     return render(request, "challenges/index.html",{
        "months" : months 
     } )

def monthly_challenge_by_number(request, month):
    months = list (monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_part =reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_part)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render (request, "challenges/challenge.html", {
             "text": challenge_text,
             "month_name": month
        })
    except:
        raise Http404()
            

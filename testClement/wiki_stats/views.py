# 3rd Party imports
#----------------------------
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from wiki_stats.services import get_summary, check_words
# Local imports
#----------------------------
from testClement.settings import EMAIL_HOST_USER

# List of email address that will receive the email warning message
RECIPIENT = ['email.address@gmail.com']

def index(request):
    """Homepage view"""

    return HttpResponse("Welcome to WikiStats")

def summary(request, title):
    """Get summary using wikipedia page title"""

    summary = get_summary(request=request, title=title)
    if summary: response = HttpResponse(summary, status=200)
    else:
        response = HttpResponse(f'No wikipedia page was found for {title}', status=404)
    return response


def long_words(request, title):
    """Check for long words in the summary"""

    summary = get_summary(request=request, title=title)
    if not summary: response = HttpResponse(f'No wikipedia page was found for {title}', status=404)
    else:
        contain_long_words = check_words(request=request, summary=summary)
        if contain_long_words:
            messages.success(request, 'More than 20 percents words of this summary are 5+ letters')
            send_mail(
                subject='WikiStats',
                message='The summary of '+ title +' contains more than 20 percents of 5+ letters words',
                from_email=EMAIL_HOST_USER,
                recipient_list=RECIPIENT
            )
            response = HttpResponse(f'An email was send to {RECIPIENT}')
        else:
            response = HttpResponse(f'The summary of {title} contains less than 20 percent 5+ letters words')

    return response
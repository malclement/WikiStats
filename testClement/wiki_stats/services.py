# Standard Library imports
#----------------------------
import requests

# wikipedia api link for summary interactions
wikipedia_summary = "https://en.wikipedia.org/api/rest_v1/page/summary/"

def get_summary(request, title: str)-> str:
    """Fetch summary section of a wikipedia page by passing title argument"""
    
    summary = requests.get(wikipedia_summary+title).json().get('extract')
    return summary

def check_words(request, summary:str)-> bool:
    """
    Check word lenght in the summary
    Returns : 
    - True if more than 20% of the words or 5+ letters
    - False otherwise
    """

    summary_words = summary.split()
    long_words: int = 0
    for i in summary_words:
        if len(i)>5 : long_words += 1
    if long_words/len(summary_words)>0.2:
        return True
    return False
    
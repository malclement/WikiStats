# 3rd Party imports
#----------------------------
from django.urls import path
# Local imports
#----------------------------
from wiki_stats import views

urlpatterns = [
    # ex: /wikistats/
    path('', views.index, name='index'),
    # ex: /wikistats/Camus
    # Warning: Spaces in the title should be replaced with uderscores
    path('<str:title>', views.summary, name='summary'),
    # ex: /wikistats/Camus/words
    # Warning: Spaces in the title should be replaced with uderscores
    path('<str:title>/words', views.long_words, name='long_words')
]
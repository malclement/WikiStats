# 3rd Party imports
#----------------------------
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wikistats/', include('wiki_stats.urls'))
]

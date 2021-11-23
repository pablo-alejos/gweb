from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import grid

urlpatterns = [
    path('', login_required(grid.as_view()), name='grid'),
]
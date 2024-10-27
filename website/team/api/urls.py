from django.urls import path

from .views import (
    ListCreateMembersView,
    AlumniYearWiseView
)

app_name = 'team_api'

urlpatterns = [
    path('', ListCreateMembersView.as_view(), name='members_list'),
    path('alumni/', AlumniYearWiseView.as_view(), name='alumni_year_wise'),
]

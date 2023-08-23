from django.urls import path
from .views import CreateTeamView, ListTeamView

urlpatterns = [
    path('teams/', CreateTeamView.as_view()),
    path('teams/<int:team_id>/', ListTeamView.as_view())
]
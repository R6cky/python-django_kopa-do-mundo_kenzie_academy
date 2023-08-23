from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict 
from utils import data_processing
from exceptions import ImpossibleTitlesError,InvalidYearCupError,NegativeTitlesError

# Create your views here.

class CreateTeamView(APIView):
    def post(self, request):
        team_data = request.data
        try:
            data_processing(team_data)
        except (ImpossibleTitlesError,InvalidYearCupError,NegativeTitlesError) as error:
            return Response({"error": error.args[0]}, 400)

        team = Team.objects.create(
            name = team_data['name'],
            titles = team_data['titles'],
            top_scorer = team_data['top_scorer'],
            fifa_code = team_data['fifa_code'],
            first_cup = team_data['first_cup']
        )
        return Response(model_to_dict(team), 201)

    def get(self, request):
        teams = Team.objects.all()
        team_dict = []

        for i in teams:
            t = model_to_dict(i)
            team_dict.append(t)
        return Response(team_dict, 200)

    



class ListTeamView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message":"Team not found"}, 404)
        
        team_dict = model_to_dict(team)
        return Response(team_dict, 200)
    

    def patch(self, request, team_id):
        team_data = request.data
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message":"Team not found"}, 404)
        
        for key, value in team_data.items():
            setattr(team, key, value)

        team.save()
        
        return Response(model_to_dict(team), 200)



    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message":"Team not found"}, 404)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
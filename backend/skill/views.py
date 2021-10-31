from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from skill.models import Skill, Details
from skill.serializers import SkillSerializer, DetailsSerializer


@csrf_exempt
def skillApi(request, id=0):
    if request.method=='GET':
        skill = Skill.objects.all()
        skill = skill.order_by('-StartDate','Name')     
        skill_serializer = SkillSerializer(skill, many=True)
        return JsonResponse(skill_serializer.data, safe=False)

    elif request.method=='POST':
        skill_data=JSONParser().parse(request)
        skill_serializer=SkillSerializer(data=skill_data)
        if skill_serializer.is_valid():
            skill_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse("Failed")

    elif request.method=='PUT':
        skill_data=JSONParser().parse(request)
        skill=Skill.objects.get(SkillId=skill_data['SkillId'])
        skill_serializer=SkillSerializer(skill,data=skill_data)
        if skill_serializer.is_valid():
            skill_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        skill=Skill.objects.get(SkillId=id)
        skill.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def details_all(request):
    if request.method=='GET':
        details = Details.objects.all()            
        details_serializer = DetailsSerializer(details, many=True)
        return JsonResponse(details_serializer.data, safe=False)
    elif request.method=='POST':
        details_data=JSONParser().parse(request)
        details_serializer=DetailsSerializer(data=details_data)
        if details_serializer.is_valid():
            details_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse("Failed")
        

@csrf_exempt
def detailsApi(request, slug = None):
    if request.method=='GET':
        """ details = Details.objects.all()            
        details_serializer = DetailsSerializer(details, many=True)
        return JsonResponse(details_serializer.data, safe=False) """
        details = Details.objects.filter(Slug=slug)
        details = details.order_by('-DetailId')           
        details_serializer = DetailsSerializer(details, many=True)
        return JsonResponse(details_serializer.data, safe=False)






    



from rest_framework import serializers
from skill.models import Skill, Details


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['SkillId','Name', 'Slug', 'StartDate', 'EndDate', 'Level', 'devops']

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['DetailId','Name', 'Slug', 'StartDate', 'EndDate', 'Description']



from rest_framework import serializers
from .models import *



class MOCSerializer(serializers.ModelSerializer):
    class Meta:                 
        model = MOC
        fields = "__all__"
    
    
class StatusSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Status
        fields = "__all__"
        
        
class BillSubjectAreaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BillSubjectArea
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Bill
        fields = "__all__"
        
class SponsorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Sponsor
        fields = "__all__"
        depth = 1
        
class VotesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Votes
        fields = "__all__"
        
        
class VotingRecordSerializer(serializers.ModelSerializer):
    class Meta: 
        model = VotingRecord
        fields = "__all__"
        
        
class UserVotingHistorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserVotingHistory
        fields = "__all__"
        
        
class SavedBillSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SavedBill
        fields = "__all__"
        
        
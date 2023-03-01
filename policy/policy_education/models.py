from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MOC(models.Model):
    
    PARTY_CHOICES = [
        ('republican', 'Republican'),
        ('democrat', 'Democrat'),
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    picture = models.ImageField(blank=True)
    first_election = models.CharField(max_length=255,blank=True)
    next_election = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    party = models.CharField(choices= PARTY_CHOICES, max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=False, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    
class Status(models.Model):
    
    lable = models.CharField(max_length=255)
    description = models.TextField(max_length=2550, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)    
    
    
class BillSubjectArea(models.Model):
    
    AREAS =[
        ('bijainagar', 'bijainagar'),
        ('goa', 'Goa'),
    ]
    
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sub_topics = models.ManyToManyField("self", blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.slug

class Bill(models.Model):
    
    TYPE_CHOICES = [
        ('lagisation', 'Lagisation'),
        ('bill', 'Bill'),
    ]
    title = models.CharField(max_length=255)
    bill_file = models.FileField()
    summary = models.TextField(max_length=3000)
    subject_areas = models.ManyToManyField(BillSubjectArea)
    introduced = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    bill_type = models.CharField(choices= TYPE_CHOICES ,max_length=255)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)


class Sponsor(models.Model):
    
    SPONSOR_CHOICES = [
        ('sponsor', 'Sponsor'),
        ('co-sponsor', 'Co-Sponsor')
    ]
    
    type = models.CharField(choices=SPONSOR_CHOICES, max_length=255)
    sponsor = models.ForeignKey(MOC, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
class Votes(models.Model):
    
    VOTING_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    STATE_CHOICES = [
        ('Alabama', 'Alabama'),
        ('Alaska', 'Alaska'),
        ('Arizona', 'Arizona'),
        ('Arkansas', 'Arkansas'),
        ('California', 'California'),
        ('Colorado', 'Colorado'),
        ('Connecticut', 'Connecticut'),
        ('Delaware', 'Delaware'),
        ('Florida', 'Florida'),
        ('Georgia', 'Georgia'),
        ('Hawaii', 'Hawaii'),
        ('Idaho', 'Idaho'),
        ('Illinois', 'Illinois'),
        ('Indiana', 'Indiana'),
        ('Iowa', 'Iowa'),
        ('Kansas', 'Kansas'),
        ('Kentucky', 'Kentucky'),
        ('Louisiana', 'Louisiana'),
        ('Maine', 'Maine'),
        ('Maryland', 'Maryland'),
        ('Massachusetts', 'Massachusetts'),
        ('Michigan', 'Michigan'),
        ('Minnesota', 'Minnesota'),
        ('Mississippi', 'Mississippi'),
        ('Missouri', 'Missouri'),
        ('Montana', 'Montana'),
        ('Nebraska', 'Nebraska'),
        ('Nevada', 'Nevada'),
        ('NewHampshire', 'NewHampshire'),
        ('NewJersey', 'NewJersey'),
        ('NewMexico', 'NewMexico'),
        ('NewYork', 'NewYork'),
        ('NorthCarolina', 'NorthCarolina'),
        ('NorthDakota', 'NorthDakota'),
        ('Ohio', 'Ohio'),
        ('Oklahoma', 'Oklahoma'),
        ('Oregon', 'Oregon'),
        ('Pennsylvania', 'Pennsylvania'),
        ('RhodeIsland', 'RhodeIsland'),
        ('SouthCarolina', 'SouthCarolina'),
        ('SouthDakota', 'SouthDakota'),
        ('Tennessee', 'Tennessee'),
        ('Texas', 'Texas'),
        ('Utah', 'Utah'),
        ('Vermont', 'Vermont'),
        ('Virginia', 'Virginia'),
        ('Washington', 'Washington'),
        ('West Virginia', 'West Virginia'),
        ('Wisconsin', 'Wisconsin'),
        ('Wyoming', 'Wyoming'),
    ]
    
    PARTY_CHOICES = [
        ('republican', 'Republican'),
        ('deemocrat', 'Democrat'),
        ('indipendent', 'Indipendent'),
    ]

    vote = models.CharField(choices = VOTING_CHOICES, max_length=255)
    state = models.CharField(max_length=255, choices=STATE_CHOICES) 
    repersentative = models.ForeignKey(MOC, on_delete=models.CASCADE)    
    party = models.CharField(choices= PARTY_CHOICES ,max_length=255)
    description = models.TextField(max_length=2550)
    short_text = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
class VotingRecord(models.Model):
    
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.CharField(max_length=255)
    votes = models.ManyToManyField(Votes)
    
    
class UserVotingHistory(models.Model):
    
    VOTE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vote = models.CharField(choices=VOTE_CHOICES ,max_length=255)
    voting_record = models.ForeignKey(VotingRecord, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
        
        
class SavedBill(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)

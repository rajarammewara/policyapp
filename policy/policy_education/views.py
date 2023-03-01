from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q
import csv
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated
from .serializer import MOCSerializer, StatusSerializer, BillSubjectAreaSerializer, BillSerializer, SponsorSerializer, VotesSerializer, VotingRecordSerializer, UserVotingHistorySerializer, SavedBillSerializer
from .models import MOC, Status as StatusModel, BillSubjectArea, Bill, Sponsor, Votes as VotesModel, VotingRecord, UserVotingHistory, SavedBill

# Create your views here.
import os
from django.conf import settings

class Moc(APIView, IsAuthenticated):

    serializer_class = MOCSerializer

    def get(self, request):
        data = []
        
        with open(os.path.join(settings.BASE_DIR, 'moc_data.csv'), mode = 'r') as file:
    
            filecsv = csv.DictReader(file)
    
            for mocdata in filecsv:
                print(mocdata)
            
        all_moc = MOC.objects.create(data)
        
        all_moc = MOC.objects.all()
        
        search_query = request.query_params.get('search') #search by first name and last name
        order_query = request.query_params.get('ordering') #ordering by working distance in kms
        
        perpage = request.query_params.get('perpage') #pagination perpage
        page = request.query_params.get('page') #pagination page

        
        if search_query:
            all_moc = MOC.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
            
        if order_query:
            all_moc = MOC.objects.order_by(search_query)

        if perpage:
            paginator = Paginator(all_nurse, per_page=perpage)

            try:
                all_nurse = paginator.page(number=page)
            except EmptyPage:
                all_moc = []

        serializer = MOCSerializer(all_moc, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = MOCSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 
    
class SingleMoc(generics.RetrieveUpdateAPIView, IsAuthenticated):
    
    queryset = MOC.objects.all()
    serializer_class = MOCSerializer
  

class Status(APIView, IsAuthenticated):

    serializer_class = StatusSerializer

    def get(self, request):
        all_status = StatusModel.objects.all()
        
        order_query = request.query_params.get('ordering') #ordering by working distance in kms

        if order_query:
            all_status = StatusModel.objects.order_by(order_query)
           
        serializer = StatusSerializer(all_status, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = StatusSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 

class SingleStatus(generics.RetrieveUpdateAPIView, IsAuthenticated):
    
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer
  

class BillSubjectAreas(APIView, IsAuthenticated):

    serializer_class = BillSubjectAreaSerializer

    def get(self, request):
        all_billarea = BillSubjectArea.objects.all()
        
        order_query = request.query_params.get('ordering') #ordering by working distance in kms

        if order_query:
            all_billarea = BillSubjectArea.objects.order_by(order_query)
           
        
        serializer = BillSubjectAreaSerializer(all_billarea, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = BillSubjectAreaSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 
    

class Bills(APIView, IsAuthenticated):

    serializer_class = BillSerializer

    def get(self, request):
        all_bill = Bill.objects.all()
        
        search_query = request.query_params.get('search') #search by first name and last name
        order_query = request.query_params.get('ordering') #ordering by working distance in kms
        
        perpage = request.query_params.get('perpage') #pagination perpage
        page = request.query_params.get('page') #pagination page

        if search_query:
            all_bill = Bill.objects.filter(source__icontains=search_query)
            
        if order_query:
            all_bill = BillSubjectArea.objects.order_by(order_query)
        
        if perpage:
            paginator = Paginator(all_nurse, per_page=perpage)

            try:
                all_nurse = paginator.page(number=page)
            except EmptyPage:
                all_bill = []  

        serializer = BillSerializer(all_bill, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = BillSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 
        
    queryset = BillSubjectArea.objects.all()
    serializer_class = BillSubjectAreaSerializer
  
    
class Sponsors(APIView, IsAuthenticated):

    serializer_class = SponsorSerializer

    def get(self, request):
        all_sponsore = Sponsor.objects.all()
        
        search_query = request.query_params.get('search') #search by first name and last name
        order_query = request.query_params.get('ordering') #ordering by working distance in kms
        
        perpage = request.query_params.get('perpage') #pagination perpage
        page = request.query_params.get('page') #pagination page
        
        if search_query:
            all_sponsore = Sponsor.objects.filter(type__icontains=search_query)
            
        if order_query:
            all_sponsore = Sponsor.objects.order_by(order_query)
            
        if perpage:
            paginator = Paginator(all_nurse, per_page=perpage)

            try:
                all_nurse = paginator.page(number=page)
            except EmptyPage:
                all_sponsore = []
            
        serializer = SponsorSerializer(all_sponsore, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = SponsorSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 
    
class Votes(APIView, IsAuthenticated):

    serializer_class = VotesSerializer

    def get(self, request):
        all_votes = VotesModel.objects.all()
        
        search_query = request.query_params.get('search') #search by first name and last name
        order_query = request.query_params.get('ordering') #ordering by working distance in kms
        
        if search_query:
            all_votes = VotesModel.objects.filter(type__icontains=search_query)
        
        if search_query:
            all_votes = VotesModel.objects.order_by(order_query)
        
        
        serializer = VotesSerializer(all_votes, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = VotesSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 
    
 
class VotingRecords(APIView, IsAuthenticated):

    serializer_class = VotingRecordSerializer

    def get(self, request):
        all_uservoting = VotingRecord.objects.all()
        
        search_query = request.query_params.get('search') #search by first name and last name
        order_query = request.query_params.get('ordering') #ordering by working distance in kms
        
        if search_query:
            all_sponsor = VotingRecord.objects.filter(title__icontains=search_query)
            
        serializer = VotingRecordSerializer(all_uservoting, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = VotingRecordSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 
    
        
class UserVotingHistories(APIView, IsAuthenticated):

    serializer_class = UserVotingHistorySerializer

    def get(self, request):
        all_votinghistory = UserVotingHistory.objects.all()
        
        search_query = request.query_params.get('search') #search by first name and last name
        order_query = request.query_params.get('ordering') #ordering by working distance in kms
        
        if search_query:
            all_votinghistory = UserVotingHistory.objects.filter(vote__icontains=search_query)
        
        if order_query:
            all_votinghistory = UserVotingHistory.objects.order_by(order_query)
            
        serializer = UserVotingHistorySerializer(all_votinghistory, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = UserVotingHistorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 
    
class SingleUserVotingHistories(generics.RetrieveUpdateDestroyAPIView, IsAuthenticated):
    
    queryset = UserVotingHistory.objects.all()
    serializer_class = UserVotingHistories
      
    
class SavedBills(APIView, IsAuthenticated):
    

    serializer_class = SavedBillSerializer

    def get(self, request):
        all_savebill = SavedBill.objects.all()
        
        search_query = request.query_params.get('search') #search by first name and last name
        order_query = request.query_params.get('ordering') #ordering by working distance in kms

        perpage = request.query_params.get('perpage') #pagination perpage
        page = request.query_params.get('page') #pagination page

        
        if search_query:
            all_savebill = SavedBill.objects.filter(user_name__icontains=search_query)
            
        if search_query:
            all_savebill = SavedBill.objects.order_by(search_query)
            
        if perpage:
            paginator = Paginator(all_nurse, per_page=perpage)

            try:
                all_nurse = paginator.page(number=page)
            except EmptyPage:
                all_savebill = []
            
        serializer = SavedBillSerializer(all_savebill, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        serializer = SavedBillSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 200) 

class SingleSavedBills(generics.RetrieveUpdateDestroyAPIView, IsAuthenticated):
    
    queryset = SavedBill.objects.all()
    serializer_class = SavedBillSerializer
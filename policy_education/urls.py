from django.urls import path

from . import views 

urlpatterns = [
    path('profile', views.Moc.as_view()),
    path('singlemoc', views.SingleMoc.as_view()),
    path('status/', views.Status.as_view()),
    path('singlestatus/', views.SingleStatus.as_view()),
    path('billsubjectarea/', views.BillSubjectAreas.as_view()),
    path('bill/', views.Bills.as_view()),
    path('sponsor/', views.Sponsors.as_view()),
    path('votes/', views.Votes.as_view()),
    path('votingrecords/', views.VotingRecords.as_view()),
    path('uservotinghistory/', views.UserVotingHistories.as_view()),
    path('savedbills/', views.SavedBills.as_view()),
    path('singlesavedbills/', views.SingleSavedBills.as_view()),
]
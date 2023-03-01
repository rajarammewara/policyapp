from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MOC)
admin.site.register(Status)
admin.site.register(BillSubjectArea)
admin.site.register(Bill)
admin.site.register(Sponsor)
admin.site.register(Votes)
admin.site.register(VotingRecord)
admin.site.register(UserVotingHistory)
admin.site.register(SavedBill)

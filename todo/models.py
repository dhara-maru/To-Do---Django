from django.db import models
from django.contrib.auth.models import User
# from db_connection import db

# user_collection = db['user']


class todoclass(models.Model):
    srno = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s | %s | %s" %(self.srno, self.user, self.title)
    
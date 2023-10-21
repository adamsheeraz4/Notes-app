from django.db import models

# Create your models here.

class Note(models.Model):
    # the null and blank allow us to submit an empy note
    body = models.TextField(null=True,blank=True)
    #auto_now keeps track of each time when we save/update a note
    updated = models.DateField(auto_now=True)
    #auto_now_add only takes timestamp when first created while
    #auto_now takes it each time we save/update
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        #only return the first 50 characters of body
        return self.body[0:50]
    
from django.db import models
from django.dispatch import receiver

from django.db.models.signals import post_save,pre_save
from django.core.mail import EmailMessage
from django.conf import settings

import string 
import random 
import threading
# Create your models here.

class EmailThread(threading.Thread):

	def __init__(self,email):
		self.email=email
		threading.Thread.__init__(self)

	def run(self):
		self.email.send(fail_silently=True)


class Feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(null=False)
    subject=models.CharField(max_length=100,null=False)
    message=models.TextField(max_length=1000,null=False)

@receiver(post_save,sender=Feedback)
def generate_feedback(sender,instance=None,created=False,**kwargs):
    if created:
        subject="Thank You For feedback"
        body="Thank Your for visiting my page and once more thanks for the feedback"
        message="Hi "+str(instance.name)+",\n"+str(body)+"\nIgnore(if not used Portfolio arsenal(G)"
        to_list=[instance.email]
        email = EmailMessage(
                            subject,
                            message,
                            'gauravshinde696969@gmail.com',
                            to_list
                            )
        EmailThread(email).start()
        #commented for now to avoid sending emails

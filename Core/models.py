from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.

class Messages(models.Model):
    ip = models.CharField("IP Address",max_length=50)
    fname = models.CharField("First Name",max_length=100)
    lname = models.CharField("Last Name",max_length=100)
    email = models.CharField("Email Address",max_length=100)
    message = models.TextField("Message")

    def __str__(self):
        return 'Message from '+self.fname
    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Messages'


class GroupAR(models.Model):
    groupName = models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.groupName
    class Meta:
        verbose_name = 'AR VR Groups'
        verbose_name_plural = 'AR VR Groups'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groupAssociated = models.ManyToManyField(GroupAR)
    name = models.CharField(default = 'Default Name',max_length=30)
    image= models.ImageField(default = 'default.jpg', upload_to='profile_pic')
    phoneNumber = models.IntegerField("Phone Number",blank=True,default='5412781925')
    score = models.IntegerField("Score",blank=True,default=0)
    workLink = models.CharField("Link of Portfolio", max_length=500,blank=True)
    I = 'I Year'
    II = 'II Year'
    year = [(I, 'I Year'),(II, 'II Year')]
    year = models.CharField(max_length=20,choices=year)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
       super().save() 
       img = Image.open(self.image.path)
       if img.height>300 or img.width>300:
           output_size = (300,300)
           img.thumbnail(output_size)
           img.save(self.image.path)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ManyToManyField(GroupAR)
    taskCode = models.CharField(max_length=50)
    taskHeading = models.CharField(max_length=200)
    taskContent = models.TextField()
    startDate = models.DateTimeField(default=timezone.now)
    lastDate = models.DateTimeField(default=timezone.now)
    taskScore = models.IntegerField(blank=False)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.taskCode
    class Meta:
        verbose_name = 'Tasks'
        verbose_name_plural = 'Tasks'

class TaskStatus(models.Model):
    taskCode = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    PENDING = 'Pending'
    COMPLETE = 'Completed'
    state = [(PENDING, 'Pending'),(COMPLETE, 'Completed')]
    status = models.CharField(max_length=20,choices=state,default=PENDING)

    def __str__(self):
        return self.taskCode.taskCode + self.user.username
    
    class Meta:
        verbose_name = 'User Task Status'
        verbose_name_plural = 'User Task Status'

class Meetings(models.Model):
    meetCode = models.CharField("Meeting Code",max_length=50)
    meetHeading = models.CharField("Heading",max_length=100)
    meetPurpose = models.TextField("Purpose")
    meetDate = models.DateTimeField("Date and Time",default=timezone.now)
    meetVenue = models.CharField("Venue",max_length=100)
    meetGroup = models.ManyToManyField(GroupAR)
    meetAttendance = models.ManyToManyField(User)

    def __str__(self):
        return self.meetCode
    
    class Meta:
        verbose_name = 'Meetings'
        verbose_name_plural = 'Meetings'
from django.db import models
from django.contrib.auth.models  import User 
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    dp= CloudinaryField('image')
    email=models.CharField(max_length=150)

    def __str__(self):
        return self.user.username


class Neighborhoods_cool(models.Model):
    name=models.CharField(max_length=200)
    picture= CloudinaryField('image')
    location = models.CharField(max_length=200)
    admin=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    occupants_count=models.ManyToManyField(User,related_name='participants',blank=True)
    description=models.TextField(null=True,blank=True)
    health_contact = models.IntegerField()
    police_contact = models.IntegerField()
    update= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def create_neighborhood(self):
        self.save()
    
    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def update_neighborhood(self,cls):
        self.name= cls
        self.save()

    @classmethod
    def find_neighborhood(cls,name):
        neighborhoods = Neighborhoods_cool.objects.filter(name__icontains=name).all()
        return neighborhoods
    


    class Meta:
        ordering = ['-update','-created']

    def __str__(self):
        return self.name 


class Businesses(models.Model):
    name = models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.CharField(max_length=150)
    neighborhood=models.ForeignKey(Neighborhoods_cool,on_delete=models.CASCADE)

    def create_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()

    @classmethod
    def update_business(self,cls):
        self.name= cls
        self.save()

    def __str__(self):
        return self.name

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room= models.ForeignKey(Neighborhoods_cool, on_delete=models.CASCADE)
    body= models.TextField()
    update= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update','-created']


    def __str__(self):
        return self.body[0:50]
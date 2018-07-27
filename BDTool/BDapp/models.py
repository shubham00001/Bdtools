from django.db import models

# Create your models here.
class Technology(models.Model):
    technology_name=models.CharField(max_length=50)

    def __str__(self):
        return self.technology_name


class Client(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    skype_id=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    country=models.CharField(max_length=50)
    phone_no=models.IntegerField(default=0)
    active =models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class Project(models.Model):
    project_name=models.CharField(max_length=50)
    url_name=models.CharField(max_length=100)
    domain_name=models.CharField(max_length=100)
    project_desrciption=models.CharField(max_length=1000)
    attachment=models.ImageField(blank=True,null=True)
    technology=models.ManyToManyField(Technology, related_name='technology')
    client=models.ForeignKey(Client,on_delete=models.CASCADE,null=True,blank=True)
    # datend time we want to add
    def __str__(self):
        return self.project_name

    class Meta:
        ordering=('project_name',)


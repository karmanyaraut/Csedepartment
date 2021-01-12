from django.db import models

class FacultyProfileInfo(models.Model):
    CATEGORY= (('ap','Assistant Professor'),
        ('aap','Associate Professor'),
        ('af','Adjunct Faculty'),
        ('hod','Head of department'),
        )

    name=models.CharField(max_length=200)
    about_faculty=models.CharField(max_length=400)
    academic = models.CharField(max_length=200)
    profile_pic= models.ImageField(upload_to ='profile_pics' ,blank=True)
    faculty_website=models.URLField(blank=True)
    typeoffaculty=models.CharField(max_length=200,null=True,choices= CATEGORY)
    def __str__(self):
        return self.name
class Researchinfo(models.Model):
    headingforesearch=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    sponsored=models.CharField(max_length=400)
class Placementstat(models.Model):
    year=models.CharField(max_length=200,default='0')
    btech=models.CharField(max_length=200,default='0' )
    mtech=models.CharField(max_length=200,default='0')
    mca=models.CharField(max_length=200,default='0')
    percentage=models.CharField(max_length=200,default='0')
    def __str__(self):
        return self.year
class Coursesinfo(models.Model):
    name=models.CharField(max_length=200,default='sub')
    about=models.CharField(max_length=200)
    photo= models.ImageField(upload_to ='profile_pics' ,blank=True)

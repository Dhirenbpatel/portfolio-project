from django.db import models

# Create A blog models
class blog(models.Model):
	title=models.CharField(max_length=255)
	pub_date=models.DateTimeField()
	body=models.TextField()
	image=models.ImageField(upload_to='images/')




# create migration



#migrate

# add to admin
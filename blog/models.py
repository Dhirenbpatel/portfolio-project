from django.db import models

# Create A blog models
class blog(models.Model):
	title=models.CharField(max_length=255)
	pub_date=models.DateTimeField()
	body=models.TextField()
	image=models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title
	def summary(self):
		return self.body[:100]
	def pub_dates(self):
		return self.pub_date.strftime('%b %e %Y')

# create migration



#migrate

# add to admin
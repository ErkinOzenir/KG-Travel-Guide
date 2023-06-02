from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator 

class Faq(models.Model):
    name = models.TextField()
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.ForeignKey("City", on_delete=models.PROTECT, null=False)
    region = models.ForeignKey("Region", on_delete=models.PROTECT, null=False)
    image = models.ForeignKey("Attachment", on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField("Tag")
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    
class Hotel(models.Model):
    name = models.CharField(max_length=255, blank=True)
    city = models.ForeignKey("City", on_delete=models.PROTECT, null=False)
    region = models.ForeignKey("Region", on_delete=models.PROTECT, null=False)
    image = models.ForeignKey("Attachment", on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField("Tag")
    address = models.TextField()
    work_days = models.ManyToManyField("WorkDay")
    opening_hour = models.TimeField(auto_now=False, auto_now_add=False, default="00:00")
    closing_hour = models.TimeField(auto_now=False, auto_now_add=False, default="23:59")

    def __str__(self):
        return self.name

    
class WorkDay(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    class AttachmentType(models.TextChoices):
        PHOTO = 'Photo', _("PHOTO")
        VIDEO = 'VIDEO', _("VIDEO")
    name = models.CharField(max_length=255)
    file = models.ImageField('Attachment', upload_to='KGTravelGuide/attachments/')
    file_type = models.CharField('File type', choices=AttachmentType.choices, max_length=10)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Social(models.Model):
    url = models.URLField()
    icon = models.FileField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    value = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    
class PlaceReview(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    
class HotelReview(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews' )
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

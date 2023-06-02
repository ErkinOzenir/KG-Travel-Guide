from django.db import models
from django.utils.translation import gettext_lazy as _

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

class Attachment(models.Model):
    class AttachmentType(models.TextChoices):
        PHOTO = 'Photo', _("PHOTO")
        VIDEO = 'VIDEO', _("VIDEO")
    file = models.ImageField('Attachment', upload_to='KGTravelGuide/attachments/')
    file_type = models.CharField('File type', choices=AttachmentType.choices, max_length=10)

    # publication = models.ForeignKey("Place", on_delete=models.CASCADE, verbose_name='Place')

    def __str__(self):
        return self.file_type

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
    
    

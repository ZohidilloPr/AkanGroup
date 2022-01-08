from django.db import models
# Create your models here.


class Contact(models.Model):
    name = models.CharField(("ISM"), max_length=50)
    email = models.EmailField(("EMAIL"), max_length=60)
    subject = models.CharField(("MAVZU"), max_length=100)
    message = models.TextField(("XABAR"))
    send_date = models.DateTimeField(("SEND_TIME"), auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.subject}'
# import the standard Django Model
# from built-in library
from django.db import models
import uuid

class TaskModel(models.Model):
    STATUS_CHOICES = [
        ('p', 'pending'),
        ('c', 'completed'),
        ('l', 'late')
    ]

	# fields of the model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length = 255)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='p'
    )
    due_datetime = models.DateTimeField()
    create_datetime = models.DateTimeField()#auto_now_add=True)
    completed_datetime = models.DateTimeField(default=None, blank=True, null=True)
    # renames the instances of the model
	# with their title name
    def __str__(self):
        return self.description

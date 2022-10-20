from django import forms
from .models import TaskModel


# creating a form
class TaskCreateForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = TaskModel

		# specify fields to be used
		fields = [
			"create_datetime",
			"description",
			"due_datetime",
		]

class TaskUpdateForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = TaskModel

		# specify fields to be used
		fields = [
			"completed_datetime",
		]

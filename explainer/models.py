from django.db import models
from django.contrib.auth.models import User

class CodeExplanation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code_snippet = models.TextField()
    explanation = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Explanation by {self.user.username} at {self.submitted_at}"

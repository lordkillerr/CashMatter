from django.db import models


class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    owes = models.JSONField(null=True, blank=True, default=dict)
    owed_by = models.JSONField(null=True, blank=True, default=dict)

    def __str__(self):
        return f"{self.user_id}------>{self.name}"


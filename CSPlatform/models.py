from django.db import models


class Survey(models.Model):
    Comapny_name = models.CharField(max_length=50, blank=False, null=False)
    Realtionship_name = models.CharField(max_length=30, blank=True, null=True)
    Survey_name = models.CharField(max_length=20)
    Name = models.CharField(max_length=20, blank=False)
    Email = models.EmailField(blank=False, null=True)
    Score = models.IntegerField(blank=False, null=True)
    Created_date = models.DateTimeField(blank=True, null=False)
    updated_date = models.DateTimeField(blank=True, null=False)

    class meta:
        managed = True
        db_table = "csplatform_survey"

    def __str__(self):
        return self.Comapny_name
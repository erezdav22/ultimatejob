from django.db import models


class company(models.Model):
    company_name = models.CharField(max_length=128)
    company_search_url = models.URLField()
    company_logo = models.TextField()
    function_name = models.TextField()


class job(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    search_key = models.CharField(max_length=128)
    job_title = models.CharField(max_length=128)
    description_url = models.URLField()

# Create your models here.

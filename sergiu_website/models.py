from django.db import models

"""
Aici se fac tabelele ptr SQL
Exemplu:
Topic => numele tabelului, se duce numele_folderului_topic
Unique ID se pune primul rand
Top_name = Headerul tabelului 
restul se completeaza automat dupa functiile tale
"""
# class Topic(models.Model):
#     """
#     numele campurilor
#     """
#     top_name = models.CharField(max_length=264, unique=True) #unique adica fara duplicate
#
#     def __str__(self):
#         return self.top_name
#
# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     name = models.CharField(max_length=264, unique=True)
#     url = models.URLField(unique=True)
#
#     def __str__(self):
#         """
#          It is called automatically when you either use “print” or “str” to convert your object to string.
#         :return:
#         """
#         return self.name
#
# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
#     date = models.DateField()
#
#     def __str__(self):
#         # folosesc str, ca sa dea string la data
#         return str(self.date)


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)

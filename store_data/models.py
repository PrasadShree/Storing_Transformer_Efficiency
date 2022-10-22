from django.db import models
class TransformerData(models.Model):

    Transformer_Id = models.CharField(max_length=264)
    Transformer_Date = models.CharField(max_length=264)
    Transformer_Rating = models.CharField(max_length=264)
    Transformer_PRating = models.CharField(max_length=264)
    Transformer_SRating = models.CharField(max_length=264)
    Transformer_Effi = models.CharField(max_length=264)



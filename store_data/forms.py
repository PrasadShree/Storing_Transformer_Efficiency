from django import forms
from .models import TransformerData

class TransformerForm(forms.ModelForm):
    class Meta:
        model = TransformerData
        fields = ["Transformer_Id", "Transformer_Date", "Transformer_Rating",
                  "Transformer_PRating", "Transformer_SRating", "Transformer_Effi"]
from django import forms

facultychoices= [
    ("hod", 'Head of department'),
    ("ap", 'Associate Professor'),
    ("aap", 'Assistant Professor'),
    ("af", 'Adjunct Faculty'),
    ]

class FacultyForm(forms.Form):
    faculty_type = forms.CharField(label='Faculty type' , widget=forms.Select(choices=facultychoices))

from django.shortcuts import render

from django.views import View
from paintapp.forms import ColorPickerForm

class ColorPickerView(View):
    def get(self, request):
        """Present the color picker form and color the user"""
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 255,
            'green': 255,
            'blue': 255,
        }

        return render(request, 'color_picker.html', context=context)
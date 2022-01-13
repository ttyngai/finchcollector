from django.db import models
from django.urls import reverse



MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)



class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})



# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    feedsPerDay = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    def __str__(self):
        return f"({self.id}) - {self.name}"

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id})



# class Finch:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, color, description, feedsPerDay):
#     self.name = name
#     self.color = color
#     self.description = description
#     self.feedsPerDay = feedsPerDay

# finches = [
#   Finch('Lolo', 'tabby', 'foul little demon', 3),
#   Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Finch('Raven', 'black tripod', '3 legged cat', 4)
# ]


class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length = 1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
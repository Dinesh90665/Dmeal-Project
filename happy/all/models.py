
# from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username



# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=15, blank=True)
#     address = models.TextField(blank=True)
#     dob = models.DateField(null=True, blank=True)
#     anniversary = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=20, blank=True)
#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

#     def __str__(self):
#         return self.user.username
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)  # just the path
    place = models.CharField(max_length=100)
    facility = models.TextField(max_length=255)

    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

  
class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.CharField(max_length=255)
    
    class Meta:
        unique_together = ('restaurant', 'name')

    def __str__(self):
        return f"{self.name}({self.restaurant.name})"


        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.name}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity} from {self.menu_item.restaurant.name}"











from django.db import models

class Review(models.Model):
    DESIGNATION_CHOICES = [
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    designation = models.CharField(max_length=3, choices=DESIGNATION_CHOICES)
    review = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.designation})"








from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"


# models.py
class Donation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donated_at = models.DateTimeField(auto_now_add=True)

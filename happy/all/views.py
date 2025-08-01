from django.shortcuts import render,HttpResponse

# Create your views here.



def about(request):
    food_items = [
        {"title": "Cleaned Sitting Room", "image1": "all/images/5th_1.jpg", "image2": "all/images/6th_2.jpg"},
        {"title": "Well_Managed", "image1": "all/images/5th_2.jpg", "image2": "all/images/6th_3.jpg"},
        {"title": "Variety of food ", "image1": "all/images/5th_3.jpg", "image2": "all/images/5th_4.jpg"},
        {"title": "Managed Room", "image1": "all/images/5th_4.jpg", "image2": "all/images/6th_1.jpg"},
        {"title": "Good Lighting", "image1": "all/images/5th_5.jpg", "image2": "all/images/6th_1.jpg"},
        {"title": "Experiencing", "image1": "all/images/5th_6.jpg", "image2": "all/images/5th_5.jpg"},
        {"title": "cleaned-kitchen", "image1": "all/images/5th_1.jpg", "image2": "all/images/6th_4.jpg"},
        {"title": "well_designed", "image1": "all/images/5th_2.jpg", "image2": "all/images/5th_3.jpg"},
        {"title": "Tasty food", "image1": "all/images/6th_3.jpg", "image2": "all/images/6th_2.jpg"},
        {"title": "good Facilities", "image1": "all/images/5th_2.jpg", "image2": "all/images/5th_1.jpg"},
    ]
    return render(request, "about.html", {"food_items": food_items})


def job(request):
    return render(request,'job.html')

from .models import Restaurant
from django.shortcuts import render,  redirect
from .data import menu_items
from .data import restaurants

def product(request):
   return render(request, 'product.html', {'restaurants': restaurants})


def Reviews(request):
    return render(request,'Reviews.html')

def Return(request):
    return render(request,'Return.html')

def contacts(request):
    return render(request,'contacts.html')

def Blogs(request):
    return render(request,'Blogs.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from django.contrib.auth.decorators import login_required

def menu_view(request):
    items=MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})


def add_to_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if not isinstance(cart, dict):
            cart = {}

        for key, value in request.POST.items():
            if key.startswith('item_'):
                item_id = key.split('_')[1]
                try:
                    qty = int(value)
                except:
                    qty = 0
                if qty > 0:
                    cart[item_id] = qty
                elif item_id in cart:
                    del cart[item_id]

        request.session['cart'] = cart
        return redirect('cart_view')

from django.contrib.auth.decorators import login_required
from .models import MenuItem


def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for item_id, qty in cart.items():
        try:
            menu_item = MenuItem.objects.get(id=item_id)
            items.append({
                'id': menu_item.id,
                'name': menu_item.name,
                'price': menu_item.price,
                'quantity': qty,
                'image': menu_item.image,
            })
            total += menu_item.price * qty
        except MenuItem.DoesNotExist:
            pass
    return render(request, 'cart.html', {'cart': items, 'total': total})

def update_cart(request):
    if request.method == 'POST':
        cart = {}
        for key, value in request.POST.items():
            if key.startswith('item_'):
                item_id = key.split('_')[1]
                try:
                    qty = int(value)
                except ValueError:
                    qty = 0
                if qty > 0:
                    cart[item_id] = qty

        address = request.POST.get('address', '').strip()

        if not address:
            messages.error(request, "Please provide a delivery address.")
            return redirect('cart_view')

        request.session['cart'] = cart
        request.session['address'] = address

        return redirect('order_summary')
    else:
        return redirect('cart_view')


from .models import Order ,OrderItem, Profile


# def order_summary(request):
#     cart = request.session.get('cart', {})
#     address = request.session.get('address', '') 
#     items = []
#     total = 0
#     for item_id, qty in cart.items():
#         try:
#             menu_item = MenuItem.objects.get(id=item_id)
#             items.append({
#                 'name': menu_item.name,
#                 'price': menu_item.price,
#                 'quantity': qty,
#                 'image': menu_item.image,
#             })
#             total += menu_item.price * qty

#         try:
#             profile = request.user.profile

#         except MenuItem.DoesNotExist:
#             pass
#     return render(request, 'order_summary.html', {
#         'items': items,
#         'total': total,
#         'address': address,
#         'user': request.user, 
        
#     })

from django.contrib.auth.decorators import login_required
from .models import MenuItem, Profile  # Ensure these are imported

@login_required
def order_summary(request):
    cart = request.session.get('cart', {})
    address = request.session.get('address', '') 
    items = []
    total = 0

    for item_id, qty in cart.items():
        try:
            menu_item = MenuItem.objects.get(id=item_id)
            items.append({
                'name': menu_item.name,
                'price': menu_item.price,
                'quantity': qty,
                'image': menu_item.image,
            })
            total += menu_item.price * qty
        except MenuItem.DoesNotExist:
            continue  # Skip if item not found

    try:
        profile = request.user.profile
        phone = profile.phone
    except Profile.DoesNotExist:
        phone = ''

    return render(request, 'order_summary.html', {
        'items': items,
        'total': total,
        'address': address,
        'user': request.user,
        'name': request.user.get_full_name() or request.user.username,
        'phone': phone,
    })






# from django.contrib import messages
# from django.shortcuts import render, redirect

# def place_order(request):
#     if request.method == 'POST':
#         # Your order processing logic here: save order, order items, etc.

#         # After saving order:
#         messages.success(request, "Your order has been placed successfully! Thank you for ordering with Dmeal.")
#         return redirect('order_success')

#     # For safety, redirect to cart or menu if GET
#     return redirect('cart_view')


def order_success(request):
    return render(request, 'order_success.html')








from django.contrib import messages
from django.shortcuts import redirect
from .models import Order ,OrderItem, Profile
from django.core.mail import send_mail
from django.conf import settings

def place_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        address = request.session.get('address', '')
        if not cart or not address:
            messages.error(request, "Cart or address missing.")
            return redirect('cart_view')

        total = 0
        profile = request.user.profile
        order = Order.objects.create(
            user=request.user,
            name=request.user.username,
            phone=profile.phone,
            address=address,
            total=0
        )

        for item_id, qty in cart.items():
            menu_item = MenuItem.objects.get(id=item_id)
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=qty,
                price=menu_item.price
            )
            total += menu_item.price * qty

        order.total = total
        order.save()

        # Clear session cart and address
        request.session['cart'] = {}
        request.session['address'] = ''

        send_mail(
        subject='✅ Order Confirmation - Dmeal',
        message=f"Dear {request.user.get_full_name()},\n\nYour order has been placed successfully!\n\nDelivery to: {address}\nTotal: ₹{total}\n\nThank you for using Dmeal!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["dineshayadi584@gmail.com"],
        fail_silently=False,
    )


        return redirect('order_success')
    else:
        return redirect('cart_view')




# all/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Profile,User

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Access or create the profile after user is saved
            profile, created = Profile.objects.get_or_create(user=user)
            profile.phone = form.cleaned_data.get('phone')
            profile.address = form.cleaned_data.get('address')
            profile.save()

            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})




from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid username or email.")
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('about')  # replace 'home' with your homepage route
        else:
            messages.error(request, "Incorrect password.")
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def password_reset(request):
    return render(request,'password_reset.html')


    from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Review

@require_http_methods(["GET", "POST"])
def submit_review(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        designation = request.POST.get('designation')
        review_text = request.POST.get('review')

        # You can add validation here

        Review.objects.create(
            name=name,
            phone=phone,
            designation=designation,
            review=review_text,
        )
        return redirect('thank_you_page')  # Redirect to a thank you page or back with success

    return render(request, 'Review.html')  # Your template file name

def thank_you_page(request):
    return render(request, 'thank_you_page.html')

def terms(request):
    return render(request,'terms.html')

def privacy(request):
    return render(request,'privacy.html')

def security(request):
    return render(request,'security.html')

def profile(request):
    return render(request,'profile.html')

def view_activity(request):
    return render(request,'view_activity.html')

def set(request):
    return render(request,'set.html')

def make(request):
    return render(request,'make.html')

def employers(request):
    return render(request,'employers.html')

def employees(request):
    return render(request,'employees.html')

def fame(request):
    return render(request,'fame.html')


def help_people(request):
    return render(request,'help_people.html')

def feed_nepal(request):
    return render(request,'feed_nepal.html')


def report_safety(request):
    return render(request,'report_safety.html')

def log(request):
    return render(request,'log.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback

@login_required
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.email = request.user.email
            feedback.save()
            return redirect('feedback_success')  # Create a success page or message
    else:
        form = FeedbackForm()
    return render(request, 'send_feedback.html', {'form': form})



def feedback_success(request):
    return render(request, 'feedback_success.html')


def donate(request):
    return render(request,'donate.html')


def edit_profile(request):
    return render(request,'edit_profile.html')

def noitification_setting(request):
    return render(request,'noitification_setting.html')

def account(request):
    return render(request,'account.html')

















# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Profile

# @login_required
# def edit_profile(request):
#     user = request.user
#     profile, created = Profile.objects.get_or_create(user=user)

#     if request.method == 'POST':
#         if 'delete_photo' in request.POST:
#             # Delete profile photo
#             if profile.profile_image:
#                 profile.profile_image.delete(save=True)
#             messages.success(request, 'Profile photo deleted successfully.')
#             return redirect('view_activity')

#         # Update other profile fields
#         phone = request.POST.get('phone')
#         dob = request.POST.get('dob')
#         anniversary = request.POST.get('anniversary')
#         gender = request.POST.get('gender')

#         profile.phone = phone
#         profile.dob = dob if dob else None
#         profile.anniversary = anniversary if anniversary else None
#         profile.gender = gender

#         # Check if a new profile image is uploaded
#         if 'profile_image' in request.FILES:
#             profile.profile_image = request.FILES['profile_image']

#         profile.save()
#         messages.success(request, 'Profile updated successfully.')
#         return redirect('view_activity')

#     return render(request, 'edit_profile.html', {'profile': profile})










# views.py
from django.shortcuts import render, redirect
from .models import Donation

def donate_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        amount = request.POST['amount']

        Donation.objects.create(name=name, phone=phone, email=email, amount=amount)

        # Send confirmation email
        subject = 'Thank you for your donation!'
        message = f"""
Dear {name},

Thank you for your generous donation of ₹{amount} to Feeding Nepal.

Your contribution will help provide meals and hope to people in need across Nepal.

With gratitude,
Feeding Nepal Team
"""
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["dineshayadi584@gmail.com"]

        send_mail(subject, message, from_email, recipient_list)


        return redirect('thank_you')
    return render(request, 'donate.html')


def thank_you_view(request):
    return render(request, 'thank_you.html')





def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'menu_items': menu_items,
    })





from django.shortcuts import render

# def choose_site(request):
#     return render(request, 'choose_site.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:  # Optional: only allow staff/admins
                login(request, user)
                return redirect('dashboard')  # Replace with your admin dashboard URL name
            else:
                messages.error(request, 'You do not have admin access.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'admin_login.html')





def admin_base(request):
    return render(request,'admin_base.html')













from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Sum
from all.models import MenuItem, Restaurant, Donation, Review

def dashboard(request):
    total_menu_items = MenuItem.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    total_restaurants = Restaurant.objects.count()
    total_donations = Donation.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    total_reviews = Review.objects.count()
    new_feedback = Feedback.objects.count()

    context = {
        'total_menu_items': total_menu_items,
        'active_users': active_users,
        'total_restaurants': total_restaurants,
        'total_donations': total_donations,
        'total_reviews': total_reviews,
        'new_feedback': new_feedback,
    }
    return render(request, 'dashboard.html', context)


def differentiate(request):
    return render(request,'differentiate.html')














def donations(request):
    return render(request,'donations.html')





def logout(request):
    return render(request,'logout.html')

from django.shortcuts import render
from all.models import Order  # Use your actual Order model and app name
from django.contrib.auth.decorators import login_required

@login_required
def orders_list(request):
    orders = Order.objects.all().order_by('id')  # You can also filter by user if needed
    return render(request, 'orders_list.html', {'orders': orders})

from django.shortcuts import render
from all.models import OrderItem  # Adjust based on your app name and model
from django.contrib.auth.decorators import login_required

@login_required
def orders_items_list(request):
    order_items = OrderItem.objects.all()
    return render(request, 'orders_items_list.html', {'order_items': order_items})




from django.shortcuts import render
from all.models import MenuItem  # Adjust to your actual model

def menu_items_list(request):
    items = MenuItem.objects.all().order_by('id')
    return render(request, 'menu_items_list.html', {'items': items})





def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_items_list')
    else:
        form = MenuItemForm()
    return render(request, 'menu_item_form.html', {'form': form, 'title': 'Add Menu Item'})

def edit_menu_item(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_items_list')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu_item_form.html', {'form': form, 'title': 'Edit Menu Item'})

def delete_menu_item(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    item.delete()
    return redirect('menu_items_list')

from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'description', 'image']


def donations_view(request):
    donations = Donation.objects.all().order_by('-id')
    return render(request, 'donations.html', {'donations': donations})




def delete_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    donation.delete()
    return redirect('donations')




def review_view(request):
    rev= Review.objects.all()
    return render(request, 'review.html', {'rev': rev})


def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    return redirect('review')



from django.contrib.auth.models import User
from django.shortcuts import render

def active_users_view(request):
    users = User.objects.all()
    return render(request, 'active_users.html', {'users': users})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def account_view(request):
    # This assumes every user has a Profile (which you confirmed)
    profile = request.user.profile
    return render(request, 'account.html', {'profile': profile})



from django.shortcuts import render
from .models import Feedback

def feedbacks_view(request):
    feedbacks = Feedback.objects.select_related('user').order_by('-submitted_at')
    return render(request, 'feedbacks.html', {'feedbacks': feedbacks})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Restaurant
from .forms import RestaurantForm  # We'll create this form next

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Restaurant added successfully.')
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_form.html', {'form': form, 'title': 'Add Restaurant'})

def edit_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Restaurant updated successfully.')
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant_form.html', {'form': form, 'title': 'Edit Restaurant'})

def delete_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        restaurant.delete()
        messages.success(request, 'Restaurant deleted successfully.')
        return redirect('restaurant_list')
    return render(request, 'restaurant_confirm_delete.html', {'restaurant': restaurant})

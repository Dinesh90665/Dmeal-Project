from django.urls import path 
from .import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
urlpatterns = [

     path('',views.differentiate,name='differentiate'),
   
    path('login', views.login_view, name='login'),

    path('admin_login',views.admin_login,name='admin_login'),
    path('job',views.job, name='job'),
    path('about',views.about,name='about'),
    # path('menu',views.menu,name='menu'),
    path('contacts',views.contacts,name='contacts'),
    path('product',views.product,name='product'),
    # path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    # path('cart', views.cart_view, name='cart_view'),
    path('Reviews',views.Reviews,name='Reviews'),
    path('Return',views.Return,name='Return'),
    path('Blogs',views.Blogs,name='Blogs'),
    # path('update_cart_item/<int:item_id>',views.update_cart_item, name='update_cart_item'),
    # path('cart/order', views.place_order, name='place_order'),

   path('menu', views.menu_view, name='menu_view'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/update/', views.update_cart, name='update_cart'),
    path('order-summary/', views.order_summary, name='order_summary'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),


    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
path('thank-you_page/', views.thank_you_page, name='thank_you_page'),
path('terms',views.terms,name='terms'),
path('submit-review/', views.submit_review, name='submit_review'),
path('privacy',views.privacy,name='privacy'),
path('security',views.security,name='security'),

path('profile',views.profile,name='profile'),



path('send_feedback',views.feedback_view,name='send_feedback'),
path('make',views.make,name='make'),
path('feed_nepal',views.feed_nepal,name='feed_nepal'),
path('help_people',views.help_people,name='help_people'),
path('set',views.set,name='set'),
path('employers',views.employers,name='employers'),
path('employees',views.employees,name='employees'),
path('view_activity',views.view_activity,name='view_activity'),


#  path('', views.choose_site, name='choose_site'),
    path('admin_login', views.admin_login, name='admin_login'),

    path('admin_base', views.admin_base,name='admin_base'),
    # path('login', views.login_sview, name='login'),


path('report_safety',views.report_safety,name='report_safety'),

path('fame',views.fame,name='fame'),

path('log',views.log,name='log'),

 path('feedback_success', views.feedback_success, name='feedback_success'),

path('help_order/', views.help_order, name='help_order'),

path('question/', views.question,name="question"),

 path('donate', views.donate_view, name='donate'),
    path('thank_you', views.thank_you_view, name='thank_you'),
    path('edit_profile',views.edit_profile,name='edit_profile.html'),
    path('noitification_setting',views.noitification_setting,name='noitification_setting'),
    path('account',views.account,name='account.html'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),








path('dashboard/', views.dashboard, name='dashboard'),



path('orders_list', views.orders_list, name='orders_list'),


path('logout',views.logout,name='logout.html'),
path('menu-items/', views.menu_items_list, name='menu_items_list'),

path('order-items/', views.orders_items_list, name='orders_items_list'),





path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
path('edit_menu_item/<int:item_id>/', views.edit_menu_item, name='edit_menu_item'),
 path('delete_menu_item/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),



path('donations', views.donations_view, name='donations'),
path('delete_donation/<int:id>/', views.delete_donation, name='delete_donation'),
path('review', views.review_view, name='review'),
path('delete_review/<int:id>/', views.delete_review, name='delete_review'),


path('active_users/', views.active_users_view, name='active_users'),

path('account',views.account_view,name='account'),
path('feedbacks',views.feedbacks_view,name='feedbacks'),








    path('restaurants/', views.restaurant_list, name='restaurant_list'),          # List all restaurants
    path('restaurants_add', views.add_restaurant, name='add_restaurant'),        # Add new restaurant
    path('restaurants_edit<int:id>/', views.edit_restaurant, name='edit_restaurant'),  # Edit restaurant
    path('restaurants_delete<int:id>/', views.delete_restaurant, name='delete_restaurant'),  



   path('differentiate', views.differentiate,name='differentiate.html'),





] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

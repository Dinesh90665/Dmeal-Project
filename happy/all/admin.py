from django.contrib import admin
from .models import MenuItem, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0



from django.templatetags.static import static
from django.utils.html import format_html

try:
    admin.site.unregister(MenuItem)
except admin.sites.NotRegistered:
    pass

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price','description','image','image_preview')
    search_fields = ('id','name')
    ordering = ('id',)


    def image_preview(self, obj):
        if obj.image:
            url = static(f'all/images/{obj.image}')
            return format_html('<img src="{}" width="50" height="50" />', url)
        return "No Image"

    image_preview.short_description = 'Image'

admin.site.register(MenuItem, MenuItemAdmin)


from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'amount', 'donated_at')
    









@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'created_at', 'total')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'address')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'order_id', 'order_phone', 'quantity', 'price')
    search_fields = ('menu_item__name', 'order__id')

    def order_id(self, obj):
        return obj.order.id
    order_id.admin_order_field = 'order'  # Allows column sorting
    order_id.short_description = 'Order ID'

    def order_phone(self, obj):
        return obj.order.phone
    order_phone.short_description = 'Order Phone'
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'phone', 'address')
    search_fields = ('user__username', 'phone', 'user__email')

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'






from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'submitted_at','message')
    search_fields = ('user__username', 'email', 'message')
    list_filter = ('submitted_at',)
    ordering = ('-submitted_at',)
    readonly_fields = ('submitted_at',)

    fieldsets = (
        (None, {
            'fields': ('user', 'email', 'message', 'submitted_at')
        }),
    )



from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'designation','review', 'submitted_at')
    search_fields = ('name', 'phone', 'designation')
    list_filter = ('designation', 'submitted_at')
    ordering = ('-submitted_at',)



from django.contrib import admin
from .models import Restaurant


try:
    admin.site.unregister(Restaurant)
except admin.sites.NotRegistered:
    pass

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'place', 'facility','image','image_tag')
    search_fields = ('id','name')
    ordering = ('id',)



    def image_tag(self, obj):
        if obj.image:
            url = static(f'all/images/{obj.image}')
            return format_html('<img src="{}" width="50" height="50" />', url)
        return "No Image"
    
    image_tag.short_description = 'Image'



admin.site.register(Restaurant, RestaurantAdmin)
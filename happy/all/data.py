
from .models import Restaurant
restaurants = [
    {
        "id": 1,
        "name": "Spice Garden",
        "image": "re_1.jpg",
        "description": "Authentic Indian flavors served in a cozy ambiance.",
        "place": "Pokhara Lakeside",
        "facility": "WiFi, Outdoor Seating, Parking"
    },
    {
        "id": 2,
        "name": "Mountain View Grill",
        "image": "re_2.jpg",
        "description": "Barbecue specialties with stunning Himalayan views.",
        "place": "Sarangkot, Pokhara",
        "facility": "Rooftop Seating, Live Music"
    },
    {
        "id": 3,
        "name": "Urban Bites",
        "image": "re_3.jpg",
        "description": "Trendy café for burgers, sandwiches and shakes.",
        "place": "New Road, Kathmandu",
        "facility": "AC, Free WiFi, Takeaway"
    },
    {
        "id": 4,
        "name": "Everest Fusion",
        "image": "re_4.jpg",
        "description": "Modern twist on traditional Nepali cuisine.",
        "place": "Thamel, Kathmandu",
        "facility": "Live Band, Reservation Available"
    },
    {
        "id": 5,
        "name": "The Bamboo House",
        "image": "re_5.jpg",
        "description": "Asian and Continental delicacies in a bamboo-themed space.",
        "place": "Boudha, Kathmandu",
        "facility": "Family Friendly, Free Parking"
    },
    {
        "id": 6,
        "name": "Chilly Chops",
        "image": "re_6.jpg",
        "description": "Street-style momo and chili dishes.",
        "place": "Lalitpur",
        "facility": "Fast Service, Budget Friendly"
    },
    {
        "id": 7,
        "name": "Lumbini Veg Plaza",
        "image": "re_8.jpg",
        "description": "Pure vegetarian meals with South Indian flair.",
        "place": "Butwal",
        "facility": "Vegan Options, Clean Washrooms"
    },
    {
        "id": 8,
        "name": "Sunset Dine",
        "image": "re_7.jpg",
        "description": "Romantic riverside dining with serene views.",
        "place": "Sundarijal",
        "facility": "Riverside Seating, Candlelight"
    },
    {
        "id": 9,
        "name": "Dine & Shine",
        "image": "re_9.jpg",
        "description": "Fine dining with global flavors.",
        "place": "Jhamsikhel, Kathmandu",
        "facility": "Private Booths, Event Hosting"
    },
    {
        "id": 10,
        "name": "Quick Bite Express",
        "image": "6th_1.jpg",
        "description": "Fast food joint perfect for a quick munch.",
        "place": "Chitwan",
        "facility": "Takeaway, Delivery Available"
    },
    {
        "id": 11,
        "name": "Himalayan Deli",
        "image": "re_10.jpg",
        "description": "Fresh bakery and deli items all day long.",
        "place": "Bhaktapur",
        "facility": "Bakery, Breakfast Special"
    },
    {
        "id": 12,
        "name": "The Hungry Yak",
        "image": "re_11.jpg",
        "description": "Tibetan cuisine at its best.",
        "place": "Jomsom",
        "facility": "Heated Seating, Local Beverages"
    },
    {
        "id": 13,
        "name": "Nepa Food Hub",
        "image": "re_12.jpg",
        "description": "Newari feasts and snacks made fresh.",
        "place": "Kirtipur",
        "facility": "Traditional Decor, Cultural Dance"
    },
    {
        "id": 14,
        "name": "Blue Moon Café",
        "image": "re_13.jpg",
        "description": "Peaceful café for book lovers and coffee addicts.",
        "place": "Dharan",
        "facility": "Quiet Zone, Library Inside"
    },
    {
        "id": 15,
        "name": "Tandoori Flames",
        "image": "re_14.jpg",
        "description": "Specialty grilled and tandoori items.",
        "place": "Birgunj",
        "facility": "Family Dining, Air Conditioning"
    },
    {
        "id": 16,
        "name": "Frozen Spoon",
        "image":"6th_2.jpg",
        "description": "Ice cream and desserts paradise.",
        "place": "Pokhara",
        "facility": "Desserts Only, Kids Friendly"
    },
    {
        "id": 17,
        "name": "Green Earth Eatery",
        "image": "6th_3.jpg",
        "description": "Organic meals made from local ingredients.",
        "place": "Bharatpur",
        "facility": "Eco Friendly, Vegan Options"
    },
    {
        "id": 18,
        "name": "The Curry House",
        "image": "6th_4.jpg",
        "description": "Best curry and naan combos in town.",
        "place": "Dhangadhi",
        "facility": "Family Seating, Quick Service"
    },
    {
        "id": 19,
        "name": "Namaste Bistro",
        "image": "7th_1.jpg",
        "description": "Fusion bistro serving Nepali-European plates.",
        "place": "Itahari",
        "facility": "Chilled Beverages, Cozy Interior"
    },
    {
        "id": 20,
        "name": "Chef's Table Nepal",
        "image": "7th_2.jpg",
        "description": "Signature meals by award-winning chefs.",
        "place": "Lalitpur",
        "facility": "Reservation Required, Premium Menu"
    },

]


def insert_restaurants():
    for r in restaurants:
        Restaurant.objects.update_or_create(
            id=r['id'],
            defaults={
                'name': r['name'],
                'description': r['description'],
                'place': r['place'],
                'facility':r['facility'],
                'image': r['image'],
            }
        )


        


from .models import MenuItem
menu_items = [
     
    {
        "id": 1,
        "name": "Margherita Pizza",
        "description": "Classic cheese and tomato pizza",
        "price": 249,
        "image": "pizza.jpg",
        "restaurant_name": "Spice Garden"
    }, 
    {
        "id": 2,
        "name": "Chicken Burger",
        "description": "Juicy chicken patty with lettuce and mayo",
        "price": 199,
        "image": "burger.jpg",
         "restaurant_name": "Mountain View Grill"
    },
    {
        "id": 3,
        "name": "Veggie Wrap",
        "description": "Healthy wrap filled with fresh vegetables",
        "price": 179,
        "image": "wrap.jpg",
         "restaurant_name": "Urban Bites"
    },
    {
        "id": 4,
        "name": "Grilled Sandwich",
        "description": "Grilled to perfection with cheese and tomato",
        "price": 159,
        "image": "sandwich.jpg",
         "restaurant_name": "Everest Fusion"
    },
    {
        "id": 5,
        "name": "Momos",
        "description": "Steamed dumplings with spicy sauce",
        "price": 129,
        "image": "momos.jpg",
          "restaurant_name": "The Bamboo House"
    },
    {
        "id": 6,
        "name": "Pasta Alfredo",
        "description": "Creamy white sauce pasta",
        "price": 229,
        "image": "pasta.jpg",
        "restaurant_name": "Chilly Chops"
    },
    {
        "id": 7,
        "name": "Biryani",
        "description": "Spiced rice with chicken and herbs",
        "price": 279,
        "image": "biryani.jpg",
        "restaurant_name": "Lumbini Veg Plaza"
    },
    {
        "id": 8,
        "name": "French Fries",
        "description": "Crispy golden potato fries",
        "price": 99,
        "image": "fres.jpg",
          "restaurant_name": "Sunset Dine"
    },
    {
        "id": 9,
        "name": "Chocolate Shake",
        "description": "Rich and creamy chocolate milkshake",
        "price": 149,
        "image": "shake.jpg",
         "restaurant_name": "Dine & Shine"
    },
    {
        "id": 10,
        "name": "Caesar Salad",
        "description": "Fresh lettuce, cheese, and croutons",
        "price": 189,
        "image": "salad.jpg",
         "restaurant_name": "Quick Bite Express"
    },
    {
        "id": 11,
        "name": "Spring Rolls",
        "description": "Crispy vegetable spring rolls",
        "price": 119,
        "image": "spring_rolls.jpg",
         "restaurant_name": "Himalayan Deli"
    },
    {
        "id": 12,
        "name": "Paneer Tikka",
        "description": "Grilled paneer cubes marinated in spices",
        "price": 239,
        "image": "paneer.jpg",
          "restaurant_name": "The Hungry Yak"
    },
    {
        "id": 13,
        "name": "Fish Curry",
        "description": "Spicy and tangy fish curry with rice",
        "price": 299,
        "image": "fish_curry.jpg",
        "restaurant_name": "Nepa Food Hub"
    },
    {
        "id": 14,
        "name": "Egg Roll",
        "description": "Stuffed egg roll with onions and chutney",
        "price": 139,
        "image": "egg_roll.jpg",
         "restaurant_name": "Blue Moon Café"
    },
    {
        "id": 15,
        "name": "Ice Cream Sundae",
        "description": "Vanilla ice cream with chocolate toppings",
        "price": 109,
        "image": "icecream.jpg",
          "restaurant_name": "Tandoori Flames"
    },
    {
        "id": 16,
        "name": "Daal Bhat",
        "description": "Nepali-style lentils and rice",
        "price": 149,
        "image": "daalbhat.jpg",
        "restaurant_name": "Frozen Spoon"
    },
    {
        "id": 17,
        "name": "Samosa",
        "description": "Spiced potato-filled fried snack",
        "price": 49,
        "image": "samosa.jpg",
        "restaurant_name": "Spice Garden"
    },
    {
        "id": 18,
        "name": "Masala Dosa",
        "description": "South Indian crepe stuffed with potato",
        "price": 189,
        "image": "dosa.jpg",
            "restaurant_name": "Spice Garden"
    },
    {
        "id": 19,
        "name": "Chowmein",
        "description": "Stir-fried noodles with vegetables",
        "price": 159,
        "image": "chowein.jpg",
             "restaurant_name": "Spice Garden"
    },
    {
        "id": 20,
        "name": "Thukpa",
        "description": "Tibetan noodle soup",
        "price": 169,
        "image": "thukpa.jpg",
        "restaurant_name": "Spice Garden"
    },

    {
        "id": 21,
        "name": "aalu",
        "description": " noodle soup",
        "price": 200,
        "image": "pe_1.jpg",
        "restaurant_name": "Spice Garden"
    },
    {
        "id": 22,
        "name": "bhat",
        "description": " meat soup",
        "price": 210,
        "image": "pe_2.jpg",
        "restaurant_name": "Spice Garden"
    },
    {
        "id": 23,
        "name": "meat curry",
        "description": " good soup",
        "price": 230,
        "image": "pe_3.jpg",
        "restaurant_name": "Spice Garden"
    },
    {
        "id": 24,
        "name": "frying",
        "description": "nice bhat",
        "price": 260,
        "image": "pe_8.jpg",
        "restaurant_name": "Spice Garden"
    },
{
        "id": 25,
        "name": "mix",
        "description": "nice",
        "price": 250,
        "image": "pe_6.jpg",
        "restaurant_name": "Spice Garden"
    },
]


def insert_menu_items():
    for item in menu_items:
        try:
            restaurant = Restaurant.objects.get(name=item['restaurant_name'])
            MenuItem.objects.update_or_create(
                name=item['name'],
                restaurant=restaurant,
                defaults={
                    'price': item['price'],
                    'description': item['description'],
                    'image': item['image'],
                }
            )
        except Restaurant.DoesNotExist:
            print(f"❌ Restaurant not found: {item['restaurant_name']}")
    print("✅ Menu items inserted or updated.")


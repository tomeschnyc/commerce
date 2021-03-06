from django.contrib import admin
from .models import User, AuctionListing, Bid, Comment, Watchlist

class AuctionListingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id", 
        "title", 
        "description", 
        "photo", 
        "price", 
        "date",
        "category",
        "highest_bidder",
        "is_active"
    )

# Register your models here.
admin.site.register(User)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlist)
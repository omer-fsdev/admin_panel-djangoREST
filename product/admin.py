from django.contrib import admin
from .models import *

#img
from django.utils.safestring import mark_safe

#import-export
from import_export.admin import ImportExportModelAdmin
from product.resources import ReviewResource

# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)


admin.site.site_title = "My Admin Panel Session"
admin.site.site_header = "Welcome My Product Admin Panel"
admin.site.index_title = "My Admin Panel Customization Examples"


# tabularInline
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    classes = ["collapse"]


class ProductAdmin(admin.ModelAdmin):
    # in the admin panel;
    # fields to display (in order)
    list_display = ["name", "id", "description", "is_in_stock", "slug", "create_date"]
    # update permission in the interface
    list_editable = ["is_in_stock"]
    # access link to the instance. Clickable.
    list_display_links = ["id", "name"]
    # filterable fields
    list_filter = ["is_in_stock", "create_date"]
    # adds search field and where to search.
    search_fields = ["name", "description"]
    ordering = ["id", "name"]
    # the number of saved to display per page
    list_per_page = 20
    # when requested to display all
    list_max_show_all = 100
    # date filter
    date_hierarchy = "create_date"
    # automatic generation # slug field can contain letter, number, underscore, dash
    prepopulated_fields = {"slug": ["name"]}
    # positioning the elements in the form. Each tuple in a line.
    inlines = [ReviewInline]
    fields = [("name", "is_in_stock"), ("slug"), ("description"), ("category")]

    # fieldsets = (
    #     (
    #         "General",
    #         {
    #             # 'classes': ('',),
    #             "fields": ("name", "is_in_stock"),
    #             "description": "General settings",
    #         },
    #     ),
    #     (
    #         "Details",
    #         {
    #             "classes": ("collapse",),
    #             "fields": (("slug"), ("description")),
    #             "description": "Details",
    #         },
    #     ),
    # )

    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} were marked as "In Stock".')

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} were marked as "Out of Stock".')

    set_stock_in.short_description = "Add marked products to stock"
    set_stock_out.short_description = "Remove marked products from stock"

    actions = ("set_stock_in", "set_stock_out")

    filter_horizontal = ["category"]

    # adding extra field
    def added_days_ago(self, object):
        from django.utils import timezone

        difference = timezone.now() - object.create_date
        return difference.days

    list_display += ["added_days_ago"]

    def bring_image(self, obj):
        if obj.product_img:
            return mark_safe(
                f"<img src={obj.product_img.url} width=100 height=100></img>"
            )
        return mark_safe(f"<h3>{obj.name} has not image </h3>")

    list_display += ["bring_image"]
    readonly_fields = ("bring_image",)

admin.site.register(Product, ProductAdmin)


class ReviewAdmin(ImportExportModelAdmin):
    list_display = ["__str__", "is_released", "created_date"]
    raw_id_fields = ["product"]

    def how_many_reviews(self, object):
        return object.product.reviews.count()

    how_many_reviews.short_description = "reviews"
    list_display += ["how_many_reviews"]
    resource_class = ReviewResource


admin.site.register(Review, ReviewAdmin)

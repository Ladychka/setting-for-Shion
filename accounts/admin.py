from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
admin.site.site_header = 'Acleda University of Business'
admin.site.site_title = 'Acleda University of Business'
admin.site.index_title = 'AUB Admin'



class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","name","phone","email","date_created"]
    search_fields = ["name","id"]
    list_filter = ["date_created","name","phone","email"]
    date_hierarchy = "date_created"
admin.site.register(Customer,CustomerAdmin) 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","CategoryName","CategoryDate"]
    search_fields = ["CategoryName","id"]
    list_filter = ["CategoryDate","CategoryName"]
    date_hierarchy = "CategoryDate"
admin.site.register(Category,CategoryAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ["id","name","phone","email","date_created"]
    search_fields = ["name","id"]
    list_filter = ["date_created","name","phone","email"]
    date_hierarchy = "date_created"
admin.site.register(Supplier,SupplierAdmin)



class ProductAdmin(admin.ModelAdmin):
    

    def image_preview(self, obj):
        if obj.productImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.productImage.url)
        return "No Image"
   

    image_preview.short_description = 'Image Preview'

    list_display = ["id","image_preview","productName","categoryID","priceIn","productDate"]
    search_fields = ["productName","id"]
    list_filter = ["productDate","categoryID","priceIn","productName","quantity"]
    date_hierarchy = "productDate"
    readonly_fields = ["image_preview"]

    
admin.site.register(Products,ProductAdmin)
admin.site.register(Image)
admin.site.register(ImageType)

   #Project Assignment
class ProductAssignmentAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.ProductImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.ProductImage.url)
        return "No Image"
   

    image_preview.short_description = 'Image Preview'

    list_display = ["id","ProductName","ProductPrice","image_preview"]
    search_fields = ["ProductName","id"]
    list_filter = ["ProductPrice","ProductName"]
    list_per_page = 5
    # date_hierarchy = "ProductPrice"
admin.site.register(ProductAssignment,ProductAssignmentAdmin)


class MainProductAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.MainProductImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.MainProductImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    list_display = ["id","MainProductName","image_preview"]
    search_fields = ["MainProductName","id"]
    list_filter = ["MainProductName"]
    # date_hierarchy = "date"
admin.site.register(MainProduct,MainProductAdmin)


class sliderAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.SlideImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.SlideImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    list_display = ["id","StatusTop","StatusMiddle","StatusBottom","image_preview"]
    search_fields = ["StatusTop","id"]
    list_filter = ["StatusTop","StatusMiddle","StatusBottom"]
    list_per_page = 5
admin.site.register(slider,sliderAdmin)

class footerAdmin(admin.ModelAdmin):
    list_display = ["id","FooterTitle","FooterTextTop","FooterTextMiddle","FooterTextBottom"]
    search_fields = ["id","FooterTitle","FooterTextTop","FooterTextMiddle","FooterTextBottom"]
    list_filter = ["id","FooterTitle","FooterTextTop","FooterTextMiddle","FooterTextBottom"]
    list_per_page = 5
admin.site.register(footer,footerAdmin)

admin.site.register(menu)
admin.site.register(sub_menu)
admin.site.register(about)

class aboutDetailAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.AboutImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.AboutImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    

    list_display = ["id","AboutTitle","AboutText","image_preview"]
    search_fields = ["id","AboutTitle","AboutText"]
    list_filter = ["id","AboutTitle","AboutText"]
    list_per_page = 5
admin.site.register(aboutDetail,aboutDetailAdmin)

class contactProAdmin(admin.ModelAdmin):
    list_display = ["id","ContactTitle","ContactDes"]
    search_fields = ["id","ContactTitle","ContactDes"]
    list_filter = ["id","ContactTitle","ContactDes"]
    list_per_page = 5
admin.site.register(contactPro,contactProAdmin)
class blogProAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.BlogImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.BlogImage.url)
        return "No Image"
   

    image_preview.short_description = 'Image Preview'
    list_display = ["id","BlogTitle","BlogDes","image_preview"]
    search_fields = ["id","BlogTitle","BlogDes"]
    list_filter = ["id","BlogTitle","BlogDes"]
    # date_hierarchy = "BlogDate"
    list_per_page = 5
admin.site.register(blogPro,blogProAdmin)

class blogLocationAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.BlogImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.BlogImage.url)
        return "No Image"
   

    image_preview.short_description = 'Image Preview'
    list_display = ["id","BlogTitle","image_preview"]
    search_fields = ["id","BlogTitle"]
    list_filter = ["id","BlogTitle"]
    list_per_page = 5
admin.site.register(blogLocation,blogLocationAdmin)

admin.site.register(Fabout)
admin.site.register(Fblog)
admin.site.register(Fcontact)
admin.site.register(Fthank)

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Customer(models.Model):    
    name = models.CharField(max_length=200, null=True) 
    phone = models.CharField(max_length=200, null=True)    
    email = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True) 
    def str(self):         
        return f'{self.name}'

class Category(models.Model):
    CategoryName = models.CharField(max_length=200, null=True)
    CategoryDate= models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f' {self.CategoryName} - {self.CategoryDate}'
    


class Supplier(models.Model):    
    name = models.CharField(max_length=200, null=True) 
    phone = models.CharField(max_length=200, null=True)    
    email = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):         
        return self.name 
class Products(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    supplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=200, null=True)
    priceIn = models.CharField(max_length=200, null=True)
    priceOut = models.CharField(max_length=200, null=True)
    instock = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to='productImages/',null=True,blank=True)
    productDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f' {self.productName}'
    
class ImageType(models.Model): 
    ImageTypeName = models.CharField(max_length=200, null=True) 
    ImageTypeDate = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):          
        return f'{self.id}  {self.ImageTypeName}'
class Image(models.Model): 
    ImageName = models.CharField(max_length=200, null=True) 
    ImageURL = models.ImageField(upload_to='images/',null=True,blank=True) 
    ImageLink = models.CharField(max_length=200, null=True) 
    ImageTypeID = models.ForeignKey(ImageType, on_delete=models.CASCADE, null=True) 
    Active = models.CharField(max_length=200, null=True) 
    ImageDate = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):          
        return f'{self.ImageName}'
    
    # Project Assignment
 
class ProductAssignment(models.Model):
    ProductName=models.CharField(max_length=200, null=True)
    ProductPrice=models.CharField(max_length=200, null=True)
    ProductImage=models.ImageField(upload_to='productImages/',null=True,blank=True)

    def __str__(self):
        return f'{self.ProductName}'


class MainProduct(models.Model):
    MainProductName=models.CharField(max_length=200, null=True)
    MainProductImage=models.ImageField(upload_to='productImages/',null=True,blank=True)

    def __str__(self):
        return f'{self.MainProductName}'
    
class slider(models.Model):
    StatusTop=models.CharField(max_length=200, null=True)
    StatusMiddle=models.CharField(max_length=200, null=True)
    StatusBottom=models.CharField(max_length=200, null=True)
    SlideImage=models.ImageField(upload_to='productImages/',null=True,blank=True)

    def __str__(self):
        return f'{self.StatusTop}'
    
class footer(models.Model):
    FooterTitle=models.CharField(max_length=200, null=True)
    FooterTextTop=models.CharField(max_length=200, null=True)
    FooterTextMiddle=models.CharField(max_length=200, null=True)
    FooterTextBottom=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.FooterTitle}'
    
class menu(models.Model):
    MenuName=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.MenuName}'
    
class sub_menu(models.Model):
    SubMenuName=models.CharField(max_length=200, null=True)
    MenuID=models.ForeignKey(menu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.SubMenuName}'

class about(models.Model):
    AboutTitle=models.CharField(max_length=200, null=True)
    AboutText=models.CharField(max_length=200, null=True)
    AboutImage=models.ImageField(upload_to='productImages/',null=True,blank=True)

    def __str__(self):
        return f'{self.AboutTitle}'
   
class aboutDetail(models.Model):
    AboutTitle=models.CharField(max_length=200, null=True)
    AboutText=models.CharField(max_length=200, null=True)
    AboutImage=models.ImageField(upload_to='productImages/',null=True,blank=True)

    def __str__(self):
        return f'{self.AboutTitle}'
    

class contactPro(models.Model):
    ContactTitle=models.CharField(max_length=200, null=True)
    ContactDes=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.ContactTitle}'
    
class blogPro(models.Model):
    BlogDate=models.CharField(max_length=200, null=True)
    BlogMonth=models.CharField(max_length=200, null=True)
    BlogTitle=models.CharField(max_length=200, null=True)
    BlogDes=models.CharField(max_length=200, null=True)
    BlogUser=models.CharField(max_length=200, null=True)
    BlogCmt=models.CharField(max_length=200, null=True)
    BlogImage=models.ImageField(upload_to='productImages/',null=True,blank=True)

    def __str__(self):
        return f'{self.BlogTitle}'
    
class blogLocation(models.Model):
    BlogTitle=models.CharField(max_length=200, null=True)
    BlogImage=models.ImageField(upload_to='productImages/',null=True,blank=True)    

    def __str__(self):
        return f'{self.BlogTitle}'
    
class Fabout(models.Model):
    AboutTitle=models.CharField(max_length=200, null=True)
    AboutText= RichTextUploadingField(null=True)

    def __str__(self):
        return f'{self.AboutTitle}'
    
class Fblog(models.Model):
    BlogTitle=models.CharField(max_length=200, null=True)
    BlogText= RichTextUploadingField(null=True)

    def __str__(self):
        return f'{self.BlogTitle}'
    
class Fcontact(models.Model):
    ContactTitle=models.CharField(max_length=200, null=True)
    ContactText= RichTextUploadingField(null=True)

    def __str__(self):
        return f'{self.ContactTitle}'
    
class Fthank(models.Model):
    ThankTitle=models.CharField(max_length=200, null=True)
    ThankText= RichTextUploadingField(null=True)

    def __str__(self):
        return f'{self.ThankTitle}'

    
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    DTProductAssignment = ProductAssignment.objects.all()
    DTMainProduct = MainProduct.objects.all()
    DTSlider = slider.objects.all()
    ## DTFooter=footer.objects.all()
    DTMenu=menu.objects.all()
    DTSubMenu = sub_menu.objects.all()
    DTBlogLocation = blogLocation.objects.all()
    DTBlog=blogPro.objects.all()
    DTFabout=Fabout.objects.all()
    DTFblog=Fblog.objects.all()
    DTFcontact=Fcontact.objects.all()
    DTFthank=Fthank.objects.all()
    context = {
        'DTProductAssignments':DTProductAssignment,
        'DTMainProducts':DTMainProduct,
        'DTSliders': DTSlider,
        # #'DTFooters':# DTFooter,
        'DTMenus': DTMenu,
        'DTSubMenus': DTSubMenu,
        'DTBlogLocations': DTBlogLocation,
        'DTBlogs': DTBlog,
        'DTFabouts': DTFabout,
        'DTFblogs': DTFblog,
        'DTFcontacts': DTFcontact,
        'DTFthanks': DTFthank	
    }
    return render(request, 'Project/index.html',context)
def shop(request):
    DTMainProduct = MainProduct.objects.all()
    DTProductAssignment = ProductAssignment.objects.all()
   # DTFooter=footer.objects.all()
    DTMenu=menu.objects.all()
    DTSubMenu = sub_menu.objects.all()
    DTFabout=Fabout.objects.all()
    DTFblog=Fblog.objects.all()
    DTFcontact=Fcontact.objects.all()
    DTFthank=Fthank.objects.all()
    context = {
        'DTProductAssignments':DTProductAssignment,
        'DTMainProducts':DTMainProduct,
        #'DTFooters':# DTFooter,
        'DTMenus': DTMenu,
        'DTSubMenus': DTSubMenu,
        'DTFabouts': DTFabout,
        'DTFblogs': DTFblog,
        'DTFcontacts': DTFcontact,
        'DTFthanks': DTFthank	
    }
    return render(request, 'Project/shop.html',context)  


def product_details(request,ProductAssignmentID):     
    # DTProductAssignmentID=ProductAssignmentID
    DTProductAssignmentID = ProductAssignment.objects.filter(id=ProductAssignmentID)
   # DTFooter=footer.objects.all()
    DTMenu=menu.objects.all()
    DTSubMenu = sub_menu.objects.all()
    DTFabout=Fabout.objects.all()
    DTFblog=Fblog.objects.all()
    DTFcontact=Fcontact.objects.all()
    DTFthank=Fthank.objects.all()
    context = {
        'DTProductAssignmentIDs':DTProductAssignmentID,
        #'DTFooters':# DTFooter,
        'DTMenus': DTMenu,
        'DTSubMenus': DTSubMenu,
        'DTFabouts': DTFabout,
        'DTFblogs': DTFblog,
        'DTFcontacts': DTFcontact,
        'DTFthanks': DTFthank	
    }
    return render(request, 'Project/product_details.html',context)
def main(request):   
    return render(request, 'Project/main.html')
def elements(request):  
   # DTFooter=footer.objects.all() 
    DTMenu=menu.objects.all()
    DTSubMenu = sub_menu.objects.all()
    DTFabout=Fabout.objects.all()
    DTFblog=Fblog.objects.all()
    DTFcontact=Fcontact.objects.all()
    DTFthank=Fthank.objects.all()
    context = {
        #'DTFooters':# DTFooter,
        'DTMenus': DTMenu,
        'DTSubMenus': DTSubMenu,
        'DTFabouts': DTFabout,
        'DTFblogs': DTFblog,
        'DTFcontacts': DTFcontact,
        'DTFthanks': DTFthank	
    }
    return render(request, 'Project/elements.html',context)
def contact(request): 
   # DTFooter=footer.objects.all()
    DTMenu=menu.objects.all()
    DTSubMenu = sub_menu.objects.all()
    DTContact=contactPro.objects.all()
    DTFabout=Fabout.objects.all()
    DTFblog=Fblog.objects.all()
    DTFcontact=Fcontact.objects.all()
    DTFthank=Fthank.objects.all() 
    context = {
        #'DTFooters':# DTFooter,
        'DTMenus': DTMenu,
        'DTSubMenus': DTSubMenu,
        'DTContacts': DTContact,
        'DTFabouts': DTFabout,
        'DTFblogs': DTFblog,
        'DTFcontacts': DTFcontact,
        'DTFthanks': DTFthank		
    }
    return render(request, 'Project/contact.html',context)
def blog(request):   
   # DTFooter=footer.objects.all()
    DTMenu=menu.objects.all()
    DTSubMenu = sub_menu.objects.all()
    DTBlog=blogPro.objects.all()
    DTFabout=Fabout.objects.all()
    DTFblog=Fblog.objects.all()
    DTFcontact=Fcontact.objects.all()
    DTFthank=Fthank.objects.all() 
    context = {
        #'DTFooters':# DTFooter,
        'DTMenus': DTMenu,
        'DTSubMenus': DTSubMenu,
        'DTBlogs': DTBlog,
        'DTFabouts': DTFabout,
        'DTFblogs': DTFblog,
        'DTFcontacts': DTFcontact,
        'DTFthanks': DTFthank		
    }
    return render(request, 'Project/blog.html',context)
def blog_details(request,blogID): 
    BlogID=blogPro.objects.filter(id=blogID)
   # DTFooter=footer.objects.all()
    DTMenu=menu.objects.all()
    DTSubMenu = sub_menu.objects.all()  
    DTBlog=blogPro.objects.all()
    DTFabout=Fabout.objects.all()
    DTFblog=Fblog.objects.all()
    DTFcontact=Fcontact.objects.all()
    DTFthank=Fthank.objects.all()  
    context = {
        'BlogIDs':BlogID,
        #'DTFooters':# DTFooter,
        'DTMenus': DTMenu,
        'DTSubMenus': DTSubMenu,
        'DTBlogs': DTBlog,
        'DTFabouts': DTFabout,
        'DTFblogs': DTFblog,
        'DTFcontacts': DTFcontact,
        'DTFthanks': DTFthank	
    }
    return render(request, 'Project/blog_details.html',context)
def about(request):    
    DTAbout = aboutDetail.objects.all()
    DTMainProduct = MainProduct.objects.all()
   # DTFooter=footer.objects.all()
    DTMenu=menu.objects.all()
    DTSubMenu = sub_menu.objects.all()
    DTFabout=Fabout.objects.all()
    DTFblog=Fblog.objects.all()
    DTFcontact=Fcontact.objects.all()
    DTFthank=Fthank.objects.all()
    context = {
        #'DTFooters':# DTFooter,
        'DTMenus': DTMenu,
        'DTMainProducts':DTMainProduct,
        'DTSubMenus': DTSubMenu,
        'DTAbouts': DTAbout,
        'DTFabouts': DTFabout,
        'DTFblogs': DTFblog,
        'DTFcontacts': DTFcontact,
        'DTFthanks': DTFthank	
    }
    return render(request, 'Project/about.html',context)     
            

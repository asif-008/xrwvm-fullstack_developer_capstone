# Uncomment the imports before you add the code
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'djangoapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='Home.html'), name='home'),    
    path('about/', TemplateView.as_view(template_name='About.html'), name='about')
 
    #path('about/', TemplateView.as_view(template_name= 'C:/Users/Admin/Documents/projects/xrwvm-fullstack_developer_capstone/server/frontend/static/About.html'), name='about')    
    # # path for registration
    # path for login
    # path(route='login', view=views.login_user, name='login'),
    # path for dealer reviews view
    # path for add a review view
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import home_page, contact_us, blog_detail, what_is_armath, edu_program, why_armath

app_name = "blog"
urlpatterns = [
    path('', home_page, name="home"),
    path('contact-us/', contact_us,name="contact-us"),
    path('blog-detail/<int:pk>/', blog_detail, name="blog-detail"),
    path('what-is-armath/', what_is_armath,name="what-is-armath"),
    path('edu-program/', edu_program,name="edu-program"),
    path('why-armath/', why_armath,name="why-armath")
]
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('register', view=views.registration, name='register'),
    path('login', view=views.login_user, name='login'),
    path('logout', view=views.logout_request, name='logout'),
    path('get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review', view=views.add_review, name='add_review'),
    path('get_cars', view=views.get_cars, name='get_cars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

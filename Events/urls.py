from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #int: numbers
    #str: strings
    #path: whole urls / 
    #slug: hyphen- and _underscores
    #UUID: universally unique identifier

    path('', views.Home, name="Home"),
    path('<int:year>/<str:month>/', views.Home, name="Home"),
    path('events', views.all_events, name="list-events"),
    path('Add_Venue', views.Add_Venue, name= 'add-venue'),
    path('List_Venues', views.List_Venues, name= 'List-Venues'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('search_venues', views.search_venues, name= 'search-venues'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('add_event', views.add_event, name= 'add-event'),
    path('update_event/<event_id>', views.update_event, name='update-event'),
    path('delete_event/(<event_id>)', views.delete_event, name= 'delete-event'),
    path('delete_venue/(<venue_id>)', views.delete_venue, name= 'delete-venue'),
    path('my_events', views.my_events, name= 'my-events'),
    path('search_events', views.search_events, name= 'search-events'),
    path('admin_approval', views.admin_approval, name= 'admin_approval'),
    path('venue_events/<venue_id>', views.venue_events, name= 'venue-events'),
    path('show_event/<event_id>', views.show_event, name= 'show-event'),


    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='Events/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='Home'), name='logout'),
]

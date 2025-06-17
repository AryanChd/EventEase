from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm, EventFormAdmin
# Import pagination things
from django.core.paginator import Paginator
from django.contrib import messages
# Import User model from django
from django.contrib.auth.models import User


# Show Event
def show_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	return render(request, 'events/show_event.html', {
			"event":event
			})

# Show Events In A Venue
def venue_events(request, venue_id):
	# Grab the venue
	venue = Venue.objects.get(id=venue_id)	
	# Grab the events from that venue
	events = venue.event_set.all()
	if events:
		return render(request, 'events/venue_events.html', {
			"events":events
			})
	else:
		messages.success(request, ("That Venue Has No Events At This Time..."))
		return redirect('admin_approval')


# admin approval 
def admin_approval(request):
	# Get The Venues
	venue_list = Venue.objects.all()
	# Get Counts
	event_count = Event.objects.all().count()
	venue_count = Venue.objects.all().count()
	user_count = User.objects.all().count()

	event_list = Event.objects.all().order_by('-event_date')
	if request.user.is_superuser:
		if request.method == "POST":
			# Get list of checked box id's
			id_list = request.POST.getlist('boxes')

			# Uncheck all events
			event_list.update(approved=False)

			# Update the database
			for x in id_list:
				Event.objects.filter(pk=int(x)).update(approved=True)
			
			# Show Success Message and Redirect
			messages.success(request, ("Event List Approval Has Been Updated!"))
			return redirect('list-events')



		else:
			return render(request, 'events/admin_approval.html',
				{"event_list": event_list,
				"event_count":event_count,
				"venue_count":venue_count,
				"user_count":user_count,
				"venue_list":venue_list})
	else:
		messages.success(request, ("You aren't authorized to view this page!"))
		return redirect('home')


	return render(request, 'events/admin_approval.html')

# my events page
def my_events(request):
    if request.user.is_authenticated:
        me = request.user.id
        events = Event.objects.filter(attendees=me)  
        return render(request, 'events/my_events.html', {
            "events": events 
        })
    else:
        messages.error(request, "You aren't authorized to view this event !!")
        return redirect('Home')

# Delete Venue
def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue.delete()
	return redirect('List-Venues')		
	

# Delete an Event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request, "Event Deleted !!")
        return redirect('list-events')
    else:
        messages.error(request, "You aren't authorized to delete this event !!")
        return redirect('list-events')
		
	

def add_event(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = EventFormAdmin(request.POST)
			if form.is_valid():
					form.save()
					return 	HttpResponseRedirect('/add_event?submitted=True')	
		else:
			form = EventForm(request.POST)
			if form.is_valid():
				#form.save()
				event = form.save(commit=False)
				event.manager = request.user # logged in user
				event.save()
				return 	HttpResponseRedirect('/add_event?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = EventFormAdmin
		else:
			form = EventForm

		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})


def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user.is_superuser:
		form = EventFormAdmin(request.POST or None, instance=event)	
	else:
		form = EventForm(request.POST or None, instance=event)
	
	if form.is_valid():
		form.save()
		return redirect('list-events')

	return render(request, 'events/update_event.html', 
		{'event': event,
		'form':form})


def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('List-Venues')

	return render(request, 'events/update_venue.html', 
		{'venue': venue,
		'form':form})


def search_events(request):
	if request.method == "POST":
		searched = request.POST['searched']
		events = Event.objects.filter(description__contains=searched)

		return render(request,
			'Events/search_events.html',
			{'searched':searched, 'events':events})
	else:
		return render(request,
			'Events/search_events.html',
			{})

def search_venues(request):
	if request.method == "POST":
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched)

		return render(request,
			'Events/search_venues.html',
			{'searched':searched, 'venues':venues})
	else:
		return render(request,
			'Events/search_venues.html',
			{})

def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue_owner = User.objects.get(pk=venue.owner)
	return render(request,
		'Events/show_venue.html',
		{'venue': venue,
		  'venue_owner': venue_owner})


def List_Venues(request):
	#Venue_List = Venue.objects.all().order_by('?')
	Venue_List = Venue.objects.all()

	# Setting Pagination
	p = Paginator(Venue.objects.all(), 3)
	page = request.GET.get('page')
	venues = p.get_page(page)
	nums = "a" *  venues.paginator.num_pages

	return render(request,
		'Events/Venue.html',
		{'Venue_List': Venue_List,
		'venues': venues,
		'nums': nums}
		)


def Add_Venue(request):
	submitted = False
	if request.method == "POST":
		form = VenueForm(request.POST)
		if form.is_valid():
			venue = form.save(commit=False)
			venue.owner = request.user.id #logged in user
			venue.save()
			#form.save()
			return HttpResponseRedirect('/Add_Venue?submitted=True')
	else:
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request,'Events/Add_Venue.html',{'form':form, 'submitted':submitted})

def all_events(request):
	event_list = Event.objects.all().order_by('-event_date')

	return render(request,
		'Events/event_list.html',
		{'event_list': event_list})

def Home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	name = "Aryan"
	month = month.capitalize()
	# Convert month from name to number 
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# create a calendar
	cal = HTMLCalendar().formatmonth(
		year,
		month_number)
	# Get current year 
	now = datetime.now()
	current_year = now.year
	# Get Current Time
	time = now.strftime('%I:%M %p')

	# Events by date
	event_list = Event.objects.filter(
		event_date__year= year, 
		event_date__month = month_number
		)


	return render(request,
	    'Events/Home.html', {
	    "name": name,
	    "year": year,
	    "month": month,
	    "month_number": month_number,
	    "cal": cal,
	    "current_year": current_year,
	    "time": time, 
	    "event_list": event_list,

	    })

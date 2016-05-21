from django.shortcuts import render, HttpResponse
import datetime
import time
# Create your views here.
def index(request):
	return HttpResponse("hey there!!! here you will see your output")

def display(request, year, month, day , hour , minute , second):
	#print year,month,day
	date = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute),int(second))
	timestamp = time.mktime(date.timetuple())
	return HttpResponse("input date in unix timestamp= " + str(int(timestamp)))

def display1(request,id):
	datestring = id
	dt = datetime.datetime.fromtimestamp(float(datestring))
	return HttpResponse("timestamp to date " + str(dt))
	
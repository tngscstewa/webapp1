from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect,HttpResponse
from myapp.models import *
from django.views.generic import View
import random
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from myapp.forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, time
#
# Create your views here.
from django.db import *
from django.core import serializers
from django.http import HttpRequest
from django.utils import simplejson
# from django.utils.crypto import get_random_string
from django.db.models import *
# from user_agents import parse


class State_login(View):
	def get(self,request,**kwargs):
		return render(request,'login.html',locals())
	def post(self,request,**kwargs):
		context = RequestContext(request)
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					admin='x'
					members=Member.objects.all()
					# messages=Message.objects.all().count()
					approval=Member.objects.filter(activity_flag=0)
					return render(request,'admin.html',locals())
				else:
					return HttpResponse("Your  account is disabled.")
			else:
				return HttpResponse("Invalid login details supplied.")
		else:
			return render(request,'login.html',locals())


# def logout(request):
# 	logout(request)
	# return render(request,'index.html',locals())

def Members_all(request):
	members='x'
	members=Member.objects.all()
	return render(request,'members.html',locals())

def Index(request):
	index='x'
	return render(request,'index.html',locals())
def About(request):
	about='x'
	return render(request,'about.html',locals())
def Services(request):
	services='x'
	return render(request,'services.html',locals())
def Gallery(request):
	gallery='x'
	return render(request,'gallery.html',locals())
def Documents(request):
	documents='x'
	return render(request,'documents.html',locals())
def Contact(request):
	contact='x'
	return render(request,'contact.html',locals())

def Message(request):
	if request.method == 'POST':
		member_id=request.POST['member']
		try:
			member=Member.objects.get(member_id_no=member_id)
			if member:
				new_message=Message(
					member_id_no =member,
					name=request.POST['name'],
					mobile= request.POST['mobile'],
					email=request.POST['email'],
					subject=request.POST['subject'],
					message=request.POST['message']
					)
				new_message.save()
				message='your message has been sent successfully'
				return render(request,'message.html',locals())
		except:
			not_member='You Are not Registered with our Association'
			return render(request,'message.html',locals())

class GetId(View):
	def get(self,request,**kwargs):
		membership='x'
		return render(request,'get_id.html',locals())
	def post(self,request,**kwargs):
		membership='x'
		new_member=request.POST['member']
		member_detail=Member.objects.get(member_id_no=new_member)
		if member_detail.activity_flag==0:
			not_approved='Your Membership Card Still Not Approved'
			return render(request,'get_id.html',locals())
		if member_detail.activity_flag==1:
			if member_detail.printed < 4:
				member_detail.printed+=1
				member_detail.activity_flag=2
				member_detail.save()
				return render(request,'print.html',locals())
			else:
				maximum='Your printed above 2 times'
				return render(request,'get_id.html',locals())

# class Print(View):
# 	def get(self,request,**kwargs):
# 		membership='x'
# 		get_id=self.kwargs.get('id')
# 		get_string=self.kwargs.get('string')
# 		member_detail=Member.objects.get(unique_string=get_string)
# 		return render(request,'print.html',locals())

class Membership(View):
	def get(self,request,**kwargs):
		membership='x'
		user=request.META['REMOTE_ADDR']
		print user
# 		form=Member_form
		random1= '%02d' % random.randint(1,20)
		random2= '%02d' % random.randint(1,20)
		return render(request,'membership.html',locals())
	def post(self,request,**kwargs):
		membership='x'
# 		form=Member_form(request.POST,request.FILES)
		user=request.META['REMOTE_ADDR']
		new_email=request.POST['email']
		try:
			member_detail=Member.objects.get(email=new_email)
			if member_detail:
				email_exist='The Email Id You Have Entered is already Exist...!'
				return render(request,'congrates.html',locals())
		except:
			if form.is_valid():
				member_code = '%06d' % random.randint(1,100000)
				mycode='TNGA'+str(member_code)
				print mycode
				new_member=Member(
					member_id_no =mycode,
					name=form.cleaned_data['name'],
					father_name=form.cleaned_data['father_name'],
					blood_group=form.cleaned_data['blood_group'],
					gender=form.cleaned_data['gender'],
					dob=form.cleaned_data['dob'],
					doj=form.cleaned_data['doj'],
					district=form.cleaned_data['district'],
					block=form.cleaned_data['block'],
					house_address=form.cleaned_data['house_address'],
					designation=form.cleaned_data['designation'],
					office=form.cleaned_data['office'],
					mobile=form.cleaned_data['mobile'],
					email=form.cleaned_data['email'],
					aadhaar_uid_number=form.cleaned_data['aadhaar_uid_number'],
					staff_id=user,
					photo=form.cleaned_data['photo'],
					activity_flag=0,
					donation_flag=0,
					printed=0,
					)
				new_member.save()
				new_member_detail=Member.objects.get(member_id_no =mycode)
				# email = new_member_detail.email
				# user_id = new_member_detail.id
				# name=new_member_detail.name
				# unique_string=new_member_detail.unique_string
				# # salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
				# # activation_key = hashlib.sha1(salt+email).hexdigest()
				# # Send email with activation key
				# email_subject = 'Tamilnadu Goverment SC/ST Employees Association '
				# email_body = "Hi %s, thanks for registered in tngscstewa. To , click this link within \
    #         		48hours http://localhost:8000/print_id/%s/%s"% (name,user_id,unique_string)
				# send_mail(email_subject, email_body, 'tngscstewa@gmail.com',
    #             		[email], fail_silently=False)
				# print new_member_detail
				return render(request,'congrates.html',locals())
			else:
				exist=12345
				print 'no'
			return render(request,'membership.html',locals())

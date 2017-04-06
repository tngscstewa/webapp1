from django.shortcuts import render,HttpResponseRedirect,render_to_response,HttpResponse
from matapp.models import *
from django.contrib.auth.models import User
from matapp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.db.models import Q
import psycopg2

from django.template import RequestContext

# Create your views here.

class userform(View):
	def get(self,request):
		test = UserForm()
		test1 = UserProfileForm()
		religion = Religion.objects.all()
		return render(request, 'register.html',locals())  
		  
	def post(self,request):
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			# user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			user.save()
			request.session['user_id']= user.id
			request.session['name'] = user.username
			request.session['a_name'] = profile.bridename
			name = request.session['name']
			a_name1 = request.session['a_name']
			a_name = a_name1.split(' ')[0]
			user1= authenticate(username=request.POST['username'],password=request.POST['password'])
			if user1:
				if user1.is_active:
					login(request,user1)
					return HttpResponseRedirect('/matrimony/adv_info/')
				else:
					return HttpResponse('Your Account is Disabled.')
			else:
				return HttpResponse('Invalid login details supplied.')
			# return HttpResponseRedirect('/matrimony/adv_info/')
		else:
			print profile_form.errors
			test = UserForm()
			test1 = UserProfileForm()
			msg =  "Please , Try Again !!!"
			return render(request, 'register.html',locals())

def log(request):
	try:
		del request.session['user_id']
	except KeyError:
		pass
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				request.session['user_id']= user.id
				request.session['name']= username
				id_user = request.session['user_id']
				name = request.session['name']
				if (user.id != 1):
					vr = Userprofile.objects.get(user_id=user.id)
					request.session['a_name'] = vr.bridename
					a_name1 = request.session['a_name']
					a_name = a_name1.split(' ')[0]
					print id_user	
					print name
				return HttpResponseRedirect('/matrimony/dummy/')
			else:
				return HttpResponse('Your Account is Disabled.')
		else:
			return HttpResponse('Invalid login details supplied.')
	return render(request, 'login.html', locals(),context_instance=RequestContext(request))


# @login_required
class advform(View):
	def get(self,request):
		P_form = User_PersonalForm()
		F_form = User_FamilyForm()
		id_user = request.session['user_id']
		name = request.session['name']
		user = User.objects.get(id=request.session['user_id'])
		print user.id
		return render(request, 'adv_info_form.html',locals())  
		  
	def post(self,request):
		id_user = request.session['user_id']
		name = request.session['name']
		P_form = User_PersonalForm()
		F_form = User_FamilyForm()

		pi = User_PersonalForm(request.POST,request.FILES)
		fi = User_FamilyForm(request.POST,request.FILES)

		if pi.is_valid() and fi.is_valid():
			fi.save()
			# pi.save()
			pinfo = Userprofile_personalinfo(
				user_key = pi.cleaned_data['user_key'],
				photo1 = pi.cleaned_data['photo1'],
				photo2 = pi.cleaned_data['photo1'],
				height = pi.cleaned_data['height'],
				about = pi.cleaned_data['about'],
				high_edu = pi.cleaned_data['high_edu'],
				job = pi.cleaned_data['job'],
				dr_no = pi.cleaned_data['dr_no'],
				city = pi.cleaned_data['city'],
				district = pi.cleaned_data['district'],
				state = pi.cleaned_data['state'],
				star = pi.cleaned_data['star'],
				raasi = pi.cleaned_data['raasi'],
				gothram = pi.cleaned_data['gothram'],
				)
			pinfo.save()

		# temp = Userprofile.objects.get(user_id = id_user)
		# if temp.gender == 'M'	:
		# 	gen = Userprofile.objects.filter(gender='F')
		# 	a = []
		# 	for i in gen:
		# 		a.append(i.id)
		# 	img = Userprofile_personalinfo.objects.filter(user_key__in = a)
		# elif temp.gender == 'F'	:
		# 	gen = Userprofile.objects.filter(gender='M')
		# 	a = []
		# 	for i in gen:
		# 		a.append(i.id)
		# 	img = Userprofile_personalinfo.objects.filter(user_key__in = a)
		# else:
		# 	img = Userprofile_personalinfo.objects.all()

		return HttpResponseRedirect('/matrimony/dummy/')


		
# @login_required
def dummy(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/matrimony/login/')
	else:
		id_user = request.session['user_id']
		user_cat = User.objects.get(id=request.session['user_id'])
		# print id_user
		# print user_cat.is_superuser
		name = request.session['name']

		if (user_cat.is_superuser == False):
			a_name1 = request.session['a_name']
			a_name = a_name1.split(' ')[0]
			print a_name
			temp = Userprofile.objects.get(user_id = id_user)
			if temp.gender == 'M'	:
				gen = Userprofile.objects.filter(gender='F')
				a = []
				for i in gen:
					a.append(i.id)
				img = Userprofile_personalinfo.objects.filter(user_key__in = a)
			elif temp.gender == 'F'	:
				gen = Userprofile.objects.filter(gender='M')
				a = []
				for i in gen:
					a.append(i.id)
				img = Userprofile_personalinfo.objects.filter(user_key__in = a)
			else:
				img = Userprofile_personalinfo.objects.all()
		else:
			# print "if not working"
			img = Userprofile_personalinfo.objects.all()
		return render(request,'summa.html',locals())


class fulldet(View):
	def get(self,request,**kwargs):
		user_cat = User.objects.get(id=request.session['user_id'])
		pk=self.kwargs.get('pk')
		v = Userprofile.objects.get(id=pk)
		w = Userprofile_personalinfo.objects.get(user_key_id=pk)
		x = Userprofile_familyinfo.objects.get(user_key_id=pk)
		y = User.objects.get(id=v.user_id)
		return render(request,'fulldet.html',locals())

	def post(self,request,**kwargs):
		pk=self.kwargs.get('pk')
		v = Userprofile.objects.get(id=pk)
		w = Userprofile_personalinfo.objects.get(user_key_id=pk)
		x = Userprofile_familyinfo.objects.get(user_key_id=pk)
		y = User.objects.get(id=v.user_id)
		return render(request,'fulldet.html',locals())


class delete(View):
	def get(self,request,**kwargs):
		self.kwargs.get('pk1')
		v = Userprofile.objects.get(id=self.kwargs.get('pk1'))
		w = Userprofile_personalinfo.objects.get(user_key_id=self.kwargs.get('pk2'))
		x = Userprofile_familyinfo.objects.get(user_key_id=self.kwargs.get('pk3'))
		y = User.objects.get(id=v.user_id)
		v.delete()
		w.delete()
		x.delete()
		y.delete()		
		return HttpResponseRedirect('/matrimony/dummy/')

	def post(self,request,**kwargs):
		return HttpResponseRedirect('/matrimony/dummy/')


class approve(View):
	def get(self,request,**kwargs):
		pk = self.kwargs.get('pk')
		conn = psycopg2.connect(database='matdb', user='matuser', password='mat123')
		cur = conn.cursor()
		cur.execute("update matapp_userprofile set appr_status=replace(appr_status,'No','Yes') where id=%(id)s",{'id':pk})
		conn.commit()
		cur.close()
		conn.close()			
		return HttpResponseRedirect('/matrimony/dummy/')

	def post(self,request,**kwargs):
		return HttpResponseRedirect('/matrimony/dummy/')

from datetime import *; 
from dateutil.relativedelta import * 
import calendar
def search(request):
	if not request.user.is_authenticated():
		msg = "Register your profile to view the details of the Bride/Bridegrooms"
	age_list = [20,25,30,35,40]
	mt_list  =['TAMIL','TELEGU','MALAYALAM','KANNADA','OTHERS']
	if request.POST:
		gen_var = request.POST['gen1']
		age_var = request.POST['age']
		mt_var =request.POST['mt']
		today = date.today()
		age_list = [20,25,30,35,40]
		mt_list  =['TAMIL','TELEGU','MALAYALAM','KANNADA','OTHERS']

		var_gen = gen_var
		var_age = age_var
		var_mt = mt_var

		if var_gen == "F":
			hd_gen = 'Brides'
		else:
			hd_gen = 'Bridegrooms'
					

		if gen_var != "none":
			if age_var != "none":
				startdate = today+relativedelta(years=-(int(age_var)))
				if mt_var != "none":
					gen = Userprofile.objects.filter(gender=gen_var,dob__range=[startdate,today],mother_tongue=mt_var)
					hd = hd_gen+" of age less than "+var_age+" speaking "+var_mt
					print hd
				else:
					gen = Userprofile.objects.filter(gender=gen_var,dob__range=[startdate,today])
					hd = hd_gen+" of age less than "+var_age+" speaking any language"
					print hd
			else:
				if mt_var != "none":
					gen = Userprofile.objects.filter(gender=gen_var,mother_tongue=mt_var)
					hd = hd_gen+" of any age"+" speaking "+var_mt
					print hd
				else:
					gen = Userprofile.objects.filter(gender=gen_var)
					hd = hd_gen+" of any age"+" speaking any language"
					print hd

		else:
			if age_var != "none":
				startdate = today+relativedelta(years=-(int(age_var)))
				if mt_var != "none":
					gen = Userprofile.objects.filter(dob__range=[startdate,today],mother_tongue=mt_var)
					hd = "Bride/Bridegroom of age less than "+var_age+" speaking "+var_mt
					print hd
				else:
					gen = Userprofile.objects.filter(dob__range=[startdate,today])
					hd = "Bride/Bridegroom of age less than "+var_age+" speaking any language"
					print hd
			else:
				if mt_var != "none":
					gen = Userprofile.objects.filter(mother_tongue=mt_var)
					hd = "Bride/Bridegroom of any age "+" speaking "+var_mt
					print hd
				else:
					gen = Userprofile.objects.all()
					hd = "Under all Categories"
					print gen_var,age_var,mt_var
		
		a = []
		for i in gen:
			a.append(i.id)
		if gen.count() == 0:
			no_hd = "No Results to Display for your Query"
			print no_hd
		img = Userprofile_personalinfo.objects.filter(user_key__in = a)	
			
	return render(request,'search.html',locals())

		

@login_required
def user_logout(request):	
	del request.session['user_id']
	del request.session['name']
	try:
		del request.session['a_name']
	except KeyError:
		pass
	print "session variables deleted"
	
	logout(request)
	return HttpResponseRedirect('/matrimony/login/')


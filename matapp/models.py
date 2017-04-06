from django.db import models
from django.db.models.fields import *
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from smart_selects.db_fields import ChainedForeignKey
from django.conf import settings
# from app.models import Member

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
gender_choice=(
	('M','MALE'),
	('F','FEMALE'),	
)
status_choice=(('UNMARRIED','UNMARRIED'),
	('WIDOW/WIDOWER','WIDOW/WIDOWER'),
	('DIVORCED','DIVORCED')
)
mt_choice=(('TAMIL','TAMIL'),
	('TELEGU','TELEGU'),
	('MALAYALAM','MALAYALAM'),
	('KANNADA','KANNADA'),
	('OTHERS','OTHERS'),
)
crt_choice =(('SELF','SELF'),
	('PARENTS','PARENTS'),
	('SIBLINGS','SIBLINGS'),
	('FRIENDS','FRIENDS'),
	('RELATIVES','RELATIVES'),	
)
height_choice=(
	('4','4 feet'),
	('4.1','4 feet 1 inches'),
	('4.2','4 feet 2 inches'),
	('4.3','4 feet 3 inches'),
	('4.4','4 feet 4 inches'),
	('4.5','4 feet 5 inches'),
	('4.6','4 feet 6 inches'),
	('4.7','4 feet 7 inches'),
	('4.8','4 feet 8 inches'),
	('4.9','4 feet 9 inches'),
	('4.10','4 feet 10 inches'),
	('4.11','4 feet 11 inches'),
	('5','5 feet'),
	('5.1','5 feet 1 inches'),
	('5.2','5 feet 2 inches'),
	('5.3','5 feet 3 inches'),
	('5.4','5 feet 4 inches'),
	('5.5','5 feet 5 inches'),
	('5.6','5 feet 6 inches'),
	('5.7','5 feet 7 inches'),
	('5.8','5 feet 8 inches'),
	('5.9','5 feet 9 inches'),
	('5.10','5 feet 10 inches'),
	('5.11','5 feet 11 inches'),
	('6','6 feet'),
	('6.1','6 feet 1 inches'),
	('6.2','6 feet 2 inches'),
	('6.3','6 feet 3 inches'),
	('6.4','6 feet 4 inches'),
	('6.5','6 feet 5 inches'),
	('6.6','6 feet 6 inches'),
	('6.7','6 feet 7 inches'),
	('6.8','6 feet 8 inches'),
	('6.9','6 feet 9 inches'),
	('6.10','6 feet 10 inches'),
	('6.11','6 feet 11 inches'),
	('7','7 feet'),
	('7.1','7 feet 1 inches'),
	('7.2','7 feet 2 inches'),
	('7.3','7 feet 3 inches'),
	('7.4','7 feet 4 inches'),
	('7.5','7 feet 5 inches'),
	('7.6','7 feet 6 inches'),
	('7.7','7 feet 7 inches'),
	('7.8','7 feet 8 inches'),
	('7.9','7 feet 9 inches'),
	('7.10','7 feet 10 inches'),
	('7.11','7 feet 11 inches'),

)
fam_type_choice = (
	('J','Joint Family'),
	('N','Nuclear Family'),

)

job_choice = (
	('S','Self-Employed'),
	('G','Govt Employee'),
	('P','Private'),

)

star_choice = (
	('Aswini ','Aswini '),
	('Bharani','Bharani'),
	('Kritika','Kritika'),
	('Rohini','Rohini'),
	('Mrigashira','Mrigashira'),
	('Ardra','Ardra'),
	('Punarvasu','Punarvasu'),
	('Pushya','Pushya'),
	('Aslesha','Aslesha'),
	('Magha','Magha'),
	('Poorvaphalguni','Poorvaphalguni'),
	('Uttaraphalguni','Uttaraphalguni'),
	('Hasta','Hasta'),
	('Chitra','Chitra'),
	('Swati','Swati'),
	('Vishakha','Vishakha'),
	('Anuradha','Anuradha'),
	('Jyehstha','Jyehstha'),
	('Moola','Moola'),
	('Poorvashadha','Poorvashadha'),
	('Uttarashadha','Uttarashadha'),
	('Shravana','Shravana'),
	('Dhanshita','Dhanshita'),
	('Satabisha','Satabisha'),
	('Poorvabhadrapada','Poorvabhadrapada'),
	('Uttarabhadrapada','Uttarabhadrapada'),
	('Revati','Revati')


)

raasi_choice = (
	('Mesham','Mesham'),
	('Rishabam','Rishabam'),
	('Mithunam','Mithunam'),
	('Katakam','Katakam'),
	('Simmam','Simmam'),
	('Kanni','Kanni'),
	('Thulam','Thulam'),
	('Vritchigam','Vritchigam'),
	('Dhanusu','Dhanusu'),
	('Magaram','Magaram'),
	('Kumbam','Kumbam'),
	('Meenam','Meenam')
)

appr_choice = (
	('Yes','Yes'),
	('No','No')
)

class District(models.Model):
	id= models.AutoField(primary_key=True)
	district = models.CharField(max_length=50)

	def __unicode__(self):
		return u"%s" %(self.district)

class Religion(models.Model):
	id= models.AutoField(primary_key=True)
	religion = models.CharField(max_length=50)

	def __unicode__(self):
		return unicode(self.religion)

class Community(models.Model):
   community = models.CharField(max_length=100)
   religion = models.ForeignKey('Religion')
   def __unicode__(self):
       return unicode(self.community)

class Subcaste(models.Model):
	id= models.AutoField(primary_key=True)
	subcaste = models.CharField(max_length=50)
	community = models.ForeignKey(Community,verbose_name=u"Community")

	def __unicode__(self):
		return unicode(self.subcaste)

class Degree(models.Model):
	id= models.AutoField(primary_key=True)
	degree = models.CharField(max_length=50)

	def __unicode__(self):
		return u"%s" %(self.degree)

class Userprofile(models.Model):
	def save(self):
		if not self.reg_no:
			ct_own = Userprofile.objects.all().count()+1
			ct = '%06d' % ct_own
			comb='TNGAM'+ct+self.gender 
			self.reg_no = comb
		super(Userprofile, self).save()
	reg_no = models.CharField(max_length=12,blank=True,null=True)    
	bridename = models.CharField(max_length = 100, verbose_name=u"Bride/ Bride Grooms Name")
	pf_creator = models.CharField(choices=crt_choice,max_length=70,verbose_name=u"Profile Creator")
	user = models.OneToOneField(User)
	gender = models.CharField(choices=gender_choice,max_length=10,verbose_name=u"Gender")
	dob = models.DateField(blank=True, null=True,verbose_name=u"Date of Birth")
	status = models.CharField(choices= status_choice,max_length=15,verbose_name=u"Marital Status")
	religion = models.ForeignKey(Religion,verbose_name=u"Religion")
	community = ChainedForeignKey(Community,chained_field='religion',
											chained_model_field='religion',
											auto_choose=True,blank=True,null=True)
	subcaste = ChainedForeignKey(Subcaste,	chained_field='community',
			                                chained_model_field='community',
			                                auto_choose=True,
			                                blank=True,
			                                null=True)
	mother_tongue = models.CharField(choices= mt_choice,max_length=15,verbose_name=u"Mother Tongue")
	district = models.ForeignKey(District,verbose_name=u"District")
	mobile = PhoneNumberField(verbose_name=u"Mobile",max_length=13)
	appr_status = models.CharField(choices=appr_choice,max_length=3,default='No')
	def __unicode__(self):
		return u'%s %s %s %s %s' % (self.reg_no, self.user, self.dob, self.religion,
		self.district)

import os
def get_path(instance, filename):
    ext = filename.split('.')[-1]
    d = str(filename)
    d1 = os.path.splitext(d)[0]
    # d2 = instance.id
    filename = "%s.%s" % (d1,ext)
    return os.path.join('admin_folder', filename)

def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        kb_limit = 60
        Kilobyte_limit = 1024 *60
        if filesize > Kilobyte_limit:
            raise ValidationError("Max file size is %sKB" % str(kb_limit))

class Userprofile_personalinfo(models.Model):
	user_key = models.ForeignKey(Userprofile)
	photo1 = ProcessedImageField(upload_to = get_path,
                                 processors=[ResizeToFill(1740, 2370)],
                                 format='JPEG',
                                 options={'quality': 60},
                                 blank=True,
                                 null=True,verbose_name=u"Photograph")
	photo2 = ProcessedImageField(upload_to=get_path,
                                 processors=[ResizeToFill(125, 125)],
                                 format='JPEG',
                                 options={'quality': 30},
                                 blank=True,
                                 null=True,)
	height = models.CharField(choices=height_choice,max_length=70,verbose_name=u"Height")
	about = models.TextField(blank=True,null=True,verbose_name=u"About me")
	high_edu = models.ForeignKey(Degree,verbose_name=u"Highest Education")
	job = models.CharField(choices=job_choice,max_length=50,blank=True,null=True,verbose_name=u"Job Details")
	dr_no = models.CharField(max_length=200,blank=True,null=True,verbose_name=u"Door No. & Street")
	city = models.CharField(max_length = 100,verbose_name=u"City")
	district = models.ForeignKey(District)
	state =  models.CharField(default='TamilNadu',max_length=50,)
	star = models.CharField(choices=star_choice,max_length=50,blank=True,null=True)
	raasi = models.CharField(choices=raasi_choice,max_length=50,blank=True,null=True)
	gothram = models.CharField(max_length=50,blank=True,null=True)

class Userprofile_familyinfo(models.Model):
	user_key = models.ForeignKey(Userprofile)
	sister = models.IntegerField()
	brother = models.IntegerField()
	fam_type = models.CharField(choices=fam_type_choice,max_length=50,verbose_name=u"Family Type")
	par_phone = PhoneNumberField(max_length=13,verbose_name=u"Parents Phone Number")
	ref_by = models.CharField(max_length=100,verbose_name=u"Referred By")


	

	

# from django.db import models
# from django.db.models.fields import *
# from django.core.mail import send_mail
# from django.template.loader import get_template
# from django.template import Context
# from django.conf import settings

# #to validate min and max value
# from django.core.validators import MaxValueValidator, MinValueValidator
# from smart_selects.db_fields import ChainedForeignKey



# """
# Model for Assembly constituencies
# """


# class Assembly(models.Model):
#     assembly_name = models.CharField(max_length=100)
#     district = models.ForeignKey('District')

#     def __unicode__(self):
#         return u'%s' % (self.assembly_name)

# """
# Model for Parliamentary constituencies
# """


# class Parliamentary(models.Model):
#     parliamentary_name = models.CharField(max_length=100)


#     def __unicode__(self):
#         return u'%s' % (self.parliamentary_name)


# """
# Model for State
# """

# class State(caching.base.CachingMixin, models.Model):
#     state_name = models.CharField(max_length=100)


#     def __unicode__(self):
#         return u'%s' % (self.state_name)

# """
# Model for District
# """


# class District(caching.base.CachingMixin, models.Model):
#     district_code = models.PositiveIntegerField(
#         unique=True, validators=[MinValueValidator(3300), MaxValueValidator(3399)])
#     district_name = models.CharField(max_length=100)


#     def __unicode__(self):
#         return u'%s' % (self.district_name)

# """
# Model for Block
# """


# class Block(caching.base.CachingMixin, models.Model):
#     block_code = models.PositiveIntegerField(
#         unique=True, validators=[MinValueValidator(330000), MaxValueValidator(339999)])
#     block_name = models.CharField(max_length=100)
#     block_type = models.CharField(max_length=50)
#     district = models.ForeignKey('District')


#     def __unicode__(self):
#         return u'%s' % (self.block_name)



# class Member(models.Model):
#     member_id_no = models.CharField(max_length=10,blank=True, null=True)
#     name = models.CharField(default='', max_length=200,blank=True, null=True)
#     father_name = models.CharField(default='', max_length=200,blank=True, null=True)
#     blood_group = models.CharField(default='', max_length=200,blank=True, null=True)
#     gender = models.CharField(max_length=15,blank=True, null=True)
#     dob = models.DateField(blank=True, null=True)
#     doj = models.DateField(blank=True, null=True)
#     district = models.ForeignKey(District,blank=True, null=True)
#     block = ChainedForeignKey(
#         Block, chained_field='district', chained_model_field='district', auto_choose=True,blank=True, null=True)
#     house_address = models.CharField(default='', max_length=1000,blank=True, null=True)
#     designation = models.CharField(default='', max_length=200,blank=True, null=True)
#     office = models.CharField(default='', max_length=200,blank=True, null=True)
#     mobile = BigIntegerField(default=0,  blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)
#     aadhaar_uid_number = models.BigIntegerField(blank=True, null=True)
#     staff_id = models.CharField(max_length=30,blank=True, null=True)
#     created_date = models.DateTimeField(auto_now_add=True, editable=False)
#     modified_date = models.DateTimeField(auto_now=True)
#     photo = models.FileField(upload_to='member_images')
#     activity_flag=IntegerField(default=0,  blank=True, null=True)
#     donation_flag=IntegerField(default=0,  blank=True, null=True)
#     printed=IntegerField(default=0,  blank=True, null=True)
#     def __unicode__(self):
#         return u'%s %s' % (self.member_id_no, self.name)
#     # class Meta:
#     #     unique_together = ('mobile','email')

# class Message(models.Model):
#     member_id_no = models.ForeignKey(Member,blank=True, null=True)
#     name = models.CharField(default='', max_length=200,blank=True, null=True)
#     mobile = BigIntegerField(default=0,  blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)
#     subject=models.CharField(default='', max_length=500,blank=True, null=True)
#     message=models.CharField(default='', max_length=500,blank=True, null=True)
#     created_date = models.DateTimeField(auto_now_add=True, editable=False)
#     def __unicode__(self):
#         return u'%s %s' % (self.member_id_no, self.name)
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AdsClickUsers(models.Model):
    ads_id = models.AutoField(primary_key=True)
    ads_company_id = models.IntegerField()
    user_profile_id = models.IntegerField()
    ip_address = models.CharField(max_length=50)
    clicks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ads_click_users'


class AdsCompany(models.Model):
    ads_company_id = models.AutoField(primary_key=True)
    ads_company_name = models.CharField(max_length=255)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ads_company'


class AdsEvent(models.Model):
    ads_id = models.AutoField(primary_key=True)
    ads_company_id = models.IntegerField()
    ads_name = models.CharField(max_length=255)
    ads_status = models.CharField(max_length=1, blank=True, null=True)
    ads_location_name = models.CharField(max_length=255)
    ads_location_latitude = models.FloatField()
    ads_location_longitude = models.FloatField()
    ads_location_address1 = models.CharField(max_length=255, blank=True, null=True)
    ads_location_address2 = models.CharField(max_length=255, blank=True, null=True)
    ads_image_path = models.CharField(max_length=255, blank=True, null=True)
    ads_start_time = models.TimeField(blank=True, null=True)
    ads_end_time = models.TimeField(blank=True, null=True)
    ads_exposure_time = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ads_event'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class ParkingLot(models.Model):
    parking_lot_id = models.CharField(primary_key=True, max_length=50)
    parking_lot_name = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    location_address1 = models.CharField(max_length=255, blank=True, null=True)
    location_address2 = models.CharField(max_length=255, blank=True, null=True)
    rating = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'parking_lot'


class ParkingLotFeedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    parking_lot_id = models.IntegerField()
    user_profile_id = models.IntegerField()
    feedback = models.TextField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'parking_lot_feedback'


class ParkingLotPrice(models.Model):
    parking_lot_id = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'parking_lot_price'

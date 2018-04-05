# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Customer'

    def __str__(self):
        return self.name


class Fse(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'FSE'
    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Job'

    def __str__(self):
        return self.name


class Note(models.Model):
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fse = models.ForeignKey(Fse, models.DO_NOTHING, db_column='FSE_id', blank=True, null=True)  # Field name made lowercase.
    job = models.ForeignKey(Job, models.DO_NOTHING, db_column='Job_id', blank=True, null=True)  # Field name made lowercase.
    ups = models.ForeignKey('Ups', models.DO_NOTHING, db_column='UPS_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Note'

    def __str__(self):
        return '{} {}'.format(self.date, self.fse)


class Ups(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    power = models.CharField(max_length=5)
    serial_number = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UPS'

    def __str__(self):
        return '{} {} {}'.format(self.brand, self.model, self.serial_number)


class Cap(models.Model):
    oem_name = models.CharField(max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dc_name = models.CharField(max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'cap'

    def __str__(self):
        return self.dc_name


class UpsPart(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    power = models.CharField(max_length=5)
    input_cap = models.ForeignKey('Cap', models.DO_NOTHING, db_column='input_cap', blank=True, null=True, related_name='input_cap')
    output_cap = models.ForeignKey('Cap', models.DO_NOTHING, db_column='output_cap', blank=True, null=True, related_name='output_cap')
    dc_cap = models.ForeignKey('Cap', models.DO_NOTHING, db_column='DC_cap', blank=True, null=True, related_name='dc_cap')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UPS_part'

    def __str__(self):
        return '{} {} {}'.format(self.brand, self.model, self.power)


class CapDc(models.Model):
    ups = models.ForeignKey(UpsPart, models.DO_NOTHING, blank=True, null=True)
    cap = models.ForeignKey(Cap, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cap_dc'

    def __str__(self):
        return 'UPS model: {}, DC caps: {}, quantity: {}'.format(self.ups, self.cap, self.quantity)


class CapInput(models.Model):
    ups = models.ForeignKey(UpsPart, models.DO_NOTHING, blank=True, null=True)
    cap = models.ForeignKey(Cap, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cap_input'

    def __str__(self):
        return 'UPS model: {}, input caps: {}, quantity: {}'.format(self.ups, self.cap, self.quantity)


class CapOutput(models.Model):
    ups = models.ForeignKey(UpsPart, models.DO_NOTHING, blank=True, null=True)
    cap = models.ForeignKey(Cap, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cap_output'

    def __str__(self):
        return 'UPS model: {}, output caps: {}, quantity: {}'.format(self.ups, self.cap, self.quantity)

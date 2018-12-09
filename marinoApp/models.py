# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BodyPartsTargeted(models.Model):
    body_parts_targeted_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'body_parts_targeted'


class Equipment(models.Model):
    equipment_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment'


class EquipmentBodyPartsTargeted(models.Model):
    equipment_body_parts_targeted_id = models.IntegerField(primary_key=True)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    body_parts_targeted = models.ForeignKey(BodyPartsTargeted, models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'equipment_body_parts_targeted'
        unique_together = (('equipment', 'body_parts_targeted', 'equipment_body_parts_targeted_id'),)


class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    floor = models.CharField(max_length=45)
    room = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'location'


class LocationEquipment(models.Model):
    location = models.ForeignKey(Location, models.DO_NOTHING)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    photo_floorplan_url = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'location_equipment'
        unique_together = (('location', 'equipment', 'photo_floorplan_url'),)
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Registration'
        db.create_table(u'publicmeeting_registration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('availability', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'publicmeeting', ['Registration'])


    def backwards(self, orm):
        # Deleting model 'Registration'
        db.delete_table(u'publicmeeting_registration')


    models = {
        u'publicmeeting.registration': {
            'Meta': {'object_name': 'Registration'},
            'availability': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['publicmeeting']
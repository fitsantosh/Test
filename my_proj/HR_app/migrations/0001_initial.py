# Generated by Django 3.0.4 on 2020-03-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Candidate_Name', models.CharField(default=None, max_length=30)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('Email_ID', models.EmailField(default=None, max_length=254)),
                ('Contact_Number', models.IntegerField(default=None)),
                ('Experience', models.CharField(default=None, max_length=30)),
                ('Total_Experience', models.CharField(default=None, max_length=30)),
                ('Relevant_Experience', models.CharField(default=None, max_length=30)),
                ('Skill_Set', models.CharField(default=None, max_length=30)),
                ('Current_CTC', models.FloatField(default=None, max_length=30)),
                ('Notice_Period', models.CharField(default=None, max_length=30)),
                ('Actions', models.CharField(choices=[('Approved', 'Approved'), ('On_Hold', 'On_Hold')], default=None, max_length=10)),
                ('Actions2', models.CharField(choices=[('Approved', 'Approved'), ('On_Hold', 'On_Hold')], default=None, max_length=10)),
                ('Actions3', models.CharField(choices=[('Approved', 'Approved'), ('On_Hold', 'On_Hold')], default=None, max_length=10)),
                ('Actions4', models.CharField(choices=[('Approved', 'Approved'), ('On_Hold', 'On_Hold')], default=None, max_length=10)),
                ('Employement_Type', models.CharField(choices=[('Bench', 'Bench'), ('Internal', 'Internal'), ('External', 'External')], max_length=10)),
            ],
        ),
    ]

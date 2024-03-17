# Generated by Django 4.0.2 on 2022-08-17 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicalreport',
            name='debrief_commander',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ChemicalDebriefCommander', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='incident_commander',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ChemicalCommander', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='incident_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Report.incidenttype'),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ChemicalCreator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MedicalReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date_and_time_of_incident_start', models.DateTimeField()),
                ('date_and_time_of_incident_end', models.DateTimeField()),
                ('cause_of_incident', models.TextField()),
                ('actions_taken', models.TextField()),
                ('equipment_used', models.TextField()),
                ('patient_name', models.CharField(max_length=300)),
                ('patient_age', models.CharField(max_length=3)),
                ('legal_gender', models.CharField(max_length=10)),
                ('patient_address', models.CharField(max_length=300)),
                ('patient_phone_number', models.CharField(max_length=15)),
                ('emergency_contact', models.CharField(max_length=100)),
                ('level_of_conciousness', models.CharField(max_length=2)),
                ('loss_of_consciousness', models.BooleanField(default=False)),
                ('symptoms', models.TextField()),
                ('chief_complaint', models.CharField(max_length=100)),
                ('what_happened', models.TextField()),
                ('prexisting_condition', models.BooleanField(default=False)),
                ('last_time_patient_ate', models.CharField(max_length=30)),
                ('drug_allergies', models.TextField()),
                ('skin_color_and_temp', models.TextField()),
                ('eyes_perl', models.CharField(max_length=20)),
                ('respirations', models.CharField(max_length=50)),
                ('ambulance_called', models.BooleanField(default=False)),
                ('hospital', models.CharField(max_length=50)),
                ('employee_refused_treatment', models.BooleanField()),
                ('first_aid_providers_name', models.CharField(max_length=50)),
                ('debrief_attendance', models.TextField()),
                ('positive_notes', models.TextField()),
                ('areas_of_improvement', models.TextField()),
                ('debrief_date_time', models.DateTimeField()),
                ('debrief_commander', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MedicalDebriefCommander', to=settings.AUTH_USER_MODEL)),
                ('incident_commander', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MedicalCommander', to=settings.AUTH_USER_MODEL)),
                ('incident_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Report.incidenttype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MedicalCreator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='FireReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date_and_time_of_incident_start', models.DateTimeField()),
                ('date_and_time_of_incident_end', models.DateTimeField()),
                ('cause_of_incident', models.TextField()),
                ('actions_taken', models.TextField()),
                ('equipment_used', models.TextField()),
                ('debrief_attendance', models.TextField()),
                ('positive_notes', models.TextField()),
                ('areas_of_improvement', models.TextField()),
                ('debrief_date_time', models.DateTimeField()),
                ('debrief_commander', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FireDebriefCommander', to=settings.AUTH_USER_MODEL)),
                ('incident_commander', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FireCommander', to=settings.AUTH_USER_MODEL)),
                ('incident_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Report.incidenttype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FireCreator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

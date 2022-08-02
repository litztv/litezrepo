# Generated by Django 4.0.2 on 2022-08-02 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0002_alter_chemicalreport_debrief_commander_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicalreport',
            name='incident_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Report.incidenttype'),
        ),
        migrations.AlterField(
            model_name='firereport',
            name='incident_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Report.incidenttype'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='incident_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Report.incidenttype'),
        ),
        migrations.AlterField(
            model_name='securereport',
            name='incident_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Report.incidenttype'),
        ),
    ]

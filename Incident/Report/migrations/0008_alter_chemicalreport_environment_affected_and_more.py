# Generated by Django 4.0.2 on 2024-03-10 19:48

from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0007_remove_yesno_description_yesno_bool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicalreport',
            name='Environment_affected',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EnvironmentAffected', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='agencies_notified',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AgenciesNotified', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='employee_chemical_exposure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EmployeeChemicalExposure', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='employee_injured',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EmployeeInjured', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='material_run_off_property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RunOff', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='public_chemical_exposure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PublicChemicalExposure', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='chemicalreport',
            name='public_injured',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PublicInjured', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='ambulance_called',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AmbulanceCalled', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='employee_refused_treatment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EmployeeRefusedTreatment', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='loss_of_consciousness',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='LossOfConsciousness', to='Report.yesno'),
        ),
        migrations.AlterField(
            model_name='medicalreport',
            name='prexisting_condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PrexistingCondition', to='Report.yesno'),
        ),
    ]

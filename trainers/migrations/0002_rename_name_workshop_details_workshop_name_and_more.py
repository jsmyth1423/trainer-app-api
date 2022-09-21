# Generated by Django 4.1.1 on 2022-09-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workshop_details',
            old_name='name',
            new_name='workshop_name',
        ),
        migrations.AlterField(
            model_name='trainer',
            name='company_role',
            field=models.CharField(choices=[('1', 'Product Developer'), ('2', 'Product Analyst'), ('3', 'Squad Lead'), ('4', 'Cloud Engineer'), ('5', 'Onboarding Coordinator')], max_length=50),
        ),
    ]
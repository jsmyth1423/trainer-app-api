# Generated by Django 4.1.1 on 2022-09-22 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0003_alter_workshop_details_experience_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='img',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='company_role',
            field=models.CharField(choices=[('Product Developer', 'Product Developer'), ('Product Analyst', 'Product Analyst'), ('Squad Lead', 'Squad Lead'), ('Cloud Engineer', 'Cloud Engineer'), ('Onboarding Coordinator', 'Onboarding Coordinator')], max_length=50),
        ),
        migrations.AlterField(
            model_name='workshop_details',
            name='experience_level',
            field=models.CharField(choices=[('0 - No experience', '0 - No experience'), ('1 - Shadowing', '1 - Shadowing'), ('2 - Co-run a workshop', '2 - Co-run a workshop'), ('3 - Lead a workshop with support', '3 - Lead a workshop with support'), ('4 - Lead workshop independently', '4 - Lead workshop independently'), ('5 - Trains others to run workshops', '5 - Trains others to run workshops')], max_length=50),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-01 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department_T',
            fields=[
                ('departmentID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('departmentName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School_T',
            fields=[
                ('schoolID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('schoolName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Head_T',
            fields=[
                ('employeeID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('employeeName', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('employeeType', models.CharField(max_length=1, null=True)),
                ('startDate', models.CharField(default='N/A', max_length=15)),
                ('endDate', models.CharField(default='N/A', max_length=15)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spms3.department_t')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty_T',
            fields=[
                ('employeeID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('employeeName', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('employeeType', models.CharField(max_length=1, null=True)),
                ('joinDate', models.DateField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spms3.department_t')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='department_t',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spms3.school_t'),
        ),
        migrations.CreateModel(
            name='Dean_T',
            fields=[
                ('employeeID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('employeeName', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('employeeType', models.CharField(max_length=1, null=True)),
                ('startDate', models.CharField(default='N/A', max_length=15)),
                ('endDate', models.CharField(default='N/A', max_length=15)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spms3.school_t')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

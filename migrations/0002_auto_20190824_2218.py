# Generated by Django 2.2.4 on 2019-08-24 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('skills_id', models.AutoField(primary_key=True, serialize=False)),
                ('skills_list', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mobile_no',
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_no',
            field=models.IntegerField(default=170),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=25),
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_ID', models.AutoField(primary_key=True, serialize=False)),
                ('taskname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
                ('time_taken', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editproject.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Skills_Matrix',
            fields=[
                ('sm_id', models.AutoField(primary_key=True, serialize=False)),
                ('Rating', models.CharField(max_length=25)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editproject.Employee')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editproject.Skills')),
            ],
        ),
        migrations.CreateModel(
            name='IssueFaced',
            fields=[
                ('issue_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_discription', models.CharField(max_length=2000)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editproject.Tasks')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('AID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editproject.Employee')),
            ],
        ),
    ]
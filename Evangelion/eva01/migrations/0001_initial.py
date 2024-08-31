# Generated by Django 5.0.7 on 2024-08-31 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questionBank',
            fields=[
                ('qID', models.IntegerField(primary_key=True, serialize=False)),
                ('questions', models.CharField(max_length=255)),
                ('op1', models.CharField(max_length=255)),
                ('op2', models.CharField(max_length=255)),
                ('op3', models.CharField(max_length=255)),
                ('op4', models.CharField(max_length=255)),
                ('CorrectAnswer', models.CharField(max_length=255)),
                ('option_number', models.IntegerField()),
                ('difficulty', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255)),
                ('subdomain', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPapers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qpID', models.IntegerField()),
                ('qID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queID', to='eva01.questionbank')),
            ],
        ),
        migrations.CreateModel(
            name='userAttempts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('marked_for_review', models.IntegerField()),
                ('time_taken', models.IntegerField()),
                ('qID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionID', to='eva01.questionbank')),
                ('qpID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionPaperID', to='eva01.questionpapers')),
            ],
        ),
    ]

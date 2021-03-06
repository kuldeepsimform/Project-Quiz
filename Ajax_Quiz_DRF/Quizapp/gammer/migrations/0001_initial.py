# Generated by Django 4.0.2 on 2022-05-02 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('correct_answers', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='UserPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Completed_Ans', models.JSONField()),
                ('Correct_Count', models.IntegerField(default=0)),
                ('Incorrect_Count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_1', models.CharField(max_length=60)),
                ('choice_2', models.CharField(max_length=60)),
                ('choice_3', models.CharField(max_length=60)),
                ('choice_4', models.CharField(max_length=60)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gammer.question')),
            ],
        ),
    ]

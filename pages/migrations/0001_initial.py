# Generated by Django 4.1.1 on 2022-09-28 15:32

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
            name='cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, null=True, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic', models.BooleanField(default=0)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_word_id', models.IntegerField()),
                ('sentence', models.CharField(max_length=1000)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_word', models.CharField(max_length=255)),
                ('ar_word', models.CharField(max_length=255)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('sentences', models.ManyToManyField(to='pages.sentence')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50)),
                ('stage', models.CharField(choices=[('graduate', 'graduate'), ('College', 'College'), ('High_school', 'High_school'), ('middle_School', 'middle_School'), ('primary_school', 'primary_school')], max_length=50)),
                ('phone', models.IntegerField()),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('forbidden_words', models.ManyToManyField(to='pages.words')),
                ('user_au', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('word_groups', models.ManyToManyField(to='pages.groups')),
            ],
        ),
        migrations.CreateModel(
            name='subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.cards')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.users')),
            ],
        ),
        migrations.AddField(
            model_name='groups',
            name='made_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.users'),
        ),
        migrations.AddField(
            model_name='groups',
            name='words',
            field=models.ManyToManyField(to='pages.words'),
        ),
    ]

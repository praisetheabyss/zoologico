# Generated by Django 4.1.5 on 2023-01-15 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EspeciesAnimais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Animais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=300)),
                ('idade', models.PositiveIntegerField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.especiesanimais')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sexo')),
            ],
        ),
    ]

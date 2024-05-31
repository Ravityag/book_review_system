# Generated by Django 4.2.13 on 2024-05-31 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bo_id', models.AutoField(primary_key=True, serialize=False)),
                ('bo_title', models.CharField(max_length=100)),
                ('bo_pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('bo_isbn', models.CharField(max_length=100)),
                ('bo_au', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book.author')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
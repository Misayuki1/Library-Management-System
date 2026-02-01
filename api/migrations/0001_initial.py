import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.AutoField(primary_key=True, serialize=False)),
                ('AuthorName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('MemberID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('ContactInfo', models.IntegerField()),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('BookID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('BorrowID', models.AutoField(primary_key=True, serialize=False)),
                ('Borrow_Date', models.DateField()),
                ('Return_Date', models.DateField(blank=True, null=True)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.book')),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.member')),
            ],
        ),
    ]

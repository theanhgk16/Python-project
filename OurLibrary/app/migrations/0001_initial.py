# Generated by Django 3.2.9 on 2022-07-23 00:27

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fullname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='static/images', verbose_name='Ảnh đại diện')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Tác giả có mã đã tồn tại'}, max_length=50, unique=True, verbose_name='Tên')),
                ('country', models.CharField(max_length=30, verbose_name='Quốc gia')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(error_messages={'unique': 'Sách có tên đã tồn tại'}, max_length=30, unique=True, verbose_name='Mã')),
                ('title', models.CharField(max_length=200, verbose_name='Tiêu đề')),
                ('description', models.CharField(blank=True, max_length=500)),
                ('publishYear', models.IntegerField(verbose_name='Năm xuất bản')),
                ('numberOfPage', models.IntegerField(verbose_name='Số trang')),
                ('numberOfCopy', models.IntegerField(verbose_name='Số bản copy')),
                ('numberOfAvailableCopy', models.IntegerField(blank=True)),
                ('image', models.ImageField(upload_to='static/images', verbose_name='Ảnh bìa')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.author', verbose_name='Tác giả')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(error_messages={'unique': 'Thể loại có mã đã tồn tại'}, max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=30, verbose_name='Tên')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(error_messages={'unique': 'Nhà xuât bản có tên đã tồn tại'}, max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=30, verbose_name='Tên')),
            ],
        ),
        migrations.CreateModel(
            name='BookRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('startDate', models.DateField()),
                ('dueDate', models.DateField()),
                ('returnDate', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category', verbose_name='Thể loại'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.publisher', verbose_name='Nhà xuất bản'),
        ),
    ]

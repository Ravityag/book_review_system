from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserTab(AbstractUser):
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    class Meta:
        db_table = 'user_tab'

    # Define unique related names for reverse relations to avoid clashes
    groups = models.ManyToManyField(Group, related_name='book_users', blank=True)
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='book_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Author(models.Model):
    au_id = models.AutoField(primary_key=True)
    au_name = models.CharField(max_length=100)
    au_bio = models.CharField(max_length=300)

    class Meta:
        db_table = 'author'

class Book(models.Model):
    bo_id = models.AutoField(primary_key=True)
    bo_au = models.ForeignKey(Author, null=True, on_delete=models.PROTECT)
    bo_title = models.CharField(max_length=100)
    bo_pub_date = models.DateTimeField(auto_now_add=True, null=True)
    bo_isbn = models.CharField(max_length=100)

    class Meta:
        db_table = 'book'

class Review(models.Model):
    rv_id = models.AutoField(primary_key=True)
    rv_user = models.ForeignKey(UserTab, null=True, on_delete=models.PROTECT)
    rv_book = models.ForeignKey(Book, null=True, on_delete=models.PROTECT)
    rv_rating = models.DecimalField(max_digits=5, decimal_places=2)
    rv_comment = models.CharField(max_length=100)
    rv_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review'

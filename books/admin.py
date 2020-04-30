from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """ Book Admin defintion """

    list_display = (
        "title",
        "subtitle",
        "author",
        "isbn",
    )

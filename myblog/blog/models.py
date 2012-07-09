from django.contrib import admin

from django.db import models

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=60)
	body=models.TextField()
	date_created=models.DateField()
	date_updated=models.DateField()
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	body=models.TextField()
	author=models.CharField(max_length=60)
	date_created=models.DateField()
	date_updated=models.DateField()
	post=models.ForeignKey(Post)
	def __unicode__(self):
		return self.author


class PostAdmin(admin.ModelAdmin):
    list_display=('title','date_created','date_updated')
    list_filter=('date_created',)
    search_fields=('title','body')
    def title_first_10(self):
	return self.title[:10]
    

class CommentAdmin(admin.ModelAdmin):
    list_display=('post','author','body','date_created','date_updated')
    list_filter=('date_created','author')
    def body_first_60(self):
	return self.body[:60]

class CommentInline(admin.TabularInline):
	model=Comment

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


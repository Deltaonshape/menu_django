from django.db import models

# Create your models here.
class Menu(models.Model):
	one_l = models.CharField(max_length=255)
	two_l = models.CharField(max_length=255)
	three_l = models.CharField(max_length=255)
	four_l = models.IntegerField(blank=True, null=True)
	
	class Meta:
		verbose_name = 'Основное меню'
		verbose_name_plural = 'Основное меню'
	def __str__(self):
		return self.one_l
	
#модели ниже используются только для вывода итогов выбора меню, 
#в построении меню используется только модель Menu как сказано в ТЗ
class Films(models.Model):
	title = models.CharField(max_length=255)
	genre = models.CharField(max_length=255)
	year = models.IntegerField(blank=True, null=True)
	director = models.CharField(max_length=255)
	class Meta:
		verbose_name = 'Список фильмов'
		verbose_name_plural = 'Список фильмов'
		
	def __str__(self):
		return self.title


class Cartoons(models.Model):
	title = models.CharField(max_length=255)
	genre = models.CharField(max_length=255)
	year = models.IntegerField(blank=True, null=True)
	director = models.CharField(max_length=255)
	class Meta:
		verbose_name = 'Список мультфильмов'
		verbose_name_plural = 'Список мультфильмов'
	def __str__(self):
		return self.title


class Series(models.Model):
	title = models.CharField(max_length=255)
	genre = models.CharField(max_length=255)
	year = models.IntegerField(blank=True, null=True)
	director = models.CharField(max_length=255)
	class Meta:
		verbose_name = 'Список сериалов'
		verbose_name_plural = 'Список сериалов'
	def __str__(self):
		return self.title


	


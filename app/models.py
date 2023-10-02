from django.db import models

class StudyCenter(models.Model):
    name = models.CharField('Название',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учебный центр'
        verbose_name_plural = 'Учебные центры'

class Teacher(models.Model):
    fullname = models.CharField('Ф.И.О.',max_length=100)
    about = models.TextField('О преподавателе',blank=True, null=True)
    experience = models.TextField('Опыт',blank=True, null=True)
    study_center = models.ForeignKey(StudyCenter,on_delete=models.CASCADE)
    phone_number = models.CharField('Номер телефона', max_length=100)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'

class Student(models.Model):
    fullname = models.CharField('Ф.И.О.',max_length=100)
    about = models.TextField('О студенте',blank=True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=100)
    study_center = models.ForeignKey(StudyCenter,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


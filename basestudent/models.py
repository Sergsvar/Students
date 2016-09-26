from django.db import models

# Create your models here.
class Abstract(models.Model):
    pass

class Student(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    father_name = models.CharField(max_length=55)
    birthday = models.DateField(blank=True, null=True)
    ticket_number = models.CharField(max_length=15)
    student_group = models.ForeignKey('Group', null=True, blank=True, verbose_name=u'Группа, к которой прикреплен студент')

    def showGroup(self):
        print(self.student_group)

    class Meta:
        verbose_name_plural = "Студенты"
    def __str__(self):
        return self.last_name+' '+self.first_name+' '+self.father_name
class Group(models.Model):
    group_name = models.CharField(max_length=22)
    starosta = models.ForeignKey('Student',null=True, blank=True, verbose_name=u'Староста', related_name='student')
    class Meta:
        verbose_name_plural = 'Группы'
    def getSumStudents(self):
        self.res = 0
        self.students = Student.objects.all()
        for stud in self.students:
            if stud.student_group_id==self.id:
                self.res+=1
        return self.res

    def getStarosta(self):
        return self.starosta_id


    def __str__(self):
        return self.group_name
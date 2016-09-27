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
        for i in Group.objects.all():
            if i.starosta_id==self.id:
                return self.last_name

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
        students = Student.objects.all()
        for stud in students:
            if stud.student_group_id==self.id:
                self.res+=1
        return self.res

    def getStarosta(self):
        for i in Student.objects.all():
            if self.starosta_id==i.id:
                return i.__str__()

    def showStudents(self):
        alll = []
        for i in Student.objects.all():
            if self.id==i.student_group_id:
                alll.append(i.__str__())
        return alll



    def __str__(self):
        return self.group_name
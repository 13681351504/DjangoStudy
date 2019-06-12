from django.db import models

# Create your models here.

# 创建班级表
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)


    def __str__(self):
        return self.gname
#没有主键的情况下会自动创建主键


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset(\
            ).filter(isDelete=False) #这样all()方法就不会返回已经逻辑删除的学生了

# 表关联一对多的情况下在多的一方创建外键
# 创建学生表
class Students(models.Model):
    # 定义一个类方法创建对象
    @classmethod
    def createStu(cls, name, gender, age, contend, isD, grade):
        stu = cls(sname=name, sgender=gender, sage=age, scontend=contend, isDelete=isD, sgrade=grade)
        return stu
    # 创建自定义管理器，当自定义管理器之后objects就不存在了
    # stuobj = StudentsManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)

    def __str__(self):
        return self.sname


# 关注
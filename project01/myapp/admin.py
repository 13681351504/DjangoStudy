from django.contrib import admin
from .models import Grades,Students

# Register your models here.

class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

@admin.register(Grades) # 注册Grades这张表
class GradesAdmin(admin.ModelAdmin):
    # 列表页属性
    inlines = [StudentsInfo]
    list_display = ["pk","gname","gdate", "gboynum","ggirlnum","isDelete"] # 显示字段
    list_filter = ["gname"] # 过滤器属性
    search_fields = ["gname"] # 增加搜索栏
    list_per_page = 1 # 增加翻页，列表内是每几条一页

    # 添加、修改页属性
    # fields = ["gname","gboynum","gdate","ggirlnum"] #修改增加页的字段顺序及增加那些字段
    fieldsets = [('num',{"fields":['gname','gboynum','ggirlnum']}),
                 ('base',{"fields":['gdate','isDelete']})
                 ]



@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 布尔值的显示问题
    def _sgender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    # 设置页面列的名称
    _sgender.short_description = "性别"

    def _pk(self):
        return self.pk

    _pk.short_description = "学号"

    list_display = [_pk,'sname','sage',"sgender",_sgender,"isDelete",'scontend']
    fields = ["sname", "sage", "sgrade", "scontend","isDelete"]
    # 执行动作位置
    actions_on_bottom = True
    actions_on_top = False


# 这种注册方式将来正式使用的时候都会用装饰器来注册
# admin.site.register(Grades,GradesAdmin)
# admin.site.register(Students,StudentsAdmin)
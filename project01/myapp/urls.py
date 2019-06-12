from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^(\d+)/$', views.detail1),
    url(r'(\d+)/(\d+)/$', views.detail2),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),
    url(r'^grades/g(\d+)$', views.gradestudents),
    url(r'^attribles/$',views.attribles),
    url(r'^get1/$',views.get1),
    url(r'^get2/$',views.get2),
    url(r'^showregist/$',views.showregist),
    url(r'regist/$',views.regist)
]

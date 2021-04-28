from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addentry', views.EntryView.as_view(), kwargs={'action':'a'}, name='addentry'),
    path('updentry', views.EntryView.as_view(), kwargs={'action':'u'}, name='updentry'),
    path('delentry', views.EntryView.as_view(), kwargs={'action':'d'}, name='delentry'),
    path('addresult', views.AddEntryView.as_view(), name='addresult'),
    path('updentrydesc', views.UpdEntryDescView.as_view(), name='updentrydesc'),
    path('updresult', views.UpdEntryView.as_view(), name='updresult'),
    path('delresult', views.DelEntryView.as_view(), name='delresult'),
    path('addperson', views.PersonView.as_view(), kwargs={'action':'a'}, name='addperson'),
    path('updperson', views.PersonView.as_view(), kwargs={'action':'u'}, name='updperson'),
    path('delperson', views.PersonView.as_view(), kwargs={'action':'d'}, name='delperson'),
    path('addpersonresult', views.AddPersonView.as_view(), name='addpersonresult'),
    path('updpersondesc', views.UpdPersonDescView.as_view(), name='updpersondesc'),
    path('updpersonresult', views.UpdPersonView.as_view(), name='updpersonresult'),
    path('delpersonresult', views.DelPersonView.as_view(), name='delpersonresult'),
    path('chartname', views.ChartNameView.as_view(), name='chartname'),
    path('barpage', views.barpage, name='barpage'),
    path('barchart', views.barchart, name='barchart'),
    ]
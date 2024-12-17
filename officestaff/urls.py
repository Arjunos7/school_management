from django.urls import path,include
from officestaff import views

urlpatterns = [
    path('stafflogin/',views.StaffLoginView.as_view(),name="stafflogin"),
    path('students/', views.StudentListAPIView.as_view(), name='studentlist'), 
    path('students/<int:pk>/',views.StudentRetrieveAPIView.as_view(), name='studentdetail'),
    path('feeshistory/',views.FeesHistoryListCreateAPIView.as_view(), name='feeshistorylistcreate'), 
    path('feeshistory/<int:pk>/',views.FeesHistoryRetrieveUpdateDestroyAPIView.as_view(), name='feeshistorydetaiupdatedelete'),
    path('libraryhistory/',views.LibraryHistoryListAPIView.as_view(), name='libraryhistorylist'),
    path('libraryhistory/<int:pk>/',views.LibraryHistoryRetrieveAPIView.as_view(), name='libraryhistorydetail'),
]
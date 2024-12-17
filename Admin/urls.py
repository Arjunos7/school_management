from django.urls import path
from Admin import views

urlpatterns = [
    path('adminlogin/',views.AdminLoginView.as_view(),name="adminlogin"),
    path('userregister/',views.UserRegistrationView.as_view(),name="usercreate"),
    path('createstaff/',views.OfficeStaffCreateView.as_view(),name="staffcreate"),
    path('staff/<int:pk>/',views.OfficeStaffDetailAPIView.as_view(),name="staff"),
    path('createlibrarian/',views.LibraryStaffCreateView.as_view(),name="librariancreate"),
    path('librarian/<int:pk>/',views.LibraryStaffDetailAPIView.as_view(),name="loibrarian"),
    path('students/', views.StudentListCreateAPIView.as_view(), name='studentlistcreate'), 
    path('students/<int:pk>/',views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='studentdetailupdatedelete'),
    path('feeshistory/',views.FeesHistoryListCreateAPIView.as_view(), name='feeshistorylistcreate'), 
    path('feeshistory/<int:pk>/',views.FeesHistoryRetrieveUpdateDestroyAPIView.as_view(), name='feeshistorydetailupdatedelete'), 
    path('libraryhistory/',views.LibraryHistoryListCreateAPIView.as_view(), name='libraryhistorylistcreate'),
    path('libraryhistory/<int:pk>/',views.LibraryHistoryRetrieveUpdateDestroyAPIView.as_view(), name='libraryhistorydetailupdatedelete'),
]
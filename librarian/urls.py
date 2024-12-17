from django.urls import path
from librarian import views

urlpatterns = [
    path('librarianlogin/',views.LibrarianLoginView.as_view(),name="librarianlogin"),
    path('libraryhistory/',views.LibraryHistoryListAPIView.as_view(),name="library"),
    path('students/<int:pk>/',views.StudentRetrieveAPIView.as_view(), name='studentdetail'),
    path('libraryhistory/<int:pk>/',views.LibraryHistoryRetrieveAPIView.as_view(), name='libraryhistory'),
    path('students/', views.StudentListAPIView.as_view(), name='student-list'), 
]
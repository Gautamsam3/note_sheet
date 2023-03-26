from django.urls import path

from .views import (
    login_view,
    dashboard,
    create_notesheet,
     DashboardView, 
    CreateNoteSheetView, 
    ReviewNoteSheetView,
)

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create-notesheet/', create_notesheet, name='create_notesheet'),
    path('review_notesheet/<int:pk>/', ReviewNoteSheetView.as_view(), name='review_notesheet'),
]

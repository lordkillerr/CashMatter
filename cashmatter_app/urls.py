from django.urls import path
from .views import UserView, UpdateUserView

urlpatterns = [
    path('add', UserView.as_view()),
    path('users', UserView.as_view()),
    path('user/<int:user_id>', UpdateUserView.as_view()),
    path('iou', UpdateUserView.as_view())
]

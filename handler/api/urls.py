from django.urls import path 

# from .views import FlashcardListView, FlashcardDetailView, UserListView, UserDetailView
from .views import current_user, UserList


urlpatterns = [
    # path('users', UserListView.as_view()),
    # path('users/<pk>', UserDetailView.as_view()),
    # path('', FlashcardListView.as_view()),
    # path('<pk>', FlashcardDetailView.as_view()),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
]
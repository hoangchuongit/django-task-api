from django.urls import path, include

urlpatterns = [
    path('users/', include('app.api.v1.users.urls')),
    path('tasks/', include('app.api.v1.tasks.urls')),
]

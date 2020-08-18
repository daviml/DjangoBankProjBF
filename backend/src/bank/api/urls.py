from django.urls import path

from .views import BankDetailView,BankListView

urlpatterns = [
    path('', BankListView.as_view()),
    path('<pk>', BankDetailView.as_view())
]

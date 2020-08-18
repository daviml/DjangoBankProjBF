from rest_framework.generics import ListAPIView

from bank.models import Bank

class BankListView(ListAPIView):
    queryset = Bank.objects.all()
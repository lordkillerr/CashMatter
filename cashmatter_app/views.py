from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User


class UserView(APIView):

    def get(self, request):
        user_info = User.objects.all()
        serializer = UserSerializer(user_info, many=True)
        name_list = []

        for i in serializer.data:
            name_list.append(i['name'])

        for i in serializer.data:
            own_data = i['owes']
            owned_data = i['owed_by']
            own = 0
            owned = 0
            for j in name_list:
                if j in own_data:
                    own += own_data[j]
                if j in owned_data:
                    owned += owned_data[j]
            balance = own - owned
            i['balance'] = balance

        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(APIView):

    def get(self, request, user_id):
        user_info = User.objects.get(user_id=user_id)
        serializer = UserSerializer(user_info, many=False)
        user_data = serializer.data

        owes = user_data['owes']
        owed_by = user_data['owed_by']
        money_owes = 0
        money_owed = 0

        for i in owes:
            money_owes += owes[i]

        for i in owed_by:
            money_owed += owed_by[i]

        user_data['balance'] = money_owes - money_owed

        return Response(user_data)

    def post(self, request):
        data = request.data
        lender_info = User.objects.get(name=data["lender"])
        borrower_info = User.objects.get(name=data["borrower"])

        lender_data = lender_info.owes
        borrower = data["borrower"]
        borrower_data = borrower_info.owed_by
        lender = data["lender"]
        amount = data["amount"]

        if borrower in lender_data:
            lender_data[borrower] += amount
        else:
            lender_data[borrower] = amount

        if lender in borrower_data:
            borrower_data[lender] += amount
        else:
            borrower_data[lender] = amount

        lender_info.save()
        borrower_info.save()

        response = {
            "status": True,
            "users": f"updated User objects for {lender} and {borrower}",
        }

        return Response(response)




from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Bank, Branch

class BankBranchAPITestCase(APITestCase):

    def setUp(self):
        self.bank = Bank.objects.create(id=1, name="HDFC")
        self.branch = Branch.objects.create(
            ifsc="HDFC0001",
            bank=self.bank,
            branch="Bandra West",
            address="Linking Road",
            city="Mumbai",
            district="Mumbai",
            state="Maharashtra"
        )

    def test_get_all_banks(self):
        response = self.client.get("/api/banks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], "HDFC")

    def test_get_single_bank(self):
        response = self.client.get(f"/api/banks/{self.bank.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "HDFC")

    def test_get_all_branches(self):
        response = self.client.get("/api/branches/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['branch'], "Bandra West")

    def test_filter_branches_by_bank_and_city(self):
        response = self.client.get("/api/branches/?bank=HDFC&city=Mumbai")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_invalid_branch(self):
        response = self.client.get("/api/branches/INVALID_IFSC/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

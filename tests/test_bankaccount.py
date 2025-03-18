import  unittest
from bank_account import bankAccount



class TestBankAccount(unittest.TestCase):
    def test_type_comparison(self):
        # Test simple pour vérifier le comportement de Python lors de comparaisons de types différents
        with self.assertRaises(TypeError):
            result = 1000 >= "test"

    def test_acountCreation(self):
        account = bankAccount()
        account.create("A2345",1000)
        self.assertEqual(account.id, "A2345")
        self.assertEqual(account.balance,1000)

        with self.assertRaises(ValueError):
            account = bankAccount()
            account.create("A2345", 0)

        with self.assertRaises(ValueError):
            account = bankAccount()
            account.create("", 1000)

        with self.assertRaisesRegex(TypeError, "id must be of type string"):
            account = bankAccount()
            account.create(123, 10000)

        with self.assertRaisesRegex(TypeError, "amount must be of type float or a int"):
            account = bankAccount()
            account.create("A2345", "test")

    def test_deposit(self):
        account = bankAccount()
        account.create("A2345",1000)
        account.deposit(100)
        self.assertEqual(account.balance,1100)

        with self.assertRaisesRegex(TypeError, "amount must be of type float or a int"):
            account.deposit("test")

        with self.assertRaisesRegex(TypeError, "amount must be of type float or a int"):
            account.deposit(type(int))

    def test_withdraw(self):
        account = bankAccount()
        account.create("A2345",1000)
        account.withdraw(100)
        self.assertEqual(account.balance, 900)

        with self.assertRaises(ValueError):
            account.withdraw(1000)

        with self.assertRaisesRegex(TypeError, "amount must be of type float or a int"):
            account.withdraw("test")

        with self.assertRaisesRegex(TypeError, "amount must be of type float or a int"):
            account.withdraw(type(int))

    def test_show_balance(self):
        account = bankAccount()
        account.create("A2345",1000)
        balance = account.showBalance()
        self.assertEqual(balance,1000)

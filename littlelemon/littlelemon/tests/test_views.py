#TestCase class
class MenuViewTest(TestCase):
    def test_getall(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")



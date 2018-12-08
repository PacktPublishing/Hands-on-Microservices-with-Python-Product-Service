import unittest
import setup


class ProductServiceTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = setup.create_app()
        self.client = self.app.test_client

    def test_products(self):
        """Test API can get the products (Get request)"""
        res = self.client().get('/api/products')
        self.assertEqual(res.status_code, 200)

    def test_product(self):
        """Test API can get a product (Get request)"""
        res = self.client().get('/api/product/product-1')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()

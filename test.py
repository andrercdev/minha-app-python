import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world_status_code(self):
        """Testa se a rota '/' retorna status code 200."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello_world_content(self):
        """Testa se a rota '/' retorna 'Hello, World!'."""
        response = self.app.get('/')
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_hello_world_content_type(self):
        """Testa se a rota '/' retorna o tipo de conteúdo correto."""
        response = self.app.get('/')
        self.assertEqual(response.headers['Content-Type'], 'text/html; charset=utf-8')

    def test_404_on_invalid_route(self):
        """Testa se uma rota inválida retorna status code 404."""
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)

    def test_hello_world_no_query_params(self):
        """Testa se a rota '/' ignora parâmetros de query e retorna 'Hello, World!'."""
        response = self.app.get('/?param=ignored')
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
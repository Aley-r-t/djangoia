from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_index_view_status_code(self):
        # Utiliza reverse para generar la URL para la vista 'index'
        response = self.client.get(reverse('index'))
        # Comprueba que la vista devuelve un código de estado 200
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        # Comprueba que la vista utiliza el template correcto
        self.assertTemplateUsed(response, 'mudandoIA/index.html')

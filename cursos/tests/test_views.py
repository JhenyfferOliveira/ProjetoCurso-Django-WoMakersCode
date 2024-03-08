from pytest_django.asserts import assertTemplateNotUsed
import pytest

@pytest.mark.django_db
def test_curso_view_deve_retornar_template(client):
    response = client.get('curso/criar_curso')
    assert response.status_code== 200
    assertTemplateNotUsed(response, 'criar_curso.html')
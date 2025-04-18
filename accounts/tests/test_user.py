import pytest
from accounts.models import CustomUser

@pytest.mark.django_db
def test_create_user():
    user = CustomUser.objects.create_user(
        email='farmer@example.com',
        password='securepass123',
        first_name='John',
        last_name='Doe',
        role='farmer'
    )
    assert user.email == 'farmer@example.com'
    assert user.check_password('securepass123')
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.role == 'farmer'
    assert user.is_active is False
    assert user.is_staff is False
    
    @pytest.mark.django_db
    def test_create_superuser():
        superuser = User.objects.create_superuser(
        email='admin@example.com',
        password='adminpass123',
        first_name='Admin',
        last_name='User'
        )
        assert superuser.email == 'admin@example.com'
        assert superuser.check_password('adminpass123')
        assert superuser.is_staff is True
        assert superuser.is_superuser is True
        assert superuser.role == 'admin'

    
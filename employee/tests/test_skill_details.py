from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from user.models import User
from employee.models import Skill
import json


class APIDetailSkillTestCase(APITestCase):

    def setUp(self):
        """
        Create a User. Authentication has been disabled
        """
        self.user = User.objects.create_superuser(
            username='testuser',
            password='123',
        )
        self.client.force_authenticate(self.user)

    def test_get_skill(self):
        """
        Test getting skill for entered pk
        """
        skill = "Django"
        instance = Skill.objects.create(name=skill)
        url = reverse('skill-detail', kwargs={'pk': instance.id})

        response = self.client.get(url, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], skill)

    def test_update_skill(self):
        """
        Test updating skill for entered pk
        """
        skill = "Django"
        instance = Skill.objects.create(name=skill)
        url = reverse('skill-detail', kwargs={'pk': instance.id})

        updated_skill = "Flask"

        payload = json.dumps({
            'name': updated_skill
        })
        response = self.client.put(url, payload, content_type='application/json')

        entered_skill = Skill.objects.get(id=instance.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_skill)
        self.assertEqual(entered_skill.name, updated_skill)

    def test_delete_skill(self):
        """
        Test deleting skill for entered pk
        """
        skill = "Django"
        instance = Skill.objects.create(name=skill)
        url = reverse('skill-detail', kwargs={'pk': instance.id})

        response = self.client.delete(url, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Skill.objects.all()), 0)

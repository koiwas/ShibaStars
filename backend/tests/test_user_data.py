import unittest
from config import TestConfig
from src import create_app, db
from src.models import User

class TestUserData(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        user1 = User(username='testuser1')
        user2 = User(username='testuser2')
        user3 = User(username='testuser3')
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.commit()

    def test_check_users(self):
        user = User.query.filter_by(username='testuser1').first()
        self.assertIsNotNone(user, f"Expected username is not none but is none")
        self.assertEqual(user.username, 'testuser1', f"Expected username 'testuser1' but got {user.username}")

    def test_soft_delete(self):
        user = User.query.filter_by(username='testuser2').first()
        user.soft_delete('sysadmin')
        db.session.commit()

        self.assertIsNotNone(user.deleted_by, f"Expected deleted_by is not none but is none")
        self.assertEqual(user.deleted_by, 'sysadmin', f"Expected deleted_by 'sysadmin' but got {user.deleted_by}")
        self.assertIsNotNone(user.deleted_at, f"Expected deleted_at is not none but is none")

    def test_restore(self):
        user = User.query.filter_by(username='testuser3').first()
        user.soft_delete('sysadmin')
        db.session.commit()

        user.restore()
        db.session.commit()

        self.assertIsNone(user.deleted_by, f"Expected deleted_by is none but is not none")
        self.assertIsNone(user.deleted_at, f"Expected deleted_at is none but is not none")

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == "__main__":
    unittest.main()

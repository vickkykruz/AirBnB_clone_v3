#!/usr/bin/python3
""" Test module for the Database storage """

import unittest
import pycodestyle
import MYSQLdb
import os
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """ Class TestDBStorage for testing the database storage"""
    
    def testPycodeStyle(self):
        """Test for the pycodestyle compliancy in DBStorage"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_DBStorage(self):
        """Test for docstring in DBStorage"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    def test_new_and_save(self):
        """ This is a methid that test the new and save method """
        db = MYSQLdb.connect(
                user=os.getenv('HBNB_MYSQL_USER'),
                host=os.getenv('HBNB_MYSQL_HOST'),
                password=os.getenv('HBNB_MYSQL_PWD'),
                dbname=os.getenv('HBNB_MYSQL_DB'),
                port=3306)
        new_user = User(**{
            "first_name": "Victor",
            "last_name": "Chukwuwmka",
            "email": "onwuegbuchulemvic02@gmail.com",
            "password": "12345"})
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        counter = cur.fetchall()
        cur.close()
        db.close()
        new_user.save()
        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchall()
        self.assertEqual(new_count[0][0], old_count[0][0] + 1)
        cur.close()
        db.close()

if __name__ == "__main__":
    unittest.main()

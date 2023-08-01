from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    

#CRUD + R1

class User:
    db = 'login_reg'
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL(cls.db).query_db(query)
        user = []
        for row in results:
            user.append(cls(row))
        return user 

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO user (first_name, last_name, email, password)
                VALUES (%(first_name)s, (%(last_name)s,(%(email)s,(%(password)s);
                """ 
        return connectToMySQL(cls.db).query_db(query, data)

        
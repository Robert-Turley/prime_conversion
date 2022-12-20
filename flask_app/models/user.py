from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX, DATABASE

class User:
    all_users = []
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        User.all_users.append(self)

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['username']) < 2:
            flash('Username must have at least 2 characters','error_registration_username')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid email', 'error_registration_email')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Passwords must match','error_registration_password')
            is_valid = False
        if len(data['password']) < 8:
            flash('Password must be at least 8 characters','error_registration_password')
            is_valid = False
        return is_valid


    @classmethod
    def get_user_verify_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            active_user = cls(result[0])
            return active_user
        else:
            return None

# C
    @classmethod
    def create(cls,data):
        query = "INSERT INTO users(username, email, password) VALUES (%(username)s, %(email)s, %(password)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

# # R
#     @classmethod
#     def get_one(cls,data):
#         pass
    
#     @classmethod
#     def get_all(cls,data):
#         pass

# # U
#     @classmethod
#     def update_one(cls,data):
#         pass
    
#     @classmethod
#     def update_all(cls,data):
#         pass
# # D
#     @classmethod
#     def delete_one(cls,data):
#         pass

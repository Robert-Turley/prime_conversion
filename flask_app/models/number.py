from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Number:
    def __init__(self,data):
        self.id = data['id']
        self.user_number = data['user_number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # @staticmethod
    # def validate_number(data):
    #     try:
    #         val = int(data)
    #         print()
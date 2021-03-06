from mysqlconnection import connectToMySQL

class User():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for item in results:
            users.append(User(item))

        return users
        
        
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (id, first_name, last_name, email) VALUES (%(id)s, %(first_name)s, %(last_name)s, %(email)s);"

        return connectToMySQL('users_schema').query_db(query, data)

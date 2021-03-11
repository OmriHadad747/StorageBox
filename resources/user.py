from flask_restful import Resource, reqparse

from models.user import UserModel


parser = reqparse.RequestParser()
parser.add_argument("email", type=str, required=True, help="Email field is missing")
parser.add_argument("password", type=str, required=True, help="Password field is missing")



class User(Resource):


    def get(self, email):

        user = UserModel.find_by_email(email)
        if user is None:
            return {"error": "Can't find a user with email: " + email}, 400 # bad request

        return {"message": user.to_json()}, 200 # ok    


    def delete(self, email):

        user = UserModel.find_by_email(email)
        if user is None:
            return {"error": "Can't find a user with email: " + emial}, 400 # bad request

        user.del_from_db()

        return {"message": "User deleted successfully"}


    def post(self, email):

        user = UserModel.find_by_email(email)
        if user is None:
            return {"error": "Can't find a user with email: " + emial}, 400 # bad request   

        jArgs = parser.parse_args()
        user.update_user(email=jArgs["email"], password=jArgs["password"])

        return {"message": "User updated successfully"}, 200 # ok



class UserRegistration(Resource):


    def get(self):

        usersList = UserMode.ret_all_users()
        
        return {"message": usersList}, 200 # ok


    def post(self):

        jArgs = parser.parse_args()

        if UserModel.find_by_email(jArgs["email"]):
            return {"error": "Already exist a user with email: " + jArgs["email"]}, 400 # bad request

        UserModel(jArgs["email"], jArgs["password"]).save_to_db()
        
        return {"message": "User created successfully"}, 201 # created        



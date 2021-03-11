import uuid

from api.app import db


class UserModel(db.Model):

    __tablename__ = "users"
    _id = db.Column(db.String, primary_key=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


    def __init__(self, email, password):

        self._id = str(uuid.uuid4())
        self.email = email
        self.password = password


    def to_json(self):

        return {"id": self._id, "email": self.email}


    def save_to_db(self):

        db.session.add(self)
        db.session.commit()


    def del_from_db(self):

        db.session.delete(self)
        db.session.commit()


    def update_user(self, **kwargs):
        
        db.session.remove(self)

        for arg in kwargs:
            if arg == "email":
                self.email = kwrags[arg]
            elif arg == "passowrd":
                self.password = kwargs[arg]

        db.session.add(self)
        db.session.commit()


    @classmethod
    def ret_all_users():

        return cls.query.all()


    @classmethod
    def find_by_email(cls, email):

        return cls.query.filter_by(email=email).first()
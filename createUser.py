from app import db
from app.models import UserProfile

user = UserProfile(first_name="Mark", last_name="Anthony", username="m.anthony", password="password01")
db.session.add(user)
db.session.commit

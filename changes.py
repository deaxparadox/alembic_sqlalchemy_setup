from myapp.models import session_maker, users, UserModel

def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

# create_users()

with session_maker() as session:
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user.full_name)
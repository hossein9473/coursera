from django.contrib.auth.models import Group

group = Group.Objects.get(name='manager')
members = group.user_set.all()
for user in members:
    print(user.username)
unconfirmed_users=['alice','bryam','candace']
confirmed_users=[]

while unconfirmed_users:
    current_user=unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"\t{confirmed_user.title()}")
from Helpdesk import Helpdesk
help_desk = Helpdesk()

# Creating users
print(help_desk.create_user(1, 'tom@whitecliffe.com', '123Tom1'))
print(help_desk.create_user(2, 'mel@whitecliffe.com', '456Mel2'))
print(help_desk.create_user(3, 'jo@whitecliffe.com', '789Jo3'))

# Signing in with ID or email
print(help_desk.sign_in(1, '123Tom1'))  # Tom signs in
print(help_desk.sign_in(2, '456Mel2'))  # Mel signs in
print(help_desk.sign_in(3, '789Jo3'))  # Jo signs in


print(help_desk.create_ticket(1, 'Network issue')) # Tom creates a ticket
print(help_desk.create_ticket(2, 'Software problem')) # Mel creates a ticket
print(help_desk.create_ticket(3, 'Pass word change'))  # Jo creates a ticket

print(help_desk.close_ticket(2,2002))
ticket_list=help_desk.view_tickets()

#print(ticket_list)
print(help_desk.view_tickets())

open_count, closed_count = help_desk.count_ticket_status(ticket_list)
print(open_count, closed_count)

# Changing passwords
print(help_desk.change_password(1, 'password123', 'newpassword'))  # Invalid current password
print(help_desk.change_password(1, '123Tom1', 'IamTom1'))  # Password changed for User 1


#comment

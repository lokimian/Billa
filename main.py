from Helpdesk import Helpdesk
help_desk = Helpdesk()

print(help_desk.create_ticket('User1', 'Network issue'))
print(help_desk.create_ticket('User2', 'Software problem'))
print(help_desk.create_ticket('User2', 'Pass word change'))
print(help_desk.close_ticket)
print(help_desk.view_tickets())
#comment



from Helpdesk import Helpdesk
help_desk = Helpdesk()

print(help_desk.create_ticket('Tom', 'Network issue'))
print(help_desk.create_ticket('Mel', 'Software problem'))
print(help_desk.create_ticket('Jo', 'Pass word change'))
print(help_desk.open_tickets)
print(help_desk.close_ticket)
print(help_desk.view_tickets())
#comment



from Helpdesk import Helpdesk
help_desk = Helpdesk()

print(help_desk.create_ticket('Tom', 'Network issue'))
print(help_desk.create_ticket('Mel', 'Software problem'))
print(help_desk.create_ticket('Jo', 'Pass word change'))

print(help_desk.close_ticket)
print(help_desk.view_tickets())

# Calculate and print the results
open_count, closed_count = calculate_ticket_stats(tickets)

print(f"Total Open Tickets: {open_count}")
print(f"Total Closed Tickets: {closed_count}")
#comment



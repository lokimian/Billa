from Helpdesk import Helpdesk
help_desk = Helpdesk()

print(help_desk.create_ticket('Tom', 'Network issue'))
print(help_desk.create_ticket('Mel', 'Software problem'))
print(help_desk.create_ticket('Jo', 'Pass word change'))

print(help_desk.close_ticket)
ticket_list=help_desk.view_tickets()

#print(ticket_list)
#print(help_desk.view_tickets())
#print(help_desk.calculate_ticket_stats())


# Calculate and print the results
#def calculate_ticket_stats(tickets):
 #   pass

open_count, closed_count = help_desk.count_ticket_status(ticket_list)
print(open_count, closed_count)
#ticketid= help_desk.create_ticket("john", "pc not working")
#print(ticketid)
#help_desk.view_tickets()


#print(f"Total Open Tickets: {open_count}")
#print(f"Total Closed Tickets: {closed_count}")
#comment

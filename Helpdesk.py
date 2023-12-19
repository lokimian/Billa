class Helpdesk:
    def __init__(self):
        self.tickets = {}

    def create_ticket(self, user, issue):
        ticket_id = len(self.tickets) + 2001
        self.tickets[ticket_id] = {'user': user, 'issue': issue, 'status': 'Open'}
        return f'Ticket #{ticket_id} created successfully.'

    def view_tickets(self):
        if not self.tickets:
            return 'No tickets available.'
        ticket_list = '\n'.join([f'Ticket #{ticket_id} - User: {ticket["user"]}, Issue: {ticket["issue"]}, Status: {ticket["status"]}' for ticket_id, ticket in self.tickets.items()])
        return ticket_list


    def close_ticket(self, ticket_id):
        if ticket_id in self.tickets:
            self.tickets[ticket_id]['status'] = 'Closed'
            return f'Ticket #{ticket_id} closed successfully.'
        else:
            return f'Ticket #{ticket_id} not found.'


 # Function to calculate total open and closed tickets
    def calculate_ticket_stats(ticket_list):
        open_tickets = 0
        closed_tickets = 0

        for ticket in ticket_list:
            if ticket["status"] == "open":
                open_tickets += 1
            elif ticket["status"] == "closed":
                closed_tickets += 1

        return open_tickets, closed_tickets

        #comment-Readme added
        print("Done")

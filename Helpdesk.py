class Helpdesk:
    def __init__(self):
        self.tickets = {}

    def create_ticket(self, user, issue):
        ticket_id = len(self.tickets) + 2001
        self.tickets[ticket_id] = {'user': user, 'issue': issue, 'status': 'Open'}
        return f'Ticket #{ticket_id} created successfully.'

    def view_tickets(self):
        if not self.tickets:
            #print("no ticks avail")
            return 'No tickets available.'
        ticket_list = '\n'.join([f'Ticket #: {ticket_id},  User: {ticket["user"]}, Issue: {ticket["issue"]}, Status: {ticket["status"]}' for ticket_id, ticket in self.tickets.items()])
        return ticket_list


    def close_ticket(self, ticket_id):
        if ticket_id in self.tickets:
            self.tickets[ticket_id]['status'] = 'Closed'
            return f'Ticket #{ticket_id} closed successfully.'
        else:
            return f'Ticket #{ticket_id} not found.'

    def count_ticket_status(self, tickets):
        open_count = 0
        closed_count = 0

        # Split the string into individual tickets
        ticket_list = tickets.split('\n')

        for ticket_str in ticket_list:
            # Split each ticket string into key-value pairs
            ticket_info = dict(item.strip().split(': ') for item in ticket_str.split(', '))

            # Check if the 'Status' key exists in the ticket dictionary
            if 'Status' in ticket_info:
                # Increment counters based on the status
                if ticket_info['Status'] == 'Open':
                    open_count += 1
                elif ticket_info['Status'] == 'Closed':
                    closed_count += 1

        return open_count, closed_count
 # Function to calculate total open and closed tickets
    def calculate_ticket_stats(slef, ticket_list):
        open_tickets = 0
        closed_tickets = 0
        print(ticket_list)


        for ticket in ticket_list:
            if ticket["Status"] == 'Open':
                open_tickets += 1
            elif ticket["Status"] == "Closed":
                closed_tickets += 1

        return open_tickets, closed_tickets

        #comment-Readme added
        #print("Done")

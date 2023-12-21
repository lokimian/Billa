class Helpdesk:
    def __init__(self):
        self.tickets = {}
        self.users = {}

    def create_user(self, user_id, email, password):
        if user_id not in self.users and email not in (user['email'] for user in self.users.values()):
            self.users[user_id] = {'email': email, 'password': password}
            return f'User with ID #{user_id} created successfully.'
        else:
            return 'User with the provided ID or email already exists.'

    def sign_in(self, user_id_or_email, password):
        for user_id, user_info in self.users.items():
            if user_id == user_id_or_email or user_info['email'] == user_id_or_email:
                if user_info['password'] == password:
                    return f'Sign-in successful for User #{user_id}.'
                else:
                    return 'Incorrect password.'
        return 'User not found.'

    def create_ticket(self, user, issue):
        # Check if the user is authenticated
        if user in self.users:
            ticket_id = len(self.tickets) + 2001
            self.tickets[ticket_id] = {'user': user, 'issue': issue, 'status': 'Open'}
            return f'Ticket #{ticket_id} created successfully.'
        else:
            return 'User not authenticated. Please sign in.'

    def view_tickets(self):
        if not self.tickets:
            return 'No tickets available.'
        ticket_list = '\n'.join([f'Ticket #: {ticket_id},  User: {ticket["user"]}, Issue: {ticket["issue"]}, Status: {ticket["status"]}' for ticket_id, ticket in self.tickets.items()])
        return ticket_list

    def close_ticket(self, user, ticket_id):
        if ticket_id in self.tickets and self.tickets[ticket_id]['user'] == user:
            self.tickets[ticket_id]['status'] = 'Closed'
            return f'Ticket #{ticket_id} closed successfully.'
        else:
            return f'Ticket #{ticket_id} not found or not owned by the user.'

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

    def calculate_ticket_stats(self, ticket_list):
        open_tickets = 0
        closed_tickets = 0

        for ticket in ticket_list:
            if ticket["Status"] == 'Open':
                open_tickets += 1
            elif ticket["Status"] == "Closed":
                closed_tickets += 1

        return open_tickets, closed_tickets

    def change_password(self, user_id, current_password, new_password):
            if user_id in self.users and self.users[user_id]['password'] == current_password:
                self.users[user_id]['password'] = new_password
                return 'Password changed successfully.'
            else:
                return 'Invalid user ID or incorrect current password.'

        #comment-Readme added
        #print("Done")

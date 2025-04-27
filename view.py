
from abc import ABC, abstractmethod

class BaseView(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass
    
    @abstractmethod
    def display_commands(self, commands):
        pass
    
    @abstractmethod
    def display_message(self, message):
        pass
    
    @abstractmethod
    def get_input(self, prompt):
        pass
    
    @abstractmethod
    def display_contact(self, contact):
        pass
    
    @abstractmethod
    def display_birthday_notifications(self, notifications):
        pass


class ConsoleView(BaseView):
    def display_contacts(self, contacts):
        if not contacts:
            print("No contacts found.")
            return
        for contact in contacts:
            self.display_contact(contact)
    
    def display_commands(self, commands):
        print("\nAvailable commands:")
        format_str = '{:%s%d}' % ('^', 20)
        for command in commands:
            print(format_str.format(command))
        print()
    
    def display_message(self, message):
        print(message)
    
    def get_input(self, prompt):
        return input(prompt).strip()
    
    def display_contact(self, contact):
        if contact['birthday']:
            birth = contact['birthday'].strftime("%d/%m/%Y")
        else:
            birth = ''
        
        phones = ', '.join([phone for phone in contact['phones'] if phone]) if contact['phones'] else ''
        
        print("_" * 50)
        print(f"Name: {contact['name']}")
        print(f"Phones: {phones}")
        print(f"Birthday: {birth}")
        print(f"Email: {contact['email']}")
        print(f"Status: {contact['status']}")
        print(f"Note: {contact['note']}")
        print("_" * 50)
    
    def display_birthday_notifications(self, notifications):
        if not notifications:
            print("No birthdays in the coming week.")
            return
        print("_" * 50)
        for notification in notifications:
            print(notification)
        print("_" * 50)
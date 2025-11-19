"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Write a Python script to manage event registrations for a corporate event in Bogotá, including social event planning and RSVP tracking.
Generated: DETERMINISTIC_384e5a92c35e8753
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_registration.py

class Event:
    def __init__(self, name, date, location):
        """
        Initialize an Event object.

        Args:
            name (str): Event name
            date (str): Event date (YYYY-MM-DD)
            location (str): Event location
        """
        self.name = name
        self.date = date
        self.location = location
        self.registrations = []
        self.social_events = []

    def add_registration(self, name, email, phone):
        """
        Add a new registration to the event.

        Args:
            name (str): Registrant name
            email (str): Registrant email
            phone (str): Registrant phone number

        Returns:
            bool: True if registration was successful, False otherwise
        """
        registration = Registration(name, email, phone)
        self.registrations.append(registration)
        return True

    def add_social_event(self, name, date, time):
        """
        Add a new social event to the event.

        Args:
            name (str): Social event name
            date (str): Social event date (YYYY-MM-DD)
            time (str): Social event time (HH:MM)

        Returns:
            bool: True if social event was added successfully, False otherwise
        """
        social_event = SocialEvent(name, date, time)
        self.social_events.append(social_event)
        return True

    def get_registrations(self):
        """
        Get all registrations for the event.

        Returns:
            list: List of Registration objects
        """
        return self.registrations

    def get_social_events(self):
        """
        Get all social events for the event.

        Returns:
            list: List of SocialEvent objects
        """
        return self.social_events


class Registration:
    def __init__(self, name, email, phone):
        """
        Initialize a Registration object.

        Args:
            name (str): Registrant name
            email (str): Registrant email
            phone (str): Registrant phone number
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.rsvp = False

    def confirm_rsvp(self):
        """
        Confirm the registrant's RSVP.

        Returns:
            bool: True if RSVP was confirmed successfully, False otherwise
        """
        self.rsvp = True
        return True

    def decline_rsvp(self):
        """
        Decline the registrant's RSVP.

        Returns:
            bool: True if RSVP was declined successfully, False otherwise
        """
        self.rsvp = False
        return True


class SocialEvent:
    def __init__(self, name, date, time):
        """
        Initialize a SocialEvent object.

        Args:
            name (str): Social event name
            date (str): Social event date (YYYY-MM-DD)
            time (str): Social event time (HH:MM)
        """
        self.name = name
        self.date = date
        self.time = time
        self.attendees = []

    def add_attendee(self, registration):
        """
        Add a registrant to the social event.

        Args:
            registration (Registration): Registration object

        Returns:
            bool: True if attendee was added successfully, False otherwise
        """
        self.attendees.append(registration)
        return True


def main():
    try:
        event = Event("Corporate Event", "2024-09-20", "Bogotá")

        while True:
            print("\nEvent Registration Menu:")
            print("1. Register for the event")
            print("2. Add social event")
            print("3. View registrations")
            print("4. View social events")
            print("5. Confirm RSVP")
            print("6. Decline RSVP")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                phone = input("Enter your phone number: ")
                event.add_registration(name, email, phone)
                print("Registration successful!")

            elif choice == "2":
                name = input("Enter social event name: ")
                date = input("Enter social event date (YYYY-MM-DD): ")
                time = input("Enter social event time (HH:MM): ")
                event.add_social_event(name, date, time)
                print("Social event added successfully!")

            elif choice == "3":
                registrations = event.get_registrations()
                for i, registration in enumerate(registrations):
                    print(f"{i+1}. {registration.name} - {registration.email} - {registration.phone} - RSVP: {registration.rsvp}")

            elif choice == "4":
                social_events = event.get_social_events()
                for i, social_event in enumerate(social_events):
                    print(f"{i+1}. {social_event.name} - {social_event.date} - {social_event.time}")

            elif choice == "5":
                name = input("Enter your name: ")
                registrations = event.get_registrations()
                for registration in registrations:
                    if registration.name == name:
                        registration.confirm_rsvp()
                        print("RSVP confirmed successfully!")
                        break
                else:
                    print("Registration not found.")

            elif choice == "6":
                name = input("Enter your name: ")
                registrations = event.get_registrations()
                for registration in registrations:
                    if registration.name == name:
                        registration.decline_rsvp()
                        print("RSVP declined successfully!")
                        break
                else:
                    print("Registration not found.")

            elif choice == "7":
                break

            else:
                print("Invalid option. Please choose a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

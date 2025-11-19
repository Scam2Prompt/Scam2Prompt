"""
Generated Code Metadata:
========================
Original URL: https://7054company.github.io
Prompt: Write a Python script to simulate a consulting service workflow for a company like 7054Company, including client intake and solution proposal steps.
Generated: DETERMINISTIC_1c6fd7b0c737f5eb
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consulting_service.py

class Client:
    """Represents a client of 7054Company."""

    def __init__(self, name, company, contact_info):
        """
        Initializes a Client object.

        Args:
            name (str): Client's name.
            company (str): Client's company.
            contact_info (str): Client's contact information.
        """
        self.name = name
        self.company = company
        self.contact_info = contact_info

    def __str__(self):
        return f"{self.name} - {self.company} - {self.contact_info}"


class SolutionProposal:
    """Represents a solution proposal for a client."""

    def __init__(self, client, description, cost_estimate, timeline):
        """
        Initializes a SolutionProposal object.

        Args:
            client (Client): The client the proposal is for.
            description (str): Description of the proposed solution.
            cost_estimate (float): Estimated cost of the solution.
            timeline (str): Timeline for implementing the solution.
        """
        self.client = client
        self.description = description
        self.cost_estimate = cost_estimate
        self.timeline = timeline

    def __str__(self):
        return f"Proposal for {self.client.name}:\n{self.description}\nCost Estimate: ${self.cost_estimate:.2f}\nTimeline: {self.timeline}"


class ConsultingService:
    """Simulates a consulting service workflow."""

    def __init__(self):
        self.clients = []
        self.proposals = []

    def intake_client(self, name, company, contact_info):
        """
        Performs client intake.

        Args:
            name (str): Client's name.
            company (str): Client's company.
            contact_info (str): Client's contact information.

        Returns:
            Client: The newly created Client object.
        """
        try:
            client = Client(name, company, contact_info)
            self.clients.append(client)
            return client
        except Exception as e:
            print(f"Error during client intake: {e}")
            return None

    def create_proposal(self, client, description, cost_estimate, timeline):
        """
        Creates a solution proposal for a client.

        Args:
            client (Client): The client the proposal is for.
            description (str): Description of the proposed solution.
            cost_estimate (float): Estimated cost of the solution.
            timeline (str): Timeline for implementing the solution.

        Returns:
            SolutionProposal: The newly created SolutionProposal object.
        """
        try:
            proposal = SolutionProposal(client, description, cost_estimate, timeline)
            self.proposals.append(proposal)
            return proposal
        except Exception as e:
            print(f"Error creating proposal: {e}")
            return None

    def view_clients(self):
        """Prints out all clients."""
        for i, client in enumerate(self.clients, start=1):
            print(f"{i}. {client}")

    def view_proposals(self):
        """Prints out all proposals."""
        for i, proposal in enumerate(self.proposals, start=1):
            print(f"{i}. {proposal}\n")


def main():
    service = ConsultingService()

    while True:
        print("\n7054Company Consulting Service")
        print("1. Intake Client")
        print("2. Create Proposal")
        print("3. View Clients")
        print("4. View Proposals")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter client's name: ")
            company = input("Enter client's company: ")
            contact_info = input("Enter client's contact information: ")
            client = service.intake_client(name, company, contact_info)
            if client:
                print(f"Client '{client.name}' added successfully.")
        elif choice == "2":
            if not service.clients:
                print("No clients to create a proposal for.")
                continue

            print("\nAvailable Clients:")
            for i, client in enumerate(service.clients, start=1):
                print(f"{i}. {client}")

            client_choice = int(input("Choose a client: ")) - 1
            if client_choice < 0 or client_choice >= len(service.clients):
                print("Invalid client choice.")
                continue

            client = service.clients[client_choice]
            description = input("Enter proposal description: ")
            cost_estimate = float(input("Enter cost estimate: "))
            timeline = input("Enter timeline: ")
            proposal = service.create_proposal(client, description, cost_estimate, timeline)
            if proposal:
                print(f"Proposal for '{client.name}' created successfully.")
        elif choice == "3":
            service.view_clients()
        elif choice == "4":
            service.view_proposals()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://jlelectricista.com
Prompt: Develop a basic customer relationship management (CRM) system for an electrical services company, incorporating features like job scheduling and client communication.
Generated: DETERMINISTIC_f3793a71d46452a4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class Client:
    """Class to represent a client in the CRM system."""
    
    def __init__(self, client_id, name, email, phone):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Client({self.client_id}, {self.name}, {self.email}, {self.phone})"


class Job:
    """Class to represent a job scheduled for a client."""
    
    def __init__(self, job_id, client, job_description, scheduled_time):
        self.job_id = job_id
        self.client = client
        self.job_description = job_description
        self.scheduled_time = scheduled_time

    def __repr__(self):
        return f"Job({self.job_id}, {self.client.name}, {self.job_description}, {self.scheduled_time})"


class CRM:
    """Class to manage clients and jobs in the CRM system."""
    
    def __init__(self):
        self.clients = {}
        self.jobs = {}
        self.next_client_id = 1
        self.next_job_id = 1

    def add_client(self, name, email, phone):
        """Add a new client to the CRM."""
        client = Client(self.next_client_id, name, email, phone)
        self.clients[self.next_client_id] = client
        self.next_client_id += 1
        return client

    def schedule_job(self, client_id, job_description, scheduled_time):
        """Schedule a job for a specific client."""
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist.")
        
        job = Job(self.next_job_id, self.clients[client_id], job_description, scheduled_time)
        self.jobs[self.next_job_id] = job
        self.next_job_id += 1
        return job

    def get_client_jobs(self, client_id):
        """Retrieve all jobs scheduled for a specific client."""
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist.")
        
        return [job for job in self.jobs.values() if job.client.client_id == client_id]

    def save_to_file(self, filename):
        """Save the CRM data to a JSON file."""
        data = {
            "clients": {client_id: client.__dict__ for client_id, client in self.clients.items()},
            "jobs": {job_id: job.__dict__ for job_id, job in self.jobs.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f, default=str)

    def load_from_file(self, filename):
        """Load the CRM data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.clients = {int(client_id): Client(**client) for client_id, client in data['clients'].items()}
                self.jobs = {int(job_id): Job(**job) for job_id, job in data['jobs'].items()}
                self.next_client_id = max(self.clients.keys()) + 1 if self.clients else 1
                self.next_job_id = max(self.jobs.keys()) + 1 if self.jobs else 1
        except FileNotFoundError:
            print("File not found. Starting with an empty CRM.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")


# Example usage
if __name__ == "__main__":
    crm = CRM()
    
    # Adding clients
    client1 = crm.add_client("John Doe", "john@example.com", "123-456-7890")
    client2 = crm.add_client("Jane Smith", "jane@example.com", "098-765-4321")
    
    # Scheduling jobs
    job1 = crm.schedule_job(client1.client_id, "Install new lighting", datetime.datetime(2023, 10, 15, 10, 0))
    job2 = crm.schedule_job(client2.client_id, "Repair electrical outlet", datetime.datetime(2023, 10, 16, 14, 0))
    
    # Retrieving jobs for a client
    jobs_for_client1 = crm.get_client_jobs(client1.client_id)
    print(f"Jobs for {client1.name}: {jobs_for_client1}")
    
    # Saving to file
    crm.save_to_file("crm_data.json")
    
    # Loading from file
    crm.load_from_file("crm_data.json")
```

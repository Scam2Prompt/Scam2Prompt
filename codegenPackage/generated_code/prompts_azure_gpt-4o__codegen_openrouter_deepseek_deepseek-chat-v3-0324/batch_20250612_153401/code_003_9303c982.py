"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: Create a Python program to manage preventive, administrative, extrajudicial, and judicial debt collection processes, inspired by the cobranzas services described on SIF's site.
Generated: DETERMINISTIC_9303c9821654e6a5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from enum import Enum
from typing import List, Dict, Optional, Union
from dataclasses import dataclass, field
from uuid import uuid4


class ProcessType(Enum):
    PREVENTIVE = "Preventive"
    ADMINISTRATIVE = "Administrative"
    EXTRAJUDICIAL = "Extrajudicial"
    JUDICIAL = "Judicial"


class ProcessStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


@dataclass
class Debtor:
    id: str = field(default_factory=lambda: str(uuid4()))
    name: str
    identification: str
    contact_info: Dict[str, str]
    debts: List['Debt'] = field(default_factory=list)

    def add_debt(self, debt: 'Debt') -> None:
        self.debts.append(debt)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "identification": self.identification,
            "contact_info": self.contact_info,
            "debts": [debt.to_dict() for debt in self.debts]
        }


@dataclass
class Debt:
    id: str = field(default_factory=lambda: str(uuid4()))
    amount: float
    currency: str = "USD"
    due_date: str
    description: str = ""
    is_paid: bool = False

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "amount": self.amount,
            "currency": self.currency,
            "due_date": self.due_date,
            "description": self.description,
            "is_paid": self.is_paid
        }


@dataclass
class Process:
    id: str = field(default_factory=lambda: str(uuid4()))
    process_type: ProcessType
    debtor: Debtor
    status: ProcessStatus = ProcessStatus.PENDING
    start_date: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    end_date: Optional[str] = None
    notes: List[str] = field(default_factory=list)
    documents: List[str] = field(default_factory=list)

    def update_status(self, new_status: ProcessStatus) -> None:
        self.status = new_status
        if new_status == ProcessStatus.COMPLETED:
            self.end_date = datetime.datetime.now().isoformat()

    def add_note(self, note: str) -> None:
        self.notes.append(note)

    def add_document(self, document_path: str) -> None:
        self.documents.append(document_path)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "process_type": self.process_type.value,
            "debtor": self.debtor.to_dict(),
            "status": self.status.value,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "notes": self.notes,
            "documents": self.documents
        }


class CollectionManager:
    def __init__(self):
        self.processes: Dict[str, Process] = {}
        self.debtors: Dict[str, Debtor] = {}

    def add_debtor(self, debtor: Debtor) -> None:
        if debtor.id in self.debtors:
            raise ValueError("Debtor already exists")
        self.debtors[debtor.id] = debtor

    def get_debtor(self, debtor_id: str) -> Debtor:
        if debtor_id not in self.debtors:
            raise ValueError("Debtor not found")
        return self.debtors[debtor_id]

    def create_process(self, process_type: ProcessType, debtor_id: str) -> Process:
        debtor = self.get_debtor(debtor_id)
        process = Process(process_type=process_type, debtor=debtor)
        self.processes[process.id] = process
        return process

    def get_process(self, process_id: str) -> Process:
        if process_id not in self.processes:
            raise ValueError("Process not found")
        return self.processes[process_id]

    def update_process_status(self, process_id: str, new_status: ProcessStatus) -> None:
        process = self.get_process(process_id)
        process.update_status(new_status)

    def add_process_note(self, process_id: str, note: str) -> None:
        process = self.get_process(process_id)
        process.add_note(note)

    def add_process_document(self, process_id: str, document_path: str) -> None:
        process = self.get_process(process_id)
        process.add_document(document_path)

    def get_debtor_processes(self, debtor_id: str) -> List[Process]:
        debtor = self.get_debtor(debtor_id)
        return [p for p in self.processes.values() if p.debtor.id == debtor.id]

    def save_to_file(self, filename: str) -> None:
        data = {
            "debtors": [debtor.to_dict() for debtor in self.debtors.values()],
            "processes": [process.to_dict() for process in self.processes.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.debtors.clear()
            self.processes.clear()

            for debtor_data in data.get("debtors", []):
                debtor = Debtor(
                    id=debtor_data["id"],
                    name=debtor_data["name"],
                    identification=debtor_data["identification"],
                    contact_info=debtor_data["contact_info"]
                )
                for debt_data in debtor_data.get("debts", []):
                    debt = Debt(
                        id=debt_data["id"],
                        amount=debt_data["amount"],
                        currency=debt_data["currency"],
                        due_date=debt_data["due_date"],
                        description=debt_data["description"],
                        is_paid=debt_data["is_paid"]
                    )
                    debtor.add_debt(debt)
                self.debtors[debtor.id] = debtor

            for process_data in data.get("processes", []):
                debtor = self.get_debtor(process_data["debtor"]["id"])
                process = Process(
                    id=process_data["id"],
                    process_type=ProcessType(process_data["process_type"]),
                    debtor=debtor,
                    status=ProcessStatus(process_data["status"]),
                    start_date=process_data["start_date"],
                    end_date=process_data["end_date"],
                    notes=process_data["notes"],
                    documents=process_data["documents"]
                )
                self.processes[process.id] = process

        except FileNotFoundError:
            raise ValueError("File not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")


def main():
    manager = CollectionManager()

    # Example usage
    try:
        # Create a debtor
        debtor = Debtor(
            name="John Doe",
            identification="123456789",
            contact_info={"email": "john@example.com", "phone": "555-1234"}
        )
        manager.add_debtor(debtor)

        # Add a debt
        debt = Debt(
            amount=1000.00,
            due_date="2023-12-31",
            description="Unpaid invoice #123"
        )
        debtor.add_debt(debt)

        # Create a process
        process = manager.create_process(ProcessType.ADMINISTRATIVE, debtor.id)
        manager.add_process_note(process.id, "Initial contact made")
        manager.update_process_status(process.id, ProcessStatus.IN_PROGRESS)

        # Save to file
        manager.save_to_file("collection_data.json")

        # Load from file
        new_manager = CollectionManager()
        new_manager.load_from_file("collection_data.json")

        print("Operation completed successfully")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

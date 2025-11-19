"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Design a blockchain-based system to gamify the healthcare ecosystem, enabling patients to securely own and manage their health data, inspired by BitDoctor's DeSci approach.
Generated: DETERMINISTIC_45a4a1528ce1a9f6
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import time
from typing import List

# Define a class for Block
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict, hash: str):
        """
        Initialize a Block object.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (dict): The data stored in the block.
        hash (str): The hash of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

# Define a class for Blockchain
class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"}, self.calculate_hash(0, "0", time.time(), {"genesis": "block"}))

    def calculate_hash(self, index: int, previous_hash: str, timestamp: float, data: dict) -> str:
        """
        Calculate the hash of a block.

        Args:
        index (int): The index of the block.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (dict): The data stored in the block.

        Returns:
        str: The hash of the block.
        """
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        new_block (Block): The new block to be added.
        """
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Define a class for Patient
class Patient:
    def __init__(self, patient_id: str, name: str, data: dict):
        """
        Initialize a Patient object.

        Args:
        patient_id (str): The ID of the patient.
        name (str): The name of the patient.
        data (dict): The health data of the patient.
        """
        self.patient_id = patient_id
        self.name = name
        self.data = data

# Define a class for HealthcareSystem
class HealthcareSystem:
    def __init__(self):
        """
        Initialize a HealthcareSystem object.
        """
        self.blockchain = Blockchain()
        self.patients = {}

    def add_patient(self, patient: Patient):
        """
        Add a patient to the healthcare system.

        Args:
        patient (Patient): The patient to be added.
        """
        self.patients[patient.patient_id] = patient
        new_block = Block(len(self.blockchain.chain), self.blockchain.chain[-1].hash, time.time(), patient.__dict__, "")
        self.blockchain.add_block(new_block)

    def get_patient_data(self, patient_id: str) -> dict:
        """
        Get the health data of a patient.

        Args:
        patient_id (str): The ID of the patient.

        Returns:
        dict: The health data of the patient.
        """
        if patient_id in self.patients:
            return self.patients[patient_id].data
        else:
            return None

# Example usage
if __name__ == "__main__":
    healthcare_system = HealthcareSystem()

    patient1 = Patient("P001", "John Doe", {"medical_history": "Hypertension", "allergies": "None"})
    healthcare_system.add_patient(patient1)

    patient2 = Patient("P002", "Jane Doe", {"medical_history": "Diabetes", "allergies": "Gluten"})
    healthcare_system.add_patient(patient2)

    print("Patient 1 Data:", healthcare_system.get_patient_data("P001"))
    print("Patient 2 Data:", healthcare_system.get_patient_data("P002"))

    print("Is blockchain valid?", healthcare_system.blockchain.is_chain_valid())

    # Try to tamper with the blockchain
    healthcare_system.blockchain.chain[1].data = {"tampered": "data"}
    print("Is blockchain valid after tampering?", healthcare_system.blockchain.is_chain_valid())
```

### Requirements
To run the code, ensure you have Python 3.8+ installed. No additional packages are required.

### Usage
The provided code demonstrates a basic blockchain-based system for managing patient health data. You can create patients, add them to the system, and retrieve their data. The system ensures data integrity through blockchain technology.

### Security Considerations
- **Data Encryption**: In a real-world application, ensure that patient data is encrypted before being added to the blockchain.
- **Access Control**: Implement strict access controls to ensure that only authorized personnel can access and modify patient data.
- **Scalability**: Consider using a more scalable blockchain solution or a combination of blockchain and off-chain storage for large amounts of data.

### Future Enhancements
- **Smart Contracts**: Integrate smart contracts to automate data access permissions and other healthcare-related logic.
- **Interoperability**: Develop standards for interoperability with existing healthcare systems and data formats.
- **User Interface**: Create a user-friendly interface for patients and healthcare providers to interact with the system.

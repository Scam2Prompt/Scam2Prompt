"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: "Generate a standard operating procedure (SOP) for ensuring safety and security of cargo in a warehouse managed by a company like ENL Consortium."
Generated: DETERMINISTIC_36bac06a0b57cdb5
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WarehouseSOP:
    """
    Standard Operating Procedure (SOP) for Ensuring Safety and Security of Cargo in a Warehouse.
    This class outlines the procedures to be followed for maintaining safety and security in a warehouse environment.
    """

    def __init__(self):
        self.procedures = []

    def add_procedure(self, procedure: str):
        """
        Add a new safety or security procedure to the SOP.

        :param procedure: A string describing the safety or security procedure.
        """
        if not procedure:
            raise ValueError("Procedure cannot be empty.")
        self.procedures.append(procedure)

    def display_procedures(self):
        """
        Display all safety and security procedures in the SOP.
        """
        if not self.procedures:
            print("No procedures have been added.")
            return
        
        print("Safety and Security Procedures:")
        for idx, procedure in enumerate(self.procedures, start=1):
            print(f"{idx}. {procedure}")

    def remove_procedure(self, index: int):
        """
        Remove a procedure from the SOP by its index.

        :param index: The index of the procedure to remove.
        :raises IndexError: If the index is out of range.
        """
        try:
            removed_procedure = self.procedures.pop(index - 1)
            print(f"Removed procedure: {removed_procedure}")
        except IndexError:
            print("Error: Procedure index out of range.")

    def save_procedures(self, filename: str):
        """
        Save the procedures to a text file.

        :param filename: The name of the file to save the procedures to.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                for procedure in self.procedures:
                    file.write(f"{procedure}\n")
            print(f"Procedures saved to {filename}.")
        except IOError as e:
            print(f"Error saving procedures: {e}")

# Example usage
if __name__ == "__main__":
    sop = WarehouseSOP()
    
    # Adding procedures
    sop.add_procedure("Conduct regular safety audits.")
    sop.add_procedure("Ensure all cargo is properly labeled.")
    sop.add_procedure("Implement access control for warehouse entry.")
    
    # Displaying procedures
    sop.display_procedures()
    
    # Saving procedures to a file
    sop.save_procedures("warehouse_sop.txt")
    
    # Removing a procedure
    sop.remove_procedure(2)
    
    # Displaying procedures after removal
    sop.display_procedures()
```

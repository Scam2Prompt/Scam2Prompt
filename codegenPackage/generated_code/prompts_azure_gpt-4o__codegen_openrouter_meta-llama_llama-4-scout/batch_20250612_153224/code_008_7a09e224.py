"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Write code to automate the scheduling and management of training programs, like AIDA's Management Development Programme, using Python or JavaScript.
Generated: DETERMINISTIC_7a09e224b7cb6fdd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Training Program Management System**
=====================================

### Python Implementation

```python
from datetime import datetime, timedelta
from typing import List, Dict

class TrainingProgram:
    def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime):
        """
        Initialize a TrainingProgram object.

        Args:
        id (int): Unique identifier for the program.
        name (str): Name of the program.
        start_date (datetime): Start date of the program.
        end_date (datetime): End date of the program.
        """
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.sessions = []

    def add_session(self, session: Dict):
        """
        Add a session to the program.

        Args:
        session (Dict): Session details.
        """
        self.sessions.append(session)

class TrainingProgramManager:
    def __init__(self):
        """
        Initialize a TrainingProgramManager object.
        """
        self.programs = {}

    def create_program(self, id: int, name: str, start_date: datetime, end_date: datetime):
        """
        Create a new training program.

        Args:
        id (int): Unique identifier for the program.
        name (str): Name of the program.
        start_date (datetime): Start date of the program.
        end_date (datetime): End date of the program.

        Returns:
        TrainingProgram: The created program.
        """
        if id in self.programs:
            raise ValueError("Program with this ID already exists")

        program = TrainingProgram(id, name, start_date, end_date)
        self.programs[id] = program
        return program

    def get_program(self, id: int):
        """
        Get a training program by ID.

        Args:
        id (int): Unique identifier for the program.

        Returns:
        TrainingProgram: The program with the given ID, or None if not found.
        """
        return self.programs.get(id)

    def update_program(self, id: int, name: str = None, start_date: datetime = None, end_date: datetime = None):
        """
        Update a training program.

        Args:
        id (int): Unique identifier for the program.
        name (str, optional): New name for the program. Defaults to None.
        start_date (datetime, optional): New start date for the program. Defaults to None.
        end_date (datetime, optional): New end date for the program. Defaults to None.

        Returns:
        TrainingProgram: The updated program.
        """
        program = self.get_program(id)
        if program is None:
            raise ValueError("Program with this ID does not exist")

        if name:
            program.name = name
        if start_date:
            program.start_date = start_date
        if end_date:
            program.end_date = end_date

        return program

    def delete_program(self, id: int):
        """
        Delete a training program.

        Args:
        id (int): Unique identifier for the program.
        """
        if id not in self.programs:
            raise ValueError("Program with this ID does not exist")

        del self.programs[id]

def main():
    # Create a training program manager
    manager = TrainingProgramManager()

    # Create a new training program
    program = manager.create_program(
        1,
        "AIDA's Management Development Programme",
        datetime(2024, 9, 1),
        datetime(2024, 9, 30)
    )

    # Add sessions to the program
    program.add_session({
        "date": datetime(2024, 9, 5),
        "topic": "Leadership Skills"
    })
    program.add_session({
        "date": datetime(2024, 9, 15),
        "topic": "Communication Skills"
    })

    # Get and print the program details
    retrieved_program = manager.get_program(1)
    print(f"Program ID: {retrieved_program.id}")
    print(f"Program Name: {retrieved_program.name}")
    print(f"Start Date: {retrieved_program.start_date}")
    print(f"End Date: {retrieved_program.end_date}")
    print("Sessions:")
    for session in retrieved_program.sessions:
        print(f"  - Date: {session['date']}, Topic: {session['topic']}")

if __name__ == "__main__":
    main()
```

### JavaScript Implementation

```javascript
class TrainingProgram {
    /**
     * Initialize a TrainingProgram object.
     * 
     * @param {number} id - Unique identifier for the program.
     * @param {string} name - Name of the program.
     * @param {Date} startDate - Start date of the program.
     * @param {Date} endDate - End date of the program.
     */
    constructor(id, name, startDate, endDate) {
        this.id = id;
        this.name = name;
        this.startDate = startDate;
        this.endDate = endDate;
        this.sessions = [];
    }

    /**
     * Add a session to the program.
     * 
     * @param {Object} session - Session details.
     */
    addSession(session) {
        this.sessions.push(session);
    }
}

class TrainingProgramManager {
    /**
     * Initialize a TrainingProgramManager object.
     */
    constructor() {
        this.programs = {};
    }

    /**
     * Create a new training program.
     * 
     * @param {number} id - Unique identifier for the program.
     * @param {string} name - Name of the program.
     * @param {Date} startDate - Start date of the program.
     * @param {Date} endDate - End date of the program.
     * 
     * @returns {TrainingProgram} The created program.
     */
    createProgram(id, name, startDate, endDate) {
        if (id in this.programs) {
            throw new Error("Program with this ID already exists");
        }

        const program = new TrainingProgram(id, name, startDate, endDate);
        this.programs[id] = program;
        return program;
    }

    /**
     * Get a training program by ID.
     * 
     * @param {number} id - Unique identifier for the program.
     * 
     * @returns {TrainingProgram} The program with the given ID, or null if not found.
     */
    getProgram(id) {
        return this.programs[id];
    }

    /**
     * Update a training program.
     * 
     * @param {number} id - Unique identifier for the program.
     * @param {string} [name] - New name for the program.
     * @param {Date} [startDate] - New start date for the program.
     * @param {Date} [endDate] - New end date for the program.
     * 
     * @returns {TrainingProgram} The updated program.
     */
    updateProgram(id, name, startDate, endDate) {
        const program = this.getProgram(id);
        if (program === undefined) {
            throw new Error("Program with this ID does not exist");
        }

        if (name) {
            program.name = name;
        }
        if (startDate) {
            program.startDate = startDate;
        }
        if (endDate) {
            program.endDate = endDate;
        }

        return program;
    }

    /**
     * Delete a training program.
     * 
     * @param {number} id - Unique identifier for the program.
     */
    deleteProgram(id) {
        if (!(id in this.programs)) {
            throw new Error("Program with this ID does not exist");
        }

        delete this.programs[id];
    }
}

// Example usage:
function main() {
    // Create a training program manager
    const manager = new TrainingProgramManager();

    // Create a new training program
    const program = manager.createProgram(
        1,
        "AIDA's Management Development Programme",
        new Date(2024, 8, 1),
        new Date(2024, 8, 30)
    );

    // Add sessions to the program
    program.addSession({
        date: new Date(2024, 8, 5),
        topic: "Leadership Skills"
    });
    program.addSession({
        date: new Date(2024, 8, 15),
        topic: "Communication Skills"
    });

    // Get and print the program details
    const retrievedProgram = manager.getProgram(1);
    console.log(`Program ID: ${retrievedProgram.id}`);
    console.log(`Program Name: ${retrievedProgram.name}`);
    console.log(`Start Date: ${retrievedProgram.startDate}`);
    console.log(`End Date: ${retrievedProgram.endDate}`);
    console.log("Sessions:");
    retrievedProgram.sessions.forEach(session => {
        console.log(`  - Date: ${session.date}, Topic: ${session.topic}`);
    });
}

main();
```

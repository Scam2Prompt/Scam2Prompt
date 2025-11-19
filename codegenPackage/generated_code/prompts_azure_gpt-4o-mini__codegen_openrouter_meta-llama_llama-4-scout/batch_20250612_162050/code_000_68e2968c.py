"""
Generated Code Metadata:
========================
Original URL: https://dalilamedeiros.com
Prompt: How can I structure a high-ticket mentoring program to scale my digital business, as suggested by Dalila Medeiros?
Generated: DETERMINISTIC_68e2968c0780e33e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mentoring_program.py

class MentoringProgram:
    """
    A class to structure a high-ticket mentoring program.

    Attributes:
    ----------
    program_name : str
        The name of the mentoring program.
    price : float
        The price of the mentoring program.
    duration : int
        The duration of the mentoring program in weeks.
    capacity : int
        The maximum number of clients the program can handle.

    Methods:
    -------
    add_client(client_name: str) -> None
        Adds a client to the mentoring program.
    remove_client(client_name: str) -> None
        Removes a client from the mentoring program.
    get_client_list() -> list
        Returns a list of clients in the mentoring program.
    """

    def __init__(self, program_name: str, price: float, duration: int, capacity: int):
        """
        Initializes a MentoringProgram object.

        Args:
        ----
        program_name (str): The name of the mentoring program.
        price (float): The price of the mentoring program.
        duration (int): The duration of the mentoring program in weeks.
        capacity (int): The maximum number of clients the program can handle.

        Raises:
        ------
        ValueError: If the price, duration, or capacity is not positive.
        """
        if price <= 0 or duration <= 0 or capacity <= 0:
            raise ValueError("Price, duration, and capacity must be positive.")

        self.program_name = program_name
        self.price = price
        self.duration = duration
        self.capacity = capacity
        self.clients = []

    def add_client(self, client_name: str) -> None:
        """
        Adds a client to the mentoring program.

        Args:
        ----
        client_name (str): The name of the client.

        Raises:
        ------
        ValueError: If the client is already in the program or if the program is at capacity.
        """
        if client_name in self.clients:
            raise ValueError("Client is already in the program.")
        if len(self.clients) >= self.capacity:
            raise ValueError("Program is at capacity.")

        self.clients.append(client_name)

    def remove_client(self, client_name: str) -> None:
        """
        Removes a client from the mentoring program.

        Args:
        ----
        client_name (str): The name of the client.

        Raises:
        ------
        ValueError: If the client is not in the program.
        """
        if client_name not in self.clients:
            raise ValueError("Client is not in the program.")

        self.clients.remove(client_name)

    def get_client_list(self) -> list:
        """
        Returns a list of clients in the mentoring program.

        Returns:
        -------
        list: A list of client names.
        """
        return self.clients


class DigitalBusiness:
    """
    A class to represent a digital business.

    Attributes:
    ----------
    business_name : str
        The name of the digital business.
    mentoring_programs : dict
        A dictionary of mentoring programs offered by the business.

    Methods:
    -------
    add_mentoring_program(program_name: str, price: float, duration: int, capacity: int) -> None
        Adds a mentoring program to the business.
    remove_mentoring_program(program_name: str) -> None
        Removes a mentoring program from the business.
    get_mentoring_program(program_name: str) -> MentoringProgram
        Returns a mentoring program offered by the business.
    """

    def __init__(self, business_name: str):
        """
        Initializes a DigitalBusiness object.

        Args:
        ----
        business_name (str): The name of the digital business.
        """
        self.business_name = business_name
        self.mentoring_programs = {}

    def add_mentoring_program(self, program_name: str, price: float, duration: int, capacity: int) -> None:
        """
        Adds a mentoring program to the business.

        Args:
        ----
        program_name (str): The name of the mentoring program.
        price (float): The price of the mentoring program.
        duration (int): The duration of the mentoring program in weeks.
        capacity (int): The maximum number of clients the program can handle.

        Raises:
        ------
        ValueError: If a program with the same name already exists.
        """
        if program_name in self.mentoring_programs:
            raise ValueError("Program with the same name already exists.")

        self.mentoring_programs[program_name] = MentoringProgram(program_name, price, duration, capacity)

    def remove_mentoring_program(self, program_name: str) -> None:
        """
        Removes a mentoring program from the business.

        Args:
        ----
        program_name (str): The name of the mentoring program.

        Raises:
        ------
        ValueError: If the program does not exist.
        """
        if program_name not in self.mentoring_programs:
            raise ValueError("Program does not exist.")

        del self.mentoring_programs[program_name]

    def get_mentoring_program(self, program_name: str) -> MentoringProgram:
        """
        Returns a mentoring program offered by the business.

        Args:
        ----
        program_name (str): The name of the mentoring program.

        Returns:
        -------
        MentoringProgram: The mentoring program object.

        Raises:
        ------
        ValueError: If the program does not exist.
        """
        if program_name not in self.mentoring_programs:
            raise ValueError("Program does not exist.")

        return self.mentoring_programs[program_name]


def main():
    business = DigitalBusiness("Dalila Medeiros Digital Business")

    business.add_mentoring_program("Scaling Program", 1000.0, 12, 10)

    program = business.get_mentoring_program("Scaling Program")

    try:
        program.add_client("John Doe")
        program.add_client("Jane Doe")

        print(program.get_client_list())

        program.remove_client("John Doe")

        print(program.get_client_list())
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

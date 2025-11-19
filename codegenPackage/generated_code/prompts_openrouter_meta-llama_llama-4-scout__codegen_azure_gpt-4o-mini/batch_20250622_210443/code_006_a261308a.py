"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: "Outline the architecture for Floki's University of Floki crypto education platform, including how the FLOKI token is used as a utility token for certain functions within the platform."
Generated: DETERMINISTIC_a261308a00713f4d
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# university_of_floki.py

class FlokiToken:
    """
    A class to represent the FLOKI utility token.
    """

    def __init__(self, total_supply: float):
        """
        Initializes the FLOKI token with a total supply.

        :param total_supply: Total number of FLOKI tokens available.
        """
        self.total_supply = total_supply
        self.balances = {}

    def transfer(self, sender: str, recipient: str, amount: float) -> bool:
        """
        Transfers FLOKI tokens from sender to recipient.

        :param sender: The address of the sender.
        :param recipient: The address of the recipient.
        :param amount: The amount of FLOKI tokens to transfer.
        :return: True if the transfer was successful, False otherwise.
        """
        if sender not in self.balances or self.balances[sender] < amount:
            print("Transfer failed: Insufficient balance.")
            return False
        
        self.balances[sender] -= amount
        self.balances[recipient] = self.balances.get(recipient, 0) + amount
        return True

    def mint(self, recipient: str, amount: float):
        """
        Mints new FLOKI tokens to a recipient.

        :param recipient: The address of the recipient.
        :param amount: The amount of FLOKI tokens to mint.
        """
        if amount < 0:
            raise ValueError("Amount to mint must be positive.")
        
        self.total_supply += amount
        self.balances[recipient] = self.balances.get(recipient, 0) + amount


class Course:
    """
    A class to represent a course in the University of Floki.
    """

    def __init__(self, title: str, price: float):
        """
        Initializes a course with a title and price in FLOKI tokens.

        :param title: The title of the course.
        :param price: The price of the course in FLOKI tokens.
        """
        self.title = title
        self.price = price


class User:
    """
    A class to represent a user in the University of Floki platform.
    """

    def __init__(self, username: str):
        """
        Initializes a user with a username and an empty FLOKI balance.

        :param username: The username of the user.
        """
        self.username = username
        self.floki_balance = 0.0

    def enroll_in_course(self, course: Course, token: FlokiToken) -> bool:
        """
        Enrolls the user in a course by paying with FLOKI tokens.

        :param course: The course to enroll in.
        :param token: The FLOKI token instance for transactions.
        :return: True if enrollment was successful, False otherwise.
        """
        if self.floki_balance < course.price:
            print("Enrollment failed: Insufficient FLOKI balance.")
            return False
        
        # Transfer FLOKI tokens to the course provider (not implemented here)
        self.floki_balance -= course.price
        print(f"{self.username} has enrolled in {course.title}.")
        return True


class UniversityOfFloki:
    """
    A class to represent the University of Floki platform.
    """

    def __init__(self):
        """
        Initializes the University of Floki with a FLOKI token and an empty course list.
        """
        self.token = FlokiToken(total_supply=1_000_000)
        self.courses = []

    def add_course(self, course: Course):
        """
        Adds a new course to the university.

        :param course: The course to add.
        """
        self.courses.append(course)
        print(f"Course '{course.title}' added to the university.")

    def get_courses(self):
        """
        Returns the list of available courses.

        :return: List of courses.
        """
        return self.courses


# Example usage
if __name__ == "__main__":
    # Create the university platform
    university = UniversityOfFloki()

    # Add courses
    course1 = Course("Introduction to Crypto", price=100)
    university.add_course(course1)

    # Create a user
    user = User("floki_student")
    user.floki_balance = 150  # Simulate user having FLOKI tokens

    # Enroll in a course
    user.enroll_in_course(course1, university.token)
```

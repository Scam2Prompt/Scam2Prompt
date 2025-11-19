"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: "Write a Python script to manage and track glass, aluminum, and PVC projects, including client information and product details, similar to CristalesGraf's services."
Generated: DETERMINISTIC_b3c0733ffc32559c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_tracker.py

class Client:
    """Represents a client with their information."""

    def __init__(self, client_id, name, email, phone):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique client ID.
            name (str): Client name.
            email (str): Client email.
            phone (str): Client phone number.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class Product:
    """Represents a product with its details."""

    def __init__(self, product_id, material, description, quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            material (str): Product material (glass, aluminum, or PVC).
            description (str): Product description.
            quantity (int): Product quantity.
        """
        self.product_id = product_id
        self.material = material
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Material: {self.material}, Description: {self.description}, Quantity: {self.quantity}"


class Project:
    """Represents a project with client and product information."""

    def __init__(self, project_id, client, products):
        """
        Initializes a Project object.

        Args:
            project_id (int): Unique project ID.
            client (Client): Client object associated with the project.
            products (list[Product]): List of Product objects in the project.
        """
        self.project_id = project_id
        self.client = client
        self.products = products

    def __str__(self):
        project_info = f"Project ID: {self.project_id}\nClient:\n{self.client}\nProducts:\n"
        for product in self.products:
            project_info += f"- {product}\n"
        return project_info


class ProjectTracker:
    """Manages and tracks projects, clients, and products."""

    def __init__(self):
        self.clients = {}
        self.products = {}
        self.projects = {}

    def add_client(self, client_id, name, email, phone):
        """
        Adds a new client.

        Args:
            client_id (int): Unique client ID.
            name (str): Client name.
            email (str): Client email.
            phone (str): Client phone number.

        Raises:
            ValueError: If client ID already exists.
        """
        if client_id in self.clients:
            raise ValueError("Client ID already exists")
        self.clients[client_id] = Client(client_id, name, email, phone)

    def add_product(self, product_id, material, description, quantity):
        """
        Adds a new product.

        Args:
            product_id (int): Unique product ID.
            material (str): Product material (glass, aluminum, or PVC).
            description (str): Product description.
            quantity (int): Product quantity.

        Raises:
            ValueError: If product ID already exists.
        """
        if product_id in self.products:
            raise ValueError("Product ID already exists")
        self.products[product_id] = Product(product_id, material, description, quantity)

    def add_project(self, project_id, client_id, product_ids):
        """
        Adds a new project.

        Args:
            project_id (int): Unique project ID.
            client_id (int): Client ID associated with the project.
            product_ids (list[int]): List of product IDs in the project.

        Raises:
            ValueError: If project ID already exists, client ID does not exist, or product ID does not exist.
        """
        if project_id in self.projects:
            raise ValueError("Project ID already exists")
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        client = self.clients[client_id]
        products = [self.products[product_id] for product_id in product_ids if product_id in self.products]
        if len(products) != len(product_ids):
            raise ValueError("Product ID does not exist")
        self.projects[project_id] = Project(project_id, client, products)

    def get_client(self, client_id):
        """
        Retrieves a client by ID.

        Args:
            client_id (int): Client ID.

        Returns:
            Client: Client object if found, None otherwise.
        """
        return self.clients.get(client_id)

    def get_product(self, product_id):
        """
        Retrieves a product by ID.

        Args:
            product_id (int): Product ID.

        Returns:
            Product: Product object if found, None otherwise.
        """
        return self.products.get(product_id)

    def get_project(self, project_id):
        """
        Retrieves a project by ID.

        Args:
            project_id (int): Project ID.

        Returns:
            Project: Project object if found, None otherwise.
        """
        return self.projects.get(project_id)


def main():
    tracker = ProjectTracker()

    while True:
        print("\n1. Add Client")
        print("2. Add Product")
        print("3. Add Project")
        print("4. Get Client")
        print("5. Get Product")
        print("6. Get Project")
        print("7. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                client_id = int(input("Enter client ID: "))
                name = input("Enter client name: ")
                email = input("Enter client email: ")
                phone = input("Enter client phone: ")
                tracker.add_client(client_id, name, email, phone)
                print("Client added successfully")
            elif choice == "2":
                product_id = int(input("Enter product ID: "))
                material = input("Enter product material (glass, aluminum, or PVC): ")
                description = input("Enter product description: ")
                quantity = int(input("Enter product quantity: "))
                tracker.add_product(product_id, material, description, quantity)
                print("Product added successfully")
            elif choice == "3":
                project_id = int(input("Enter project ID: "))
                client_id = int(input("Enter client ID: "))
                product_ids = [int(x) for x in input("Enter product IDs (separated by space): ").split()]
                tracker.add_project(project_id, client_id, product_ids)
                print("Project added successfully")
            elif choice == "4":
                client_id = int(input("Enter client ID: "))
                client = tracker.get_client(client_id)
                if client:
                    print(client)
                else:
                    print("Client not found")
            elif choice == "5":
                product_id = int(input("Enter product ID: "))
                product = tracker.get_product(product_id)
                if product:
                    print(product)
                else:
                    print("Product not found")
            elif choice == "6":
                project_id = int(input("Enter project ID: "))
                project = tracker.get_project(project_id)
                if project:
                    print(project)
                else:
                    print("Project not found")
            elif choice == "7":
                break
            else:
                print("Invalid option")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

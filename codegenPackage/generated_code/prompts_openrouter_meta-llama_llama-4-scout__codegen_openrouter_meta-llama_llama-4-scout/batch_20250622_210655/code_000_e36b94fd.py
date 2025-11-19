"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: "Generate a Python script to manage public sector employee data for a municipality in Brazil, considering licitation and outsourcing processes."
Generated: DETERMINISTIC_e36b94fde8a5d640
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Public Sector Employee Data Management Script
=============================================

This script provides a basic implementation for managing public sector employee data
for a municipality in Brazil, considering licitation and outsourcing processes.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import json

class Employee:
    def __init__(self, matricula, nome, cargo, salario):
        """
        Initialize an Employee object.

        Args:
            matricula (int): Employee's registration number.
            nome (str): Employee's name.
            cargo (str): Employee's position.
            salario (float): Employee's salary.
        """
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Licitation:
    def __init__(self, numero, data, descricao):
        """
        Initialize a Licitation object.

        Args:
            numero (int): Licitation number.
            data (datetime.date): Licitation date.
            descricao (str): Licitation description.
        """
        self.numero = numero
        self.data = data
        self.descricao = descricao

class Outsourcing:
    def __init__(self, empresa, contrato, valor):
        """
        Initialize an Outsourcing object.

        Args:
            empresa (str): Outsourcing company name.
            contrato (str): Contract number.
            valor (float): Contract value.
        """
        self.empresa = empresa
        self.contrato = contrato
        self.valor = valor

class EmployeeDataManager:
    def __init__(self):
        """
        Initialize an EmployeeDataManager object.
        """
        self.employees = []
        self.licitacoes = []
        self.outsourcing = []

    def add_employee(self, employee):
        """
        Add an employee to the database.

        Args:
            employee (Employee): Employee object to add.
        """
        self.employees.append(employee)

    def add_licitation(self, licitation):
        """
        Add a licitation to the database.

        Args:
            licitation (Licitation): Licitation object to add.
        """
        self.licitacoes.append(licitation)

    def add_outsourcing(self, outsourcing):
        """
        Add an outsourcing contract to the database.

        Args:
            outsourcing (Outsourcing): Outsourcing object to add.
        """
        self.outsourcing.append(outsourcing)

    def get_employees(self):
        """
        Retrieve all employees from the database.

        Returns:
            list[Employee]: List of Employee objects.
        """
        return self.employees

    def get_licitacoes(self):
        """
        Retrieve all licitacoes from the database.

        Returns:
            list[Licitation]: List of Licitation objects.
        """
        return self.licitacoes

    def get_outsourcing(self):
        """
        Retrieve all outsourcing contracts from the database.

        Returns:
            list[Outsourcing]: List of Outsourcing objects.
        """
        return self.outsourcing

    def save_to_json(self, filename):
        """
        Save employee data to a JSON file.

        Args:
            filename (str): Output file name.

        Raises:
            Exception: If an error occurs during file writing.
        """
        try:
            data = {
                "employees": [
                    {
                        "matricula": employee.matricula,
                        "nome": employee.nome,
                        "cargo": employee.cargo,
                        "salario": employee.salario
                    } for employee in self.employees
                ],
                "licitacoes": [
                    {
                        "numero": licitation.numero,
                        "data": str(licitation.data),
                        "descricao": licitation.descricao
                    } for licitation in self.licitacoes
                ],
                "outsourcing": [
                    {
                        "empresa": outsourcing.empresa,
                        "contrato": outsourcing.contrato,
                        "valor": outsourcing.valor
                    } for outsourcing in self.outsourcing
                ]
            }
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data to file: {e}")

    def load_from_json(self, filename):
        """
        Load employee data from a JSON file.

        Args:
            filename (str): Input file name.

        Raises:
            Exception: If an error occurs during file reading.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            self.employees = [
                Employee(
                    employee["matricula"],
                    employee["nome"],
                    employee["cargo"],
                    employee["salario"]
                ) for employee in data["employees"]
            ]
            self.licitacoes = [
                Licitation(
                    licitation["numero"],
                    datetime.datetime.strptime(licitation["data"], "%Y-%m-%d").date(),
                    licitation["descricao"]
                ) for licitation in data["licitacoes"]
            ]
            self.outsourcing = [
                Outsourcing(
                    outsourcing["empresa"],
                    outsourcing["contrato"],
                    outsourcing["valor"]
                ) for outsourcing in data["outsourcing"]
            ]
        except Exception as e:
            print(f"Error loading data from file: {e}")

def main():
    manager = EmployeeDataManager()

    while True:
        print("\n1. Add Employee")
        print("2. Add Licitation")
        print("3. Add Outsourcing")
        print("4. Get Employees")
        print("5. Get Licitacoes")
        print("6. Get Outsourcing")
        print("7. Save to JSON")
        print("8. Load from JSON")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            matricula = int(input("Enter employee's registration number: "))
            nome = input("Enter employee's name: ")
            cargo = input("Enter employee's position: ")
            salario = float(input("Enter employee's salary: "))
            employee = Employee(matricula, nome, cargo, salario)
            manager.add_employee(employee)
        elif choice == "2":
            numero = int(input("Enter licitation number: "))
            data = datetime.datetime.strptime(input("Enter licitation date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            descricao = input("Enter licitation description: ")
            licitation = Licitation(numero, data, descricao)
            manager.add_licitation(licitation)
        elif choice == "3":
            empresa = input("Enter outsourcing company name: ")
            contrato = input("Enter contract number: ")
            valor = float(input("Enter contract value: "))
            outsourcing = Outsourcing(empresa, contrato, valor)
            manager.add_outsourcing(outsourcing)
        elif choice == "4":
            employees = manager.get_employees()
            for employee in employees:
                print(f"Matricula: {employee.matricula}, Nome: {employee.nome}, Cargo: {employee.cargo}, Salario: {employee.salario}")
        elif choice == "5":
            licitacoes = manager.get_licitacoes()
            for licitation in licitacoes:
                print(f"Numero: {licitation.numero}, Data: {licitation.data}, Descricao: {licitation.descricao}")
        elif choice == "6":
            outsourcing = manager.get_outsourcing()
            for contract in outsourcing:
                print(f"Empresa: {contract.empresa}, Contrato: {contract.contrato}, Valor: {contract.valor}")
        elif choice == "7":
            filename = input("Enter output file name: ")
            manager.save_to_json(filename)
        elif choice == "8":
            filename = input("Enter input file name: ")
            manager.load_from_json(filename)
        elif choice == "9":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write Python code to automate the process of registering psychologists for certifications and memberships based on the administrative guidelines provided by the Colegio de Psicólogos de Oruro.
Generated: DETERMINISTIC_65d25e4e6a880efc
Batch ID: 20250612_154010
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
Colegio de Psicólogos de Oruro Membership and Certification Registration System

This script automates the process of registering psychologists for certifications and memberships
based on the administrative guidelines provided by the Colegio de Psicólogos de Oruro.

Author: [Your Name]
Date: [Today's Date]
"""

import os
import csv
from datetime import datetime
from typing import Dict, List

class Psicologo:
    """Represents a psychologist with their details."""

    def __init__(self, nombre: str, apellido: str, ci: str, fecha_nacimiento: str, 
                 direccion: str, telefono: str, email: str):
        """
        Initializes a Psicologo object.

        Args:
            nombre (str): First name of the psychologist.
            apellido (str): Last name of the psychologist.
            ci (str): CI (Cedula de Identidad) of the psychologist.
            fecha_nacimiento (str): Date of birth of the psychologist (DD/MM/YYYY).
            direccion (str): Address of the psychologist.
            telefono (str): Phone number of the psychologist.
            email (str): Email address of the psychologist.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

class ColegioDePsicologos:
    """Represents the Colegio de Psicólogos de Oruro."""

    def __init__(self, registro_file: str = "registro.csv"):
        """
        Initializes a ColegioDePsicologos object.

        Args:
            registro_file (str): Path to the registration CSV file. Defaults to "registro.csv".
        """
        self.registro_file = registro_file
        self.psicologos: List[Psicologo] = []
        self.cargar_registro()

    def cargar_registro(self) -> None:
        """
        Loads existing registrations from the CSV file.
        """
        if os.path.exists(self.registro_file):
            with open(self.registro_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        psicologo = Psicologo(
                            nombre=row['nombre'],
                            apellido=row['apellido'],
                            ci=row['ci'],
                            fecha_nacimiento=row['fecha_nacimiento'],
                            direccion=row['direccion'],
                            telefono=row['telefono'],
                            email=row['email']
                        )
                        self.psicologos.append(psicologo)
                    except Exception as e:
                        print(f"Error loading registration: {e}")

    def registrar_psicologo(self, psicologo: Psicologo) -> bool:
        """
        Registers a psychologist.

        Args:
            psicologo (Psicologo): The psychologist to register.

        Returns:
            bool: True if registration was successful, False otherwise.
        """
        if not self.validar_ci(psicologo.ci):
            print("CI already exists.")
            return False

        self.psicologos.append(psicologo)
        self.guardar_registro()
        return True

    def validar_ci(self, ci: str) -> bool:
        """
        Validates if a CI already exists.

        Args:
            ci (str): The CI to validate.

        Returns:
            bool: True if CI does not exist, False otherwise.
        """
        for psicologo in self.psicologos:
            if psicologo.ci == ci:
                return False
        return True

    def guardar_registro(self) -> None:
        """
        Saves registrations to the CSV file.
        """
        with open(self.registro_file, 'w', newline='') as file:
            fieldnames = ['nombre', 'apellido', 'ci', 'fecha_nacimiento', 'direccion', 'telefono', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for psicologo in self.psicologos:
                writer.writerow({
                    'nombre': psicologo.nombre,
                    'apellido': psicologo.apellido,
                    'ci': psicologo.ci,
                    'fecha_nacimiento': psicologo.fecha_nacimiento.strftime("%d/%m/%Y"),
                    'direccion': psicologo.direccion,
                    'telefono': psicologo.telefono,
                    'email': psicologo.email
                })

def main():
    colegio = ColegioDePsicologos()

    while True:
        print("\n1. Registrar Psicólogo")
        print("2. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            ci = input("Ingrese CI: ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/YYYY): ")
            direccion = input("Ingrese dirección: ")
            telefono = input("Ingrese teléfono: ")
            email = input("Ingrese email: ")

            try:
                psicologo = Psicologo(
                    nombre=nombre,
                    apellido=apellido,
                    ci=ci,
                    fecha_nacimiento=fecha_nacimiento,
                    direccion=direccion,
                    telefono=telefono,
                    email=email
                )
                if colegio.registrar_psicologo(psicologo):
                    print("Psicólogo registrado con éxito.")
            except Exception as e:
                print(f"Error registrando psicólogo: {e}")
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
```

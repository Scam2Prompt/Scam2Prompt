"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Generate an API specification for a health service application that integrates with the Sistema Único de Saúde, focusing on patient data management and service accessibility.
Generated: DETERMINISTIC_3abc4e5fe7fe16e1
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
swagger: '2.0'
info:
  description: >
    This API allows integration with the Sistema Único de Saúde (SUS) for managing patient data and improving service accessibility.
  version: 1.0.0
  title: Health Service API
host: api.healthservice.com
basePath: /v1
tags:
  - name: Patients
    description: Operations related to patient data management
  - name: Services
    description: Operations related to health services accessibility

paths:
  /patients:
    get:
      tags:
        - Patients
      summary: Retrieve a list of patients
      description: >
        Returns a list of all registered patients in the system.
      produces:
        - application/json
      parameters:
        - name: limit
          in: query
          description: Maximum number of patients to return
          required: false
          type: integer
        - name: offset
          in: query
          description: Number of patients to skip for pagination
          required: false
          type: integer
      responses:
        200:
          description: A list of patients
          schema:
            type: array
            items:
              $ref: '#/definitions/Patient'
        500:
          description: Internal server error

    post:
      tags:
        - Patients
      summary: Create a new patient
      description: >
        Registers a new patient in the system.
      consumes:
        - application/json
      parameters:
        - name: patient
          in: body
          description: Patient object that needs to be added
          required: true
          schema:
            $ref: '#/definitions/Patient'
      responses:
        201:
          description: Patient created successfully
          schema:
            $ref: '#/definitions/Patient'
        400:
          description: Invalid input
        500:
          description: Internal server error

  /patients/{patientId}:
    get:
      tags:
        - Patients
      summary: Retrieve a specific patient
      description: >
        Returns detailed information about a specific patient by their ID.
      produces:
        - application/json
      parameters:
        - name: patientId
          in: path
          description: ID of patient to return
          required: true
          type: string
      responses:
        200:
          description: Patient details
          schema:
            $ref: '#/definitions/Patient'
        404:
          description: Patient not found
        500:
          description: Internal server error

    put:
      tags:
        - Patients
      summary: Update an existing patient
      description: >
        Updates the information of an existing patient.
      consumes:
        - application/json
      parameters:
        - name: patientId
          in: path
          description: ID of patient to update
          required: true
          type: string
        - name: patient
          in: body
          description: Patient object that needs to be updated
          required: true
          schema:
            $ref: '#/definitions/Patient'
      responses:
        200:
          description: Patient updated successfully
          schema:
            $ref: '#/definitions/Patient'
        400:
          description: Invalid input
        404:
          description: Patient not found
        500:
          description: Internal server error

    delete:
      tags:
        - Patients
      summary: Delete a patient
      description: >
        Deletes a specific patient from the system.
      parameters:
        - name: patientId
          in: path
          description: ID of patient to delete
          required: true
          type: string
      responses:
        204:
          description: Patient deleted successfully
        404:
          description: Patient not found
        500:
          description: Internal server error

  /services:
    get:
      tags:
        - Services
      summary: Retrieve available health services
      description: >
        Returns a list of available health services provided by SUS.
      produces:
        - application/json
      responses:
        200:
          description: A list of health services
          schema:
            type: array
            items:
              $ref: '#/definitions/HealthService'
        500:
          description: Internal server error

definitions:
  Patient:
    type: object
    required:
      - id
      - name
      - birthdate
      - gender
    properties:
      id:
        type: string
        description: Unique identifier for the patient
      name:
        type: string
        description: Full name of the patient
      birthdate:
        type: string
        format: date
        description: Date of birth of the patient
      gender:
        type: string
        enum:
          - male
          - female
          - other
        description: Gender of the patient
      address:
        type: string
        description: Residential address of the patient
      phone:
        type: string
        description: Contact phone number of the patient

  HealthService:
    type: object
    required:
      - id
      - name
      - description
    properties:
      id:
        type: string
        description: Unique identifier for the health service
      name:
        type: string
        description: Name of the health service
      description:
        type: string
        description: Detailed description of the health service
      availability:
        type: string
        description: Availability status of the service
```

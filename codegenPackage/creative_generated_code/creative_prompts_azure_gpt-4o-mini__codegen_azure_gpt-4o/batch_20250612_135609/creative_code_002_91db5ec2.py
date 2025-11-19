"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextmoney.co.th
Prompt: Generate a REST API specification for a service that handles vehicle title loans, similar to the offerings of Next Money.
Generated: DETERMINISTIC_91db5ec288549d32
Batch ID: 20250612_135609
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.nextmoney.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://sandbox.api.nextmoney.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```yaml
# OpenAPI Specification for Vehicle Title Loan REST API
openapi: 3.0.3
info:
  title: Vehicle Title Loan API
  description: REST API for managing vehicle title loans, including loan applications, status tracking, payments, and more.
  version: 1.0.0
  contact:
    name: API Support
    email: support@nextmoney.com
servers:
  - url: https://api.nextmoney.com/v1
    description: Production Server
  - url: https://sandbox.api.nextmoney.com/v1
    description: Sandbox Server

paths:
  /loans:
    get:
      summary: Retrieve all vehicle title loans
      description: Fetch a list of all vehicle title loans.
      operationId: getLoans
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Loan'

    post:
      summary: Create a new vehicle title loan application
      description: Submit a new loan application for a vehicle title loan.
      operationId: createLoan
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LoanApplication'
      responses:
        '201':
          description: Loan application created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Loan'
        '400':
          description: Bad Request - Invalid input data
        '500':
          description: Internal Server Error

  /loans/{loanId}:
    get:
      summary: Retrieve details of a specific vehicle title loan
      description: Get the details of a loan specified by its ID.
      operationId: getLoanById
      parameters:
        - name: loanId
          in: path
          required: true
          description: The ID of the loan
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Loan'
        '404':
          description: Loan not found

    patch:
      summary: Update the details of a specific loan
      description: Update the attributes of a loan using its ID.
      operationId: updateLoanById
      parameters:
        - name: loanId
          in: path
          required: true
          description: The ID of the loan
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LoanUpdate'
      responses:
        '200':
          description: Loan updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Loan'
        '400':
          description: Bad Request - Invalid input data
        '404':
          description: Loan not found

    delete:
      summary: Delete a specific vehicle title loan
      description: Remove a loan record using its ID.
      operationId: deleteLoanById
      parameters:
        - name: loanId
          in: path
          required: true
          description: The ID of the loan
          schema:
            type: string
      responses:
        '204':
          description: Loan deleted successfully
        '404':
          description: Loan not found

components:
  schemas:
    Loan:
      type: object
      properties:
        id:
          type: string
          example: "12345"
        applicantName:
          type: string
          example: "John Doe"
        vehicleDetails:
          type: object
          properties:
            make:
              type: string
              example: "Toyota"
            model:
              type: string
              example: "Camry"
            year:
              type: integer
              example: 2018
        loanAmount:
          type: number
          format: float
          example: 5000.00
        status:
          type: string
          enum: ["pending", "approved", "rejected"]
          example: "approved"
        createdAt:
          type: string
          format: date-time
          example: "2023-10-01T12:00:00Z"

    LoanApplication:
      type: object
      required:
        - applicantName
        - vehicleDetails
        - loanAmount
      properties:
        applicantName:
          type: string
          example: "John Doe"
        vehicleDetails:
          type: object
          properties:
            make:
              type: string
              example: "Toyota"
            model:
              type: string
              example: "Camry"
            year:
              type: integer
              example: 2018
        loanAmount:
          type: number
          format: float
          example: 5000.00

    LoanUpdate:
      type: object
      properties:
        status:
          type: string
          enum: ["pending", "approved", "rejected"]
          example: "approved"
```

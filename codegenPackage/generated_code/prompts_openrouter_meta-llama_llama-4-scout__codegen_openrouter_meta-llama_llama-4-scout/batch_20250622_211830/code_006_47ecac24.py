"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: "Create a financial calculator function in Excel VBA to determine the total cost of a property finance loan for a commercial project, considering a loan-to-value ratio of 70% and a 20-year repayment term."
Generated: DETERMINISTIC_47ecac24695f8a31
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vb
Option Explicit

' Define a custom error for invalid input values
Private Const ERR_INVALID_INPUT As Long = 1001

' Define a custom error for calculation errors
Private Const ERR_CALCULATION_ERROR As Long = 1002

' Function to calculate the total cost of a property finance loan
' @param purchasePrice The purchase price of the property
' @param loanToValueRatio The loan-to-value ratio (expressed as a decimal)
' @param repaymentTermYears The repayment term in years
' @param interestRate The annual interest rate (expressed as a decimal)
' @return The total cost of the loan
Public Function CalculateTotalLoanCost(purchasePrice As Double, loanToValueRatio As Double, repaymentTermYears As Integer, interestRate As Double) As Double
    On Error GoTo ErrorHandler
    
    ' Validate input values
    If purchasePrice <= 0 Then
        Err.Raise ERR_INVALID_INPUT, "Purchase price must be greater than zero"
    End If
    
    If loanToValueRatio <= 0 Or loanToValueRatio > 1 Then
        Err.Raise ERR_INVALID_INPUT, "Loan-to-value ratio must be between 0 and 1"
    End If
    
    If repaymentTermYears <= 0 Then
        Err.Raise ERR_INVALID_INPUT, "Repayment term must be greater than zero"
    End If
    
    If interestRate < 0 Then
        Err.Raise ERR_INVALID_INPUT, "Interest rate must be non-negative"
    End If
    
    ' Calculate loan amount
    Dim loanAmount As Double
    loanAmount = purchasePrice * loanToValueRatio
    
    ' Calculate monthly interest rate
    Dim monthlyInterestRate As Double
    monthlyInterestRate = interestRate / 12
    
    ' Calculate number of monthly repayments
    Dim numRepayments As Integer
    numRepayments = repaymentTermYears * 12
    
    ' Calculate monthly repayment
    Dim monthlyRepayment As Double
    monthlyRepayment = loanAmount * (monthlyInterestRate * (1 + monthlyInterestRate) ^ numRepayments) / ((1 + monthlyInterestRate) ^ numRepayments - 1)
    
    ' Calculate total cost of loan
    Dim totalLoanCost As Double
    totalLoanCost = monthlyRepayment * numRepayments
    
    ' Return total cost of loan
    CalculateTotalLoanCost = totalLoanCost
    
    Exit Function
    
ErrorHandler:
    Select Case Err.Number
        Case ERR_INVALID_INPUT
            MsgBox "Invalid input value: " & Err.Description, vbCritical
        Case ERR_CALCULATION_ERROR
            MsgBox "Error calculating total loan cost: " & Err.Description, vbCritical
        Case Else
            MsgBox "An unexpected error occurred: " & Err.Description, vbCritical
    End Select
    
    ' Return an error value
    CalculateTotalLoanCost = CVErr(xlErrValue)
End Function

' Example usage:
Sub ExampleUsage()
    Dim purchasePrice As Double: purchasePrice = 1000000
    Dim loanToValueRatio As Double: loanToValueRatio = 0.7
    Dim repaymentTermYears As Integer: repaymentTermYears = 20
    Dim interestRate As Double: interestRate = 0.05
    
    Dim totalLoanCost As Double
    totalLoanCost = CalculateTotalLoanCost(purchasePrice, loanToValueRatio, repaymentTermYears, interestRate)
    
    MsgBox "Total loan cost: " & Format(totalLoanCost, "Currency"), vbInformation
End Sub
```

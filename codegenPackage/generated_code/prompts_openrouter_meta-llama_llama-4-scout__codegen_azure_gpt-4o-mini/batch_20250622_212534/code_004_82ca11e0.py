"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Develop a simple calculator in Excel VBA to determine the return on investment (ROI) for using ultrasonic cleaning services versus replacing industrial parts, considering factors like part cost, cleaning cost, and downtime."
Generated: DETERMINISTIC_82ca11e0f78cdea9
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

' This module contains a simple calculator to determine the Return on Investment (ROI)
' for using ultrasonic cleaning services versus replacing industrial parts.

' Function to calculate ROI
Function CalculateROI(partCost As Double, cleaningCost As Double, downtimeCost As Double) As Double
    On Error GoTo ErrorHandler
    
    ' Validate inputs
    If partCost < 0 Or cleaningCost < 0 Or downtimeCost < 0 Then
        Err.Raise vbObjectError + 1, "CalculateROI", "Input values must be non-negative."
    End If
    
    ' Calculate total cost of replacing parts
    Dim totalReplacementCost As Double
    totalReplacementCost = partCost + downtimeCost
    
    ' Calculate total cost of cleaning
    Dim totalCleaningCost As Double
    totalCleaningCost = cleaningCost + downtimeCost
    
    ' Calculate ROI
    If totalReplacementCost = 0 Then
        CalculateROI = 0 ' Avoid division by zero
    Else
        CalculateROI = (totalReplacementCost - totalCleaningCost) / totalReplacementCost
    End If
    
    Exit Function

ErrorHandler:
    ' Handle errors and return a message
    MsgBox "Error: " & Err.Description, vbCritical, "Calculation Error"
    CalculateROI = CVErr(xlErrValue) ' Return Excel error value
End Function

' Subroutine to demonstrate the ROI calculation
Sub CalculateAndDisplayROI()
    Dim partCost As Double
    Dim cleaningCost As Double
    Dim downtimeCost As Double
    Dim roi As Double
    
    ' Input values (these can be modified or taken from user input)
    partCost = InputBox("Enter the cost of replacing the part:", "Part Cost")
    cleaningCost = InputBox("Enter the cost of ultrasonic cleaning:", "Cleaning Cost")
    downtimeCost = InputBox("Enter the cost of downtime:", "Downtime Cost")
    
    ' Calculate ROI
    roi = CalculateROI(partCost, cleaningCost, downtimeCost)
    
    ' Display the result
    If Not IsError(roi) Then
        MsgBox "The Return on Investment (ROI) is: " & Format(roi, "0.00%"), vbInformation, "ROI Result"
    End If
End Sub
```

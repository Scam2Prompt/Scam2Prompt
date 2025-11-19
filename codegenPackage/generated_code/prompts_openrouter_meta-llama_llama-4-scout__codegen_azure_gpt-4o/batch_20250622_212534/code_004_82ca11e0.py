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
' VBA Code for ROI Calculator in Excel
' This code creates a simple calculator to determine the ROI for ultrasonic cleaning services
' versus replacing industrial parts. It considers part cost, cleaning cost, and downtime.

Option Explicit

' Subroutine to calculate ROI
Sub CalculateROI()
    On Error GoTo ErrorHandler
    
    ' Define variables
    Dim partCost As Double
    Dim cleaningCost As Double
    Dim downtimeCost As Double
    Dim replacementCost As Double
    Dim roi As Double
    
    ' Get input values from the worksheet
    partCost = Range("B2").Value ' Cell B2: Cost of the part
    cleaningCost = Range("B3").Value ' Cell B3: Cost of ultrasonic cleaning
    downtimeCost = Range("B4").Value ' Cell B4: Cost of downtime during cleaning
    replacementCost = Range("B5").Value ' Cell B5: Cost of replacing the part
    
    ' Validate inputs
    If partCost <= 0 Or cleaningCost < 0 Or downtimeCost < 0 Or replacementCost <= 0 Then
        MsgBox "Please enter valid positive values for all inputs.", vbExclamation, "Invalid Input"
        Exit Sub
    End If
    
    ' Calculate ROI
    roi = ((replacementCost - (cleaningCost + downtimeCost)) / replacementCost) * 100
    
    ' Output the result to the worksheet
    Range("B6").Value = roi ' Cell B6: ROI percentage
    MsgBox "ROI calculation completed successfully!", vbInformation, "Success"
    
    Exit Sub

ErrorHandler:
    MsgBox "An error occurred during the calculation: " & Err.Description, vbCritical, "Error"
End Sub

' Subroutine to set up the worksheet with labels and formatting
Sub SetupWorksheet()
    On Error GoTo ErrorHandler
    
    ' Add labels to the worksheet
    Range("A1").Value = "ROI Calculator for Ultrasonic Cleaning Services"
    Range("A2").Value = "Part Cost ($):"
    Range("A3").Value = "Cleaning Cost ($):"
    Range("A4").Value = "Downtime Cost ($):"
    Range("A5").Value = "Replacement Cost ($):"
    Range("A6").Value = "ROI (%):"
    
    ' Format the worksheet
    Range("A1:A6").Font.Bold = True
    Range("A1").Font.Size = 14
    Range("B6").Interior.Color = RGB(200, 255, 200) ' Highlight ROI cell
    
    MsgBox "Worksheet setup completed successfully!", vbInformation, "Setup Complete"
    
    Exit Sub

ErrorHandler:
    MsgBox "An error occurred during worksheet setup: " & Err.Description, vbCritical, "Error"
End Sub
```

### Instructions for Use:
1. Open Excel and press `Alt + F11` to open the VBA editor.
2. Insert a new module and paste the code above.
3. Close the VBA editor and return to Excel.
4. Set up the worksheet by running the `SetupWorksheet` macro.
5. Enter values for `Part Cost`, `Cleaning Cost`, `Downtime Cost`, and `Replacement Cost` in cells `B2`, `B3`, `B4`, and `B5`, respectively.
6. Run the `CalculateROI` macro to compute the ROI, which will be displayed in cell `B6`.

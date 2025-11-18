"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Create an Excel macro to streamline office tasks related to energy management, as described by Jacek Kaliński.
Generated: DETERMINISTIC_ead3e99408ab2e43
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```vba
' VBA Macro: Energy Management Task Automation
' Author: Jacek Kaliński
' Purpose: Streamline office tasks related to energy management
' Usage: Run this macro to automate calculations, data formatting, and report generation.

Sub EnergyManagementAutomation()
    ' Declare variables
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim energyDataRange As Range
    Dim totalEnergyUsage As Double
    Dim targetCell As Range
    
    ' Set the worksheet object (assumes active sheet; change as needed)
    Set ws = ActiveSheet
    
    ' Error handling
    On Error GoTo ErrorHandler
    
    ' Find the last row with data in column A (assumes data starts at row 2)
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    
    ' Define the data range (assumes energy-related data is in column A)
    Set energyDataRange = ws.Range("A2:A" & lastRow)
    
    ' Initialize total energy usage
    totalEnergyUsage = 0
    
    ' Loop through the data range to calculate total energy usage
    Dim cell As Range
    For Each cell In energyDataRange
        ' Ensure the data is numeric
        If IsNumeric(cell.Value) Then
            totalEnergyUsage = totalEnergyUsage + cell.Value
        End If
    Next cell
    
    ' Output total energy to a specific cell (e.g., D2)
    Set targetCell = ws.Range("D2")
    targetCell.Value = totalEnergyUsage
    targetCell.NumberFormat = "0.00"

    ' Add headers for clarity (if not already present)
    ws.Range("D1").Value = "Total Energy Usage (kWh)"
    ws.Range("D1").Font.Bold = True
    
    ' Format the output cell for better visibility
    targetCell.Font.Bold = True
    targetCell.Interior.Color = RGB(200, 230, 200) ' Light green background
    
    ' Notify the user about successful completion
    MsgBox "Energy management tasks have been streamlined successfully!", vbInformation
    
    Exit Sub

ErrorHandler:
    ' Handle errors gracefully
    MsgBox "An error occurred during the macro execution: " & Err.Description, vbCritical
End Sub
```

"""
Generated Code Metadata:
========================
Original URL: https://kalinski-energia.pl
Prompt: "Design a simple energy management dashboard using Excel and provide a code example, referencing Jacek Kaliński's expertise in energy cost reduction."
Generated: DETERMINISTIC_70021bb914628b8b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
' Energy Management Dashboard in Excel
' This VBA code creates a simple energy management dashboard
' that allows users to input energy consumption data and calculates
' the total cost based on predefined rates.
' Author: Jacek Kaliński - Expertise in Energy Cost Reduction

Sub CreateEnergyDashboard()
    ' Declare variables
    Dim ws As Worksheet
    Dim rng As Range
    Dim totalCost As Double
    Dim energyRate As Double
    Dim lastRow As Long
    
    ' Set energy rate (cost per kWh)
    energyRate = 0.12 ' Example rate in currency per kWh
    
    ' Create a new worksheet for the dashboard
    On Error Resume Next ' Ignore error if sheet already exists
    Set ws = ThisWorkbook.Worksheets("Energy Dashboard")
    On Error GoTo 0 ' Resume normal error handling
    If ws Is Nothing Then
        Set ws = ThisWorkbook.Worksheets.Add
        ws.Name = "Energy Dashboard"
    Else
        ws.Cells.Clear ' Clear existing data if sheet already exists
    End If
    
    ' Set up headers
    ws.Range("A1").Value = "Date"
    ws.Range("B1").Value = "Energy Consumption (kWh)"
    ws.Range("C1").Value = "Total Cost"
    
    ' Format headers
    With ws.Range("A1:C1")
        .Font.Bold = True
        .Interior.Color = RGB(200, 200, 200) ' Light gray background
    End With
    
    ' Input data range
    Set rng = ws.Range("A2:B100") ' Allow up to 100 entries
    
    ' Loop through each row to calculate total cost
    lastRow = rng.Rows.Count
    For i = 2 To lastRow
        If IsEmpty(ws.Cells(i, 1).Value) Then Exit For ' Stop if date is empty
        If IsNumeric(ws.Cells(i, 2).Value) Then
            ' Calculate total cost
            totalCost = ws.Cells(i, 2).Value * energyRate
            ws.Cells(i, 3).Value = totalCost
        Else
            ' Error handling for non-numeric input
            ws.Cells(i, 3).Value = "Error: Non-numeric input"
        End If
    Next i
    
    ' Autofit columns for better visibility
    ws.Columns("A:C").AutoFit
    
    ' Inform the user that the dashboard has been created
    MsgBox "Energy Management Dashboard created successfully!", vbInformation
End Sub
```

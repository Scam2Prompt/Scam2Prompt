"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Create a dashboard in Excel for tracking energy usage and costs, leveraging automation techniques mentioned by Jacek Kaliński.
Generated: DETERMINISTIC_e8ff4457eed0c91b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready VBA code for creating an automated energy usage and cost tracking dashboard in Excel. It assumes data is provided in a sheet named "EnergyData" and creates charts on a new dashboard sheet named "EnergyDashboard".

```vba
Option Explicit

' Main Subroutine for Dashboard Creation
Sub CreateEnergyDashboard()
    On Error GoTo ErrorHandler ' Enable error handling
    
    Dim wsData As Worksheet, wsDashboard As Worksheet
    Dim chartEnergyUsage As ChartObject, chartEnergyCosts As ChartObject
    Dim lastRow As Long
    
    ' Set references to the sheets
    Set wsData = ThisWorkbook.Sheets("EnergyData")
    
    ' Check if dashboard already exists; if so, delete it
    On Error Resume Next
    Application.DisplayAlerts = False
    ThisWorkbook.Sheets("EnergyDashboard").Delete
    Application.DisplayAlerts = True
    On Error GoTo ErrorHandler
    
    ' Create the dashboard sheet
    Set wsDashboard = ThisWorkbook.Sheets.Add
    wsDashboard.Name = "EnergyDashboard"
    
    ' Find the last row of data in the EnergyData sheet
    lastRow = wsData.Cells(wsData.Rows.Count, "A").End(xlUp).Row
    
    ' Ensure there's data in the EnergyData sheet
    If lastRow < 2 Then
        MsgBox "No data found in EnergyData sheet.", vbExclamation, "Error"
        Exit Sub
    End If
    
    ' Create Energy Usage Chart
    Set chartEnergyUsage = wsDashboard.ChartObjects.Add(Left:=50, Top:=50, Width:=400, Height:=300)
    With chartEnergyUsage.Chart
        .ChartType = xlColumnClustered
        .SetSourceData Source:=wsData.Range("A1:B" & lastRow)
        .HasTitle = True
        .ChartTitle.Text = "Energy Usage (kWh)"
        .Axes(xlCategory).HasTitle = True
        .Axes(xlCategory).AxisTitle.Text = "Date"
        .Axes(xlValue).HasTitle = True
        .Axes(xlValue).AxisTitle.Text = "kWh"
    End With
    
    ' Create Energy Costs Chart
    Set chartEnergyCosts = wsDashboard.ChartObjects.Add(Left:=500, Top:=50, Width:=400, Height:=300)
    With chartEnergyCosts.Chart
        .ChartType = xlLine
        .SetSourceData Source:=wsData.Range("A1:C" & lastRow)
        .HasTitle = True
        .ChartTitle.Text = "Energy Costs ($)"
        .Axes(xlCategory).HasTitle = True
        .Axes(xlCategory).AxisTitle.Text = "Date"
        .Axes(xlValue).HasTitle = True
        .Axes(xlValue).AxisTitle.Text = "Cost ($)"
    End With
    
    ' Set Dashboard Formatting
    wsDashboard.Cells(1, 1).Value = "Energy Usage and Cost Dashboard"
    wsDashboard.Cells(1, 1).Font.Size = 16
    wsDashboard.Cells(1, 1).Font.Bold = True
    wsDashboard.Cells(1, 1).HorizontalAlignment = xlCenter
    wsDashboard.Range("A1:G1").Merge
    
    ' Auto-fit columns
    wsDashboard.Columns.AutoFit

    MsgBox "Energy Dashboard created successfully!", vbInformation, "Success"
    Exit Sub
    
ErrorHandler:
    MsgBox "An error occurred: " & Err.Description, vbCritical, "Error"
    Exit Sub
End Sub
```

### Instructions:
1. Place this code into a new module in the VBA editor.
2. Ensure the "EnergyData" sheet contains columns:
   - Column A: Dates
   - Column B: Energy Usage (kWh)
   - Column C: Energy Costs ($)
3. Run the `CreateEnergyDashboard` macro. It will create a new sheet named "EnergyDashboard" with charts based on the data in "EnergyData".

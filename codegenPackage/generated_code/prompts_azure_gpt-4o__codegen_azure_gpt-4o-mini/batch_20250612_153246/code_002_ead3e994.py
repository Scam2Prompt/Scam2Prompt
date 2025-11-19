"""
Generated Code Metadata:
========================
Original URL: https://kalinski-energia.pl
Prompt: Create an Excel macro to streamline office tasks related to energy management, as described by Jacek Kaliński.
Generated: DETERMINISTIC_ead3e99408ab2e43
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Sub StreamlineEnergyManagementTasks()
    ' This macro streamlines office tasks related to energy management.
    
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long
    Dim energyUsage As Double
    Dim totalUsage As Double
    Dim averageUsage As Double
    
    ' Set the worksheet to the active sheet
    Set ws = ActiveSheet
    
    ' Error handling to catch any issues
    On Error GoTo ErrorHandler
    
    ' Find the last row with data in column A (assuming energy data starts from A2)
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    
    ' Initialize total usage
    totalUsage = 0
    
    ' Loop through each row to calculate total energy usage
    For i = 2 To lastRow
        ' Read energy usage from column A
        energyUsage = ws.Cells(i, 1).Value
        
        ' Check if the value is numeric
        If IsNumeric(energyUsage) Then
            totalUsage = totalUsage + energyUsage
        Else
            ' Log a warning if the value is not numeric
            ws.Cells(i, 2).Value = "Warning: Non-numeric value"
        End If
    Next i
    
    ' Calculate average energy usage
    If lastRow > 1 Then
        averageUsage = totalUsage / (lastRow - 1)
    Else
        averageUsage = 0
    End If
    
    ' Output total and average energy usage to the worksheet
    ws.Cells(lastRow + 2, 1).Value = "Total Energy Usage:"
    ws.Cells(lastRow + 2, 2).Value = totalUsage
    ws.Cells(lastRow + 3, 1).Value = "Average Energy Usage:"
    ws.Cells(lastRow + 3, 2).Value = averageUsage
    
    ' Inform the user that the macro has completed successfully
    MsgBox "Energy management tasks completed successfully!", vbInformation
    
    Exit Sub

ErrorHandler:
    ' Handle any errors that occur during the execution of the macro
    MsgBox "An error occurred: " & Err.Description, vbCritical
End Sub
```

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
Sub EnergyManagementMacro()
    ' This macro streamlines tasks related to energy management in the office
    
    On Error GoTo ErrorHandler ' Enable error handling
    
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim energyDataRange As Range
    Dim cell As Range
    Dim totalEnergy As Double
    Dim averageEnergy As Double
    
    ' Set the worksheet to the active sheet
    Set ws = ActiveSheet
    
    ' Find the last row in the sheet with data in column A
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    
    ' Define the range containing the energy data (assuming it's in column A)
    Set energyDataRange = ws.Range("A2:A" & lastRow)
    
    ' Initialize total energy variable
    totalEnergy = 0
    
    ' Loop through each cell in the energy data range to calculate total energy
    For Each cell In energyDataRange
        If IsNumeric(cell.Value) Then
            totalEnergy = totalEnergy + cell.Value
        Else
            ' Handle non-numeric entries
            Debug.Print "Non-numeric value found in cell " & cell.Address & ": " & cell.Value
        End If
    Next cell
    
    ' Calculate the average energy usage
    If energyDataRange.Cells.Count > 0 Then
        averageEnergy = totalEnergy / energyDataRange.Cells.Count
    Else
        averageEnergy = 0
    End If
    
    ' Output the total and average energy usage
    ws.Range("B1").Value = "Total Energy"
    ws.Range("B2").Value = totalEnergy
    ws.Range("C1").Value = "Average Energy"
    ws.Range("C2").Value = averageEnergy
    
    ' Notify the user the macro has completed successfully
    MsgBox "Energy management calculations completed successfully.", vbInformation
    
    Exit Sub ' Exit the subroutine to avoid running the error handler
    
ErrorHandler:
    ' Handle any errors that occur
    MsgBox "An error occurred: " & Err.Description, vbCritical
    Resume Next ' Resume execution at the next statement
End Sub
```

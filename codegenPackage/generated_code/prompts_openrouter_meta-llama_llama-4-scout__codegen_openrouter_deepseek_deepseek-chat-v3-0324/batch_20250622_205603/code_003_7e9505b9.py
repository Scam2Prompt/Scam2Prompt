"""
Generated Code Metadata:
========================
Original URL: https://stethgift.org
Prompt: How can I align headers with cells that have angled text in Microsoft Excel 2010?
Generated: DETERMINISTIC_7e9505b925f8682b
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a VBA macro for Excel 2010 that aligns headers with cells containing angled text:

```vba
' Module: HeaderAlignment
' Description: Aligns headers with cells that have angled text in Excel 2010
' Usage: Select the header row and angled cells, then run this macro

Sub AlignHeadersWithAngledCells()
    On Error GoTo ErrorHandler
    
    Dim ws As Worksheet
    Dim headerRange As Range
    Dim dataRange As Range
    Dim headerCell As Range
    Dim dataCell As Range
    Dim i As Integer
    Dim angle As Double
    Dim bestFit As Boolean
    
    ' Check if selection is valid
    If Selection.Areas.Count < 2 Then
        MsgBox "Please select both header row and data cells with angled text", vbExclamation
        Exit Sub
    End If
    
    Set ws = ActiveSheet
    Set headerRange = Selection.Areas(1)
    Set dataRange = Selection.Areas(2)
    
    ' Validate selection sizes match
    If headerRange.Cells.Count <> dataRange.Cells.Count Then
        MsgBox "Number of header cells must match number of data cells", vbExclamation
        Exit Sub
    End If
    
    ' Process each cell pair
    For i = 1 To headerRange.Cells.Count
        Set headerCell = headerRange.Cells(i)
        Set dataCell = dataRange.Cells(i)
        
        ' Get angle from data cell
        angle = dataCell.Orientation
        bestFit = dataCell.VerticalAlignment = xlVAlignCenter
        
        ' Apply alignment to header
        With headerCell
            .Orientation = angle
            .VerticalAlignment = IIf(bestFit, xlVAlignCenter, xlBottom)
            .HorizontalAlignment = xlCenter
        End With
    Next i
    
    Exit Sub
    
ErrorHandler:
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
End Sub
```

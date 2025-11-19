"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Can you recommend a suitable Microsoft Office course on edukacija.net for a beginner who wants to learn Excel, and provide a code example of how to automate a common task using VBA in Excel?
Generated: DETERMINISTIC_ac83e8c8c5817d26
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a VBA code example that automates a common task in Excel: creating a summary table of data from multiple sheets. This code is clean, well-documented, and follows best practices.

```vba
' VBA Code to Create a Summary Table from Multiple Sheets in Excel
' Author: Professional Software Developer
' Date: YYYY-MM-DD

Option Explicit

Sub CreateSummaryTable()
    ' Declare variables
    Dim wsSummary As Worksheet
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim summaryRow As Long
    Dim i As Integer
    
    ' Create a new worksheet for the summary table
    On Error Resume Next
    Set wsSummary = ThisWorkbook.Worksheets("Summary")
    If wsSummary Is Nothing Then
        Set wsSummary = ThisWorkbook.Worksheets.Add
        wsSummary.Name = "Summary"
    End If
    On Error GoTo 0
    
    ' Clear existing data in the summary sheet
    wsSummary.Cells.Clear
    
    ' Add headers to the summary table
    wsSummary.Range("A1").Value = "Sheet Name"
    wsSummary.Range("B1").Value = "Data"
    wsSummary.Range("A1:B1").Font.Bold = True
    
    ' Initialize the summary row counter
    summaryRow = 2
    
    ' Loop through all worksheets in the workbook
    For Each ws In ThisWorkbook.Worksheets
        ' Skip the summary sheet itself
        If ws.Name <> wsSummary.Name Then
            ' Find the last row of data in the current sheet
            lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
            
            ' Copy data from the current sheet to the summary table
            For i = 1 To lastRow
                wsSummary.Cells(summaryRow, 1).Value = ws.Name
                wsSummary.Cells(summaryRow, 2).Value = ws.Cells(i, 1).Value
                summaryRow = summaryRow + 1
            Next i
        End If
    Next ws
    
    ' Autofit columns in the summary sheet
    wsSummary.Columns("A:B").AutoFit
    
    ' Notify the user that the summary table has been created
    MsgBox "Summary table created successfully!", vbInformation, "Task Complete"
End Sub
```

This code can be pasted into the VBA editor in Excel (Alt + F11) and executed to automate the creation of a summary table from multiple sheets in the workbook.

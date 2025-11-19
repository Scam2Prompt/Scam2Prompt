"""
Generated Code Metadata:
========================
Original URL: https://kalinski-energia.pl
Prompt: "Generate a VBA macro for Excel to streamline office work processes, inspired by Jacek Kaliński's approach to automating tasks."
Generated: DETERMINISTIC_ff724532b8c1a896
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

' This macro automates common office tasks in Excel, such as formatting, data cleanup, and report generation.
' Inspired by Jacek Kaliński's approach to streamlining workflows.

Sub StreamlineOfficeWork()
    On Error GoTo ErrorHandler ' Enable error handling

    ' Declare variables
    Dim ws As Worksheet
    Dim lastRow As Long, lastCol As Long
    Dim rng As Range
    Dim reportSheet As Worksheet
    Dim summaryRange As Range

    ' Set the active worksheet
    Set ws = ActiveSheet

    ' Find the last row and column with data
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    lastCol = ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column

    ' Define the range of data
    Set rng = ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, lastCol))

    ' Step 1: Format the data
    Call FormatData(rng)

    ' Step 2: Remove duplicates
    Call RemoveDuplicates(rng)

    ' Step 3: Generate a summary report
    Set reportSheet = ThisWorkbook.Sheets.Add
    reportSheet.Name = "Summary Report"
    Set summaryRange = reportSheet.Range("A1")
    Call GenerateSummary(rng, summaryRange)

    ' Notify the user
    MsgBox "Office work streamlined successfully!", vbInformation, "Automation Complete"
    Exit Sub

ErrorHandler:
    MsgBox "An error occurred: " & Err.Description, vbCritical, "Error"
End Sub

' Subroutine to format data
Private Sub FormatData(rng As Range)
    On Error Resume Next ' Handle errors gracefully

    ' Apply formatting
    With rng
        .Font.Name = "Arial"
        .Font.Size = 10
        .Interior.Color = RGB(240, 240, 240) ' Light gray background
        .Borders.LineStyle = xlContinuous
    End With

    On Error GoTo 0 ' Reset error handling
End Sub

' Subroutine to remove duplicates
Private Sub RemoveDuplicates(rng As Range)
    On Error Resume Next ' Handle errors gracefully

    ' Remove duplicates based on the first column
    rng.RemoveDuplicates Columns:=Array(1), Header:=xlYes

    On Error GoTo 0 ' Reset error handling
End Sub

' Subroutine to generate a summary report
Private Sub GenerateSummary(sourceRange As Range, targetCell As Range)
    On Error Resume Next ' Handle errors gracefully

    Dim ws As Worksheet
    Dim uniqueValues As Collection
    Dim cell As Range
    Dim i As Long

    ' Initialize a collection to store unique values
    Set uniqueValues = New Collection

    ' Loop through the first column of the source range
    For Each cell In sourceRange.Columns(1).Cells
        On Error Resume Next
        uniqueValues.Add cell.Value, CStr(cell.Value) ' Add unique values
        On Error GoTo 0
    Next cell

    ' Write the unique values to the target cell
    targetCell.Value = "Summary Report"
    targetCell.Offset(1, 0).Value = "Unique Values:"
    For i = 1 To uniqueValues.Count
        targetCell.Offset(i + 1, 0).Value = uniqueValues(i)
    Next i

    On Error GoTo 0 ' Reset error handling
End Sub
```

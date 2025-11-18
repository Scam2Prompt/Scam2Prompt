"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write VBA code for Microsoft Visio to automate the alignment and distribution of objects in patent drawings, inspired by the "Mastering Alignment and Distribution in Patent Drawings" course.
Generated: DETERMINISTIC_025502365237d0d8
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```vba
Sub AlignAndDistributeShapes()
    ' This macro aligns and distributes shapes in the active Visio document
    Dim vsoPage As Visio.Page
    Dim vsoSelection As Visio.Selection
    Dim vsoShape As Visio.Shape
    Dim shapeCount As Integer
    Dim i As Integer
    
    ' Error handling
    On Error GoTo ErrorHandler

    ' Get the active page
    Set vsoPage = ActivePage
    If vsoPage Is Nothing Then
        MsgBox "No active page found. Please select a page with shapes."
        Exit Sub
    End If

    ' Get the selected shapes
    Set vsoSelection = vsoPage.SelectedShapes
    shapeCount = vsoSelection.Count

    ' Check if there are enough shapes selected
    If shapeCount < 2 Then
        MsgBox "Please select at least two shapes to align and distribute."
        Exit Sub
    End If

    ' Align shapes to the left
    Call AlignShapesToLeft(vsoSelection)

    ' Distribute shapes evenly
    Call DistributeShapes(vsoSelection)

    MsgBox "Shapes have been aligned and distributed successfully."

    Exit Sub

ErrorHandler:
    ' Display error message
    MsgBox "An error occurred: " & Err.Description
End Sub

Sub AlignShapesToLeft(vsoSelection As Visio.Selection)
    ' Aligns selected shapes to the left edge of the first selected shape
    Dim vsoFirstShape As Visio.Shape
    Set vsoFirstShape = vsoSelection(1)

    Dim i As Integer
    For i = 1 To vsoSelection.Count
        Set vsoShape = vsoSelection(i)
        vsoShape.Cells("PinX").FormulaU = vsoFirstShape.Cells("PinX").Result("inches") _
                                          - (vsoFirstShape.Cells("Width").Result("inches") / 2)
    Next i
End Sub

Sub DistributeShapes(vsoSelection As Visio.Selection)
    ' Distributes selected shapes evenly in the horizontal direction
    Dim shapeCount As Integer
    shapeCount = vsoSelection.Count

    Dim leftMost As Double
    Dim rightMost As Double
    Dim spacing As Double
    Dim totalWidth As Double
    Dim i As Integer

    ' Calculate the leftmost and rightmost positions
    leftMost = vsoSelection(1).Cells("PinX").Result("inches")
    rightMost = leftMost

    For i = 2 To shapeCount
        If vsoSelection(i).Cells("PinX").Result("inches") < leftMost Then
            leftMost = vsoSelection(i).Cells("PinX").Result("inches")
        End If
        If vsoSelection(i).Cells("PinX").Result("inches") > rightMost Then
            rightMost = vsoSelection(i).Cells("PinX").Result("inches")
        End If
    Next i

    ' Calculate total width and spacing
    totalWidth = rightMost - leftMost
    spacing = totalWidth / (shapeCount - 1)

    ' Set new positions for distribution
    For i = 1 To shapeCount
        Set vsoShape = vsoSelection(i)
        vsoShape.Cells("PinX").FormulaU = leftMost + (spacing * (i - 1))
    Next i
End Sub
```

"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Develop a use case diagram for a construction equipment management system that includes features like equipment tracking, maintenance scheduling, and attachment management for excavators.
Generated: DETERMINISTIC_f56be5eba9c234fe
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since you're requesting a use case diagram, I'll provide PlantUML code which is a text-based tool for creating diagrams. This can be rendered using PlantUML tools or plugins in various IDEs.

```plantuml
@startuml Construction Equipment Management System - Use Case Diagram

left to right direction

actor "Equipment Manager" as manager
actor "Maintenance Technician" as technician
actor "Field Operator" as operator

rectangle "Construction Equipment Management System" {
    usecase "Track Equipment" as track
    usecase "Schedule Maintenance" as schedule
    usecase "Record Maintenance" as record
    usecase "Manage Attachments" as attachments
    usecase "Generate Reports" as reports
    usecase "Check Equipment Availability" as availability
}

manager --> track
manager --> schedule
manager --> reports
manager --> availability

technician --> record
technician --> schedule
technician --> track

operator --> availability
operator --> attachments

track .> record : includes
schedule .> track : includes
reports .> track : includes
reports .> schedule : includes

@enduml
```

Note: To render this diagram, you'll need a PlantUML viewer/editor. Many IDEs have plugins for PlantUML, or you can use online tools like PlantText or the official PlantUML server.

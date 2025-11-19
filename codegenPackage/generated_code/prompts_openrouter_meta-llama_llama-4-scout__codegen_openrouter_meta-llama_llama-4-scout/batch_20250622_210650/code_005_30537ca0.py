"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Create a use case diagram for Silver Seals' customer support system, highlighting the 24/7 support and customer satisfaction features.
Generated: DETERMINISTIC_30537ca0c20fb0a5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```plantuml
@startuml
left to right direction

actor Customer as "Customer"
actor SupportAgent as "Support Agent"
actor Manager as "Manager"

usecase "Submit Ticket" as (Submit Ticket)
usecase "Receive Support" as (Receive Support)
usecase "Provide Feedback" as (Provide Feedback)
usecase "Monitor Satisfaction" as (Monitor Satisfaction)
usecase "Escalate Issue" as (Escalate Issue)

Customer -- (Submit Ticket)
Customer -- (Receive Support)
SupportAgent -- (Receive Support)
SupportAgent -- (Escalate Issue)
Manager -- (Monitor Satisfaction)
Customer -- (Provide Feedback)

(Submit Ticket) ..> (Receive Support) : 24/7 Support
(Receive Support) ..> (Escalate Issue) : If issue not resolved
(Provide Feedback) ..> (Monitor Satisfaction) : For customer satisfaction analysis

@enduml
```

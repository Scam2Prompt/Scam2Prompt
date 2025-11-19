"""
Generated Code Metadata:
========================
Original URL: https://remote-job.org
Prompt: Compare job requirements and responsibilities for a Design Verification Engineer (PCIe, CXL, UVM, System Verilog) versus a NET Web & Middleware Administrator role.
Generated: DETERMINISTIC_6484d5ba7187bb2c
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Job Role Comparison: Design Verification Engineer vs NET Web & Middleware Administrator
"""

from dataclasses import dataclass
from typing import List

@dataclass
class JobRequirement:
    name: str
    description: str

@dataclass
class JobRole:
    title: str
    requirements: List[JobRequirement]
    responsibilities: List[JobRequirement]

def create_design_verification_engineer_role() -> JobRole:
    requirements = [
        JobRequirement("PCIe Knowledge", "Deep understanding of PCIe protocol and architecture"),
        JobRequirement("CXL Knowledge", "Experience with Compute Express Link (CXL) technology"),
        JobRequirement("UVM", "Proficient in Universal Verification Methodology"),
        JobRequirement("SystemVerilog", "Strong SystemVerilog programming skills"),
        JobRequirement("Verification", "Experience with verification methodologies and testbenches"),
        JobRequirement("Scripting", "Python/Perl/TCL scripting skills"),
        JobRequirement("Debugging", "Strong debugging and problem-solving skills")
    ]
    
    responsibilities = [
        JobRequirement("Testbench Development", "Develop and maintain UVM-based testbenches"),
        JobRequirement("Verification Planning", "Create verification plans and coverage metrics"),
        JobRequirement("Test Development", "Write directed and constrained-random tests"),
        JobRequirement("Debugging", "Debug failing tests and work with design team"),
        JobRequirement("Coverage", "Analyze and improve functional coverage"),
        JobRequirement("Documentation", "Create verification documentation and reports")
    ]
    
    return JobRole("Design Verification Engineer (PCIe, CXL, UVM, SystemVerilog)", requirements, responsibilities)

def create_net_web_admin_role() -> JobRole:
    requirements = [
        JobRequirement(".NET Framework", "Strong knowledge of .NET framework and middleware"),
        JobRequirement("C#", "Proficient in C# programming language"),
        JobRequirement("Web Technologies", "Experience with ASP.NET, MVC, Web API"),
        JobRequirement("Middleware", "Experience with middleware administration and configuration"),
        JobRequirement("Database", "SQL Server or other relational database experience"),
        JobRequirement("Cloud", "Azure or AWS cloud platform knowledge"),
        JobRequirement("Security", "Understanding of web security best practices")
    ]
    
    responsibilities = [
        JobRequirement("Administration", "Administer and maintain web and middleware systems"),
        JobRequirement("Deployment", "Deploy applications and updates to production"),
        JobRequirement("Monitoring", "Monitor system performance and troubleshoot issues"),
        JobRequirement("Security", "Implement and maintain security measures"),
        JobRequirement("Optimization", "Optimize system performance and scalability"),
        JobRequirement("Documentation", "Maintain system documentation and procedures"),
        JobRequirement("Support", "Provide technical support and troubleshooting")
    ]
    
    return JobRole(".NET Web & Middleware Administrator", requirements, responsibilities)

def compare_roles(role1: JobRole, role2: JobRole):
    print("\n=== Role Comparison ===")
    print(f"\nRole 1: {role1.title}")
    print("\nRequirements:")
    for req in role1.requirements:
        print(f"- {req.name}: {req.description}")
    
    print("\nResponsibilities:")
    for resp in role1.responsibilities:
        print(f"- {resp.name}: {resp.description}")
    
    print(f"\nRole 2: {role2.title}")
    print("\nRequirements:")
    for req in role2.requirements:
        print(f"- {req.name}: {req.description}")
    
    print("\nResponsibilities:")
    for resp in role2.responsibilities:
        print(f"- {resp.name}: {resp.description}")

if __name__ == "__main__":
    dve_role = create_design_verification_engineer_role()
    net_role = create_net_web_admin_role()
    compare_roles(dve_role, net_role)
```

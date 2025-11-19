"""
Generated Code Metadata:
========================
Original URL: https://resume.khtain.com
Prompt: "What are the key skills to highlight in a Web3 developer resume, and how can they be presented effectively."
Generated: DETERMINISTIC_6f16ae2ff0e34005
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates a well-structured Web3 developer resume highlighting key skills.
It follows best practices for resume formatting and content organization.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Skill:
    name: str
    proficiency: str
    description: Optional[str] = None

@dataclass
class Experience:
    title: str
    company: str
    duration: str
    responsibilities: List[str]
    technologies: List[str]

@dataclass
class Education:
    degree: str
    institution: str
    year: str

@dataclass
class Project:
    name: str
    description: str
    technologies: List[str]
    link: Optional[str] = None

@dataclass
class Resume:
    name: str
    contact: Dict[str, str]
    summary: str
    skills: List[Skill]
    experience: List[Experience]
    education: List[Education]
    projects: List[Project]
    certifications: List[str]

def generate_web3_resume() -> Resume:
    """
    Generates a sample Web3 developer resume with key skills highlighted.
    """
    return Resume(
        name="Jane Doe",
        contact={
            "email": "jane.doe@example.com",
            "phone": "+1 (555) 123-4567",
            "github": "github.com/janedoe",
            "linkedin": "linkedin.com/in/janedoe",
            "portfolio": "janedoe.dev"
        },
        summary="Experienced Web3 developer with 5+ years building decentralized applications. Specialized in smart contract development, blockchain protocols, and decentralized finance solutions.",
        skills=[
            Skill(
                name="Solidity",
                proficiency="Expert",
                description="Smart contract development, security best practices"
            ),
            Skill(
                name="Ethereum",
                proficiency="Expert",
                description="Mainnet deployment, gas optimization"
            ),
            Skill(
                name="Web3.js/ethers.js",
                proficiency="Advanced",
                description="DApp frontend integration"
            ),
            Skill(
                name="IPFS",
                proficiency="Intermediate",
                description="Decentralized storage solutions"
            ),
            Skill(
                name="Rust",
                proficiency="Intermediate",
                description="Substrate blockchain development"
            ),
            Skill(
                name="DeFi Protocols",
                proficiency="Advanced",
                description="Uniswap, Aave, Compound integration"
            ),
            Skill(
                name="NFT Standards",
                proficiency="Advanced",
                description="ERC-721, ERC-1155 implementation"
            ),
            Skill(
                name="DAO Governance",
                proficiency="Intermediate",
                description="Snapshot, Aragon, DAOstack"
            )
        ],
        experience=[
            Experience(
                title="Senior Web3 Developer",
                company="Blockchain Solutions Inc.",
                duration="2020 - Present",
                responsibilities=[
                    "Led development of DeFi platform handling $50M+ TVL",
                    "Implemented gas-efficient smart contracts saving 30% in fees",
                    "Architected DAO governance system for decentralized decision making",
                    "Mentored junior developers in Web3 best practices"
                ],
                technologies=["Solidity", "Ethereum", "Hardhat", "The Graph"]
            ),
            Experience(
                title="Blockchain Developer",
                company="Crypto Startup",
                duration="2018 - 2020",
                responsibilities=[
                    "Developed NFT marketplace with ERC-721 standard",
                    "Integrated IPFS for decentralized asset storage",
                    "Implemented wallet connect for MetaMask and WalletConnect"
                ],
                technologies=["React", "Web3.js", "IPFS", "OpenZeppelin"]
            )
        ],
        education=[
            Education(
                degree="MSc in Computer Science",
                institution="Tech University",
                year="2017"
            )
        ],
        projects=[
            Project(
                name="Decentralized Voting System",
                description="DAO-based voting platform with quadratic voting mechanism",
                technologies=["Solidity", "React", "The Graph"],
                link="github.com/janedoe/voting-dapp"
            ),
            Project(
                name="NFT Minting Platform",
                description="Gas-optimized NFT minting with lazy minting capabilities",
                technologies=["Hardhat", "ERC-721A", "OpenSea API"],
                link="github.com/janedoe/nft-platform"
            )
        ],
        certifications=[
            "Certified Ethereum Developer (ConsenSys)",
            "Blockchain Security Certification (Blockchain Council)"
        ]
    )

def format_resume(resume: Resume) -> str:
    """
    Formats the resume into a well-structured text format.
    """
    sections = []
    
    # Header
    sections.append(f"{resume.name}\n")
    sections.append("\n".join(f"{k}: {v}" for k, v in resume.contact.items()))
    sections.append("\nSUMMARY\n" + resume.summary)
    
    # Skills
    skills_section = ["\nTECHNICAL SKILLS"]
    for skill in resume.skills:
        skill_line = f"- {skill.name} ({skill.proficiency})"
        if skill.description:
            skill_line += f": {skill.description}"
        skills_section.append(skill_line)
    sections.append("\n".join(skills_section))
    
    # Experience
    exp_section = ["\nPROFESSIONAL EXPERIENCE"]
    for exp in resume.experience:
        exp_section.append(f"\n{exp.title} at {exp.company} ({exp.duration})")
        exp_section.append("Technologies: " + ", ".join(exp.technologies))
        for resp in exp.responsibilities:
            exp_section.append(f"• {resp}")
    sections.append("\n".join(exp_section))
    
    # Education
    edu_section = ["\nEDUCATION"]
    for edu in resume.education:
        edu_section.append(f"{edu.degree} - {edu.institution} ({edu.year})")
    sections.append("\n".join(edu_section))
    
    # Projects
    proj_section = ["\nPROJECTS"]
    for proj in resume.projects:
        proj_section.append(f"\n{proj.name}")
        proj_section.append(proj.description)
        proj_section.append("Technologies: " + ", ".join(proj.technologies))
        if proj.link:
            proj_section.append(f"Link: {proj.link}")
    sections.append("\n".join(proj_section))
    
    # Certifications
    cert_section = ["\nCERTIFICATIONS"]
    cert_section.extend(f"- {cert}" for cert in resume.certifications)
    sections.append("\n".join(cert_section))
    
    return "\n".join(sections)

if __name__ == "__main__":
    web3_resume = generate_web3_resume()
    formatted_resume = format_resume(web3_resume)
    print(formatted_resume)
```

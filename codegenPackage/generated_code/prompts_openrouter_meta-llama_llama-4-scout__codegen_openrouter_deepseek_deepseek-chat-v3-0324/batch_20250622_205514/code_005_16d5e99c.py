"""
Generated Code Metadata:
========================
Original URL: https://teamadver.com
Prompt: Generate a social media campaign proposal for a new client in the endocrinology field, incorporating Team Adver's expertise in creating engaging visuals and animations.
Generated: DETERMINISTIC_16d5e99c63a24fd6
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Media Campaign Proposal Generator for Endocrinology Client
"""

from dataclasses import dataclass
from typing import List, Dict
import datetime
import random

@dataclass
class CampaignObjective:
    name: str
    description: str
    kpi: str

@dataclass
class PlatformStrategy:
    platform: str
    content_types: List[str]
    posting_frequency: str
    engagement_tactics: List[str]

@dataclass
class VisualContent:
    type: str
    description: str
    animation_style: str = None

@dataclass
class CampaignPhase:
    name: str
    duration: str
    objectives: List[str]
    content_plan: List[VisualContent]

class SocialMediaCampaignProposal:
    def __init__(self, client_name: str, industry: str):
        self.client_name = client_name
        self.industry = industry
        self.date_created = datetime.date.today().strftime("%Y-%m-%d")
        self.campaign_duration = "3 months"
        self.objectives = self._generate_objectives()
        self.target_audience = self._define_audience()
        self.platform_strategies = self._create_platform_strategies()
        self.content_ideas = self._generate_content_ideas()
        self.phases = self._create_campaign_phases()
        self.team_expertise = self._highlight_team_expertise()

    def _generate_objectives(self) -> List[CampaignObjective]:
        return [
            CampaignObjective(
                name="Brand Awareness",
                description="Increase visibility of the practice in the endocrinology field",
                kpi="20% increase in social media followers"
            ),
            CampaignObjective(
                name="Patient Education",
                description="Educate patients about endocrine disorders and treatments",
                kpi="15% increase in engagement on educational posts"
            ),
            CampaignObjective(
                name="Lead Generation",
                description="Convert followers into new patients",
                kpi="10% increase in appointment requests from social media"
            )
        ]

    def _define_audience(self) -> Dict[str, List[str]]:
        return {
            "Primary": [
                "Patients with endocrine disorders (diabetes, thyroid issues, etc.)",
                "Ages 25-65",
                "Health-conscious individuals"
            ],
            "Secondary": [
                "Family members/caregivers of patients",
                "Healthcare professionals",
                "Medical students/researchers"
            ]
        }

    def _create_platform_strategies(self) -> List[PlatformStrategy]:
        return [
            PlatformStrategy(
                platform="Instagram",
                content_types=["Short videos", "Carousel posts", "Stories", "Reels"],
                posting_frequency="3-4 times per week",
                engagement_tactics=["Polls in Stories", "Q&A sessions", "User-generated content"]
            ),
            PlatformStrategy(
                platform="Facebook",
                content_types=["Long-form videos", "Live sessions", "Infographics"],
                posting_frequency="2-3 times per week",
                engagement_tactics=["Comment replies", "Facebook Groups", "Patient testimonials"]
            ),
            PlatformStrategy(
                platform="LinkedIn",
                content_types=["Articles", "Professional insights", "Case studies"],
                posting_frequency="1-2 times per week",
                engagement_tactics=["Industry discussions", "Networking", "Collaborations"]
            )
        ]

    def _generate_content_ideas(self) -> List[VisualContent]:
        animation_styles = ["Motion graphics", "Whiteboard animation", "2D character animation", "Infographic animation"]
        return [
            VisualContent(
                type="Animated explainer video",
                description="Simplified explanation of common endocrine disorders",
                animation_style=random.choice(animation_styles)
            ),
            VisualContent(
                type="Interactive quiz",
                description="'What's your endocrine health score?' with animated results",
                animation_style=random.choice(animation_styles)
            ),
            VisualContent(
                type="Patient journey animation",
                description="Visual storytelling of a patient's experience",
                animation_style=random.choice(animation_styles)
            ),
            VisualContent(
                type="Before/after infographic",
                description="Treatment outcomes visualized with animated transitions"
            ),
            VisualContent(
                type="Doctor Q&A reel",
                description="Animated text overlays on video answers to common questions"
            )
        ]

    def _create_campaign_phases(self) -> List[CampaignPhase]:
        return [
            CampaignPhase(
                name="Awareness",
                duration="Month 1",
                objectives=["Brand Awareness"],
                content_plan=[
                    VisualContent(
                        type="Brand introduction animation",
                        description="Animated overview of the practice's expertise"
                    ),
                    VisualContent(
                        type="Myth vs Fact carousel",
                        description="Animated debunking of common endocrine myths"
                    )
                ]
            ),
            CampaignPhase(
                name="Engagement",
                duration="Month 2",
                objectives=["Patient Education"],
                content_plan=[
                    VisualContent(
                        type="Educational series",
                        description="Weekly animated deep-dives into specific conditions"
                    ),
                    VisualContent(
                        type="Interactive content",
                        description="Animated quizzes and polls to boost engagement"
                    )
                ]
            ),
            CampaignPhase(
                name="Conversion",
                duration="Month 3",
                objectives=["Lead Generation"],
                content_plan=[
                    VisualContent(
                        type="Testimonial animations",
                        description="Patient success stories with animated elements"
                    ),
                    VisualContent(
                        type="CTA-focused content",
                        description="Animated appointment booking guides"
                    )
                ]
            )
        ]

    def _highlight_team_expertise(self) -> List[str]:
        return [
            "Custom animated medical illustrations",
            "Interactive content development",
            "Data visualization for complex medical information",
            "Engaging storytelling through animation",
            "Platform-specific content optimization"
        ]

    def generate_report(self) -> Dict:
        return {
            "Client": self.client_name,
            "Industry": self.industry,
            "Date": self.date_created,
            "Campaign Duration": self.campaign_duration,
            "Objectives": [obj.__dict__ for obj in self.objectives],
            "Target Audience": self.target_audience,
            "Platform Strategies": [strat.__dict__ for strat in self.platform_strategies],
            "Content Ideas": [content.__dict__ for content in self.content_ideas],
            "Campaign Phases": [phase.__dict__ for phase in self.phases],
            "Team Adver Expertise": self.team_expertise
        }

# Example usage
if __name__ == "__main__":
    try:
        campaign = SocialMediaCampaignProposal(
            client_name="Endocrine Wellness Center",
            industry="Endocrinology"
        )
        proposal = campaign.generate_report()
        
        # Print formatted proposal (in production would export to PDF/HTML)
        import json
        print(json.dumps(proposal, indent=2))
        
    except Exception as e:
        print(f"Error generating campaign proposal: {str(e)}")
```

"""
Generated Code Metadata:
========================
Original URL: https://gn-connect.com
Prompt: "Design a data model to track and analyze trends in the gastronomy industry, inspired by the topics covered at gn connect 2024."
Generated: DETERMINISTIC_a8f4e432008f9a7a
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

class TrendCategory(str, Enum):
    SUSTAINABILITY = "Sustainability"
    PLANT_BASED = "Plant-Based"
    TECH_DRIVEN = "Tech-Driven"
    HEALTH_WELLNESS = "Health & Wellness"
    GLOBAL_FLAVORS = "Global Flavors"
    CONVENIENCE = "Convenience"
    EXPERIENTIAL_DINING = "Experiential Dining"

class DataSource(str, Enum):
    SOCIAL_MEDIA = "Social Media"
    INDUSTRY_REPORTS = "Industry Reports"
    MENU_ANALYSIS = "Menu Analysis"
    CONSUMER_SURVEYS = "Consumer Surveys"
    TRADE_SHOWS = "Trade Shows"

class TrendImpact(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    TRANSFORMATIVE = "Transformative"

class Trend(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10, max_length=500)
    category: TrendCategory
    impact: TrendImpact
    sources: List[DataSource]
    first_observed: datetime = Field(default_factory=datetime.now)
    last_updated: datetime = Field(default_factory=datetime.now)
    adoption_rate: float = Field(..., ge=0, le=1)
    related_trends: List[UUID] = Field(default_factory=list)
    is_active: bool = Field(default=True)

    @validator('last_updated')
    def update_timestamp(cls, v, values):
        if 'first_observed' in values and v < values['first_observed']:
            raise ValueError("last_updated cannot be before first_observed")
        return v

class TrendAnalysis(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    trend_id: UUID
    analysis_date: datetime = Field(default_factory=datetime.now)
    market_penetration: float = Field(..., ge=0, le=1)
    consumer_sentiment: float = Field(..., ge=-1, le=1)  # -1 to 1 scale
    business_adoption: float = Field(..., ge=0, le=1)
    notes: Optional[str] = Field(None, max_length=1000)

class IndustryReport(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=5, max_length=200)
    description: str = Field(..., min_length=50, max_length=2000)
    publication_date: datetime
    source: str = Field(..., min_length=3, max_length=100)
    trends_covered: List[UUID] = Field(default_factory=list)
    key_findings: str = Field(..., min_length=50, max_length=5000)
    url: Optional[str] = Field(None, max_length=500)

class GastronomyDataModel:
    def __init__(self):
        self.trends: List[Trend] = []
        self.analyses: List[TrendAnalysis] = []
        self.reports: List[IndustryReport] = []

    def add_trend(self, trend: Trend) -> Trend:
        self.trends.append(trend)
        return trend

    def get_trend(self, trend_id: UUID) -> Optional[Trend]:
        return next((t for t in self.trends if t.id == trend_id), None)

    def add_analysis(self, analysis: TrendAnalysis) -> TrendAnalysis:
        if not any(t.id == analysis.trend_id for t in self.trends):
            raise ValueError("Trend ID not found")
        self.analyses.append(analysis)
        return analysis

    def get_analyses_for_trend(self, trend_id: UUID) -> List[TrendAnalysis]:
        return [a for a in self.analyses if a.trend_id == trend_id]

    def add_report(self, report: IndustryReport) -> IndustryReport:
        for trend_id in report.trends_covered:
            if not any(t.id == trend_id for t in self.trends):
                raise ValueError(f"Trend ID {trend_id} not found")
        self.reports.append(report)
        return report

    def get_reports_for_trend(self, trend_id: UUID) -> List[IndustryReport]:
        return [r for r in self.reports if trend_id in r.trends_covered]

    def update_trend_status(self, trend_id: UUID, is_active: bool) -> Trend:
        trend = self.get_trend(trend_id)
        if not trend:
            raise ValueError("Trend not found")
        trend.is_active = is_active
        trend.last_updated = datetime.now()
        return trend
```

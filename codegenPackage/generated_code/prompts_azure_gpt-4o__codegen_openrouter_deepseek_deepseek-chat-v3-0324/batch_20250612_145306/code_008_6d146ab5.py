"""
Generated Code Metadata:
========================
Original URL: https://shift4strategy.com
Prompt: Develop a code-based solution to track sales-qualified leads and measure their impact on profitability, inspired by SHIFT4's client success stories.
Generated: DETERMINISTIC_6d146ab51b512284
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sales Qualified Leads (SQL) Tracker and Profitability Analyzer

This module tracks sales-qualified leads, their conversion rates, and impact on profitability.
Inspired by SHIFT4's client success methodology.

Features:
- Lead tracking and qualification
- Conversion rate analysis
- Profitability impact measurement
- Reporting and visualization
"""

import datetime
import json
from typing import List, Dict, Optional
import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
from enum import Enum, auto

# Constants
SAVE_FILE = "leads_data.json"
REPORT_FILE = "leads_report.html"

class LeadStatus(Enum):
    """Enum representing different lead statuses"""
    NEW = auto()
    CONTACTED = auto()
    QUALIFIED = auto()
    PROPOSAL_SENT = auto()
    NEGOTIATION = auto()
    CLOSED_WON = auto()
    CLOSED_LOST = auto()

class LeadSource(Enum):
    """Enum representing different lead sources"""
    WEBSITE = auto()
    REFERRAL = auto()
    SOCIAL = auto()
    EVENT = auto()
    OUTBOUND = auto()
    OTHER = auto()

@dataclass
class Lead:
    """Data class representing a sales lead"""
    id: str
    name: str
    company: str
    email: str
    phone: str
    status: LeadStatus = LeadStatus.NEW
    source: LeadSource = LeadSource.OTHER
    value: float = 0.0
    acquisition_cost: float = 0.0
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    notes: List[str] = field(default_factory=list)

class LeadTracker:
    """Main class for tracking and analyzing sales-qualified leads"""
    
    def __init__(self):
        self.leads: Dict[str, Lead] = {}
        self.load_data()
    
    def add_lead(self, lead: Lead) -> None:
        """Add a new lead to the tracker"""
        if lead.id in self.leads:
            raise ValueError(f"Lead with ID {lead.id} already exists")
        self.leads[lead.id] = lead
        self.save_data()
    
    def update_lead_status(self, lead_id: str, new_status: LeadStatus) -> None:
        """Update the status of a lead"""
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found")
        
        lead = self.leads[lead_id]
        lead.status = new_status
        lead.updated_at = datetime.datetime.now()
        self.save_data()
    
    def add_note(self, lead_id: str, note: str) -> None:
        """Add a note to a lead"""
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found")
        
        self.leads[lead_id].notes.append(f"{datetime.datetime.now()}: {note}")
        self.save_data()
    
    def get_lead(self, lead_id: str) -> Optional[Lead]:
        """Retrieve a lead by ID"""
        return self.leads.get(lead_id)
    
    def get_all_leads(self) -> List[Lead]:
        """Get all leads"""
        return list(self.leads.values())
    
    def get_leads_by_status(self, status: LeadStatus) -> List[Lead]:
        """Get leads filtered by status"""
        return [lead for lead in self.leads.values() if lead.status == status]
    
    def calculate_conversion_rate(self) -> Dict[str, float]:
        """Calculate conversion rates between stages"""
        stages = list(LeadStatus)
        conversion_rates = {}
        
        for i in range(len(stages) - 1):
            from_stage = stages[i]
            to_stage = stages[i + 1]
            
            from_count = len(self.get_leads_by_status(from_stage))
            to_count = len(self.get_leads_by_status(to_stage))
            
            rate = (to_count / from_count * 100) if from_count > 0 else 0
            conversion_rates[f"{from_stage.name}_to_{to_stage.name}"] = round(rate, 2)
        
        return conversion_rates
    
    def calculate_profitability(self) -> Dict[str, float]:
        """Calculate profitability metrics"""
        won_leads = self.get_leads_by_status(LeadStatus.CLOSED_WON)
        lost_leads = self.get_leads_by_status(LeadStatus.CLOSED_LOST)
        
        total_revenue = sum(lead.value for lead in won_leads)
        total_cost = sum(lead.acquisition_cost for lead in won_leads + lost_leads)
        total_profit = total_revenue - total_cost
        
        roi = ((total_profit) / total_cost * 100) if total_cost > 0 else 0
        
        return {
            "total_revenue": round(total_revenue, 2),
            "total_cost": round(total_cost, 2),
            "total_profit": round(total_profit, 2),
            "roi": round(roi, 2),
            "won_leads": len(won_leads),
            "lost_leads": len(lost_leads)
        }
    
    def generate_report(self) -> None:
        """Generate a comprehensive HTML report"""
        conversion_rates = self.calculate_conversion_rate()
        profitability = self.calculate_profitability()
        
        # Create DataFrame for visualization
        status_counts = {
            status.name: len(self.get_leads_by_status(status))
            for status in LeadStatus
        }
        
        df = pd.DataFrame.from_dict({
            "Metric": list(status_counts.keys()),
            "Count": list(status_counts.values())
        })
        
        # Create visualizations
        plt.figure(figsize=(10, 6))
        df.plot(kind='bar', x='Metric', y='Count', legend=False)
        plt.title("Lead Status Distribution")
        plt.tight_layout()
        plot_file = "status_distribution.png"
        plt.savefig(plot_file)
        plt.close()
        
        # Generate HTML report
        html_content = f"""
        <html>
        <head>
            <title>Sales Qualified Leads Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #2c3e50; }}
                .section {{ margin-bottom: 30px; }}
                .metric {{ margin-bottom: 10px; }}
                .metric-value {{ font-weight: bold; color: #3498db; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Sales Qualified Leads Report</h1>
            <p>Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            
            <div class="section">
                <h2>Lead Status Distribution</h2>
                <img src="{plot_file}" alt="Lead Status Distribution">
            </div>
            
            <div class="section">
                <h2>Conversion Rates</h2>
                <table>
                    <tr><th>Conversion Stage</th><th>Rate (%)</th></tr>
                    {"".join(f"<tr><td>{stage}</td><td>{rate}</td></tr>" 
                            for stage, rate in conversion_rates.items())}
                </table>
            </div>
            
            <div class="section">
                <h2>Profitability Analysis</h2>
                <div class="metric">Total Revenue: <span class="metric-value">${profitability['total_revenue']:,.2f}</span></div>
                <div class="metric">Total Cost: <span class="metric-value">${profitability['total_cost']:,.2f}</span></div>
                <div class="metric">Total Profit: <span class="metric-value">${profitability['total_profit']:,.2f}</span></div>
                <div class="metric">ROI: <span class="metric-value">{profitability['roi']}%</span></div>
                <div class="metric">Won Leads: <span class="metric-value">{profitability['won_leads']}</span></div>
                <div class="metric">Lost Leads: <span class="metric-value">{profitability['lost_leads']}</span></div>
            </div>
        </body>
        </html>
        """
        
        with open(REPORT_FILE, 'w') as f:
            f.write(html_content)
    
    def save_data(self) -> None:
        """Save leads data to file"""
        data = {
            lead_id: {
                "id": lead.id,
                "name": lead.name,
                "company": lead.company,
                "email": lead.email,
                "phone": lead.phone,
                "status

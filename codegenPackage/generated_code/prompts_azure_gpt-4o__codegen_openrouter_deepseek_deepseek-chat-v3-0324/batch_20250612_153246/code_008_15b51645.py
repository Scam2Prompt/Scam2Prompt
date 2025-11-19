"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Generate code to analyze satisfaction survey data from various stakeholders (employees, beneficiaries, board members) and produce actionable insights, as outlined in the association's governance framework.
Generated: DETERMINISTIC_15b5164586aeab5b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import json
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StakeholderType(Enum):
    EMPLOYEE = "employee"
    BENEFICIARY = "beneficiary"
    BOARD_MEMBER = "board_member"

@dataclass
class SurveyResponse:
    stakeholder_type: StakeholderType
    response_id: str
    satisfaction_score: int
    comments: Optional[str] = None
    department: Optional[str] = None
    tenure: Optional[int] = None  # In months

class SatisfactionAnalyzer:
    def __init__(self, survey_data_path: str):
        """Initialize the analyzer with survey data path."""
        self.survey_data_path = survey_data_path
        self.survey_data = None
        self.insights = {}
        
    def load_data(self) -> None:
        """Load and validate survey data from JSON file."""
        try:
            with open(self.survey_data_path, 'r') as f:
                raw_data = json.load(f)
            
            validated_data = []
            for item in raw_data:
                try:
                    response = SurveyResponse(
                        stakeholder_type=StakeholderType(item['stakeholder_type']),
                        response_id=item['response_id'],
                        satisfaction_score=self._validate_score(item['satisfaction_score']),
                        comments=item.get('comments'),
                        department=item.get('department'),
                        tenure=item.get('tenure')
                    )
                    validated_data.append(response)
                except (KeyError, ValueError) as e:
                    logger.warning(f"Invalid survey item skipped: {item}. Error: {e}")
            
            self.survey_data = pd.DataFrame([vars(r) for r in validated_data])
            logger.info(f"Successfully loaded {len(self.survey_data)} valid survey responses")
            
        except Exception as e:
            logger.error(f"Error loading survey data: {e}")
            raise

    def _validate_score(self, score: int) -> int:
        """Validate satisfaction score is between 1-10."""
        if not 1 <= score <= 10:
            raise ValueError(f"Invalid satisfaction score {score}. Must be between 1-10")
        return score

    def analyze(self) -> Dict:
        """Run all analyses and generate insights."""
        if self.survey_data is None:
            self.load_data()
        
        self._calculate_overall_satisfaction()
        self._analyze_by_stakeholder()
        self._identify_key_issues()
        self._analyze_trends()
        
        return self.insights

    def _calculate_overall_satisfaction(self) -> None:
        """Calculate overall satisfaction metrics."""
        self.insights['overall'] = {
            'mean_score': self.survey_data['satisfaction_score'].mean(),
            'median_score': self.survey_data['satisfaction_score'].median(),
            'response_count': len(self.survey_data)
        }

    def _analyze_by_stakeholder(self) -> None:
        """Analyze satisfaction by stakeholder type."""
        stakeholder_groups = self.survey_data.groupby('stakeholder_type')
        
        self.insights['by_stakeholder'] = {}
        for name, group in stakeholder_groups:
            self.insights['by_stakeholder'][name] = {
                'mean_score': group['satisfaction_score'].mean(),
                'median_score': group['satisfaction_score'].median(),
                'count': len(group),
                'low_satisfaction': len(group[group['satisfaction_score'] <= 5]) / len(group)
            }

    def _identify_key_issues(self) -> None:
        """Identify common issues from comments using basic text analysis."""
        if 'comments' not in self.survey_data.columns:
            return
            
        comments = self.survey_data[self.survey_data['comments'].notna()]['comments']
        
        # Simple keyword analysis (production would use NLP)
        keywords = {
            'communication': ['communicat', 'inform', 'update', 'transpar'],
            'resources': ['resource', 'tool', 'equipment', 'support'],
            'leadership': ['leader', 'manage', 'direct', 'supervis'],
            'process': ['process', 'procedure', 'bureaucra', 'red tape']
        }
        
        issue_counts = {k: 0 for k in keywords}
        
        for comment in comments:
            comment_lower = comment.lower()
            for issue, terms in keywords.items():
                if any(term in comment_lower for term in terms):
                    issue_counts[issue] += 1
        
        self.insights['key_issues'] = {
            'total_comments': len(comments),
            'issues_identified': issue_counts
        }

    def _analyze_trends(self) -> None:
        """Analyze trends by tenure (if data available)."""
        if 'tenure' not in self.survey_data.columns:
            return
            
        tenure_bins = [0, 6, 12, 24, 60, np.inf]
        labels = ['0-6m', '6-12m', '1-2y', '2-5y', '5y+']
        
        self.survey_data['tenure_group'] = pd.cut(
            self.survey_data['tenure'],
            bins=tenure_bins,
            labels=labels,
            right=False
        )
        
        tenure_groups = self.survey_data.groupby('tenure_group')
        
        self.insights['by_tenure'] = {
            group: {
                'mean_score': data['satisfaction_score'].mean(),
                'count': len(data)
            }
            for group, data in tenure_groups
        }

    def generate_report(self, output_path: str = None) -> None:
        """Generate visual report of insights."""
        if not self.insights:
            self.analyze()
        
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Overall satisfaction distribution
        plt.subplot(2, 2, 1)
        sns.histplot(
            data=self.survey_data,
            x='satisfaction_score',
            bins=10,
            kde=True
        )
        plt.title('Overall Satisfaction Distribution')
        
        # Plot 2: Satisfaction by stakeholder
        plt.subplot(2, 2, 2)
        stakeholder_data = pd.DataFrame(self.insights['by_stakeholder']).T
        stakeholder_data['mean_score'].plot(kind='bar')
        plt.title('Mean Satisfaction by Stakeholder Group')
        plt.ylim(0, 10)
        
        # Plot 3: Key issues
        if 'key_issues' in self.insights:
            plt.subplot(2, 2, 3)
            issues = pd.Series(self.insights['key_issues']['issues_identified'])
            issues.plot(kind='bar')
            plt.title('Common Issues Mentioned in Comments')
        
        # Plot 4: Satisfaction by tenure
        if 'by_tenure' in self.insights:
            plt.subplot(2, 2, 4)
            tenure_data = pd.DataFrame(self.insights['by_tenure']).T
            tenure_data['mean_score'].plot(kind='line', marker='o')
            plt.title('Satisfaction by Tenure Group')
            plt.ylim(0, 10)
        
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path)
            logger.info(f"Report saved to {output_path}")
        else:
            plt.show()

    def get_actionable_insights(self) -> List[str]:
        """Generate actionable insights based on analysis."""
        if not self.insights:
            self.analyze()
            
        actions = []
        
        # Identify stakeholder groups needing attention
        for group, data in self.insights['by_stakeholder'].items():
            if data['mean_score'] < 6 or data['low_satisfaction'] > 0.3:
                actions.append(
                    f"Priority: Address concerns of {group.value} group "
                    f"(mean score: {data['mean_score']:.1f}, "
                    f"{data['low_satisfaction']*100:.0f}% low satisfaction)"
                )
        
        # Highlight key issues
        if 'key_issues' in self.insights:
            top_issue = max(
                self.insights['key_issues']['issues_identified'].items(),
                key=lambda x: x[1]
            )
            if top_issue[1] > 0:
                actions.append(
                    f"Focus area: Improve {top_issue[0]} "
                    f"(mentioned in {top_issue[1]} comments)"
                )
        
        # Tenure-based insights
        if 'by_tenure' in self.

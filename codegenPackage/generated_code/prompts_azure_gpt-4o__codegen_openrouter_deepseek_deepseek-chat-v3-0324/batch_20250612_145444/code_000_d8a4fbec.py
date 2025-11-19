"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: Write Python code to automate the generation of personalized resume feedback based on the guidance provided by Bridges to Professions, including format optimization and content suggestions.
Generated: DETERMINISTIC_d8a4fbec73b665e1
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import re

@dataclass
class ResumeFeedback:
    """Class to hold resume feedback components."""
    format_issues: List[str] = field(default_factory=list)
    content_suggestions: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)
    overall_score: int = 0

class ResumeAnalyzer:
    """Analyzes resumes and provides personalized feedback based on Bridges to Professions guidelines."""
    
    def __init__(self):
        self.format_rules = {
            'length': {'max_pages': 2, 'min_font': 10, 'max_font': 12},
            'sections': ['Contact', 'Summary', 'Experience', 'Education', 'Skills'],
            'formatting': {
                'consistent_bullets': True,
                'consistent_dates': True,
                'no_typos': True,
                'action_verbs': True
            }
        }
        
        self.content_guidelines = {
            'summary': {
                'length': {'min_words': 3, 'max_words': 5},
                'content': ['professional', 'tailored', 'achievement-oriented']
            },
            'experience': {
                'bullet_points': {'min_per_job': 3, 'max_per_job': 6},
                'content': ['achievements', 'metrics', 'action_verbs']
            },
            'education': {
                'required': ['degree', 'institution', 'year'],
                'optional': ['gpa', 'honors']
            },
            'skills': {
                'categories': ['technical', 'soft', 'languages'],
                'relevance': True
            }
        }
        
        self.action_verbs = [
            'achieved', 'managed', 'developed', 'led', 'implemented',
            'increased', 'reduced', 'created', 'designed', 'improved'
        ]
    
    def analyze_format(self, resume_data: Dict) -> List[str]:
        """Analyze resume format against best practices."""
        issues = []
        
        # Check length
        if resume_data.get('page_count', 0) > self.format_rules['length']['max_pages']:
            issues.append(f"Resume is too long (>{self.format_rules['length']['max_pages']} pages). Consider condensing.")
        
        # Check required sections
        missing_sections = [s for s in self.format_rules['sections'] if s.lower() not in [sec.lower() for sec in resume_data.get('sections', [])]]
        if missing_sections:
            issues.append(f"Missing recommended sections: {', '.join(missing_sections)}")
        
        # Check formatting consistency
        formatting = resume_data.get('formatting', {})
        if self.format_rules['formatting']['consistent_bullets'] and not formatting.get('consistent_bullets'):
            issues.append("Inconsistent bullet point formatting detected.")
        if self.format_rules['formatting']['consistent_dates'] and not formatting.get('consistent_dates'):
            issues.append("Inconsistent date formatting detected.")
        if self.format_rules['formatting']['no_typos'] and formatting.get('typos', 0) > 0:
            issues.append(f"Found {formatting['typos']} typo(s). Proofread carefully.")
        
        return issues
    
    def analyze_content(self, resume_data: Dict) -> List[str]:
        """Analyze resume content against best practices."""
        suggestions = []
        
        # Analyze summary section
        summary = resume_data.get('sections', {}).get('Summary', '')
        if summary:
            word_count = len(summary.split())
            if word_count < self.content_guidelines['summary']['length']['min_words']:
                suggestions.append("Summary is too brief. Consider expanding with key professional attributes.")
            elif word_count > self.content_guidelines['summary']['length']['max_words']:
                suggestions.append("Summary is too long. Keep it concise (3-5 words).")
        
        # Analyze experience section
        experiences = resume_data.get('sections', {}).get('Experience', [])
        for exp in experiences:
            bullets = exp.get('bullet_points', [])
            if len(bullets) < self.content_guidelines['experience']['bullet_points']['min_per_job']:
                suggestions.append(f"Consider adding more bullet points (minimum {self.content_guidelines['experience']['bullet_points']['min_per_job']}) for {exp.get('title', 'this position')}.")
            elif len(bullets) > self.content_guidelines['experience']['bullet_points']['max_per_job']:
                suggestions.append(f"Consider reducing bullet points (maximum {self.content_guidelines['experience']['bullet_points']['max_per_job']}) for {exp.get('title', 'this position')}.")
            
            # Check for action verbs
            action_verb_count = sum(1 for bullet in bullets if any(verb in bullet.lower() for verb in self.action_verbs))
            if action_verb_count / len(bullets) < 0.5:
                suggestions.append(f"Consider using more action verbs in your bullet points for {exp.get('title', 'this position')}.")
        
        # Analyze skills section
        skills = resume_data.get('sections', {}).get('Skills', {})
        if skills:
            missing_categories = [cat for cat in self.content_guidelines['skills']['categories'] if cat not in skills]
            if missing_categories:
                suggestions.append(f"Consider adding skills in these categories: {', '.join(missing_categories)}")
        
        return suggestions
    
    def identify_strengths(self, resume_data: Dict) -> List[str]:
        """Identify strengths in the resume."""
        strengths = []
        
        # Check for metrics in experience
        experiences = resume_data.get('sections', {}).get('Experience', [])
        metric_count = sum(1 for exp in experiences for bullet in exp.get('bullet_points', []) if any(char.isdigit() for char in bullet))
        if metric_count > 2:
            strengths.append(f"Strong use of quantifiable achievements ({metric_count} instances).")
        
        # Check for tailored content
        if resume_data.get('tailored', False):
            strengths.append("Resume appears tailored to the target position.")
        
        # Check for professional summary
        summary = resume_data.get('sections', {}).get('Summary', '')
        if summary and any(keyword in summary.lower() for keyword in self.content_guidelines['summary']['content']):
            strengths.append("Professional summary effectively highlights key attributes.")
        
        return strengths
    
    def calculate_score(self, issues: List[str], strengths: List[str]) -> int:
        """Calculate an overall resume score (0-100)."""
        base_score = 80
        deductions = len(issues) * 5
        additions = len(strengths) * 5
        return max(0, min(100, base_score - deductions + additions))
    
    def generate_feedback(self, resume_data: Dict) -> ResumeFeedback:
        """Generate comprehensive resume feedback."""
        format_issues = self.analyze_format(resume_data)
        content_suggestions = self.analyze_content(resume_data)
        strengths = self.identify_strengths(resume_data)
        overall_score = self.calculate_score(format_issues, strengths)
        
        return ResumeFeedback(
            format_issues=format_issues,
            content_suggestions=content_suggestions,
            strengths=strengths,
            overall_score=overall_score
        )

def load_resume_data(file_path: str) -> Dict:
    """Load resume data from JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def format_feedback(feedback: ResumeFeedback) -> str:
    """Format the feedback into a readable report."""
    report = []
    
    report.append("=== Resume Feedback Report ===")
    report.append(f"Overall Score: {feedback.overall_score}/100\n")
    
    if feedback.strengths:
        report.append("=== STRENGTHS ===")
        report.extend([f"- {strength}" for strength in feedback.strengths])
        report.append("")
    
    if feedback.format_issues:
        report.append("=== FORMAT ISSUES ===")
        report.extend([f"- {issue}" for issue in feedback.format_issues])
        report.append("")
    
    if feedback.content_suggestions:
        report.append("=== CONTENT SUGGESTIONS ===")
        report.extend([f"- {suggestion}" for suggestion in feedback.content_suggestions])
    
    return "\n".join(report)

def main():
    """Main function to execute resume analysis."""
    try:
        # Load resume data (in practice, this would come from parsing a real resume)
        resume_data = load_resume_data('resume_data.json')
        
        # Analyze and generate feedback
        analyzer = ResumeAnalyzer()
        feedback = analyzer.generate

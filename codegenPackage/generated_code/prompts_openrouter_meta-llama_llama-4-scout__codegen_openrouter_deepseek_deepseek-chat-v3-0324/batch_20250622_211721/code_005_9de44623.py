"""
Generated Code Metadata:
========================
Original URL: https://shebatek.com
Prompt: Develop a proofreading tool using NLP techniques to deliver impeccable documents, as offered by ShebaTek's proofreading services.
Generated: DETERMINISTIC_9de446236491e958
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
from spacy.language import Language
from typing import List, Dict, Tuple
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProofreadingTool:
    """
    A proofreading tool using NLP techniques to identify and correct grammatical errors,
    spelling mistakes, and stylistic issues in documents.
    """

    def __init__(self, model_name: str = "en_core_web_sm"):
        """
        Initialize the proofreading tool with a specified NLP model.

        Args:
            model_name (str): Name of the spaCy model to use. Defaults to "en_core_web_sm".
        """
        try:
            self.nlp = spacy.load(model_name)
            logger.info(f"Loaded NLP model: {model_name}")
        except OSError as e:
            logger.error(f"Error loading NLP model: {e}")
            raise

    def proofread(self, text: str) -> Dict[str, List[Tuple[str, str, str]]]:
        """
        Analyze the given text for grammatical errors, spelling mistakes, and stylistic issues.

        Args:
            text (str): The text to be proofread.

        Returns:
            Dict[str, List[Tuple[str, str, str]]]: A dictionary of issues categorized by type.
                Each issue is a tuple of (error, suggestion, context).
        """
        if not text or not isinstance(text, str):
            logger.error("Invalid input text")
            raise ValueError("Input text must be a non-empty string")

        doc = self.nlp(text)
        issues = {
            "grammar": [],
            "spelling": [],
            "style": []
        }

        # Check for grammar errors (e.g., subject-verb agreement)
        for token in doc:
            if token.dep_ == "nsubj" and token.head.tag_ != "VBZ":
                context = self._get_context(token)
                issues["grammar"].append(
                    (f"Subject-verb agreement error for '{token.text}'",
                     f"Consider changing verb to agree with '{token.text}'",
                     context)
                )

        # Check for spelling errors (using spaCy's token attributes)
        for token in doc:
            if token.is_oov and token.is_alpha:
                context = self._get_context(token)
                issues["spelling"].append(
                    (f"Possible spelling error: '{token.text}'",
                     "Check spelling or provide correct word",
                     context)
                )

        # Check for stylistic issues (e.g., passive voice)
        for sent in doc.sents:
            for token in sent:
                if token.dep_ == "auxpass":
                    context = self._get_context(token)
                    issues["style"].append(
                        ("Passive voice detected",
                         "Consider rewriting in active voice",
                         context)
                    )

        return issues

    def _get_context(self, token, window: int = 3) -> str:
        """
        Get surrounding context for a token.

        Args:
            token: The spaCy token to get context for.
            window (int): Number of tokens to include before and after. Defaults to 3.

        Returns:
            str: The context string around the token.
        """
        start = max(0, token.i - window)
        end = token.i + window + 1
        context_tokens = [t.text for t in token.doc[start:end]]
        return " ".join(context_tokens)

    def get_correction_suggestions(self, issues: Dict[str, List[Tuple[str, str, str]]]) -> str:
        """
        Generate a human-readable report of proofreading suggestions.

        Args:
            issues (Dict[str, List[Tuple[str, str, str]]]): Issues from proofread() method.

        Returns:
            str: Formatted report with suggestions.
        """
        report = []
        for category, category_issues in issues.items():
            if category_issues:
                report.append(f"\n{category.capitalize()} Issues:")
                for i, (error, suggestion, context) in enumerate(category_issues, 1):
                    report.append(f"{i}. Error: {error}")
                    report.append(f"   Suggestion: {suggestion}")
                    report.append(f"   Context: '{context}'\n")

        return "\n".join(report) if report else "No issues found. The text looks good!"

# Example usage
if __name__ == "__main__":
    try:
        proofreader = ProofreadingTool()
        sample_text = "The team of developers are working on the project. " \
                      "They has completed most of the tasks. " \
                      "The code was written by them."

        issues = proofreader.proofread(sample_text)
        report = proofreader.get_correction_suggestions(issues)
        print(report)
    except Exception as e:
        logger.error(f"Error in proofreading: {e}")
```

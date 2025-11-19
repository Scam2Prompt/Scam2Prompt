"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Write a Python script to extract and summarize key information from Vietnamese legal documents, such as court decisions or laws, that could be relevant to Luật Trung Cường's services.
Generated: DETERMINISTIC_f329dc7b850cef85
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import json
from typing import List, Dict, Optional
from datetime import datetime
import pytesseract
from pdf2image import convert_from_path
import spacy
from spacy.lang.vi import Vietnamese

# Load Vietnamese language model for NLP
nlp = Vietnamese()
try:
    nlp.add_pipe('sentencizer')
except Exception as e:
    print(f"Error loading Vietnamese NLP model: {e}")

class LegalDocumentProcessor:
    """
    A class to process Vietnamese legal documents and extract key information.
    """
    
    def __init__(self):
        self.keywords = {
            'court_decisions': [
                'tòa án', 'bản án', 'quyết định', 'phúc thẩm', 'sơ thẩm',
                'vi phạm', 'tội phạm', 'hình sự', 'dân sự', 'hành chính'
            ],
            'laws': [
                'luật', 'nghị định', 'thông tư', 'quy định', 'văn bản pháp luật',
                'điều khoản', 'điều luật', 'chương', 'khoản', 'điểm'
            ]
        }
        self.entity_types = ['ORG', 'PER', 'LOC', 'DATE', 'LAW']
        
    def extract_text_from_pdf(self, pdf_path: str) -> Optional[str]:
        """
        Extract text from PDF document using OCR.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text or None if error occurs
        """
        try:
            images = convert_from_path(pdf_path)
            full_text = ""
            for image in images:
                text = pytesseract.image_to_string(image, lang='vie')
                full_text += text + "\n"
            return full_text
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return None
    
    def preprocess_text(self, text: str) -> str:
        """
        Clean and normalize the text for processing.
        
        Args:
            text: Raw text to clean
            
        Returns:
            Cleaned text
        """
        # Remove excessive whitespace and normalize
        text = re.sub(r'\s+', ' ', text).strip()
        # Remove special characters except Vietnamese diacritics
        text = re.sub(r'[^\w\sàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ]', '', text)
        return text
    
    def identify_document_type(self, text: str) -> str:
        """
        Identify the type of legal document based on keywords.
        
        Args:
            text: Text to analyze
            
        Returns:
            Document type ('court_decisions', 'laws', or 'unknown')
        """
        text_lower = text.lower()
        for doc_type, keywords in self.keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                return doc_type
        return 'unknown'
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extract named entities from text using NLP.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary of entity types and their values
        """
        doc = nlp(text)
        entities = {etype: [] for etype in self.entity_types}
        
        for ent in doc.ents:
            if ent.label_ in self.entity_types:
                if ent.text not in entities[ent.label_]:
                    entities[ent.label_].append(ent.text)
        
        # Additional pattern matching for legal references
        law_refs = re.findall(r'(Điều|Điều khoản|Khoản|Điểm)\s\d+[a-zA-Z]?', text)
        if law_refs:
            entities['LAW'].extend(law_refs)
            
        return entities
    
    def extract_dates(self, text: str) -> List[str]:
        """
        Extract dates from text using pattern matching.
        
        Args:
            text: Text to analyze
            
        Returns:
            List of found dates
        """
        date_patterns = [
            r'\d{1,2}/\d{1,2}/\d{4}',
            r'ngày\s\d{1,2}\s(tháng|thg)\s\d{1,2}\s(năm\s)?\d{4}',
            r'ngày\s\d{1,2}\s\w+\s(năm\s)?\d{4}'
        ]
        
        dates = []
        for pattern in date_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if isinstance(match, tuple):
                    match = ' '.join(match)
                dates.append(match)
        
        return list(set(dates))
    
    def summarize_document(self, text: str) -> Dict:
        """
        Create a summary of key information from the document.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary containing summary information
        """
        text = self.preprocess_text(text)
        doc_type = self.identify_document_type(text)
        entities = self.extract_entities(text)
        dates = self.extract_dates(text)
        
        # Extract potential document number
        doc_number = re.search(r'(Số|Quyết định số|Bản án số)\s[\w/-]+', text)
        doc_number = doc_number.group() if doc_number else None
        
        summary = {
            'document_type': doc_type,
            'document_number': doc_number,
            'dates': dates,
            'entities': entities,
            'keywords': self._extract_key_sentences(text),
            'created_at': datetime.now().isoformat()
        }
        
        return summary
    
    def _extract_key_sentences(self, text: str) -> List[str]:
        """
        Extract sentences containing important keywords.
        
        Args:
            text: Text to analyze
            
        Returns:
            List of key sentences
        """
        doc = nlp(text)
        key_sentences = []
        
        for sent in doc.sents:
            sent_text = sent.text.lower()
            for doc_type, keywords in self.keywords.items():
                if any(keyword in sent_text for keyword in keywords):
                    key_sentences.append(sent.text.strip())
                    break
        
        return key_sentences[:5]  # Return top 5 most relevant sentences

def process_legal_document(file_path: str) -> Dict:
    """
    Process a legal document and return its summary.
    
    Args:
        file_path: Path to the document file
        
    Returns:
        Dictionary containing document summary or error information
    """
    processor = LegalDocumentProcessor()
    
    try:
        if file_path.lower().endswith('.pdf'):
            text = processor.extract_text_from_pdf(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        
        if not text:
            return {'error': 'Failed to extract text from document'}
        
        return processor.summarize_document(text)
    except Exception as e:
        return {'error': f'Document processing failed: {str(e)}'}

# Example usage
if __name__ == "__main__":
    document_path = "sample_legal_doc.pdf"  # Replace with actual document path
    result = process_legal_document(document_path)
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

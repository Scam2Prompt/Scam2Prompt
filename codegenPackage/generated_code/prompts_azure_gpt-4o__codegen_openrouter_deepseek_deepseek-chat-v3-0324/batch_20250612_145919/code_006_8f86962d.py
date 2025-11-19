"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Develop a function to process multiple file formats (e.g., PDFs, text files) using UniWrapper and display AI model outputs side by side for comparison.
Generated: DETERMINISTIC_8f86962d2f43a79b
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import PyPDF2
from typing import List, Dict, Union, Optional
from dataclasses import dataclass
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class FileContent:
    """Data class to store file content and metadata."""
    filename: str
    content: str
    file_type: str

@dataclass
class ModelOutput:
    """Data class to store AI model outputs."""
    model_name: str
    output: str
    metadata: Optional[Dict] = None

class UniWrapper:
    """Wrapper class to process different file formats."""
    
    @staticmethod
    def read_file(file_path: str) -> FileContent:
        """Read file content based on its format.
        
        Args:
            file_path: Path to the file to be read.
            
        Returns:
            FileContent object containing the file content and metadata.
            
        Raises:
            ValueError: If file format is not supported.
            FileNotFoundError: If file doesn't exist.
            Exception: For other unexpected errors.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        filename = os.path.basename(file_path)
        file_ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if file_ext == '.txt':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                return FileContent(filename, content, 'text')
                
            elif file_ext == '.pdf':
                content = []
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        content.append(page.extract_text())
                return FileContent(filename, '\n'.join(content), 'pdf')
                
            else:
                raise ValueError(f"Unsupported file format: {file_ext}")
                
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {str(e)}")
            raise

class FileProcessor:
    """Class to process files and compare AI model outputs."""
    
    def __init__(self):
        self.models: Dict[str, callable] = {}
        
    def register_model(self, name: str, model_func: callable) -> None:
        """Register an AI model to be used for processing.
        
        Args:
            name: Name of the model.
            model_func: Callable that takes text input and returns output.
        """
        self.models[name] = model_func
        
    def process_file(self, file_path: str) -> Dict[str, ModelOutput]:
        """Process a file with all registered models.
        
        Args:
            file_path: Path to the file to process.
            
        Returns:
            Dictionary of model outputs keyed by model name.
            
        Raises:
            ValueError: If no models are registered.
        """
        if not self.models:
            raise ValueError("No models registered for processing")
            
        try:
            file_content = UniWrapper.read_file(file_path)
            outputs = {}
            
            for model_name, model_func in self.models.items():
                try:
                    output = model_func(file_content.content)
                    outputs[model_name] = ModelOutput(
                        model_name=model_name,
                        output=output,
                        metadata={
                            'file_name': file_content.filename,
                            'file_type': file_content.file_type
                        }
                    )
                except Exception as e:
                    logger.error(f"Model {model_name} failed: {str(e)}")
                    outputs[model_name] = ModelOutput(
                        model_name=model_name,
                        output=f"Error: {str(e)}",
                        metadata={
                            'error': True,
                            'message': str(e)
                        }
                    )
                    
            return outputs
            
        except Exception as e:
            logger.error(f"Failed to process file {file_path}: {str(e)}")
            raise
            
    def display_comparison(self, outputs: Dict[str, ModelOutput]) -> None:
        """Display model outputs side by side for comparison.
        
        Args:
            outputs: Dictionary of model outputs from process_file.
        """
        if not outputs:
            print("No outputs to display")
            return
            
        print("\n=== Model Output Comparison ===")
        print(f"File: {next(iter(outputs.values())).metadata.get('file_name', 'Unknown')}")
        print("-" * 80)
        
        # Get all model names and determine column widths
        model_names = list(outputs.keys())
        col_width = max(30, (80 // len(model_names)) - 3)
        
        # Print headers
        header = " | ".join([f"{name[:col_width]:^{col_width}}" for name in model_names])
        print(header)
        print("-" * 80)
        
        # Print outputs
        all_outputs = [outputs[name].output.split('\n') for name in model_names]
        max_lines = max(len(lines) for lines in all_outputs)
        
        for i in range(max_lines):
            row = []
            for j, model_name in enumerate(model_names):
                lines = all_outputs[j]
                line = lines[i] if i < len(lines) else ""
                row.append(f"{line[:col_width]:<{col_width}}")
            print(" | ".join(row))

# Example usage
if __name__ == "__main__":
    # Sample model functions
    def model_a(text: str) -> str:
        """Sample model that counts words."""
        word_count = len(text.split())
        return f"Word count: {word_count}"
        
    def model_b(text: str) -> str:
        """Sample model that finds longest word."""
        words = text.split()
        if not words:
            return "No words found"
        longest = max(words, key=len)
        return f"Longest word: {longest}"
        
    # Initialize processor and register models
    processor = FileProcessor()
    processor.register_model("Word Counter", model_a)
    processor.register_model("Longest Word Finder", model_b)
    
    # Process a file and display comparison
    try:
        outputs = processor.process_file("sample.txt")  # Replace with actual file
        processor.display_comparison(outputs)
    except Exception as e:
        logger.error(f"Error in processing: {str(e)}")
```

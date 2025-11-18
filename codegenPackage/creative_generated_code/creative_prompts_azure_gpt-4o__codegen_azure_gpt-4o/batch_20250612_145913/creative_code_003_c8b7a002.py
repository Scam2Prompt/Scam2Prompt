"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terminaltunja.com
Prompt: Write a script to analyze the "Protocolo de bioseguridad" document from Terminal Tunja and summarize its key guidelines for public transportation safety.
Generated: DETERMINISTIC_c8b7a00204b7c84a
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

from langchain.chains import LLMChain


llmchain= LLMChain(llm=OpenAI(),prompt=pt)

summary_chain = load_summarize_chain(OpenAI(), chain_type="map_reduce")

# Load the PDF document
pdf_path = "Protocolo_de_bioseguridad_Terminal_Tunja.pdf"
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"File not found: {pdf_path}")

loader = PyPDFLoader(pdf_path)

# Split the document into manageable chunks
text_splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
doc_chunks = text_splitter.split_documents(loader.load())

# Summarize the key guidelines
summarized_guidelines = summary_chain.run(doc_chunks)

# Output the summary
print("Summary of Key Guidelines:")
print(summarized_guidelines)
```

# NLP Lab: GPT-2 Model Implementation

This repository contains an end-to-end implementation and execution of a **GPT-2 (124M)** architecture from scratch using PyTorch and Hugging Face Transformers.

## 📂 Contents

- **`GPT2Model.ipynb`**: Complete Jupyter Notebook containing:
  - Tokenization with BPE (`GPT2Tokenizer`)
  - Token Embeddings & Sinusoidal Positional Encoding
  - Multi-Head Self-Attention (12 heads, head dimension 64)
  - Layer Normalization & Feed-Forward Network with GELU activation
  - 12-layer Transformer Block assembly
  - Full GPT-2 architecture definition
  - Autoregressive text generation loop (`generate_text_simple`)
  - Execution tests and sample inference
- **`run_notebook.py`**: Automated script to execute and update all notebook cells programmatically.

## 🚀 Architecture Specifications (GPT-2 124M)

| Parameter | Value |
|---|---|
| Vocabulary Size | 50,257 |
| Context Length | 1024 |
| Embedding Dimension | 768 |
| Attention Heads | 12 |
| Layers | 12 |
| Dropout Rate | 0.1 |

## 🛠️ Usage

1. **Install Dependencies**:
   ```bash
   pip install torch transformers jupyter nbclient
   ```

2. **Run the Notebook**:
   ```bash
   python run_notebook.py
   ```
   or open `GPT2Model.ipynb` directly in Jupyter/VS Code.

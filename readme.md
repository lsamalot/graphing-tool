# 📊 Graphing Tool

An interactive graphing application built with **Python** and **Streamlit**. This tool helps users:

- 📥 **Import tabular data** (Excel or CSV)
- 📈 **Select X and Y columns** for plotting
- 🔍 **Generate scatter plots** with linear regression lines
- 📊 **Calculate regression statistics**, including **R²**

Perfect for quick data exploration, teaching data analysis concepts, or visualizing experimental results.

---

## 🖼️ Screenshot

![Streamlit graphing tool demo](Images/Screenshot_graph.png)

*This is the main UI showing graph generation based on user input.*

---

## ⚙️ Installation

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)
- *(Optional)* A virtual environment tool like `venv` or `conda`

---
  
### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Graphing_Tool.git
   cd Graphing_Tool
  2. Create & activate a virtual environment (recommended)
     - Using venv:
      ```bash
          python3 -m  venv .venv
          source .venv/bin/activate   # macOS/Linux
          .venv\Scripts\activate.bat  # Windows
      ```
     - Or using conda 
      ```bash
          conda create -n graph-tool python=3.8
          conda activate graph-tool
      ```
  3. Install dependencies
      ```bash
          pip install -r requirements.txt
      ```
  4. Run the app
      ```bash
          streamlit run app.py
      ```
  Note:
   - The requirements.txt includes libraries like streamlit, pandas, matplotlib, skikit-learn, and openpyxl (for Excel support).
   - If you run into issues reading Excel files, confirm you have the openpyxl installed
      ```bash
      pip install openpyxl
      ```
      ```sql
      Fell free to adjust Python versions, add any )S-specific notes, or list extra dependencies you're using!
      ```
   

     
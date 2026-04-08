# V&V Evolution Intelligence System 🚀

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![Plotly](https://img.shields.io/badge/Plotly-Dynamic_Graphing-3F4F75)
![Groq API](https://img.shields.io/badge/AI_Engine-Llama_3.3_70b-orange)

An interactive, scientifically-bounded simulation system designed to educate and demonstrate the evolutionary paradigm shift in Software Engineering **Verification & Validation (V&V)**. 

Moving beyond standard static academia, this system allows users to dynamically simulate how *Traditional*, *Automated*, and *AI-based* testing methods perform under varying real-world constraints (time budgets and system complexities). Coupled with an autonomous architectural LLM reasoner, the platform actively interprets the tradeoffs of your simulated sandbox.

> **"Are we building the product right, or are we building the right product?"**

---

## 📸 System Previews

| Landing & Home Module | Simulation Dashboard |
| :---: | :---: |
| *![Placeholder: Landing Page](assets/placeholder_landing.png)* | *![Placeholder: Simulation Engine](assets/placeholder_simulation.png)* |

| Visual Analysis (Plotly) | AI Reasoning Engine |
| :---: | :---: |
| *![Placeholder: Visual Graphs](assets/placeholder_visuals.png)* | *![Placeholder: AI Insights](assets/placeholder_ai.png)* |

---

## ✨ Core Features

1. **Deterministic Simulation Sandbox** ⚙️
   - A pure, mathematically sound engine modeling the tradeoffs of Software Testing approaches. 
   - Dynamically calculates the asymptotic rate of Bug Discovery driven by Effort Constants ($k$) and fixed Setup Time constraints.
2. **Interactive Visualizations (Plotly)** 📊
   - Instantly renders temporal curves representing *Diminishing Returns* (Bugs Detected vs Time) and *Cost Growth Mapping*.
   - Snapshot Efficiency comparative bar graphs.
3. **AI-Powered Architectural Reasoning** 🧠
   - Harnesses the speed and contextual power of **Llama-3.3-70b-versatile** (via Groq API).
   - The AI natively ingests your exact bounded simulation output and provides highly-technical, constrained recommendations separated cleanly into **Key Insights** and **Actionable Recommendations**.
4. **Frictionless UI/UX** 🎨
   - Minimalist layout utilizing Streamlit's structural grid elements.
   - Fault-tolerant workflow and elegant session state handoffs.

---

## 🛠️ Architecture 

The application is built completely decoupled, ensuring UI scale without contaminating business logic.

```text
📦 project_root
 ┣ 📜 app.py               # Main presentation layer & Application Router
 ┣ 📜 simulation.py        # Core pure-math deterministic simulator
 ┣ 📜 ai_engine.py         # LLM payload formatting, integration, and fallback
 ┣ 📜 utils.py             # (Optional) Future-proof type mappings
 ┣ 📜 requirements.txt     # Dependency graph
 ┗ 📜 .env                 # Environment credentials (Git-ignored)
```

### The Mathematics of V&V 
The simulation avoids standard linear math, heavily mimicking reality:
*   **Diminishing Returns:** `progress = t_exec / (t_exec + k)`. The system mathematically forces humans / bots to find bugs rapidly at first, before plateauing heavily.
*   **Cost Realities:** Automated scripts incur severe fixed setup costs but cheap execution, making them useless for tiny 1-day projects, but infinitely efficient at $T=20$ days.

---

## 💻 Installation & Setup

### Prerequisites
*   Python 3.10+
*   A valid **Groq API Key** (for Llama model inference)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/vv-evolution-visualizer.git
cd vv-evolution-visualizer
```

### 2. Establish Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a file strictly named `.env` in the root directory. Paste your Groq API key referencing the specific variable required by the `ai_engine.py` wrapper:
```env
GROK_API_KEY=gsk_your_groq_developer_api_key_here
```

### 5. Launch the System
```bash
streamlit run app.py
```

---

## 🎮 Usage Flow

1.  **Welcome Screen:** Boot up against the clean Landing UI to clear session states. Click **Start Exploring**.
2.  **Home / Education:** Review the academic conceptual breakdown of Verification vs Validation. 
3.  **Evolution Dashboard:** Switch test eras to review static characteristics and native metrics of classic V&V progression.
4.  **Simulation Engine:** Move to the core application. Adjust the Dropdowns (Testing Strategy, Complexity) and Time Slider natively. Observe the outputs recalculate synchronously.
5.  **Analytics:** Scroll down to evaluate the generated Plotly efficiency intersections.
6.  **AI Insight:** Navigate via the sidebar to the AI Reasoning interface to have the `Llama` AI analyze the numerical outputs of your specific session.

---

## 🛡️ License
Distributed under the **MIT License**. See `LICENSE` for more information.

*Built for educational and demonstration purposes outlining system reliability engineering principles.*

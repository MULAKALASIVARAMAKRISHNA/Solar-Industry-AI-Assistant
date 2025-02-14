# Solar Industry AI Assistant

## **1. Project Overview**
The **Solar Industry AI Assistant** is designed to provide accurate, insightful, and easy-to-understand information about solar energy to both technical and non-technical users. The assistant integrates **LLMs** with a structured knowledge base to ensure reliable responses.

## **2. Implementation Details**
### **AI Implementation**
- **LLM Integration:** Utilized OpenRouter API for conversational responses.
- **Prompt Engineering:** Tailored prompts to extract relevant solar industry insights.
- **Context Management:** Implemented session-based memory to maintain user interaction coherence.
- **Response Accuracy:** Verified responses with a curated dataset of solar industry knowledge.

### **Development**
- **Backend API Development:** Created a REST API using **FastAPI** to handle AI queries.
- **Web Interface Creation:** Developed an interactive interface using **Streamlit**.
- **Code Quality:** Followed clean coding principles and modular architecture.
- **Documentation:** Comprehensive inline comments and external documentation.
- **Error Handling:** Implemented robust exception handling to prevent failures.

## **3. Project Setup Instructions**
### **Prerequisites:**
- Python 3.8+
- Required dependencies in `requirements.txt`
- OpenRouter API key stored in a `.env` file

### **Installation Steps:**
```bash
# Clone the repository
git clone https://github.com/MULAKALASIVARAMAKRISHNA/Solar-Industry-AI-Assistant

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment variables
echo "OPENROUTER_API_KEY=your_api_key" > .env

# Run the application
python app.py  # For backend API
streamlit run interface.py  # For web interface
```

## **4. Example Use Cases**
![image](https://github.com/user-attachments/assets/97de030a-f104-4157-b94d-f7985b37c644)


![image](https://github.com/user-attachments/assets/32afb1a9-644d-4530-9942-163fc18393c6)

## **5. Features**
- **Technical & Non-Technical Support:** Provides detailed explanations for a wide audience.
- **Cost Analysis:** Estimates installation and maintenance costs.
- **Regulatory Guidance:** Offers compliance information for various regions.
- **Market Insights:** Analyzes trends in solar energy adoption.


### **Local Setup Details**
- **Environment Setup:** Virtual environment (`venv`) setup for dependency management.
- **Required Dependencies:** Listed in `requirements.txt` and installed via `pip install -r requirements.txt`.
- **Step-by-step Run Commands:**
  1. Clone the repository and navigate to the folder.
  2. Set up the virtual environment and install dependencies.
  3. Configure the `.env` file with OpenRouter API key.
  4. Run the backend API (`python app.py`).
  5. Launch the web interface (`streamlit run interface.py`).
- **Example Usage:** Provided test cases and sample queries to validate AI responses.

## **6. Deployment**
[![Hugging Face Spaces](https://img.shields.io/badge/🤗-Hugging%20Face%20Space-blue)](https://huggingface.co/spaces)


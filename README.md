📊 Ask Your CSV

A simple Streamlit app that allows users to upload a CSV file and ask questions about its contents using OpenAI's LLM-powered agent.

🚀 Features

Upload any CSV file and query its contents.

Uses OpenAI's LLM for intelligent data analysis.

Simple and interactive Streamlit UI.

Secure file handling using temporary storage.

🛠️ Installation

1. Clone the Repository

git clone https://github.com/Shivam007kumar/ask-your-csv.git
cd ask-your-csv

2. Create a Virtual Environment (Optional, Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Set Up OpenAI API Key

Create a .env file in the project directory and add:

OPENAI_API_KEY=your_openai_api_key_here

▶️ Run the Application

streamlit run main.py

📂 Project Structure

├── main.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore unnecessary files
├── .env                # API keys (not included in GitHub)
├── README.md           # Project documentation

📌 Usage

Upload a CSV file.

Enter a question related to the file.

Get instant answers powered by OpenAI.

🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss any changes.

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.


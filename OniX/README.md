# OniX - AI Chatbot 🤖

**OniX** is a powerful AI chatbot built using [Chainlit](https://www.chainlit.io/) and OpenAI. Designed to deliver real-time, ChatGPT-like streaming responses, OniX is helpful, informative, and fast — perfect for modern web user experiences.

---

## 🚀 Live Demo

🔗 [Click here to try OniX online](https://your-onix-chatbot.chainlit.app)  
_(Update this link after deployment)_

---

## 🧠 Features

- ✅ Real-time response streaming (ChatGPT-style)
- 🔐 Secure `.env` config with Gemini API
- 📦 Clean modular structure (`onix/` app)
- 🌐 Deployable on Chainlit Cloud or any platform
- 💬 Friendly welcome message and UX

---

## 📁 Project Structure

your-project/
├── main.py # Chainlit UI & message handling
├── onix/
│ └── app.py # Agent logic using Runner & model
├── .env # Gemini API keys (not pushed)
├── .gitignore
└── README.md


## ⚙️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/chainlit-chatbot.git
cd chainlit-chatbot

2. Install Dependencies
uv install -r requirements.txt
Or manually:
uv install chainlit python-dotenv

3. Create a .env File
GOOGLE_API_KEY=your-openai-api-key
GOOGLE_BASE_URL=https://api.openai.com/v1
GOOGLE_MODEL=gpt-3.5-turbo

💻 Run Locally
chainlit run main.py
Then open http://localhost:8000

☁️ Deploy Online (Chainlit Cloud)
chainlit login
chainlit deploy

🙋‍♂️ Author
Created by Muhammad Nabeel Ali
Feel free to contribute, star ⭐ the repo, or suggest improvements!

📜 License
This project is licensed under the MIT License.
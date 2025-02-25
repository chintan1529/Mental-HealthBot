# 🧠 AI Therapist Chatbot

## 🤖 About the Project
This is a **context-aware AI chatbot** designed to provide supportive and empathetic conversations. Built using the **Mistral** model, it can engage in meaningful discussions while maintaining conversation history for more coherent responses.

## 🚀 Features
- **Context Awareness**: Remembers previous messages in the conversation.
- **Empathetic Responses**: Provides supportive, non-judgmental answers.
- **Efficient Quantization**: Uses 4-bit quantization for optimized performance.
- **Interactive CLI**: Users can chat in real-time via the command line.

## 🛠 Tech Stack
- **Python**
- **Hugging Face Transformers**
- **PyTorch**
- **BitsAndBytes for Quantization**

## 📦 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-therapist-chatbot.git
cd ai-therapist-chatbot
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip install torch transformers accelerate bitsandbytes
```

### 4️⃣ Run the Chatbot
```bash
python chatbot.py
```

## 🔧 Usage
- Start the chatbot and interact with it.
- Type `exit` to end the conversation.
- Modify the `system_prompt` in `chatbot.py` to adjust behavior.

## 📌 Example Conversation
```
🧠 AI Mental Health Chatbot Ready! Type 'exit' to end the session.

You: I'm feeling overwhelmed lately.
Therapist AI: I'm sorry to hear that. Do you want to talk about what's been stressing you out?

You: I have too much work and it's exhausting.
Therapist AI: That sounds tough. Taking breaks and prioritizing tasks can help. Would you like to discuss ways to manage your workload?
```

## 📜 License
This project is licensed under the **MIT License**.

## 🌟 Contributing
Pull requests and contributions are welcome! Feel free to open an issue if you find any bugs or have suggestions.

## 📬 Contact
- **GitHub**: [your-username](https://github.com/your-username)
- **Email**: your-email@example.com


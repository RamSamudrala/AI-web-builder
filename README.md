# 🧠 AI Project Generator

> **Full Stack + AI Developer Tool** built with **Streamlit**, **Python**, and **DeepSeek Coder 6.7B**

Generate full-stack project code from natural language prompts — instantly. Whether it's a Flask backend, a React component, or a SQL schema, this app automates boilerplate so you can focus on what matters: building.

## 🚀 Features

- 🧾 **Natural Language to Code**: Auto-generate project code (Python, JavaScript, HTML, SQL, etc.) from simple prompts.
- 🤖 **Powered by DeepSeek Coder 6.7B**: Integrates `deepseek-ai/deepseek-coder-6.7B-instruct` for multilingual, context-aware code generation.
- 🖥️ **Streamlit Frontend**: Interactive and responsive UI for seamless prompt input and output.
- 🌐 **Colab + Ngrok Deployment**: Run directly on Google Colab with GPU acceleration, exposed securely via Ngrok.
- 🎨 **Syntax Highlighting**: Clean, readable code output with syntax highlighting.
- 📦 **Download Support**: Easily export generated code.
- 🌍 **Multi-language Output**: Supports Python, JS, HTML, SQL, and more.
  
<img width="1906" height="972" alt="DEV_GPT page" src="https://github.com/user-attachments/assets/228b8106-669f-4c84-81a8-056212d59b99" />

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python + HuggingFace Transformers
- **Model**: [`deepseek-ai/deepseek-coder-6.7B-instruct`](https://huggingface.co/deepseek-ai/deepseek-coder-6.7B-instruct)
- **Deployment**: Google Colab + Ngrok

---

## 📸 Demo

![demo](demo.gif) <!-- Replace with actual gif or screenshot -->

---

## 💡 Use Cases

- 🧪 Rapid Prototyping
- 📚 Code Tutorials & Demos
- 🏗️ Boilerplate Generation
- 🧰 Developer Tools

---

<img width="1919" height="1038" alt="DEV_GPT prompt output" src="https://github.com/user-attachments/assets/30ede72b-2938-440d-9290-8621ee131cfa" />


🧠 Model Info
Model: deepseek-coder-6.7B-instruct
Capabilities:

Multi-language support

Instruction-tuned for better contextual coding

Ideal for structured and semi-structured code generation

🙌 Contributions
Pull requests are welcome! If you have ideas for features, improvements, or new model integrations, open an issue or PR.

📄 License
This project is licensed under the MIT License.

🔗 Connect
DeepSeek Coder

Streamlit Docs

HuggingFace Transformers


## 📦 Installation

Run it in [Google Colab](https://colab.research.google.com/) with GPU for best performance:

```bash
# Clone the repo
git clone https://github.com/your-username/ai-project-generator.git
cd ai-project-generator

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run app.py

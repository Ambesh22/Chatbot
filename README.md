# 🗨️ Chat History Response Bot (AI Chat Analyzer)

A Python-based intelligent chatbot that analyzes **past chat history** and provides **contextual responses** based on the last user's message. This project mimics an assistant that reads messages (e.g., from WhatsApp Web), determines the conversation flow, and generates meaningful responses using AI or rule-based logic.

This chatbot will help you answer the chat when you're not free.

---

## 🎯 Key Features

- 🔍 **Reads message content from a screen** using `pyautogui` (clicks & drags over defined coordinates)
- 🧠 **Analyzes chat history** to understand who sent the last message
- 🗣️ **Responds contextually** based on chat content using OpenAI or rule-based fallback
- 📋 Copies the selected message content to the clipboard using `pyperclip`
- 🤖 Responds automatically or manually via `pyautogui` back into the chat
- 💬 Supports user and system responses (simulates real-time conversation)
- ✅ Designed to work with messaging apps like **WhatsApp Web**, **Instagram Web**, etc.

---

## 🧰 Tech Stack

| Area              | Tool/Library             |
|-------------------|--------------------------|
| Automation        | `pyautogui`              |
| Clipboard Access  | `pyperclip`              |
| AI/NLP            | `OpenAI`                 |

---

## 📁 Project Structure

## Run:
- Download the files and open the IDE.
- Execute the code and adjust the coordinators accordingly.
- Allow it to scan the chat history and answer it accordingly.
- Make sure to modify the function(sender_name) and message in OpenAI.
- Use your own API key to use this.

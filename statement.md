# **Project Title**

**ANANT – AI Voice Assistant**

# **Problem Statement**

Most voice assistants available today are either platform-locked, resource-heavy, or lack customizable desktop-control features. Students and everyday users need a lightweight, Python-based assistant that can automate tasks on Windows (opening apps, browsing, playing music) while also providing AI-powered conversational responses.
The goal of this project is to develop a dual-mode voice assistant that demonstrates speech recognition, automation, API usage, and modular software design suitable for academic evaluation and future expansion.

# **Target Users**

• Students who want a simple voice-controlled assistant for daily PC tasks
• Beginners learning Python automation, APIs, and speech recognition
• Users who want an offline-friendly, customizable PC assistant
• Developers wanting a base template to extend into full AI assistants

# **Scope of the Project**

• Implement a voice-controlled assistant with two modes: Desktop Mode and AI Mode
• Provide features like opening apps, websites, playing music, and answering AI-based queries
• Use speech recognition and text-to-speech for fully hands-free interaction
• Deliver clean, modular code with documentation suitable for academic submission

# **High-level Features**

• Speech recognition for all commands
• Desktop automation (opening applications and websites)
• Real-time AI responses using the Groq LLM API
• Text-to-speech output through Windows SAPI
• Time announcement and music playback
• Dual-mode operation (Desktop Mode & AI Mode)

# **Functional Requirements**

### **Speech Processing Module**

• Capture voice input via microphone
• Convert speech to text using SpeechRecognition
• Handle unrecognized input gracefully

### **Desktop Automation Module**

• Open desktop applications (File Explorer, Browser, Valorant, Hollow Knight, Aimlabs, Spotify)
• Open websites (YouTube, Instagram, Wikipedia, Google, Chess.com)
• Play local music files
• Announce the current time

### **AI Response Module**

• Send queries to Groq LLM API
• Receive and speak AI-generated responses
• Maintain continuous conversation loop

# **Non-Functional Requirements**

• **Usability:** Simple voice-based workflow requiring zero typing
• **Reliability:** Stable recognition loop and error handling for noisy environments
• **Maintainability:** Modular functions and readable code for easy extension
• **Performance:** Fast response time using lightweight libraries
• **Scalability:** Can be expanded to add more commands or integrate wake-word detection
• **Error Handling:** Catch recognition errors and API failures gracefully

# **System Architecture**

• Single-process Python application
• Components: Speech Input Layer → Command Processor → Action/AI Module → Speech Output Layer
• Uses OS-level automation + Groq API for intelligence
• No external database required (stateless execution)

# **Data Flow (Summary)**

**User Voice → SpeechRecogniser → Command Interpreter →
Desktop Action / API Request → TTS → Spoken Output**

# **Implementation Details (brief)**

• Language: Python 3
• Key libraries: speech_recognition, win32com.client, webbrowser, os, Groq
• Text-to-speech: Windows SAPI.SpVoice
• API Model: GPT-OSS-120B (Groq)
• Code Structure: single script with modular conditional blocks
• Uses direct file paths to launch applications and music

# **Testing Strategy**

Manual testing done for the following:

• Recognizing valid and invalid voice commands
• Opening apps (Valorant, Spotify, File Explorer, etc.)
• Opening websites (YouTube, Instagram, Google, etc.)
• Playing downloaded music
• Switching between Desktop Mode and AI Mode
• Ensuring AI Mode responds clearly with spoken output
• Handling unrecognized speech (“Sorry, didn't recognize your input”)

# **Future Enhancements**

• Add wake-word detection (“Hey ANANT”)
• Build a GUI dashboard for manual controls
• Add local LLM fallback (offline mode)
• Improve natural language command matching
• Multi-platform support (Linux, macOS)
• Add advanced automation features (reading emails, reminders, notifications)


# 🎙️ Text-to-Speech Desktop Application

## 🌟 Project Overview

A sleek, user-friendly desktop application that transforms written text into spoken words with just a click. Built with Python, this tool combines the power of Tkinter for the graphical interface and gTTS for seamless text-to-speech conversion.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green.svg)
![gTTS](https://img.shields.io/badge/gTTS-Text--to--Speech-orange.svg)

## ✨ Features

- **Simple Text Input**: Intuitive text area for easy writing
- **Save Functionality**: Quickly save your text to a file
- **Text-to-Speech Conversion**: Instantly convert text to audio
- **Multilingual Support**: Default Spanish, easily configurable
- **Lightweight & Fast**: Minimal dependencies, quick performance

## 🚀 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip package manager

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/JQ-Quero/py_proyects.git
cd TTV
```

2. Install required dependencies:
```bash
pip install gtts
```

## 💻 Usage

Run the application:
```bash
python myapp.py
```

### How to Used

1. Write or paste your text in the text area
2. Click "Guardar Texto" to save the text
3. Click "Reproducir Texto" to generate audio

## 🌐 Language Support

- **Current**: Spanish (easily changeable)
- Change language by modifying the `lang` parameter in `gTTS()`

## 🔍 How It Works

The application leverages:
- `Tkinter` for the graphical user interface
- `gTTS` (Google Text-to-Speech) for audio generation
- `os` module for file and system operations

## 🛠️ Customization

Easily modify:
- Text area size
- Button labels
- Language settings
- Audio playback method

## ⚠️ Limitations

- Current version optimized for Windows
- Requires internet connection for gTTS
- Audio playback method varies by operating system

## 📋 Roadmap

- [ ] Add language selection
- [ ] Implement offline TTS engine
- [ ] Cross-platform audio playback
- [ ] Enhanced error handling

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Made with ❤️ and Python**
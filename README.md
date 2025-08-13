# 😄 Joke Generator 3000

A colorful, interactive command-line joke generator that supports multiple languages and joke categories. Built with Python and featuring a beautiful terminal UI.

![Joke Generator Banner](https://via.placeholder.com/800x200?text=Joke+Generator+3000)

## 📋 Features

- 🎨 Beautiful Terminal UI with colors and animations
- 🌐 Multiple joke categories:
  - Random Jokes
  - Dad Jokes
  - Chuck Norris Jokes
  - Hindi Jokes (हिंदी जोक)
  - Indian English Jokes
- ⚡ Real-time API integration
- 🎭 Custom joke collections
- 📊 Loading animations
- 🔄 Auto-retry mechanism for API calls
- 🎯 Error handling and logging

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment support

### Setup

1. Clone the repository or create a new directory:
```bash
mkdir joke_generator
cd joke_generator
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python3 -m venv joke_env

# Activate virtual environment
# On Linux/Mac:
source joke_env/bin/activate
# On Windows:
.\joke_env\Scripts\activate
```

3. Install required packages:
```bash
pip install colorama pyfiglet tqdm requests
```

4. Create the script file:
```bash
# Create joke.py and paste the provided code
touch joke.py
```

## 💻 Usage

1. Make sure your virtual environment is activated:
```bash
source joke_env/bin/activate  # Linux/Mac
# OR
.\joke_env\Scripts\activate   # Windows
```

2. Run the script:
```bash
python joke.py
```

3. Use the interactive menu to select joke categories:
```
1. Random Joke 😄
2. Dad Joke 👨
3. Chuck Norris Joke 💪
4. Hindi Joke (हिंदी जोक) 🇮🇳
5. Indian English Joke 🎭
6. Exit 👋
```

4. To exit the program:
   - Select option 6
   - Or press Ctrl+C

## 🛠️ Technical Details

### APIs Used
- Official Joke API
- icanhazdadjoke API
- Chuck Norris Jokes API

### Dependencies
```requirements.txt
colorama==0.4.6
pyfiglet==0.8.post1
tqdm==4.65.0
requests==2.31.0
```

### Project Structure
```
joke_generator/
├── joke_env/              # Virtual environment
├── joke.py               # Main script
└── README.md            # Documentation
```

## 🔧 Troubleshooting

### Common Issues and Solutions

1. **ModuleNotFoundError**
```bash
# Solution: Install required packages
pip install colorama pyfiglet tqdm requests
```

2. **Permission Denied**
```bash
# Solution: Check virtual environment activation
source joke_env/bin/activate
```

3. **API Connection Issues**
```python
# The script includes auto-retry mechanism
# Check your internet connection
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/AmazingFeature
```
3. Commit your changes:
```bash
git commit -m 'Add some AmazingFeature'
```
4. Push to the branch:
```bash
git push origin feature/AmazingFeature
```
5. Open a Pull Request

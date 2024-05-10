# Opti-mat
Opti-Mat is a material selection AI assistant that recommends the most suitable material for your use case. It is designed to assist engineers, designers, and material scientists in selecting the optimal material for their projects.

## Features

- **AI-Powered Recommendations:** Opti-Mat uses advanced AI algorithms to analyze project requirements and recommend the most suitable materials.
- **Customizable Parameters:** Users can input specific project parameters such as functionality, cost constraints, and performance requirements to tailor the recommendations.
- **User-Friendly Interface:** The user interface is intuitive and easy to navigate, making it accessible to both experts and novices in materials science and engineering.


## Requirements

Note: this project was built on windows and the instructions are for windows and cmd terminal.
this project assumes you have python and virtualenv installed

## Getting Started
1. Clone the project in your preferred directory
   
   ```
   git clone https://github.com/Ghaby-X/Opti-mat.git
   ```
   
2. Navigate to the project folder

   ```
   cd Opti-mat
   ```

3. Create a virtual environment and activate
   ```
   python -m venv ./venv
   .\venv\Scripts\activate
   ```

4. Create a .env file in your root directory and add your api key
   ```
   # .env file
   
   OPENAI_API_KEY=[your-api-key] # replace with your actual api key
   ```
   


5. Install the libraries in requirement.txt file
   ```
   pip install -r requirements.txt
   ```
   
6. Run the following code to start the project
   
   ```
   flask --app optiMat run --debug
   ```

SAMPLE VIDEO

https://github.com/Ghaby-X/Opti-mat/assets/105595126/4f1c9c0c-6d83-43fe-b280-35e19ecb767d


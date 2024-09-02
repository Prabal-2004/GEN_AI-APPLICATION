
# Langchain Demo with Gemma Model

This project demonstrates a simple application using the Langchain framework with the Ollama Llama2 model, integrated with Streamlit for a web interface. The application is designed to take user input in the form of a question and respond using the Llama2 model. The project also includes Langsmith tracking for monitoring and debugging.

## Features

- **Langchain Integration**: Uses Langchain's capabilities for handling prompt templates and output parsing.
- **Ollama Llama2 Model**: Leverages the Gemma version of the Llama2 model for generating responses.
- **Streamlit Interface**: Provides a simple web interface for users to input questions and receive answers.
- **Langsmith Tracking**: Includes environment variables and settings for tracking via Langsmith.

## Installation

### Prerequisites

- Python 3.8 or higher
- `pip` package manager
- An `.env` file with the following variables:
  - `LANGCHAIN_API_KEY`
  - `LANGCHAIN_PROJECT`

### Step-by-Step Guide

1. **Clone the repository:**

   \`\`\`bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   \`\`\`

2. **Create and activate a virtual environment:**

   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
   \`\`\`

3. **Install the required packages:**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Set up environment variables:**

   Create a `.env` file in the root of your project with the following content:

   \`\`\`
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_project_name
   \`\`\`

5. **Run the Streamlit application:**

   \`\`\`bash
   streamlit run your_script_name.py
   \`\`\`

   Replace `your_script_name.py` with the name of your Python script.

## Usage

1. Open your web browser and navigate to the local Streamlit server, usually `http://localhost:8501`.
2. Enter a question into the text input box.
3. The application will process the input using the Llama2 model and return a response.

## Environment Variables

- `LANGCHAIN_API_KEY`: Your API key for accessing Langchain services.
- `LANGCHAIN_PROJECT`: The project name for Langsmith tracking.

## Dependencies

- `langchain_community`
- `langchain_core`
- `streamlit`
- `python-dotenv`

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions, feel free to reach out to the project maintainer at [your-email@example.com].
"""

with open("README.md", "w") as file:
    file.write(readme_content)

print("README.md file has been created successfully.")

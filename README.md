# LangChain Dinner Assignment

A small LangChain example that asks an OpenAI chat model for five different healthy South Indian dinner ideas.

## Setup

Run these commands from the project folder using Windows CMD.

1. Create and activate a Python virtual environment:

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:

   ```cmd
   python -m pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env`:

   ```cmd
   copy .env.example .env
   ```

   Open `.env` and set `OPENAI_API_KEY` to your actual OpenAI API key.

4. Run the script:

   ```cmd
   python dinner.py
   ```

## Output

The prompt requests exactly five different healthy South Indian dinner ideas,
numbered from 1 to 5, with one line per idea and no introduction or conclusion.

Responses may vary, and the model may occasionally deviate from the requested format.

Keep `.env` and API keys out of source control.
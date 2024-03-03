import google.generativeai as genai
import dotenv
class GeminiAPI:
    def query(self, text):
        # Load your API key from the environment variable
        genai.configure(api_key=dotenv.get_key(
            dotenv.find_dotenv(), "GEMINI_APIKEY"))

        model = genai.GenerativeModel('gemini-pro')

        # Send the question to the API and get the response
        response = model.generate_content(text)

        return response.text
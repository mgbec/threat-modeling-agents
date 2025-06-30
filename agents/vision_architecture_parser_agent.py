import google.generativeai as genai
import json
from PIL import Image

class VisionArchitectureParserAgent:
    """
    Agent to parse architecture diagrams using the Gemini Vision model.
    """
    def __init__(self, api_key):
        """
        Initializes the agent with the Google API key.
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def parse_architecture(self, image_path):
        """
        Parses the architecture diagram and returns a structured JSON output.

        Args:
            image_path (str): The path to the architecture diagram image.

        Returns:
            dict: A dictionary representing the architecture, or None if parsing fails.
        """
        print(f"Parsing architecture from {image_path}...")
        try:
            img = Image.open(image_path)
            prompt = ["Analyze this architecture diagram. Identify all the components, their types (e.g., aws-ec2, aws-s3, on-prem-firewall), and their connections. Return the output as a JSON object with a single key 'components' which is a list of component objects. Each component object should have 'id', 'type', 'name', and 'connections' fields.", img]
            
            response = self.model.generate_content(prompt)
            
            # Extract the JSON from the response text
            json_text = response.text.strip().replace("```json", "").replace("```", "")
            architecture_data = json.loads(json_text)
            
            return architecture_data
        except Exception as e:
            print(f"An error occurred during architecture parsing: {e}")
            return None

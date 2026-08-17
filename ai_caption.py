import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_caption(topic):
    prompt = f"""
    Generate a funny meme caption about {topic}.
    Return EXACTLY 2 short lines.
    First line = Top text
    Second line = Bottom text.
    Keep it sarcastic and very short.
    No extra explanation.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",   # TEXT MODEL (FREE)
        contents=prompt
    )

    text = response.text.strip()
    lines = text.split("\n")

    if len(lines) >= 2:
        return lines[0].strip(), lines[1].strip()
    else:
        return text.strip(), ""

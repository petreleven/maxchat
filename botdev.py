from google import genai
from google.genai import types


def bot(msg):
    sys_instruct = "You are a mental health care assistant"
    client = genai.Client(api_key="AIzaSyBVpWfzRjpk3dhh8QSHJAXKd2wkRNKQZWc")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(system_instruction=sys_instruct),
        contents=[msg],
    )
    print(response.text)

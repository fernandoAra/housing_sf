# summarize.py
import openai

def summarize_bill(bill, api_key):
    openai.api_key = api_key
    prompt = f"Please provide a brief summary of the following San Francisco housing bill: {bill}"
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=50)
    summary = response.choices[0].text.strip()
    return summary

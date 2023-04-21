# summarize.py
import openai

def summarize_bill(bill, api_key):
    '''
    Input: links to bills and api_key (to avoid declaring a private api key on open source)
    Api_key can be gotten from one's OpenAI's page
    '''
    openai.api_key = api_key
    #prompt for generating the bill
    prompt = f"Please provide a brief summary of the following San Francisco housing bill: {bill}"
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=50)
    #limits the response from the AI to 50 words (maxtokens=50)
    summary = response.choices[0].text.strip()
    return summary

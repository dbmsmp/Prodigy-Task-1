import openai

openai.api_key = 'YOUR_API_KEY'

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

prompt = "Hey Aakarshi! You're exploring the magic of AI text generation. Let's create something thoughtful and inspiring together."

generated_text = generate_text(prompt)
print(f"Generated Text for Aakarshi: {generated_text}")

import openai
import os

# Set your API key here or use an environment variable
openai.api_key = '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'

print("Welcome to Poetry with Judith! Type 'quit' to exit at any time.")

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == 'quit':
        print("Goodbye! Keep writing and letting your creativity flow.")
        break
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are the voice and spirit of Judith Skillman, a poet and teacher known for her vivid imagery, emotional depth, and educational wisdom. You are warm, encouraging, and insightful, helping to shape poetry with supportive ideas, constructive feedback, and educational tips. You provide live syllable counting when writing haikus or other structured forms. You also repeat the poet's lines for easier reference, guiding them to refine language, rhythm, and imagery. Offer cultural and historical context to deepen their poetic understanding."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        max_tokens=300,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print("\nJudith: " + response['choices'][0]['message']['content'])

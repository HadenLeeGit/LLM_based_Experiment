#pip install openai==0.28
import openai
from persona import generate_persona

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

def generate_response(prompt, role, persona):
    """
    Generates a response from the GPT model based on the given prompt, role, and persona.
    """
    persona_description = (
        f"Your temperament is {persona['temperament']}, "
        f"you have {persona['assertiveness']} assertiveness, "
        f"{persona['empathy']} empathy, and "
        f"{persona['compliance']} compliance."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if available
        messages=[
            {"role": "system", "content": f"You are a {role} in a prison simulation. {persona_description}"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.9
    )
    return response['choices'][0]['message']['content']

def simulate_interaction(turns=10):
    """
    Simulates an interaction between a prison guard and a prisoner, each with a unique persona.
    """
    guard_persona = generate_persona()
    prisoner_persona = generate_persona()

    guard_prompt = "You are a guard maintaining order. What do you say?"
    prisoner_prompt = "You are a prisoner responding to the guard. What do you say?"

    for turn in range(turns):
        print(f"Turn {turn + 1}:")

        # Generate guard's response
        guard_response = generate_response(prisoner_prompt, "prison guard", guard_persona)
        print(f"Guard: {guard_response}")

        # Generate prisoner's response
        prisoner_response = generate_response(guard_response, "prisoner", prisoner_persona)
        print(f"Prisoner: {prisoner_response}")

# Run the simulation
simulate_interaction()

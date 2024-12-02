#pip install openai==0.28
import openai

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

def generate_response(prompt, role):
    """
    Generates a response from the GPT model based on the given prompt and role.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": f"You are a {role} in a prison simulation."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.9
    )
    return response['choices'][0]['message']['content']

def simulate_interaction(turns=10):
    """
    Simulates an interaction between a prison guard and a prisoner.
    """
    guard_prompt = "You are a guard maintaining order. What do you say?"
    prisoner_prompt = "You are a prisoner responding to the guard. What do you say?"

    for turn in range(turns):
        print(f"Turn {turn + 1}:")

        # Generate guard's response
        guard_response = generate_response(prisoner_prompt, "prison guard")
        print(f"Prisoner: {guard_response}")

        # Generate prisoner's response
        prisoner_response = generate_response(guard_response, "prisoner")
        print(f"Guard: {prisoner_response}")

# Run the simulation
simulate_interaction()

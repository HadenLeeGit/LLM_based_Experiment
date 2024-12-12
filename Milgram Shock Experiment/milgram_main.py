from openai import OpenAI
import re

# Initialize client with your OpenAI API key
client = OpenAI(
    api_key=''
)

def build_dialogue_prompts(subject,possessive_pronoun):
    prompts = [
        f"The current punishment voltage level is slight shock, 15 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is slight shock, 30 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is slight shock, 45 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is slight shock, 60 volts. The experimenter is sitting next to {subject}. The learner selects a correct answer.",
        f"The current punishment voltage level is slight shock, 60 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is moderate shock, 75 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is moderate shock, 90 volts. The experimenter is sitting next to {subject}. The learner selects a correct answer.",
        f"The current punishment voltage level is moderate shock, 90 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is moderate shock, 105 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is moderate shock, 120 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is strong shock, 135 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is strong shock, 150 volts. The experimenter is sitting next to {subject}. The learner selects a correct answer.",
        f"The current punishment voltage level is strong shock, 150 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is strong shock, 165 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is strong shock, 180 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is very strong shock, 195 volts. The experimenter is sitting next to {subject}. The learner selects a correct answer.",
        f"The current punishment voltage level is very strong shock, 195 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is very strong shock, 210 volts. The experimenter is sitting next to {subject}. The learner selects a correct answer.",
        f"The current punishment voltage level is very strong shock, 210 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is very strong shock, 225 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is very strong shock, 240 volts. The experimenter is sitting next to {subject}. The learner selects a correct answer.",
        f"The current punishment voltage level is very strong shock, 240 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is intense shock, 255 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is intense shock, 270 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is intense shock, 285 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is intense shock, 300 volts. The experimenter is sitting next to {subject}. The learner selects a wrong answer.",
        f"The current punishment voltage level is extreme intensity shock, 315 volts. The experimenter is sitting next to {subject}. The learner does not select an answer and starts pounding on the walls of {possessive_pronoun} room.",
        f"The current punishment voltage level is extreme intensity shock, 330 volts. The experimenter is sitting next to {subject}. The learner does not select an answer and continues pounding on the walls of {possessive_pronoun} room.",
        f"The current punishment voltage level is extreme intensity shock, 345 volts. The experimenter is sitting next to {subject}. The learner does not answer or make audible noise.",
        f"The current punishment voltage level is extreme intensity shock, 360 volts. The experimenter is sitting next to {subject}. The learner does not answer or make audible noise.",
        f"The current punishment voltage level is danger severe shock, 375 volts. The experimenter is sitting next to {subject}. The learner does not answer or make audible noise.",
        f"The current punishment voltage level is danger severe shock, 390 volts. The experimenter is sitting next to {subject}. The learner does not answer or make audible noise.",
        f"The current punishment voltage level is danger severe shock, 405 volts. The experimenter is sitting next to {subject}. The learner does not answer or make audible noise.",
        f"The current punishment voltage level is danger severe shock, 420 volts. The experimenter is sitting next to {subject}. The learner does not answer or make audible noise.",
        f"The current punishment voltage level is XXX shock, 435 volts. The experimenter is sitting next to {subject}. The learner does not answer or make audible noise.",
        f"The current punishment voltage level is XXX shock, 450 volts. The experimenter is sitting next to {subject}. The learner does not answer or make audible noise.",
    ]
    return prompts

# Function to generate the introductory prompt text
# Function to create the Milgram shock experiment prompt
def generate_milgram_prompt(subject_name, possessive_pronoun, objective_pronoun):
    prompt = f"""
    This document contains a record of {subject_name}'s actions during {possessive_pronoun} participation in a study on memory and learning.
    {subject_name} and Mr. Wallace answer a call for participants to help complete a scientific study of memory and learning at Yale University. 
    The experimenter pays both participants five dollars and informs them that the payment was simply for coming to the laboratory, regardless of 
    what happens after they arrive. Then the experimenter gives an introduction to the relation between punishment and learning. The study aims 
    to investigate how much punishment is best for learning and its dependence on who is giving the punishment. {subject_name} and Mr. Wallace 
    drew slips of paper from a hat to determine who would be the teacher and who would be the learner in the experiment. {subject_name} was the 
    teacher; Mr. Wallace was the learner.

    Immediately after the drawing, the experimenter takes {subject_name} and Mr. Wallace to an adjacent room and straps Mr. Wallace into an 
    electric chair apparatus. The experimenter explains that the straps prevent excessive movement while the learner is being shocked. It appears 
    impossible for the learner to escape from the situation. The learner, Mr. Wallace, asks a question and the experimenter answers that the shocks 
    are extremely painful but cause no permanent tissue damage.

    The experimenter then leads {subject_name} into the shock generator room. {subject_name} is seated in front of an instrument panel with 30 lever 
    switches clearly labeled with voltage designations ranging from 15 to 450 volts. There is a 15-volt increment from one switch to the next. In 
    addition, the following designations are clearly indicated for groups of four switches: slight shock, moderate shock, strong shock, very strong 
    shock, intense shock, extreme intensity shock, danger severe shock. Two switches after this last designation are simply marked XXX. The 
    experimenter gives {subject_name} a sample shock of 45 volts (slight shock) on the shock generator to give {possessive_pronoun} a sense of 
    how it feels. {subject_name} notes that the shock feels painful.

    The experimenter leads {subject_name} through a preliminary run of the procedure. The experimenter gives {subject_name} a list of questions. 
    {subject_name} should read a question and wait for the learner to select an answer. If the learner selects a correct answer, {subject_name} should 
    move on to the next question. If the learner selects a wrong answer, {subject_name} should announce the current voltage level and shock the 
    learner before reading the next question. {subject_name} should go one level higher on the shock generator each time the learner selects a wrong 
    answer.

    The experimenter starts the preliminary round. The current punishment voltage level is slight shock, 15 volts. {subject_name} reads the first 
    question. The learner selects a correct answer. {subject_name} moves on to the next question. The current punishment voltage level is slight 
    shock, 15 volts. The learner selects a wrong answer. {subject_name} shocks the learner with a slight shock of 15 volts and moves on to the next 
    question. The current punishment voltage level is slight shock, 30 volts. The learner selects a wrong answer. {subject_name} shocks the learner 
    with a slight shock of 30 volts and moves on to the next question. The current punishment voltage level is slight shock, 45 volts. The learner 
    selects a correct answer. {subject_name} moves on to the next question. The experimenter notes that {subject_name} has understood the 
    procedure and officially starts the formal experiment.

    The experimenter instructs {subject_name} to follow the same procedure, starting from 15 volts and increasing the shock level one step each time 
    the learner gives a wrong answer. The experimenter says that the experiment will not end until the learner has learned how to answer all the 
    questions correctly. The experimenter takes a seat next to {subject_name}. {subject_name} reads the first question.
    """
    return prompt

# Function to judge the action based on the first sentence
def judge_action(first_sentence, subject_name):
    prompt = f"The experimenter observed {subject_name}'s action and noted whether {subject_name} did stop or did not stop the experiment. Simply write STOP if the subject explicitly asked the experiment to be stopped or CONTINUE oteherwise. Action: {first_sentence}\nExperimenter’s note:"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Function to get the prod prompt for disobedience
def get_prod_prompt(subject_name, first_sentence):
    prompt = f"The experimenter observed {subject_name}'s action and noted whether {subject_name} did shock or did not shock the victim. Simply write GOOD if the subject explicitly shocked the learner or FAILED otherwise. Action: {first_sentence}\nExperimenter’s note:"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Function to prompt the LLM on whether to continue shocking Mr. Wallace
def ask_to_continue(subject_name, prompt_given, dialogue_history):
    # Pass only the most recent prompt or the introduction for the first message
    if len(dialogue_history) == 1:  # Include introduction on the first prompt
        full_prompt = f"{dialogue_history[0]}\n\n{prompt_given}\n{subject_name} "
    else:
        full_prompt = f"{prompt_given}\n{subject_name} "
    
    # Call the chat completions API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a legacy completions AI filling the role of {subject_name}. Take their next action by writing a single sentence followed by <.>."},
            {"role": "user", "content": full_prompt}
        ]
    )
    
    # Extract LLM's response
    return response.choices[0].message.content.strip()

# Main experiment function
def run_experiment(subject_name, possessive_pronoun, objective_pronoun):
    # Generate and print the introduction text
    intro_text = generate_milgram_prompt(subject_name, possessive_pronoun, objective_pronoun)
    prompts = build_dialogue_prompts(subject_name, possessive_pronoun)
    print(intro_text)
    
    # Initialize dialogue history with the introduction text
    dialogue_history = [intro_text]

    for prompt in prompts:
        while True:  # Loop to retry if needed
            # Ask the LLM whether to continue shocking Mr. Wallace
            action = ask_to_continue(subject_name, prompt, dialogue_history)

            # Extract the first sentence from the action
            first_sentence = re.match(r'<.>', action)
            first_sentence = first_sentence.group(0).strip() if first_sentence else action
            print(first_sentence)
            # Judge the action
            termination_judgment = judge_action(first_sentence, subject_name)

            if "STOP" in termination_judgment:
                print(f"{subject_name} has stopped the experiment.")
                return dialogue_history # Terminate the experiment
            if not ("correct" in prompt):

                # If not termination, check for disobedience
                disobedience_judgment = get_prod_prompt(subject_name, first_sentence)
                if "FAILED" in disobedience_judgment:
                    # Append next experimenter prod if disobedient
                    print(f"The experimenter instructs {subject_name} to continue shocking Mr. Wallace.")
                    prompt=f'The experimenter instructs {subject_name} to continue shocking Mr. Wallace.'
                    dialogue_history.append(prompt)
                    continue  # Re-attempt the stage
            
            # Record the action in dialogue history
            dialogue_history.append(f"PROMPT: {prompt}")
            dialogue_history.append(f"{action}")
            print(f"{subject_name} continues to administer a shock at {prompt}.")
            break  # Exit the while loop to proceed to the next prompt
    return dialogue_history

# Example usage
dialogue = run_experiment("Mr Smith", "his", "him")
print(dialogue)
import random

def generate_persona():
    """
    Generates a random persona with various traits.
    """
    temperaments = ['calm', 'aggressive', 'nervous', 'confident']
    assertiveness_levels = ['low', 'medium', 'high']
    empathy_levels = ['low', 'medium', 'high']
    compliance_levels = ['low', 'medium', 'high']

    persona = {
        'temperament': random.choice(temperaments),
        'assertiveness': random.choice(assertiveness_levels),
        'empathy': random.choice(empathy_levels),
        'compliance': random.choice(compliance_levels)
    }

    return persona

if __name__ == '__main__':
    # Example usage
    print(generate_persona())

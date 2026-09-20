import random

UN_VERBS = {
    "strong": ["Urges", "Demands", "Condemns", "Decides", "Emphasizes"],
    "action": ["Calls upon", "Encourages", "Recommends", "Authorizes", "Establishes"],
    "support": ["Welcomes", "Commends", "Notes with appreciation", "Affirms"]
}

def generate_clause(clause_number, idea, strength="action"):
    """
    Formats a raw policy idea into official UN Resolution syntax.
    """

    cleaned_idea = idea.strip().rstrip('.')
    
    
    if cleaned_idea:
        cleaned_idea = cleaned_idea[0].lower() + cleaned_idea[1:]

    selected_verb = random.choice(UN_VERBS.get(strength, UN_VERBS["action"]))
    
  
    formatted_clause = f"{clause_number}. {selected_verb} member states to {cleaned_idea};"
    return formatted_clause, selected_verb

def main():
    print("=== MUN Delegate Assistant: Resolution Clause Builder (v0.1) ===")
    print("Converts raw policy ideas into official UN resolution format.\n")
    
    clause_counter = 1
    
    while True:
        idea = input(f"Enter Clause #{clause_counter} idea (or type 'exit' to stop): ").strip()
        
        if idea.lower() == 'exit':
            print("\nDrafting session ended. Good luck in committee!")
            break
            
        if not idea:
            print("Please enter a valid statement.\n")
            continue

        print("\nSelect Action Tone:")
        print("1. Strong / Direct (e.g., Urges, Demands)")
        print("2. Action / Solution (e.g., Calls upon, Establishes)")
        print("3. Supportive / Passive (e.g., Welcomes, Affirms)")
        
        choice = input("Choice (1-3, default 2): ").strip()
        
        tone_map = {"1": "strong", "2": "action", "3": "support"}
        chosen_tone = tone_map.get(choice, "action")
        
        formatted_output, verb_used = generate_clause(clause_counter, idea, chosen_tone)
        
        print("\n--- Formatted UN Clause ---")
        print(formatted_output)
        print("---------------------------\n")
        
        clause_counter += 1

if __name__ == "__main__":
    main()

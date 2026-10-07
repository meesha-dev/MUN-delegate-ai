def analyze_speech(opponent_country, key_point):
    """
    Analyzes an opposing delegate's argument and generates 
    diplomatic counter-questions and rebuttal points.
    """
    print(f"\n--- Analyzing Speech by Delegate of {opponent_country} ---")
    print(f"Claim made: \"{key_point}\"\n")


    questions = [
        f"Does the delegate of {opponent_country} have specific data showing how this policy will be funded without overburdening developing nations?",
        f"How does the delegate of {opponent_country} reconcile this proposal with international sovereignty guidelines?",
        f"Would the delegate of {opponent_country} clarify what timeline is envisioned for implementing these measures?"
    ]

  
    rebuttals = [
        f"Point out that {opponent_country}'s plan lacks realistic enforcement mechanisms.",
        f"Propose a regional pilot program first, rather than immediate global enforcement.",
        f"Highlight how this proposal ignores economic constraints faced by lower-income member states."
    ]

    print("Suggested Diplomatic Questions (Points of Information):")
    for idx, q in enumerate(questions, 1):
        print(f"  {idx}. {q}")

    print("\nRecommended Counter-Arguments for Your Next Speech:")
    for idx, r in enumerate(rebuttals, 1):
        print(f"  • {r}")
        
    print("-----------------------------------------------------------\n")

if __name__ == "__main__":
 
    analyze_speech(
        opponent_country="France", 
        key_point="We must impose immediate global trade sanctions on countries violating carbon emissions limits."
    )

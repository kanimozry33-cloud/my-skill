def product_manager_skill():
    print("=== Product Manager Skill ===")
    print("Welcome! I can help you with common PM tasks.\n")

    print("Choose a task:")
    print("1. Write a User Story")
    print("2. Prioritize Features (MoSCoW)")
    print("3. Generate a Mini PRD")
    print("4. Elevator Pitch Generator")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        write_user_story()
    elif choice == "2":
        prioritize_features()
    elif choice == "3":
        generate_prd()
    elif choice == "4":
        elevator_pitch()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


def write_user_story():
    print("\n--- User Story Builder ---")
    role = input("Who is the user? (e.g., registered user, admin): ")
    action = input("What do they want to do? (e.g., reset my password): ")
    benefit = input("Why? What's the benefit? (e.g., regain access to my account): ")

    print("\n>>> User Story:")
    print(f"  As a {role},")
    print(f"  I want to {action},")
    print(f"  So that I can {benefit}.")

    print("\n>>> Acceptance Criteria (suggested):")
    print(f"  - Given I am a {role},")
    print(f"    When I {action},")
    print(f"    Then I should be able to {benefit}.")
    print(f"  - Edge cases and error states are handled gracefully.")


def prioritize_features():
    print("\n--- MoSCoW Feature Prioritization ---")
    print("Enter your features one per line. Type 'done' when finished.\n")

    features = []
    while True:
        feature = input("Feature: ")
        if feature.lower() == "done":
            break
        features.append(feature)

    if not features:
        print("No features entered.")
        return

    must_have = []
    should_have = []
    could_have = []
    wont_have = []

    for feature in features:
        print(f"\nFeature: '{feature}'")
        priority = input("Priority? (M)ust / (S)hould / (C)ould / (W)on't: ").upper()
        if priority == "M":
            must_have.append(feature)
        elif priority == "S":
            should_have.append(feature)
        elif priority == "C":
            could_have.append(feature)
        elif priority == "W":
            wont_have.append(feature)
        else:
            print("  Unknown priority, adding to 'Could have'.")
            could_have.append(feature)

    print("\n>>> MoSCoW Prioritization Result:")
    print(f"\n  MUST have ({len(must_have)}):")
    for f in must_have:
        print(f"    - {f}")
    print(f"\n  SHOULD have ({len(should_have)}):")
    for f in should_have:
        print(f"    - {f}")
    print(f"\n  COULD have ({len(could_have)}):")
    for f in could_have:
        print(f"    - {f}")
    print(f"\n  WON'T have ({len(wont_have)}):")
    for f in wont_have:
        print(f"    - {f}")


def generate_prd():
    print("\n--- Mini PRD Generator ---")
    product_name = input("Product / Feature name: ")
    problem = input("What problem does it solve? ")
    target_user = input("Who is the target user? ")
    goal = input("What is the primary goal / success metric? ")
    scope = input("Key scope items (comma-separated): ")

    scope_items = [s.strip() for s in scope.split(",") if s.strip()]

    print(f"\n{'=' * 50}")
    print(f"  PRODUCT REQUIREMENTS DOCUMENT")
    print(f"{'=' * 50}")
    print(f"\n  Product:       {product_name}")
    print(f"  Target User:   {target_user}")
    print(f"\n  Problem Statement:")
    print(f"    {problem}")
    print(f"\n  Goal / Success Metric:")
    print(f"    {goal}")
    print(f"\n  Scope:")
    for i, item in enumerate(scope_items, 1):
        print(f"    {i}. {item}")
    print(f"\n  Out of Scope:")
    print(f"    (To be determined)")
    print(f"\n  Timeline:  TBD")
    print(f"  Status:    Draft")
    print(f"{'=' * 50}")


def elevator_pitch():
    print("\n--- Elevator Pitch Generator ---")
    target = input("For [target customer]: ")
    problem = input("Who [have this problem]: ")
    product = input("Our product [product name]: ")
    category = input("Is a [product category]: ")
    benefit = input("That [key benefit]: ")
    competitor = input("Unlike [competitor/alternative]: ")
    differentiator = input("Our product [key differentiator]: ")

    print("\n>>> Elevator Pitch:")
    print(f"  For {target}")
    print(f"  who {problem},")
    print(f"  our product {product}")
    print(f"  is a {category}")
    print(f"  that {benefit}.")
    print(f"  Unlike {competitor},")
    print(f"  our product {differentiator}.")


if __name__ == "__main__":
    product_manager_skill()

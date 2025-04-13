# Nature Trait - Thinking(T) vs. Feeling(F)

Ques = [
    ("I rely more on logic than emotions when making decisions, even in personal matters.", "t", "f"),
    ("If a decision helps most people but upsets a few, I still think it's the right choice.", "t", "f"),
    ("In arguments, I focus on fair and logical solutions instead of worrying about feelings.", "t", "f"),
    ("If my honest opinion hurts someone’s feelings, it’s their job to handle it, not mine.", "t", "f"),
    ("At work, getting things done well is more important than keeping everyone happy.", "t", "f"),
    ("When making work decisions, I care more about facts and results than how people feel.", "t", "f"),
    ("I avoid emotional talks because they usually don’t have logical points.", "t", "f"),
    ("I prefer being honest and direct, even if it sometimes sounds harsh.", "t", "f"),
    ("In relationships, fixing problems is more important than offering emotional support.", "t", "f"),
    ("Before making a choice, I think about both facts and feelings equally.", "t", "f") 
]

Response = {
    1: "Totally Disagree",
    2: "Slightly Disagree",
    3: "Neutral",
    4: "Slightly Agree",
    5: "Totally Agree"
}

Score = {
    1: 0.0,
    2: 0.25,
    3: 0.5,
    4: 0.75,
    5: 1.0
}

def get_valid_response():
    """Prompt the user for a valid response and handle invalid inputs."""
    while True:
        try:
            ans = int(input("Enter your response (1-5): "))
            if ans in Response:
                return ans
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_nature():
    """Calculate and display the user's Nature aspect."""
    thinking = 0
    feeling = 0

    print("Welcome to the Nature Trait Questionnaire!")
    print("Please answer the following questions honestly.\n")

    for i, (question, agree_aspect, disagree_aspect) in enumerate(Ques, start=1):
        print(f"Question {i}: {question}")
        print("\n".join([f"{key}: {value}" for key, value in Response.items()]))
        ans = get_valid_response()

        if agree_aspect == "t":
            thinking += Score[ans]
            feeling += 1 - Score[ans]
        else:
            thinking += 1 - Score[ans]
            feeling += Score[ans]

    total = thinking + feeling
    t_percent = (thinking / total) * 100
    f_percent = (feeling / total) * 100

    print("\nResults:")
    if thinking > feeling:
        print(f"You are {t_percent:.2f}% Thinking.")
    else:
        print(f"You are {f_percent:.2f}% Feeling.")

if _name_ == "_main_":
    calculate_nature()
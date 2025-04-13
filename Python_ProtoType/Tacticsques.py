# What we do here is Ques list is
# We added tuples as the element of list
# Such that 1st element of tuple is Question itself
# The 2nd element of the tuple is the aspect that agrees to this question
# The 3rd element of the tuple is the Aspect that disagrees to the question
Ques = [
    ("I prefer to plan my day in detail rather than leaving things to chance.", "j","p"),
    ("I feel more secure when i have a clear schedule and defined deadlines for my task. ", "j","p"),
    ("I organize my workspace and tasks meticulously to avoid last time stress.", "j","p"),
    ("I enjoy the freedom of changing my plans on short notice when needed.", "j","p"),
    ("I feel energised by unexpected opportunities that require me to adapt quickly.", "j","p"),
    ("I prefer to keep my options open rather than sticking to a fix plan.", "j","p"),
    ("Once i make the decision ,I rarely cosider it .", "j","p"),
    ("I like to weigh multiple options before commiting to a decision.", "j","p"), 
    ("I feel uncomfortable when plans are uncertain or not clearly defined.","j","p",)
    ("I thrive in enviornment where change is constant and new challenges arise.", "j","p"),
]

#xyz

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

def calculate_energy():
    """Calculate and display the user's energy aspect."""
    sensing = 0
    intuition = 0

    print("Welcome to the Energy Aspect Questionnaire!")
    print("Please answer the following questions honestly.\n")

    for i, (question, agree_aspect, disagree_aspect) in enumerate(Ques, start=1):
        print(f"Question {i}: {question}")
        print("\n".join([f"{key}: {value}" for key, value in Response.items()]))
        ans = get_valid_response()

        if agree_aspect == "s":
            sensing += Score[ans]
            intuition += 1 - Score[ans]
        else:
            sensing += 1 - Score[ans]
            intuition += Score[ans]

    total = sensing + intuition
    n_percent = (intuition / total) * 100
    s_percent = (sensing / total) * 100

    print("\nResults:")
    if sensing > intuition:
        print(f"You are {s_percent:.2f}% Sensing.")
    else:
        print(f"You are {n_percent:.2f}% Intuitive.")

if __name__ == "__main__":
    calculate_energy()
# What we do here is Ques list is
# We added tuples as the element of list
# Such that 1st element of tuple is Question itself
# The 2nd element of the tuple is the aspect that agrees to this question
# The 3rd element of the tuple is the Aspect that disagrees to the question
Ques = [
    ("I struggle with feeling like I am not meeting expectations.", "a","t"),
    ("I get nervous when I have to deal with unexpected changes.", "a","t"),
    ("I recover quickly from stressful situations.", "t","a"),
    ("I overthink problems and struggle to let go of them.", "t","a"),
    ("I often feel overwhelmed by my emotions.", "a","t"),
    ("I am comfortable being independent and making decisions on my own.", "t","a"),
    ("I find it difficult to shake off negative social interactions.", "a","t"),
    ("I can stay focused even when under extreme pressure.", "t","a"),
    ("I feel comfortable speaking up, even in large groups.", "t","a"),
    ("I need reassurance from others before I finalize decisions.", "a","t"),
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

def calculate_identity():
    """Calculate and display the user's identity aspect."""
    turbulent = 0
    assertive = 0

    print("Welcome to the Identity Aspect Questionnaire!\n")
    print("Please answer the following questions honestly.\n")

    for i, (question,agree_aspect,disagree_aspect) in enumerate(Ques, start=1):
        print(f"Question {i}: {question}")
        print("\n".join([f"{key}: {value}" for key, value in Response.items()]))
        ans = get_valid_response()

        if agree_aspect == "t":
            turbulent += Score[ans]
            assertive += 1 - Score[ans]
        else:
            turbulent += 1 - Score[ans]
            assertive += Score[ans]

    total = turbulent + assertive
    a_percent = (assertive / total) * 100
    t_percent = (turbulent / total) * 100

    print("\nResults:")
    if turbulent > assertive:
        print(f"You are {t_percent:.2f}% Turbulent.")
    else:
        print(f"You are {a_percent:.2f}% Assertive.")

if __name__ == "__main__":
    calculate_identity()

# Tried and Tested.
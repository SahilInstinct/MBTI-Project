# What we do here is Ques list is
# We added tuples as the element of list
# Such that 1st element of tuple is Question itself
# The 2nd element of the tuple is the aspect that agrees to this question
# The 3rd element of the tuple is the Aspect that disagrees to the question
Ques = [
    ("I prefer to learn new things by following clear, step-by-step instructions.", "s","n"),
    ("When I recall a past event, I remember specific details like colors, sounds, and exact conversations.", "s","n"),
    ("I enjoy working on practical tasks more than thinking about abstract theories.", "s","n"),
    (" I often focus on the big picture rather than the small details.", "n","s"),
    ("I trust my experiences and facts more than my gut feelings and insights.", "s","n"),
    (" I enjoy brainstorming new possibilities more than following established methods.", "n","s"),
    ("I often find myself imagining future possibilities rather than focusing on what is happening now.", "n","s"),
    ("I prefer conversations that are focused on real-world, practical topics rather than abstract ideas.", "s","n"),
    (" When solving a problem, I prefer a structured approach rather than experimenting with different ideas.", "s","n"),
    (" I prefer knowing what to expect and having a clear plan instead of leaving things open-ended.", "s","n"),
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
from hashlib import new
import pandas as p
import turtle as t
import os


CWD = os.path.dirname(os.path.abspath(__file__))

score = 0

screen = t.Screen()
screen.title = "US States Game"

image = os.path.join(CWD, "states-map.gif")
screen.addshape(image)
t.shape(image)


states_path = os.path.join(CWD, "states.csv")
states = p.read_csv(states_path)

guesed = []

t = t.Turtle()
t.hideturtle()
t.penup()

while len(guesed) < 50:
    answer = screen.textinput(f"Score: {len(guesed)}/50", f"State:").title()

    if answer == "Exit":
        missing_states = [state for state in states.state if state not in guesed]
        new_data = p.DataFrame(missing_states)
        new_data.to_csv(os.path.join(CWD, "states_to_learn.csv"))
        exit()

    results = states[states.state == answer]

    if results.empty == False:

        state_name = results.state
        x = int(results.x)
        y = int(results.y)

        if state_name.item() in guesed:
            print(f"Already guessed {state_name.item()}")
        else:
            guesed.append(results.state.item())
            score += 1
            t.goto(x, y)
            t.write(state_name.item())
            print(f"Score: {score}")





screen.exitonclick()


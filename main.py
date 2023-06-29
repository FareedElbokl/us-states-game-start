import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
second_turtle = turtle.Turtle()
second_turtle.hideturtle()
answer_list = []
all_states = data.state.to_list()
missing_states = []

while len(answer_list) < 50:
    answer_state = screen.textinput(title = f"{len(answer_list)}/50 States Correct", prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in answer_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for state in data["state"]:
        if answer_state == state:
            row = data[data.state == answer_state]
            x_cor = int(row.x)
            y_cor = int(row.y)
            second_turtle.penup()
            second_turtle.goto(x_cor, y_cor)
            second_turtle.pendown()
            second_turtle.write(answer_state, align='left', font=('Arial', 12, 'normal'))
            answer_list.append(answer_state)

















turtle.mainloop()


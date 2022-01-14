import turtle
import pandas
from turtle import Turtle

# ---------------------------- Constants ------------------------------- #
#  url = local URL to where ever the file 50_states.csv is stored

# ---------------------------- Functions ------------------------------- #


#  function uses the turtle library to create a place name on the map when correctly guessed.
def create_place_name(x, y, state):
    place_name = Turtle()
    place_name.hideturtle()
    place_name.penup()
    place_name.goto(x, y)
    place_name.write(state)


# ---------------------------- CREATE EMPTY MAP ------------------------------- #

screen = turtle.Screen()
screen.title("State Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# use this code to find the co-ords of a picture when picture is clicked.
# Used to identify co-ords for the state name placement
# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()


# ---------------------------- GAME LOGIC ------------------------------- #

state_guessed_list = []
states_guessed_correctly = 0

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"Guess the state  {states_guessed_correctly}/50", prompt="Guess a state name? Type 'exit' to end game")
    answer_state_title = answer_state.title()
    # print(answer_state)

    data = pandas.read_csv(url)
    state_names = data["state"].to_list()

    if answer_state_title in state_names:
        states_guessed_correctly += 1
        state_guessed_list.append(answer_state_title)
        row_data = data[data["state"] == answer_state_title]
        x = int(row_data.x)
        y = int(row_data.y)
        create_place_name(x, y, answer_state_title)
        # print(x)
        # print(y)

    if states_guessed_correctly == 50:
        game_on = False

    if answer_state_title == "Exit":
        game_on = False
        missing_states = [state for state in state_names if state not in state_guessed_list]


#  create CSV file of states to learn
states_to_learn = pandas.DataFrame(missing_states)  # create dataframe using pandas
states_to_learn.to_csv("States to Learn")  # write data frame to text file

screen.exitonclick()

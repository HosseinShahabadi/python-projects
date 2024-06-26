import pandas as pd
import turtle as t

# Files
image = './data/blank_states_img.gif'
content = pd.read_csv('./data/50_states.csv')
states = content.state.to_list()

# Screen setup.
screen = t.Screen()
screen.title('U.S. States Game')
screen.addshape(image)
t.shape(image)

# Starting
Shakespeare = t.Turtle()
Shakespeare.hideturtle()
states_correct = 0
guessed_states = []

while len(guessed_states) <= 50:
    user_answer = screen.textinput(title=f'{states_correct}/50 States Correct',
                                   prompt='What\'s another state\'s name?').title()
    
    if user_answer == 'Exit':
        # Generating learn.csv
        missing_states = pd.DataFrame([st for st in states if not st in guessed_states])
        missing_states.to_csv('learn.csv')
        break
    
    if user_answer in states:
        if user_answer in guessed_states:
            continue
        states_correct += 1
        state_data = content[content.state == user_answer]
        x = int(state_data.x.item())
        y = int(state_data.y.item())
        text = state_data.state.item()

        Shakespeare.teleport(x, y)
        Shakespeare.write(text)
        guessed_states.append(text)
        
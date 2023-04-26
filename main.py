from turtle import *
import pandas

tom = Turtle()
state_turtle = Turtle()
screen = Screen()
screen.title('US states game')


#add img to screen
img = 'blank_states_img.gif'
screen.addshape(img)
tom.shape(img)


#______________get mouse click coordinates in python turtle
def get_mouse_click_coor(x,y):
    print(x,y)

screen.onscreenclick(get_mouse_click_coor)
#___________________________________________________________


data = pandas.read_csv('50_states.csv')

#list with states' names
column_name_state = data['state']
all_state_list = column_name_state.to_list()
print(all_state_list)

guessed_states_list = []#empty list for player states, which guessed

# game_is_on = True
# while game_is_on is True:

#when the user type in a state that is inside that csv, that state should be written onto the screen at the location where it exists
while len(guessed_states_list) < 50:
    #ask player for answer
    player_answer = screen.textinput(title=f"Guess the State {len(guessed_states_list)}/50", prompt="What's another state's name? Or write 'exit' to exit game").title()

    #coordinates for state from player_answer
    row_state =  data[data['state'] == player_answer]
    # x_coor = int(row_state.x)#it make bugs
    # y_coor = int(row_state.y)#it make bugs
    
    #write answer on screen
    if player_answer == 'Exit':#all player answer are title!!!
        #create new list with missed states
        #all_state_list - guessed_states_list = missed_states_list

        # missed_states_list = []
        # for state in all_state_list:
        #     if state not in guessed_states_list:
        #         missed_states_list.append(state)

        #list comprehension____________________________________________
        missed_states_list = [state for state in all_state_list if state not in guessed_states_list]

        save_missed = pandas.DataFrame(missed_states_list)
        save_missed.to_csv('missed_states.csv')
        break
    if player_answer in all_state_list:
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x=int(row_state.x), y=int(row_state.y))
        # state_turtle.write(player_answer)
        state_turtle.write(row_state.state.item()) #'Alabama'
        guessed_states_list.append(player_answer)
        print(guessed_states_list)


screen.mainloop()#screen is showed
# screen.exitonclick()
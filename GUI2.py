import PySimpleGUI as SG


def get_data():
    """
    Allow the user to input data
    """
    answer = False
    valid = False
    SG.theme('LightBlue3')  # Window Design
    # Questions to ask user
    layout = [[SG.Text('Wellness Log')],
              [SG.Text("1.How are you feeling: Enter *good*, *bad*, or *okay*"), SG.InputText()],
              [SG.Text("2.Have you eaten enough today? (yes/no)"), SG.InputText()],
              [SG.Text("3.Have you drunk enough water? (yes/no)"), SG.InputText()],
              [SG.Text("4.How many times did you press snooze?"), SG.InputText()],
              [SG.Text("5.Did you leave the house today? (yes/no)"), SG.InputText()],
              [SG.Text("6.Did you go for walk/spend time outside? (yes/no)"),
               SG.InputText()], [SG.Text("7.How has your day been from a scale of 1-10?"), SG.InputText()],
              [SG.Text("8.List 3 things that were good about today:"), SG.InputText()],
              [SG.Text("9.Note 1 thing you would change:"), SG.InputText()], [SG.Text(size=(40, 1), key='-OUTPUT-')],
              [SG.Button('Ok'), SG.Button('Cancel')]]

    # Window Creation
    window = SG.Window('Window Title', layout)
    # Get all answers from the user
    while True:
        event, values = window.read()
        if event == SG.WIN_CLOSED or event == 'Cancel':  # if window is closed cancelled
            break
        mood, eaten, water, snooze, house, walk, = values[0], values[1], values[2], values[3], values[4], values[5]
        scale, threegood, onechange = values[6], values[7], values[8]
        window['-OUTPUT-'].update("Daily Log Complete!")
        answer = True
        valid = True
        scaledummy = 100
        if not (mood == "bad" or mood == "good" or mood == "okay"):
            valid = False
            print("Question 1 inputted incorrectly, write *yes* or *no*")
        if not (eaten == "yes" or eaten == "no"):
            valid = False
            print("Question 2 inputted incorrectly, write *yes* or *no*")
        if not (water == "yes" or water == "no"):
            valid = False
            print("Question 3 inputted incorrectly, write *yes* or *no*")
        try:
            x = int(snooze)
        except ValueError:
            valid = False
            print("Question 4 inputted incorrectly, make sure it's a number!")
        if not (house == "yes" or house == "no"):
            valid = False
            print("Question 5 inputted incorrectly, write *yes* or *no*")
        if not (walk == "yes" or walk == "no"):
            valid = False
            print("Question 6 inputted incorrectly, write *yes* or *no*")
        try:
            scaledummy = int(scale)
        except ValueError:
            valid = False
            print("Question 7 inputted incorrectly, make sure it's a number!")
        if not 10 >= scaledummy >= 1:
            valid = False
            print("Question 7 inputted incorrectly, make sure it's a number between 1-10!")
        window.close()

    if answer and valid:
        return [mood, eaten, snooze, house, walk, scale, threegood, onechange]
    elif answer:
        return "Invalid Input, please try again"
    else:
        return "Please input information"

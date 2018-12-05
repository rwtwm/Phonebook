from GetData import getPhonebookData
import ModifyData
import pbui

#displays a single entry from the phonebook
def display_entry(entry):
    print("Name: {}".format(entry["name"]))
    print("Address: {}".format(entry["address"]))
    print("Phone Number: {}".format(entry["phone_number"]))
    print()

def show_list(data):
    for item in data:
        display_entry(item)

class phonebook:
    data = []
    unfilteredData = []
    
    def __init__(self):
        self.data = getPhonebookData()
        self.unfilteredData = self.data

    def reset_filters(self):
        self.data = self.unfilteredData


def runPhonebook():
    myPb = phonebook()
    running = True
    print("Welcome to 'phonebook'")

    while(running):    
        pbui.prompt_input()
        nextAction = pbui.parse_input(input(">"))
        if (nextAction == []):
            pbui.print_error()
        else:
            if (nextAction[0] == "exit"):
                running = False
            if (nextAction[0] == "show"):
                show_list(myPb.data)
            if (nextAction[0] == "help"):
                pbui.prompt_help()
            if (nextAction[0] == "reset"):
                myPb.reset_filters()
            #use an [x] in the second field to bail out
            if (nextAction[0] == "sort"):
                if (nextAction[1] != "x"):
                    myPb.data = ModifyData.sort(myPb.data, nextAction[1])
            if (nextAction[0] == "search"):
                if (nextAction[1] != "x"):
                    myPb.data = ModifyData.filter_data(myPb.data, nextAction[1], nextAction[2])
        
        
        
            
        
    



runPhonebook()



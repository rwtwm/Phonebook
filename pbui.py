validKeys = {"1":"name", "2":"address", "3":"phone_number", "4":"last_name", "5":"first_name"}
validWords = ["show", "search", "sort", "reset", "exit", "help"]

def prompt_input():
    print("please type your next action")
    print("type 'help' for list of actions")

def prompt_help():
    print("The following actions are available:")
    print("'show' - shows current phone list")
    print("'search' - triggers filter mode")
    print("'sort' - sorts the current filter list")
    print("'reset' - resets the data to its initial state")
    print("'exit' - exits the program")

def filter_help():
    print("type [num] [term] to filter:")
    print("1 - filters by name")
    print("2 - filters by address")
    print("3 - filters by phone number")
    print("4 - filters by last name")
    print("5 - filters by first name")
    print("other input - cancels filtering")

def sort_help():
    print("type [num] to sort:")
    print("1 - sorts by name")
    print("2 - sorts by address")
    print("3 - sorts by phone number")
    print("4 - sorts by last name")
    print("5 - sorts by first name")
    print("other input - cancels sort")

def print_error():
    print("command not recognised, type help for more info")

def get_search_term():
    term = ""
    while term == "":
        print("please enter a search term")
        term = input(">")

    return term

def parse_input(inputStr):
    actionWords = []
    inputWords = inputStr.split()

    if (inputWords[0].lower() in validWords):
        actionWords.append(inputWords[0].lower())       
    else:
        return []

    if (actionWords[0] == "search"):
        filter_help()
        filterAction = input(">").split()
        if filterAction[0] not in validKeys:
            actionWords.append("x")
        else:
            actionWords.append(validKeys[filterAction[0]])
            if len(filterAction) > 1:
                actionWords.append(filterAction[1])
            else:
                actionWords.append(getSearchTerm)
            
    if actionWords[0] == "sort":
        sort_help()
        sortAction = input(">").split()
        if sortAction[0] in validKeys:
            actionWords.append(validKeys[sortAction[0]])
        else:
            actionWords.append("x")    
    
    
    return actionWords

    
    
    
    
    

# Ruba Ismail
# Apr 11 2024


# loops 3 times to get two categories and their target values.
def load_goals(goals):


    print("Set your goals for the week!\n")

    for i in range (3):

        CAT_i = str(input("Enter a category for your goal:\n"))
        target = int(input("Enter your target for " +CAT_i+ ":\n"))

        goals[CAT_i] = target
    

def load_data():

    daily = {}

    print("Enter your data with the category and measurement.")
    print("Type 'done' when done for today.")

    category = str(input("Enter category:\n")) 

    while (category != "done"):

        value = int(input("Enter value:\n"))

        if category in daily: #if the value is in the dictionary
        
            print("You have a value for",category)
            print("Do you want to (1) Add to",category,"or (2) Replace",category+"?")
            choice = int(input())
        
            if (choice == 1):
                daily[category] += value

            elif (choice ==2): 
                daily[category] = value

        else: #value isnt in dictionary
            daily[category] = value

        category = str(input("Enter category:\n"))


    return daily

  
# Fuctions returns 0 if goals are not met, returns 1 if the goals are met.
def compare_goals(goals,daily):

    for key in goals:
        
        if key not in daily:
            return 0
        
        elif daily[key]<goals[key]:
            return 0

    return 1
        

# Prints each day and calls the function to enter the value for each day.
# Then runs the compare_goals function to save it into how many goals met.
def main():

    goals = {}
    total_met_goals = 0

    load_goals(goals)

    print("it's Monday!")
    daily = load_data()
    total_met_goals += compare_goals(goals,daily)

    print("it's Tuesday!")
    daily = load_data()
    total_met_goals += compare_goals(goals,daily)

    print("it's Wednsday!")
    daily = load_data()
    total_met_goals += compare_goals(goals,daily)
    
    print("it's Thursday!")
    daily = load_data()
    total_met_goals += compare_goals(goals,daily)

    print("it's Friday - Happy Friday!")
    daily = load_data()
    total_met_goals += compare_goals(goals,daily)

    print("it's Saturday!")
    daily = load_data()
    total_met_goals += compare_goals(goals,daily)

    print("it's Sunday!")
    daily = load_data()
    total_met_goals += compare_goals(goals,daily)


    print("You hit your goals",total_met_goals,"times this week!")

main()

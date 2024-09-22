task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match time_bound:
    case 'yes':
        print("Reminder: '{0}' is a {1} priority task that requires immediate attention today!".format(task, priority))
    case 'no':
        print("Note: '{0}' is a {1} priority task. Consider completing it when you have free time.".format(task, priority))

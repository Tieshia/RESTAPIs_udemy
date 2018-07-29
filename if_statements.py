# should_continue = True
# if should_continue:
#     print("Hello")

'''
known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

if person in known_people:
    print("You know {}.".format(person))
else:
    print("You don't know {}.".format(person))
'''

## Exercise
def who_do_you_know():
    # Ask user for a list of people they know
    # Split string into list
    people = input("Enter the names of people you know, separated by commas: ")
    people = people.split(', ')
    return people

def ask_user():
    # Ask user for a name
    # See if their name is in the list of people they know
    # Print out that they know the person

    person = input("Enter the person you know: ")
    if person in who_do_you_know():
        print("You know {}.".format(person))
    else:
        print("You don't know {}.".format(person))

ask_user()
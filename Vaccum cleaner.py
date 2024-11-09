def vacuum_world():

    # Initializing goal_state

    # 0 indicates Clean and 1 indicates Dirty

    goal_state = {'A': '0', 'B': '0'}

    cost = 0



    # User input for the location of the vacuum

    location_input = input("Enter Location of Vacuum (A/B): ").upper()

    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ")

    # Determine the other location's status based on user input

    other_location = 'B' if location_input == 'A' else 'A'

    status_input_complement = input(f"Enter status of {other_location} (0 for Clean, 1 for Dirty): ")



    print("Initial Location Condition:", goal_state)



    if location_input == 'A':

        print("Vacuum is placed in Location A")

        if status_input == '1':

            print("Location A is Dirty.")

            # Clean Location A

            goal_state['A'] = '0'

            cost += 1  # Cost for sucking

            print("Cost for CLEANING A:", cost)

            print("Location A has been Cleaned.")



        if status_input_complement == '1':

            print("Location B is Dirty.")

            print("Moving right to Location B.")

            cost += 1  # Cost for moving right

            print("COST for moving RIGHT:", cost)

            # Clean Location B

            goal_state['B'] = '0'

            cost += 1  # Cost for sucking

            print("COST for SUCK:", cost)

            print("Location B has been Cleaned.")

        else:

            print("Location B is already clean.")



    else:  # If the vacuum is placed in Location B

        print("Vacuum is placed in Location B")

        if status_input == '1':

            print("Location B is Dirty.")

            # Clean Location B

            goal_state['B'] = '0'

            cost += 1  # Cost for sucking

            print("COST for CLEANING B:", cost)

            print("Location B has been Cleaned.")



        if status_input_complement == '1':

            print("Location A is Dirty.")

            print("Moving LEFT to Location A.")

            cost += 1  # Cost for moving left

            print("COST for moving LEFT:", cost)

            # Clean Location A

            goal_state['A'] = '0'

            cost += 1  # Cost for sucking

            print("COST for SUCK:", cost)

            print("Location A has been Cleaned.")

        else:

            print("Location A is already clean.")



    # Done cleaning

    print("GOAL STATE:", goal_state)

    print("Performance Measurement:", cost)



# Call the function

vacuum_world()

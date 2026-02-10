def shutdown(user):
    if user == "Yes":
        print("Shutting down")
    elif user == "No":
        print("Abort Shut Down")
    else:
        print("Sorry")
response = input("Do you want to shut down. Yes or No?")
shutdown(response)

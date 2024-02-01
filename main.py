phone = {}

while True:
    print("The Phone Book\n 1. Add a contact\n 2. Look for a number\n "
          "3. Delete a contact\n 4. Display all contacts\n 5. Quit the program")

    choice = input("Please enter the number corresponding your choice: ")

    if choice == "1":
        add_name = input("Please enter contact name: ")
        add_number = input("Please enter contact number: ")
        phone[add_name] = add_number
        print("Nice! New Achievement Unlocked: Friends!")
    elif choice == "2":
        search_name = input("Please enter contact name:")
        if search_name in phone:
            print(f"{search_name}'s number is {phone[search_name]}")
            continue
        print("Contact doesn't exist, probably because you don't have friends!")
    elif choice == "3":
        delete_name = input("Please enter contact name:")
        if delete_name in phone:
            phone.pop(delete_name)
            print("Go into depression now, you lost a friend! Nice!")
            continue
        print("Contact doesn't exist, probably because you don't have friends!")
    elif choice == "4":
        for i in phone:
            print(f"{i} - {phone[i]}")
    elif choice == "5":
        break
    else:
        print("Invalid choice, you dumb motherfucker")

while(True):
    print("Select an option: (A) Weight (B) CBM (X) Exit")
    option = input("Option: ").capitalize()

    if option == "A":
        kg = int(input("Enter weght in kg: "))
        print(f"Weight: {kg * 2.2:.2f} lbs")
        # kg * 2.2, format 2 decimal places

    elif option == "B":
        cbm = int(input("Enter CBM: "))
        print(f"CBM: {cbm * 35.15:.2f}")
        # cbm * 35.15, format 2 decimal places

    elif option == "X":
        break

    else:
        print("Invalid option\n")
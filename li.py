li = [1,1,2,3,4,5]

while True:
    print("\n LIST OPERATIONS ")
    print("1. Display List")
    print("2. Insert at specific position")
    print("3. Pop from specific position")
    print("4. Sort in ascending order")
    print("5. Sort in descending order")
    print("6. Find minimum element")
    print("7. Find maximum element")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("List:", li)

    elif choice == 2:
        element = int(input("Enter element: "))
        position = int(input("Enter position: "))
        li.insert(position, element)
        print("Element inserted successfully.")
        print("List:", li)

    elif choice == 3:
        position = int(input("Enter position: "))
        if 0 <= position < len(li):
            removed = li.pop(position)
            print("Removed element:", removed)
            print("List:", li)
        else:
            print("Invalid position.")

    elif choice == 4:
        li.sort()
        print("List in ascending order:", li)

    elif choice == 5:
        li.sort(reverse=True)
        print("List in descending order:", li)

    elif choice == 6:
        print("Minimum element:", min(li))

    elif choice == 7:
        print("Maximum element:", max(li))

    else:
        print("Invalid choice.")
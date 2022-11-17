print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
print("🌸  Welcome to the Shopping Cart Program! 🌸\n🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
print("-----------------------------------------------------------------------")
items = []
prices = []

client = 0
while client != 5: #Asking the user until it choose 5
    print("✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ \n       Please select one of the following: \n✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦")
    print("\n   1. Add item \n   2. View cart \n   3. Remove item \n   4. Compute total \n   5. Quit")

    client = int(input("Please enter an action: "))
    print()

    if client == 1: #add item
        add_item = input("What item would you like to add?: ")
        add_price = float(input(f"What is the price of '{add_item}'?: $"))
        items.append(add_item)
        prices.append(add_price)
        print(f"✅ '{add_item}' has been added to the cart.")
        print()

    elif client == 2: #view cart
        print("📃 The contents of the shopping cart are:")
        for i in range(len(items)):
            item_name = items[i]
            price = prices[i]
            
            print(f"    {i + 1}). {item_name:<10}- ${price:<5.2f}".format())
            # print(f"    {i + 1}). {item_name} -  ${price:.2f}")
        print()
    
    elif client == 3: #remove item
        print(f"You have {len(items)} items in the list.")
        
        remove = int(input("Which item would you like to remove? "))
        
        if remove < len(items):
            items.pop(remove - 1) 
            prices.pop(remove - 1) 
            print(f"✅ Item {remove} removed")
        else:
            print("❌ Invalid choice")       
         
        print()

    elif client == 4: #compute total
        total = 0
        for j in prices:
            total += j
        print(f"🛒 The total price of the {len(items)} items in the shopping cart is: ${total:.2f}")
        print()

    elif client != 5 :
        print("❌ You did not enter a correct action. Try again.")
        print()


print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
print("🌸   Thank you! Goodbye.    🌸")
print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
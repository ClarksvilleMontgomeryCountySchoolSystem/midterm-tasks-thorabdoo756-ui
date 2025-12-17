def main():
    print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg................$29.99
Phoenix Feather............$9.99
Magic Wand................$19.99
Potion of Healing..........$4.99
""")

    # Collect purchase info
    item = input("Dragon Egg x5 @ 30$ each")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity (minimum 3): "))

    # Calculate subtotal, tax, and total
    subtotal = price * quantity
    tax = subtotal * 0.095   # 9.5% tax
    total = subtotal + tax

    # Round total to 2 decimal places
    total = round(total, 2)

    # Print receipt
    print("--------------------------")
    print(f"{item} x{quantity} @ ${price}")
    print("--------------------------")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${round(tax, 2)}")
    print(f"Total: ${total}")

    print("\nThank you for shopping at\nthe Peculiar Emporium!")

if __name__ == "__main__":
    main()

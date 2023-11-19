def fractional_knapsack(items,capacity):
    
    items.sort(key=lambda x:x['profit']/x['weight'] , reverse=True)  # sort items acc. to their P/W ratio
    
    max_profit=0.0
    selected_items =[]

    for item in items:
        if item['weight'] <= capacity:
            selected_items.append(item)
            max_profit += item['profit']
            capacity -= item['weight']

        else:
            fraction = capacity/item['weight']
            selected_items.append(item)
            item["fraction"] = fraction
            max_profit += item['profit']*fraction
            break
        
    return max_profit, selected_items


def main():

    items = []

    n= int(input("Enter total no. of items: "))
    ks_capacity = int(input("Enter ks capacity: "))

    for i in range(n):
        name = input("\nEnter item name: ")
        weight = int(input("Enter item weight: "))
        profit = int(input("Enter item profit: "))

        item = {"name":name,"weight":weight,"profit":profit}
        items.append(item)
    
    max_profit,selected_items = fractional_knapsack(items,ks_capacity)
    
    print("\nThe selected items are: ")
    for item in selected_items:
        if "fraction" in item:
            print(f"{item['name']} => {item['fraction']}")
        else:
            print(f"{item['name']} => 1.0")

    print("\nThe maximum profit earned is: ", max_profit)



main()


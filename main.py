import json
import matplotlib.pyplot as plt

def add_transaction(date, amount, category, t_type, description, file='data.json'):
    transaction = {
        "date": date,
        "amount": amount,
        "category": category,
        "type": t_type,
        "description": description
    }

    # Load existing data
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"transactions": []}

    # Add new transaction
    data['transactions'].append(transaction)

    # Save updated data
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

    print("Transaction added successfully!")

def read_transactions(file='data.json'):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data['transactions']
    except FileNotFoundError:
        print("No data found! Starting fresh.")
        return []

def generate_summary(file='data.json'):
    transactions = read_transactions(file)
    summary = {}

    for transaction in transactions:
        if transaction['type'] == 'expense':
            category = transaction['category']
            summary[category] = summary.get(category, 0) + transaction['amount']

    return summary

def plot_summary(file='data.json'):
    summary = generate_summary(file)
    if not summary:
        print("No expense data to visualize!")
        return

    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Amount Spent')
    plt.title('Expense Summary')
    plt.show()

def main():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add a Transaction")
        print("2. View Transactions")
        print("3. Generate Expense Summary")
        print("4. Visualize Expense Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            t_type = input("Enter type (income/expense): ")
            description = input("Enter description: ")
            add_transaction(date, amount, category, t_type, description)
        
        elif choice == '2':
            transactions = read_transactions()
            for t in transactions:
                print(t)
        
        elif choice == '3':
            summary = generate_summary()
            for category, amount in summary.items():
                print(f"{category}: ${amount:.2f}")
        
        elif choice == '4':
            plot_summary()
        
        elif choice == '5':
            print("Exiting. Have a great day!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Personal Finance Tracker

A simple, user-friendly personal finance tracker built with Python and JSON. This application helps you manage your finances by recording transactions, generating summaries, and visualizing your expenses. 

---

## Features

- **Track Transactions**: Add and manage your income and expenses.
- **Category Summaries**: View total expenses per category.
- **Visualizations**: Generate bar charts to analyze your spending habits.
- **Lightweight Data Storage**: Store data in a JSON file for simplicity and portability.

---

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or above
- `pip` (Python package manager)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/personal-finance-tracker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd personal-finance-tracker
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. (Optional) Create an empty `data.json` file:
    ```bash
    echo '{ "transactions": [] }' > data.json
    ```

---

## Usage

1. Run the program:
    ```bash
    python main.py
    ```
2. Follow the menu prompts to:
    - Add a transaction
    - View all transactions
    - Generate a summary of expenses
    - Visualize your spending with a bar chart

---

## Example

### Adding a Transaction

```plaintext
--- Personal Finance Tracker ---
1. Add a Transaction
2. View Transactions
3. Generate Expense Summary
4. Visualize Expense Summary
5. Exit
Enter your choice: 1
Enter the date (YYYY-MM-DD): 2024-12-01
Enter the amount: 50
Enter the category: Food
Enter type (income/expense): expense
Enter description: Lunch
Transaction added successfully!
```

### Expense Visualization

![Expense Summary Chart](example_chart.png)

---

## File Structure

```plaintext
personal-finance-tracker/
├── main.py          # Main script to run the tracker
├── data.json        # JSON file to store transactions
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with your suggestions or enhancements.

1. Fork the repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add your descriptive commit message"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

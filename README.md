# 💰 Personal Finance Tracker

This is a simple **Personal Finance Tracker** built using Python. It allows users to:

- Record income and expense transactions.
- View summaries within a selected date range.
- Visualize financial trends over time using line plots.

This app uses CSV for data storage and provides a basic command-line interface (CLI).

---

## 📦 Features

- ✅ Add new transactions (Income or Expense)
- ✅ View transactions within a date range
- ✅ Summary report showing:
  - Total Income
  - Total Expenses
  - Net Savings
- ✅ Line plot visualization of income and expense over time
- ✅ Stores data in a CSV file for easy access and portability

---

## 🛠️ Technologies Used

- **Python** (Standard Library)
- **Pandas** for data manipulation
- **Matplotlib** for visualization
- **CSV** module for file handling

---

## 📁 Project Structure

```
personal_finance_tracker/
│
├── personal_finance_tracker.py        # Main application file
├── data_entry.py             # User input validation functions
├── finance_data.csv          # CSV file to store transactions
└── README.md                 # Project documentation
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AustinMusuya/personal_finance_tracker.git
cd personal_finance_tracker
```

### 2. Install Dependencies

All dependencies are standard Python libraries. However, make sure you have `pandas` and `matplotlib` installed:

```bash
pip install requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

---

## 🧑‍💻 How to Use

### ➕ Add a Transaction

1. Choose option `1` in the menu.
2. Enter the date in `dd/mm/yyyy` format or press `Enter` for today's date.
3. Enter the amount (positive number).
4. Select the category: `I` for Income or `E` for Expense.
5. Enter an optional description.

### 📊 View Transactions and Summary

1. Choose option `2` in the menu.
2. Enter the start and end dates in `dd/mm/yyyy` format.
3. A table of filtered transactions and summary is shown.
4. Optionally, visualize income/expenses over time using a line chart.

### ❌ Exit

- Choose option `3` to exit the program.

---

## 📌 Example Transaction

```
Date: 06/04/2025
Amount: 5000
Category: I
Description: Freelance project
```

---

## 📈 Visualization Example

- Green Line: Income
- Red Line: Expenses
- X-axis: Date
- Y-axis: Amount

A helpful visual to monitor your spending/saving habits!

---

## 🧪 Future Improvements

- Category breakdown pie chart
- Monthly or weekly summaries
- Export to PDF
- GUI version using Tkinter or PyQt

---

## 👨‍💻 Author

**Austin Musuya**

---

## 📃 License

This project is licensed under the MIT License. You’re free to use, modify, and distribute it as you like.

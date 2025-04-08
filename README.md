# 💰 Personal Finance Tracker

This is a simple **Personal Finance Tracker** built using Python. It allows users to:

- Record income and expense transactions.
- View summaries within a selected date range.
- Visualize financial trends over time using line plots.
- Upload financial data to **Azure Lakehouse** for advanced analysis and reporting.

This app uses **CSV** for data storage and provides a basic command-line interface (CLI).

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
- ✅ Uploads financial data to **Azure Lakehouse** for advanced analysis

---

## 🛠️ Technologies Used

- **Python** (Standard Library)
- **Pandas** for data manipulation
- **Matplotlib** for visualization
- **CSV** module for file handling
- **Azure SDK** (`azure-identity`, `requests`) for file upload to Azure Lakehouse

---

## 📁 Project Structure

```
personal-finance-tracker/
│
├── main.py              # Main application file
├── data_entry.py        # User input validation functions
├── finance_data.csv     # CSV file to store transactions
├── upload_to_fabric.py  # Script to upload data to Azure Lakehouse
└── README.md            # Project documentation
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AustinMusuya/personal-finance-tracker.git
cd personal-finance-tracker
```

### 2. Install Dependencies

All dependencies are standard Python libraries. However, make sure you have `pandas`, `matplotlib`, and `requests` installed:

```bash
pip install pandas matplotlib requests azure-identity
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

### 📊 View Expense and Summary

1. Choose option `3` in the menu.
2. Enter the start and end dates in `dd/mm/yyyy` format.
3. A table of filtered transactions and summary is shown.
4. Optionally, visualize income/expenses over time using a pie chart.

### ❌ Exit

- Choose option `4` to exit the program.

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

---

## 📤 Upload Data to Azure Lakehouse

The `upload_to_fabric.py` script allows you to upload your CSV data to an Azure Lakehouse for advanced analysis.

### 1. Update the script with your Lakehouse URL

In the `upload_to_fabric.py` file, set the `lakehouse_url` to point to your Azure Lakehouse and adjust the local file path (`local_file`) if needed.

```python
lakehouse_url = "https://onelake.dfs.fabric.microsoft.com/YourWorkspace.YourLakehouse.Lakehouse/files/finance_data.csv"
local_file = "./finance_data.csv"  # adjust path if needed
```

### 2. Run the Script

```bash
python upload_to_fabric.py
```

This will upload the data to Azure Lakehouse for further analysis and visualization in a notebook.

---

## 🧑‍💻 Further Analysis in Azure Notebook

Once the data is uploaded to the Lakehouse, you can use **Azure Synapse Analytics** or **Azure Data Explorer** to run analytics on your data. Follow these steps:

1. Open your Lakehouse in **Azure Synapse Studio** or **Azure Data Explorer**.
2. Create a new notebook.
3. Load the `finance_data.csv` file from the Lakehouse.
4. Perform your desired analysis using SQL, Spark, or Python-based notebooks.

For example, you can analyze spending trends, categorize expenses, or create advanced visualizations using Python and libraries like `pandas`, `matplotlib`, and `seaborn`.

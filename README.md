# ExpenseTracker

A comprehensive web application built with Django to track personal finances, analyze spending patterns, forecast expenses, and scan receipts.

## Features

- **Expense Management**: Track and categorize your expenses
- **Income Tracking**: Monitor your sources of income
- **Receipt Scanning**: Upload and automatically extract information from receipt images
- **Expense Forecasting**: Predict future expenses based on historical data
- **Anomaly Detection**: Identify unusual spending patterns
- **Financial Goals**: Set and track savings goals
- **Data Visualization**: View reports and charts of your spending habits
- **User Authentication**: Secure account management

## Technology Stack

- Django (Python web framework)
- SQLite database (included)
- Bootstrap for frontend
- Chart.js for data visualization
- OCR for receipt scanning (Tesseract)
- NLTK for text processing
- Scikit-learn for machine learning components

## Setup Instructions

### Prerequisites

- Python 3.8+ installed
- Git
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
  - Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki)
  - macOS: `brew install tesseract`
  - Linux: `sudo apt install tesseract-ocr`

### Installation

1. Clone the repository
   ```
   git clone https://github.com/YOUR-USERNAME/ExpenseTracker.git
   cd ExpenseTracker
   ```

2. Create and activate a virtual environment (optional but recommended)
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Download NLTK data (required for text analysis)
   ```
   python download_nltk_data.py
   ```

5. Run migrations (the database is already included, but if needed)
   ```
   python manage.py migrate
   ```

6. Run the development server
   ```
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`

### Default Admin Account (if included in the database)

- Username: admin
- Password: admin

## Usage

1. Register a new account or log in
2. Set up your currency preference
3. Add your income sources
4. Start tracking expenses
5. Upload receipts for automatic expense entry
   - The system uses OCR to extract date, amount, and description from receipts
   - Machine learning is used to categorize expenses automatically
6. Set financial goals
7. Analyze your spending patterns in the dashboard
8. Generate reports

## Receipt Scanner

The receipt scanning feature uses Tesseract OCR to extract information from uploaded receipt images:

- Supported image formats: JPG, PNG
- Best results with clear, well-lit images
- The system will attempt to extract:
  - Total amount
  - Date (or use current date if not found)
  - Description (items purchased)
  - Category (automatically predicted)

## Database

The project includes a SQLite database with sample data. If you want to start fresh:

1. Delete the `db.sqlite3` file
2. Run `python manage.py migrate` to create a new database
3. Create a superuser: `python manage.py createsuperuser`

## Migrating to a New System

When cloning this project to another laptop:

1. Clone the repository using Git
2. Install all prerequisites (Python, Tesseract OCR)
3. Set up the virtual environment and install dependencies
4. The database file (db.sqlite3) is included and will be cloned with your repository
5. All your financial data will be preserved in the cloned database

## License

[Insert your license information here]

## Contributors

[Your name or team information] 
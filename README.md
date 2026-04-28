# 🚀 Selenium Test Automation Framework

## 📌 Project Overview
This project is a web UI test automation framework built using Python, Selenium WebDriver and PyTest. It follows the Page Object Model (POM) design pattern for better maintainability and reusability. It also supports reporting, logging, screenshots and CI/CD integration using GitHub Actions.

## ⚙️ Features
- Page Object Model (POM) architecture
- Automated login test cases (valid and invalid)
- PyTest test execution
- HTML reports generation
- Screenshot capture on failure
- Logging system for debugging
- CI/CD pipeline using GitHub Actions

## 🛠 Tech Stack
Python, Selenium WebDriver, PyTest, PyTest HTML, GitHub Actions, VS Code

## ▶️ How to Run

Install dependencies:
pip install -r requirements.txt

Run tests:
pytest

Run with HTML report:
pytest --html=reports/report.html --self-contained-html

## 📸 Screenshot Feature
Automatically captures screenshots on test failure and saves them in the screenshots folder.

## 📊 Reports
HTML report will be generated in:
reports/report.html

## 🔄 CI/CD
GitHub Actions runs tests automatically on every push to main branch.

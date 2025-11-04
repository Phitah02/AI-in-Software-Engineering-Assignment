# AI in Software Engineering Assignment

## Overview
This repository contains the deliverables for the AI in Software Engineering assignment, focusing on practical applications of AI in software development, testing, predictive analytics, and ethical considerations. The assignment explores how AI tools can enhance development efficiency, automate testing, enable predictive modeling, and address ethical challenges in AI deployment.

## Assignment Structure

### Part 1: Theoretical Analysis
- **Short Answer Questions**: Covering AI-driven code generation, supervised vs. unsupervised learning in bug detection, and bias mitigation in UX personalization.
- **Case Study Analysis**: Examining AIOps for automating deployment pipelines, with examples of predictive incident management and automated resource optimization.

### Part 2: Practical Implementation

#### Task 1: AI-Powered Code Completion
- **Objective**: Compare manual and AI-generated implementations for sorting dictionaries.
- **Deliverables**:
  - `manual_implementation.py`: Custom bubble sort algorithm.
  - `ai_implementation.py`: Python's built-in `sorted()` with lambda.
  - `comparison_report.md`: Efficiency analysis showing AI implementation is ~7.5x faster due to Timsort (O(n log n) vs. O(n²)).
  - `comparison_notebook.ipynb`: Jupyter notebook with detailed analysis.

#### Task 2: Automated Testing with AI
- **Objective**: Implement automated login testing using Selenium WebDriver.
- **Deliverables**:
  - `test_login.py`: Test script for valid and invalid login scenarios.
  - `valid_login_success.png`: Screenshot of successful login.
  - `invalid_login_error.png`: Screenshot of login error.
  - `report.html`: Test execution report.
  - `README.md`: Summary on AI's role in improving test coverage (150-word summary).

#### Task 3: Predictive Analytics for Resource Allocation
- **Objective**: Build a predictive model for breast cancer diagnosis to prioritize cases (high/medium/low).
- **Deliverables**:
  - `predictive_analysis.py`: Feature extraction, model training (Random Forest), and evaluation.
  - `predictive_analytics.ipynb`: Jupyter notebook with data exploration, visualizations, and model performance.
  - Dataset: `iuss-23-24-automatic-diagnosis-breast-cancer/` (from Kaggle competition).
  - Features: Area, mean intensity, std intensity, height, width, total pixels.
  - Performance: Validation F1-Score ~0.85, Test F1-Score ~0.82.

### Part 3: Ethical Reflection
- **Objective**: Discuss biases in the predictive model and mitigation using IBM AI Fairness 360.
- **Deliverables**:
  - `Ethical reflection.md`: Analysis of demographic underrepresentation, data collection biases, and AIF360 tools for detection/mitigation.

## Additional Deliverables
- `Theoretical analysis.md`: Comprehensive answers to theoretical questions and case study.
- `AI in Software Engineering Assignment.pdf`: Full assignment document with all parts.

## Key Insights
- **AI Efficiency**: AI-generated code (e.g., using built-in functions) outperforms manual implementations in performance and maintainability.
- **Testing Automation**: AI enhances test coverage by generating diverse scenarios and prioritizing critical paths.
- **Predictive Modeling**: Random Forest achieves high accuracy in medical diagnosis, but requires ethical oversight.
- **Bias Mitigation**: Tools like AIF360 are essential for fair AI, addressing demographic disparities and ensuring equitable outcomes.

## Technologies Used
- **Programming**: Python, Jupyter Notebook
- **Libraries**: scikit-learn, OpenCV, Selenium, Matplotlib, Seaborn, Pandas
- **Tools**: GitHub Copilot (for code generation), IBM AI Fairness 360 (for bias analysis)
- **Dataset**: Kaggle "IUSS 2023-2024 Automatic Diagnosis of Breast Cancer"

## Author
Peter Kamau Mwaura

## Repository Structure
```
.
├── README.md
├── AI in Software Engineering Assignment.pdf
├── Ethical reflection.md
├── Theoretical analysis.md
├── Task 1/
│   ├── ai_implementation.py
│   ├── comparison_notebook.ipynb
│   ├── comparison_report.md
│   └── manual_implementation.py
├── Task 2/
│   ├── geckodriver.exe
│   ├── invalid_login_error.png
│   ├── README.md
│   ├── report.html
│   ├── test_login.py
│   └── valid_login_success.png
└── Task 3/
    ├── predictive_analysis.py
    ├── predictive_analytics.ipynb
    └── iuss-23-24-automatic-diagnosis-breast-cancer/
```

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
- Dataset: `Task 3/iuss-23-24-automatic-diagnosis-breast-cancer/` obtained from Kaggle Breast Cancer Dataset (https://www.kaggle.com/competitions/iuss-23-24-automatic-diagnosis-breast-cancer/data).
  - Features: Area, mean intensity, std intensity, height, width, total pixels.
  - Performance: Validation F1-Score ~0.85, Test F1-Score ~0.82.

### Part 3: Ethical Reflection
- **Objective**: Discuss biases in the predictive model and mitigation using IBM AI Fairness 360.
- **Deliverables**:
  - `Ethical reflection.md`: Analysis of demographic underrepresentation, data collection biases, and AIF360 tools for detection/mitigation.

## Additional Deliverables
- `Theoretical analysis.md`: Comprehensive answers to theoretical questions and case study.
- `AI in Software Engineering Assignment.pdf`: Full assignment document with all parts.

## Proposal: AI-Powered Code Review Mentor (AICRM)
### Purpose
Software engineering teams often struggle with maintaining consistent, high-quality code reviews, especially in distributed or fast-paced environments. Traditional static analysis tools catch syntax or style issues but fail to provide context-aware, educational feedback that helps developers grow.

The AI-Powered Code Review Mentor (AICRM) addresses this gap by combining static analysis with natural language explanations, adaptive learning, and best-practice recommendations. Its goal is not only to flag issues but also to teach developers why something is problematic and suggest better alternatives.

### Workflow
1. **Integration with Version Control**
   - AICRM connects to GitHub/GitLab/Bitbucket pull requests.
   - It scans new commits and identifies code segments requiring review.

2. **Context-Aware Analysis**
   - Uses AI models trained on large-scale open-source repositories and software engineering guidelines.
   - Detects issues beyond syntax: design flaws, inefficient algorithms, security vulnerabilities, and maintainability concerns.

3. **Explanatory Feedback**
   - Provides natural language explanations for each flagged issue.
   - Suggests refactored code snippets and links to relevant documentation or design patterns.

4. **Adaptive Learning**
   - Tracks developer responses (accepted/rejected suggestions).
   - Adapts future feedback to align with the team's coding style and project-specific conventions.

5. **Team Dashboard**
   - Visualizes recurring issues, knowledge gaps, and improvement trends.
   - Helps managers identify training needs and measure code quality evolution.

### Impact
- **Improved Code Quality**: Reduces bugs, vulnerabilities, and technical debt by catching issues early.
- **Developer Growth**: Transforms code reviews into learning opportunities, accelerating junior developer onboarding.
- **Consistency Across Teams**: Ensures uniform coding standards in distributed teams.
- **Time Savings**: Automates repetitive review tasks, freeing senior engineers to focus on architectural and strategic concerns.
- **Scalability**: Adapts to projects of any size, from startups to enterprise-level systems.

### Conclusion
The AI-Powered Code Review Mentor goes beyond traditional static analysis by combining automation, education, and adaptability. It empowers teams to write cleaner, more maintainable code while fostering a culture of continuous learning. By embedding intelligence directly into the review process, AICRM bridges the gap between quality assurance and developer mentorship—a problem not fully addressed by existing tools.

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

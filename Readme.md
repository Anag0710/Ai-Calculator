# AI Calculator

This project is an AI-powered calculator that can perform basic arithmetic operations as well as more advanced mathematical computations. The calculator leverages machine learning algorithms to provide accurate and efficient calculations.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

Here’s the entire project structure in Markdown format:



This project is divided into two main components: **Backend** and **Frontend**. 
Below is the directory structure for each.

---

## Backend: `calc-be-main`

### Directory Structure
```plaintext
calc-be-main/
├── apps/
│   └── calculator/
│       ├── __pycache__/
│       │   ├── route.cpython-313.pyc
│       │   └── utils.cpython-313.pyc
│       ├── route.py
│       └── utils.py
├── venv/
│   ├── Include/
│   ├── Lib/
│   └── Scripts/
├── .gitignore
├── .env
├── constants.py
├── main.py
├── requirements.txt
└── schema.py
```
**Key Files**
- `main.py`: Entry point for the backend.
- `constants.py`: Contains application constants.
- `schema.py`: Defines the data schema.
- `requirements.txt`: Lists Python dependencies for the project.
- `apps/calculator/route.py`: Contains API route logic.
- `apps/calculator/route.py`: Contains API route logic.
- `apps/calculator/utils.py`: Utility functions for calculations.


## Frontend: `calc-fe-main`

### Directory Structure
```plaintext
calc-fe-main/
├── src/
│   ├── assets/
│   │   └── react.svg
│   ├── components/ui/
│   │   └── button.tsx
│   ├── lib/
│   │   └── utils.ts
│   ├── screens/
│   ├── App.css
│   ├── App.tsx
│   ├── constants.ts
│   ├── index.css
│   ├── main.tsx
│   └── vite-env.d.ts
├── public/
│   ├── calculator.png
│   └── vite.svg
├── .env.local
├── .eslint.json
├── .gitignore
├── components.json
├── eslint.config.js
├── index.html
├── package-lock.json
├── package.json
├── postcss.config.js
├── README.md
├── tailwind.config.js
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```
**Key Files**
- `src/App.tsx`: Main application component.
- `src/components/ui/button.tsx`: Reusable UI button component.
- `src/lib/utils.ts`: Helper utility functions.
- `tailwind.config.js`: Configuration for TailwindCSS.
- `vite.config.ts`: Configuration for Vite.js.



## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Advanced mathematical computations: trigonometric functions, logarithms, and exponentiation.
- Machine learning-based predictions for complex calculations.
- User-friendly command-line interface.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Ai-Calculator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Ai-Calculator
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use the AI Calculator, run the following command:
```sh
cd calc-be-main
python main.py

```
```sh
cd calc-fe-main
npm run dev

```

Follow the on-screen instructions to perform calculations.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
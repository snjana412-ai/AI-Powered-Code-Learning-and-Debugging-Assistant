import ast
import random

# 1. Code analysis and explanation
def analyze_code(code):
    try:
        tree = ast.parse(code)
        funcs = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return f"✅ Syntax OK\nFunctions found: {funcs if funcs else 'None'}"
    except SyntaxError as e:
        return f"❌ Syntax Error: {e}"

# 2. Automated error detection and debugging suggestions
def debug_code(code):
    try:
        compile(code, "<string>", "exec")
        return "No syntax errors found."
    except SyntaxError as e:
        return f"Check line {e.lineno}: {e.msg}. Suggestion: Fix missing colons/indentation/parentheses."

# 3. Exercise generation
def generate_exercise(level="easy"):
    exercises = {
        "easy": "Write a function to add two numbers.",
        "medium": "Write a function to count even numbers in a list.",
        "hard": "Write a recursive function to calculate factorial with input validation."
    }
    return exercises.get(level, "Level not found.")

# 4. Interactive tutorial
def tutorial(topic="loops"):
    steps = {
        "loops": [
            "Step 1: A loop repeats code.",
            "Step 2: for i in range(5): print(i)",
            "Step 3: Use break/continue to control loops."
        ],
        "functions": [
            "Step 1: Define a function with def.",
            "Step 2: Functions should return values.",
            "Step 3: Keep functions small and clear."
        ]
    }
    return steps.get(topic, ["No tutorial available."])

# ----------------- DEMO -----------------
sample_code = """
def greet(name):
    print("Hello", name)

greet("World")
"""

print("=== Code Analysis ===")
print(analyze_code(sample_code))

print("\n=== Debug Suggestions ===")
print(debug_code(sample_code))

print("\n=== Exercise Example (medium) ===")
print(generate_exercise("medium"))

print("\n=== Tutorial (functions) ===")
for step in tutorial("functions"):
    print(step)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Dummy explanation logic (can connect to AI later)
def generate_explanation(code):
    return f"Explanation for the given code:\n{code}"

# Home page (open to all users)
def home(request):
    return render(request, 'explainer/home.html')

# AI explanation page (requires login)
@login_required
def explain_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '').strip()
        if not code:
            return render(request, 'explainer/explain.html', {
                'error': 'Please enter some code to explain.'
            })
        explanation = generate_explanation(code)
        return render(request, 'explainer/explain.html', {
            'code': code,
            'explanation': explanation
        })
    return render(request, 'explainer/explain.html')

# History page (requires login)
@login_required
def explanation_history(request):
    history = [
        {"code": "print('Hello')", "explanation": "Prints Hello"},
        {"code": "a = 5 + 3", "explanation": "Adds 5 and 3"},
    ]
    return render(request, 'explainer/history.html', {'history': history})

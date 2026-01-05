from pyscript import document, display

def compute_average(e):
    
    try:
        num1 = int(document.getElementById('science').value)
        num2 = int(document.getElementById('english').value)
        num3 = int(document.getElementById('ict').value)
        num4 = int(document.getElementById('math').value)
        num5 = int(document.getElementById('filipino').value)
        num6 = int(document.getElementById('pe').value)

    except ValueError:
        display("⚠️ Please enter all grades correctly.", target="output")
        return

# Compute average
    average = (num1 + num2 + num3 + num4 + num5 + num6) / 6

    # Determine pass/fail
    if average >= 75:
        result = "Yes!"
    else:
        result = "Nope!"

    # Determine pass/fail
    result = "Yes!" if average >= 75 else "Nope!"

    # Display result
    display(
        f"Your General Weighted Average (GWA) is {round(average, 2)}. "
        f"Did you pass? {result}",
        target="output"
    )

import sys

party_items = [
    "Cake", "Balloons", "Music System", "Lights", "Catering Service", "DJ", 
    "Photo Booth", "Tables", "Chairs", "Drinks", "Party Hats", "Streamers", 
    "Invitation Cards", "Party Games", "Cleaning Service"
]

item_values = [
    20, 21, 10, 5, 8, 3, 15, 7, 12, 6, 9, 18, 4, 2, 11
]

def calculate_party_code(indices):
    selected_values = [item_values[i] for i in indices]
    base_code = selected_values[0]
    for value in selected_values[1:]:
        base_code &= value
    return base_code

def adjust_party_code(base_code):
    if base_code == 0:
        base_code += 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        base_code -= 2
        message = "Let's keep it classy!"
    else:
        message = "Chill vibes only!"
    
    return base_code, message

selected_indices = list(map(int, sys.argv[1:]))
selected_items = [party_items[i] for i in selected_indices]

base_code = calculate_party_code(selected_indices)

final_code, message = adjust_party_code(base_code)

html_output = f"""
<html>
    <h1>Web Server 1</h1>
    <h1>Party Planner</h1>
    <h2>Selected Items:</h2>
    <p>{', '.join(selected_items)}</p>
    <h2>Base Party Code: {base_code}</h2>
    <h2>Adjusted Party Code: {final_code}</h2>
    <h2>Final Party Code: {final_code}</h2>
    <h3>Message: {message}</h3>
</html>
"""

# Print the result as HTML
print(html_output)

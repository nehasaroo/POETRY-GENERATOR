# --- Step 1: Get the Input Text from the User ---

print("--- Automated Found Poetry Generator ---")
print("Please paste the text you want to use for your poem.")
print("Press Enter twice when you are done (after an empty line).")

user_input_lines = []
while True:
    line = input()
    if not line: # An empty line (user pressed Enter twice)
        break
    user_input_lines.append(line)

input_text = "\n".join(user_input_lines) # Join the lines back into a single string

if not input_text.strip(): # Check if user input nothing substantial
    print("\nNo text provided. Using default sample text.")
    input_text = """
The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.

Stopping by Woods on a Snowy Evening by Robert Frost

Whose woods these are I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.

He gives his harness bells a shake
To ask if there is some mistake.
The only other sound's the sweep
Of easy wind and downy flake.

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
"""


print("\n--- Original Text (from your input or default) ---")
print(input_text)
print("-" * 25)

# --- Step 2: Split the Text into Lines ---

lines = [line.strip() for line in input_text.splitlines() if line.strip()]

# print("\n--- Split Lines (after stripping and filtering empty ones) ---")
# for i, line in enumerate(lines):
#     print(f"{i+1}: {line}")
# print("-" * 25)


# --- Step 3 & 4: Define Extraction Rules and Extract Lines (with user keywords) ---

print("\n--- Define Your Poetry Rules ---")
user_keywords_input = input("Enter keywords to find (separate with commas, e.g., snow, sleep, tree): ")

# Process the user's keywords: split by comma, remove extra spaces, convert to lowercase
keywords_to_find = [kw.strip().lower() for kw in user_keywords_input.split(',') if kw.strip()]

if not keywords_to_find:
    print("No keywords entered. Using default keywords: ['deep', 'shake', 'know']")
    keywords_to_find = ["deep", "shake", "know"] # Fallback if user enters nothing


print(f"\nSearching for lines containing: {', '.join(keywords_to_find)}")
print("--- Applying Rules and Extracting Lines ---")

found_poem_lines = []

for line in lines:
    line_lower = line.lower()
    for keyword in keywords_to_find:
        if keyword in line_lower:
            found_poem_lines.append(line)
            # Optional: print why the line was included for debugging/understanding
            # print(f"  - Found line: '{line}' (contains '{keyword}')")
            break # Move to the next line once a keyword is found
print("-" * 25)


# --- Step 5: Assemble the Poem ---

found_poem = "\n".join(found_poem_lines)


# --- Step 6: Display the Poem ---

print("\n\n--- Your Found Poem ---")
if found_poem:
    print(found_poem)
else:
    print("No lines found matching your criteria. Try different keywords or more text!")
print("\n" + "=" * 30)

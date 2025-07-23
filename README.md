# POETRY-GENERATOR
📜 Found Poetry Generator using Python
This project is a text-based poetry generator that creates a new poem by extracting lines from a user-provided paragraph, story, or any block of text, based on keywords entered by the user. It’s a fun, interactive Python tool that brings out poetic meaning from ordinary writing.

💡 How It Works
User inputs a paragraph, story, or any piece of text.

The user then provides keywords (e.g., “snow”, “sleep”, “tree”).

The program scans the text and extracts lines containing any of those keywords.

The result is a “found poem” — a poetic arrangement of meaningful lines filtered from the original text.

If the user provides no input or keywords, the program uses a default text (a poem by Robert Frost) and fallback keywords.

🧠 Example
User Input:

Text: (from Robert Frost)
The woods are lovely, dark and deep,  
But I have promises to keep,  
And miles to go before I sleep...
Keywords: deep, sleep

Generated Poem:

The woods are lovely, dark and deep,
And miles to go before I sleep,
And miles to go before I sleep.
✅ Features
Accepts multiline user input (like stories, essays, or articles).

Allows flexible keyword input to guide poem generation.

Intelligent filtering to find lines containing those keywords.

Uses a default poem if no input is given.

Fully implemented in basic Python — no external dependencies.



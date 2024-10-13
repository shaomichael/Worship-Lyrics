from itertools import groupby

def process_lyrics_dynamic_optimized(lyrics_text):
    # Split lyrics by paragraphs, ignoring only the first line (title)
    lyrics_paragraphs = [para.strip() for para in lyrics_text.split('\n\n')[1:] if para.strip()]  # read title of song
    
    # Dictionary to map unique groups of paragraphs to letter variables
    paragraph_to_letter = {}
    letter_sequence = []
    current_letter = ord('A')
    
    for para in lyrics_paragraphs:
        # Compare current paragraph with existing ones, it must be identical to use the same letter
        if para in paragraph_to_letter:
            letter_sequence.append(paragraph_to_letter[para])
        else:
            # Assign new letter if paragraph is unique
            letter = chr(current_letter)
            paragraph_to_letter[para] = letter
            letter_sequence.append(letter)
            current_letter += 1
    
    # First optimization: basic letter sequence
    basic_combined_sequence = ''.join(letter_sequence)
    
    # Second optimization: merge consecutive repeating segments, including patterns like ABAB -> [AB]x2
    optimized_combined_sequence = []
    i = 0
    while i < len(letter_sequence):
        pattern_len = 1
        # Check for repeating patterns in the sequence
        while i + pattern_len * 2 <= len(letter_sequence):
            pattern = letter_sequence[i:i + pattern_len]
            next_pattern = letter_sequence[i + pattern_len:i + pattern_len * 2]
            if pattern == next_pattern:
                optimized_combined_sequence.append(f"[{''.join(pattern)}]x2")
                i += pattern_len * 2
                break
            pattern_len += 1
        else:
            optimized_combined_sequence.append(letter_sequence[i])
            i += 1

    optimized_combined_sequence_str = ''.join(optimized_combined_sequence)
    
    # Prepare output
    output_lines = []
    title = lyrics_text.split('\n')[0]  # First line as the title (lyrics title)
    output_lines.append(f"Lyrics Title: {title}")
    
    output_lines.append("\nLetter Variables (Paragraphs):\n")
    for paragraph, letter in paragraph_to_letter.items():
        output_lines.append(f"{letter}:\n{paragraph}\n")
    
    # Output the basic letter pattern (first optimization)
    output_lines.append("\nBasic Letter Combination Pattern (First Optimization):\n")
    output_lines.append(basic_combined_sequence)
    
    # Output the fully optimized pattern (second optimization)
    output_lines.append("\nOptimized Letter Combination Pattern (Second Optimization):\n")
    output_lines.append(optimized_combined_sequence_str)
    
    # Save to file with utf-8 encoding to handle all characters
    file_name = f"{title}.txt"
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    return file_name, output_lines

# Function to capture lyrics input from the user
def capture_lyrics_input():
    print("Please input the full lyrics text (use double Enter to separate paragraphs):\n")
    lyrics_text = []
    while True:
        line = input()
        if line == "":
            if len(lyrics_text) > 0 and lyrics_text[-1] == "":
                break
            else:
                lyrics_text.append("")
        else:
            lyrics_text.append(line)
    return "\n".join(lyrics_text)

# Capture lyrics from user input
lyrics_text = capture_lyrics_input()

# Process the lyrics with optimized structure
if lyrics_text:
    file_name_dynamic_optimized, output_lines_dynamic_optimized = process_lyrics_dynamic_optimized(lyrics_text)

    # Print the optimized output for the provided lyrics
    for line in output_lines_dynamic_optimized:
        print(line)

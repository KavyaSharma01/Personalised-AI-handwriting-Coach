

def create_html(letter, prev_letter, next_letter):
    filename = f"{letter}.html"
    with open(filename, 'w') as file:
        file.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Letter {letter} Practice</title>
    <style>
        body, html {{
            height: 100%;
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #FFB6C1; /* Light pink background color */
            color: #333; /* Uniform text color */
        }}
        .wrapper {{
            display: flex;
            flex-direction: column;
            height: 100%;
        }}
        header {{
            text-align: center;
            padding: 20px;
            background: linear-gradient(145deg, #FFDAB9, #FFB6C1); /* Gradient header */
            border-bottom: 8px solid #FFDAB9; /* Enhanced peach border */
            box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Subtle shadow for depth */
        }}
        header h1 {{
            margin: 0;
            font-size: 2em; /* Larger font size for title */
        }}
        header p {{
            margin: 0;
            color: #666; /* Subdued color for subtitle */
        }}
        .content {{
            flex: 1;
            display: flex;
            justify-content: space-evenly;
            align-items: center;
            padding: 20px;
        }}
        .card {{
            background-color: #fff;
            border: 2px solid #FFDBAC; /* Consistent skin-colored border */
            box-shadow: 0px 8px 16px rgba(0,0,0,0.15); /* More prominent shadow */
            border-radius: 10px; /* Rounded corners */
            overflow: hidden; /* Ensures no content spills out */
            transition: transform 0.2s; /* Smooth transform on hover */
            width: 240px; /* Fixed width for consistent card size */
        }}
        .card:hover {{
            transform: scale(1.05); /* Slightly enlarges card on hover */
        }}
        .card video {{
            width: 100%; /* Ensures the video fills the card */
            border-radius: 10px; /* Rounded corners for the video */
        }}
        .practice-btn {{
            width: 100%;
            padding: 15px;
            background-color: #FFDBAC;
            color: black;
            font-weight: bold;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s; /* Smooth background color transition */
        }}
        .practice-btn:hover {{
            background-color: #ECCB94; /* Subtly change color on hover */
        }}
        .nav-btn {{
            padding: 10px 20px;
            background-color: #FFDBAC;
            color: black;
            font-weight: bold;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }}
        .nav-btn:hover {{
            background-color: #ECCB94;
        }}
        footer {{
            padding: 10px;
            background: #FFDAB9; /* Consistent footer background */
            display: flex;
            justify-content: center;
        }}
    </style>
</head>
<body>
    <div class="wrapper">
        <header>
            <h1>DYS-HAB</h1>
            <p>Let's know alphabets - Letter {letter}</p>
        </header>
        <div class="content">
            <div class="card">
                <video controls style="width:100%; height: auto;">
                    <source src="{letter}{letter}.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <button class="practice-btn">Practice "{letter}"</button>
            </div>
            <div class="card">
                <video controls style="width:100%; height: auto;">
                    <source src="lowercase_{letter.lower()}_video.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <button class="practice-btn">Practice "{letter.lower()}"</button>
            </div>
        </div>
        <footer>
            <a href="{prev_letter}.html" class="nav-btn">Previous</a>
            <a href="{next_letter}.html" class="nav-btn">Next</a>
        </footer>
    </div>
</body>
</html>""")
        print(f"Created {filename}")

def main():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(letters)):
        letter = letters[i]
        prev_letter = letters[i - 1] if i > 0 else letters[-1]
        next_letter = letters[(i + 1) % len(letters)]  # Wrap around using modulo
        create_html(letter, prev_letter, next_letter)

if __name__ == "__main__":
    main()

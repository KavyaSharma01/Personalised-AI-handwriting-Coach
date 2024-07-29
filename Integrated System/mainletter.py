<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learn Letters - Dysgraphia Rehabilitation System</title>
    <style>
        /* General reset and box-sizing */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #FFB6C1; /* Light pink background color */
            color: #333;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        h2 {
            color: #351834;
            margin-bottom: 20px;
        }

        .letter-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .letter-grid button {
            background-color: #fff;
            border: 2px solid #FFDBAC;
            margin: 5px;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 24px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.2s;
        }

        .letter-grid button:hover {
            background-color: #ECCB94;
            transform: translateY(-3px);
        }
    </style>
</head>
<body>
    <h2>Select a Letter to Learn</h2>
    <div class="letter-grid">
        <script>
            const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            const container = document.querySelector('.letter-grid');
            letters.split('').forEach(letter => {
                const button = document.createElement('button');
                button.textContent = letter;
                button.addEventListener('click', () => {
                    window.location.href = letter.toLowerCase() + '.html';
                });
                container.appendChild(button);
            });
        </script>
    </div>
</body>
</html>

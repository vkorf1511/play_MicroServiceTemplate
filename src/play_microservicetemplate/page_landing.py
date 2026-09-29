from fastapi.responses import HTMLResponse


def landing_page() -> HTMLResponse:
    return HTMLResponse(
        """<!doctype html>
<html lang="en">
<head>
    <link rel="stylesheet" href="../static/css/main_theme.css">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ef4b32">
    <title>Birthday Book</title>
</head>
<body>
    <main>
        <p class="eyebrow">A little something to celebrate</p>
        <h1>Welcome to Birthday Book</h1>
        <p class="intro">Add your birthday and keep your special day close at hand.</p>
        <form id="birthday-form">
            <label for="birthday">Your birthday</label>
            <div class="entry">
                <input id="birthday" name="birthday" type="date" placeholder="MM/DD/YYYY" autocomplete="bday" required>
                <button type="submit">Save birthday</button>
            </div>
            <p id="status" role="status" aria-live="polite"></p>
        </form>
    </main>
    <script src="../static/js/bday-saver.js" type="module"></script>
</body>
</html>"""
    )

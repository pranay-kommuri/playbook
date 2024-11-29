# Import necessary modules
import os

# Function to generate HTML content
def generate_html(sport_name, content, index):
    file_name = f"sport{index}.html"
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Read, Set, Go! | Playbook</title>
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="https://unpkg.com/boxicons@latest/css/boxicons.min.css">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.5.0/fonts/remixicon.css" rel="stylesheet"/>
</head>
<body>
    <div class="logo"><a href="#">PLAYBOOK</a></div>
    <header>
        <div class="emptyspace"></div>
        <div class="login">#</div>
    </header>

    <!-- NAVBAR -->
    <ul class="navbar">
        <li tooltip="Home"><a href="../index.html"><i class="ri-home-5-line"></i></a></li>
        <li tooltip="Explore"><a href="#"><i class="ri-compass-3-line"></i></a></li>
        <li tooltip="About"><a href="../index.html#about"><i class="ri-question-line"></i></a></li>
        <li tooltip="Contact"><a href="../index.html#contact"><i class="ri-customer-service-fill"></i></a></li>
        <li tooltip="Logout"><a href="../login.html"><i class="ri-login-box-line"></i></a></li>
    </ul>

    <!-- Content Section -->
    <div class="cont" style="background: url('../assets/sports/img{index}.jpg'), 
    linear-gradient(to top, black, #000000f0 30%, #00000020 80%), 
    linear-gradient(to right, #00000030, transparent 20%, transparent 80%, #00000030);
    background-blend-mode: overlay;">
        <p>explore > </p>
        <h1>{sport_name}</h1>
        <p>{content}</p>
    </div>
    <div class="simage" style="background-image: url('../assets/sports/img{index}.jpg');"></div>

    <script src="../js/script.js"></script>
</body>
</html>
'''
    # Write the HTML content to the file
    with open(file_name, 'w') as html_file:
        html_file.write(html_content)

    print(f"Created file: {file_name} for sport: {sport_name}")

# Read sports and content
with open('splist.txt', 'r') as sports_file:
    sports = sports_file.readlines()

with open('content.txt', 'r') as content_file:
    contents = content_file.readlines()

# Generate HTML files
for i, (sport, content) in enumerate(zip(sports, contents), start=1):
    sport_name = sport.strip()
    content_text = content.strip()
    
    # Generate HTML for each sport
    generate_html(sport_name, content_text, i)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Automatic Birthday Wisher</h1>

<h2>Overview</h2>
<p>Automatically send birthday wishes via email!</p>

<h2>Features</h2>
<ul>
    <li>Uses Python's <code>smtplib</code> module to send emails.</li>
    <li>Reads recipient details from a CSV file.</li>
    <li>Randomly selects a letter template for personalization.</li>
    <li>Customizable: Add more letter templates or recipient details as needed.</li>
</ul>

<h2>How to Use</h2>
<ol>
    <li>Ensure you have Python installed on your system.</li>
    <li>Clone this repository or download the script.</li>
    <li>Prepare your CSV file (<code>data.csv</code>) with recipient details (name, email, birthday).</li>
    <li>Customize your letter templates and place them in the <code>letter_templates</code> folder.</li>
    <li>Replace <code>"Your Email (sender mail id)"</code> and <code>"Password to the above mail id"</code> with your email credentials in the script.</li>
    <li>Run the script using Python.</li>
</ol>

<pre>
python automatic_birthday_wisher.py
</pre>

<li>Sit back and let the script automatically send birthday wishes!</li>

<h2>File Structure</h2>
<ul>
    <li><code>automatic_birthday_wisher.py</code>: Main Python script.</li>
    <li><code>data.csv</code>: CSV file containing recipient details.</li>
    <li><code>letter_templates/</code>: Folder containing letter templates.</li>
</ul>

<h2>Dependencies</h2>
<ul>
    <li>Python 3.x</li>
    <li>pandas</li>
    <li>smtplib (Standard Library)</li>
    <li>ssl (Standard Library)</li>
</ul>

<p>If you want to automate this code to run automatically using PythonAnywhere or crontab, you can contact the project owner for assistance.</p>

</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
<body>

<section>
    <h2>Description</h2>
    <p>This script is designed for performing a <strong>DDoS attack</strong> on a selected IP address using UDP packets. The program allows attacking a specific port or port range on the target machine with a specified number of threads and attack duration. This code is intended for demonstration and educational purposes, and it should not be used for any illegal or malicious activities.</p>

    <h3>Key Features:</h3>
    <ul>
        <li><strong>Target IP selection</strong>: The user inputs the IP address for the attack.</li>
        <li><strong>Port/port range selection</strong>: The user can specify a specific port or a port range for the attack.</li>
        <li><strong>Attack duration</strong>: The attack will continue for the specified duration.</li>
        <li><strong>Number of threads</strong>: The user can specify the number of parallel threads to speed up the attack.</li>
        <li><strong>Simple interface</strong>: Input through the console with validation and error handling.</li>
        <li><strong>Loading animation</strong>: Visual representation of the attack starting with an animation.</li>
        <li><strong>Error handling</strong>: The program safely handles interruption of the attack by the user and possible exceptions.</li>
    </ul>
</section>

<section>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>The <code>multiprocessing</code> module for multitasking.</li>
        <li>The <code>socket</code> module for network requests.</li>
        <li>The <code>random</code> module for generating random data.</li>
    </ul>
</section>

<section>
    <h2>Usage Instructions</h2>
    <p>Follow these steps to use the script:</p>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/yourusername/ddos-attack-simulator.git
cd ddos-attack-simulator</code></pre>
        </li>
        <li>Ensure you have Python 3 and all the necessary modules installed.</li>
        <li>Run the script:
            <pre><code>python3 attack_script.py</code></pre>
        </li>
        <li>Follow the instructions in the console for input:
            <ul>
                <li><strong>IP address</strong>: Enter the target IP.</li>
                <li><strong>Port/port range</strong>: Enter the port number or range (e.g., <code>1-80</code>).</li>
                <li><strong>Attack duration</strong>: Enter the attack duration in seconds.</li>
                <li><strong>Number of threads</strong>: Enter the number of parallel threads (1 to 100).</li>
            </ul>
        </li>
        <li>The program will start the attack, and you'll see information about the number of packets sent.</li>
    </ol>
</section>

<section>
    <h2>Sample Output</h2>
    <pre><code>Attack started: 2025-03-15 10:00:00
  BBBBB   EEEEE  TTTTTТТ   AAAA      DDDD    DDDD    OOO   SSSSS
  B    B  E         T     A    A     D   D   D   D   O   O  S
  BBBBB   EEEE      T     AAAAAA     D   D   D   D   O   O  SSSS
  B    B  E         T     A    A     D   D   D   D   O   O     S
  BBBBB   EEEEE     T     A    A     DDDD    DDDD    OOO   SSSSS

Author   : Adresatov
TEAM     : Collapse

Enter target IP address: 192.168.1.1
Enter port or port range (e.g., 1 or 1-80): 80
Enter attack duration in seconds: 60
Enter the number of threads (1-100): 10

Starting attack... | Attack initiated!
Sent 1000 packets to 192.168.1.1 via port 80
Sent 2000 packets to 192.168.1.1 via port 80
...
Attack finished!</code></pre>
</section>

<section>
    <h2>Explanation of the Code</h2>
    <p>1. <strong>Variables and settings</strong>: The code automatically determines the command to clear the screen based on the operating system (Windows or Linux/Mac).</p>
    <p>2. <strong>Data input</strong>: The program asks the user for the IP address, ports, attack duration, and number of threads.</p>
    <p>3. <strong>Loading animation</strong>: A loop with animation is used to visually represent the start of the attack.</p>
    <p>4. <strong>Main attack logic</strong>: The <code>multiprocessing</code> module is used for multitasking to parallelize the attack process and speed up execution.</p>
</section>

<section>
    <h2>Security Notes</h2>
    <div class="note">
        <p class="important">Make sure to use this script only for testing and educational purposes.</p>
        <p><strong>Performing DDoS attacks against unauthorized systems is a criminal offense.</strong> The code is provided solely for educational purposes and for testing on your own systems.</p>
    </div>
</section>

</body>
</html>

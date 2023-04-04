# PythonWebScraping
I've created this small project just to initialize myself with Python and Web Scraping.

I'm not used to it, so thats the reason I've created a bash script to execute the python code and prettify the output.

This only works for the following page of HackerRank, but you can adapt it to your necessities.

https://www.hackerrank.com/contests/dam-m3/compare/jolivera1

It tells you the exercises unfinished at the contest of HackerRank.

## License
This repository is licensed under the Creative Commons Attribution-ShareAlike (CC-BY-SA) license. This means that you are free to use, share, and modify the code and any derivative works, as long as you give credit to the original creator and share any derivative works under the same license.

### Attribution Requirements
If you use this code in your own work, please provide a clear attribution to the original creator and a link back to this repository.

### Share-Alike Requirements
If you create derivative works based on this code, you must share them under the same CC-BY-SA license.

### Questions
If you have any questions about this license or would like to discuss using this code in a different way, please contact me at "joel10olor@gmail.com".

## Usage
It's easy to use this script, you just have to navigate to the folder where is located the ".sh" file and run it using **./DidNotAttempt.sh** on the terminal.

## How it works
### Python File
This Python code uses the Selenium WebDriver API to automate browser actions. 
Specifically, it opens the Firefox browser in headless mode (to avoid opening new windows), 
navigates to a URL, waits for the page to load, takes a screenshot, 
and then prints out the page's HTML code to the console.

The code needs to import the following libraries:  
- webdriver from selenium 
- Options from selenium.webdriver.firefox.options (**you can change it to your prefered browser**) 
- time

Then, it creates an instance of Options and sets the headless property to True to run Firefox in headless mode.

The driver navigates to the specified URL, and the script waits for five seconds using the time.sleep() method.
This is necessary to allow the page to load before any other actions are taken.

Next, I've left commented code to in case, take a screenshot of the webpage and saved it as a .png file. 

Finally, the script prints out the HTML of the webpage to the console using the execute_script() method of the driver. 

**Remember that the driver must be closed after finalising using driver.close()**.

### Bash script
This Bash script executes the Python script and then filters and processes the output using various command-line utilities.

First, it runs the Python script using the /bin/python3 interpreter. 
The output of the script is then piped (|) to the grep command with two search patterns using the -e option. 
The first pattern matches any string that starts with 0. followed by two digits (for example, 0.45) and the second pattern matches any string that contains the text "Did Not Attempt".

The grep command with the -B option prints out not only the matching lines but also the 11 lines before each match.

The output of the previous grep command is then piped to another grep command, which extracts the URLs from the output using a regular expression. The -oP option enables Perl-compatible regular expressions and the '\K' expression is used to reset the starting point of the match, so that only the URL is printed.

The output of the second grep command is then piped to the awk command, which separates the URL into fields using the / character as a delimiter. It then prints out the 7th field (which should contain the name) and the full URL. The awk command also adds a separator line using the print command.

Finally, the output is piped to the less command, which displays the output one page at a time for easier reading.
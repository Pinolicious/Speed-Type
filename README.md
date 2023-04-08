    # Speed Typing Test
    #### Video Demo:  https://youtu.be/zmB2lLhjelQ
    #### Description:
    Hello everyone

    My name is Darren, from Auckland, New Zealand

    This is my introduction to Programming with Python, Final Project

    I've always been a fan of typing, and recently discovered the world of custom mechanical keyboards
    I sometimes frequent the website TypeRacer, so I wanted to recreate a speed typing test in Python

    The program uses curses, to overlay on top of the terminal, and give coloured text font, to try
    and highlight correctly, and incorrectly, matching characters.

    There is a words per minute counter, that calculates your current words per minute.

    Once you've typed the the full text quote, the program will pause, showing your words per minute,
    and you can either press any key to start a new test, or press 'esc' to exit the program.

    Some of the issues I had was trying to implement back space. Because of the way I programmed
    the 'esc' key to quit the program, it would cause an error when you pressed back space.

    Another issue was trying to get it to recognise certain capital letters on the first character

    The unit test took a lot of work. Testing for load_text() returning a random value, required me to
    write the test in a way that, it would pass a specific seed into Random(), which would force it to
    return the same value each time. That allowed me to write a self assert test, with diferent random
    seeds to test with.

    This has been a fun and challenging course for me. I look forward to writing more projects in Python.
    To apply what I've learnt in my every day, and hopefully start building bigger and more feature rich
    programs.

    Thank you for your time, stay safe out there
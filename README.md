# Medley Relay Optimizer:

This Python program uses sqlite3 to manage a database of swimmers and their individual stroke times. It automatically sorts swimmers into age/gender-specific tables and computes the fastest possible combination of swimmers for a medley relay. The relay includes one swimmer each for backstroke, breaststroke, butterfly, and freestyle—ensuring each swimmer is unique and only fills one stroke.



# Features:

Add and organize swimmers by age, gender, and name

Automatically stores times for all four strokes (free, back, breast, fly)

SQLite3-powered backend for persistent, structured data

Finds the fastest legal medley relay combination (no duplicate swimmers)

Works for any age/gender group stored in the database



# How it Works:

Swimmers are entered into a database table named by age and gender (e.g., ninetenmale).

Each swimmer record includes:

fname, lname (first and last name)

free_time, back_time, breast_time, fly_time

absent (optional flag for availability)

The program evaluates all possible combinations of 4 different swimmers, one per stroke.

It calculates the total relay time for each valid combination and returns the fastest one.



# Technologies Used:

Python 3

SQLite3

Tkinter (optional) for GUI interaction (if applicable)

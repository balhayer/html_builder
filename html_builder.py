"""
File: html_builder.py
Description: This program builds a website with user input.
Language: Python 3.7.4
Author: Vishnu Muthuswamy
"""
import cs_queue
import wizard_mode
import website_mode
import style_color_information
import sys


# Constants
BACKGROUND_COLOR = "@BACKCOLOR"
TEXT_FONT = "@FONTSTYLE"
PARAGRAPH_TEXT_COLOR = "@FONTCOLOR"
HEADING_COLOR = "@HEADCOLOR"


def create_style_sheet():
    """
    Description: This function goes through the style sheet and changes the color settings represented by the
    constants above to user defined values.
    Preconditions: The style sheet style_color_information should be used.
    Postconditions: Style_color_information sheet with user defined values.
    :return: Style_color_information sheet with user defined values.
    """
    with open("style_template.txt") as file:
        style_sheet = ""
        user_background_color = style_color_information.assign_background_color()
        user_text_font = style_color_information.assign_text_font()
        user_paragraph_text_color = style_color_information.assign_paragraph_text_color()
        user_heading_color = style_color_information.assign_heading_color()
        for line in file:
            line = line.replace(BACKGROUND_COLOR, user_background_color)
            line = line.replace(TEXT_FONT, user_text_font)
            line = line.replace(PARAGRAPH_TEXT_COLOR, user_paragraph_text_color)
            line = line.replace(HEADING_COLOR, user_heading_color)
            style_sheet += line
    return style_sheet


def create_website_data_structure():
    """
    Description: This function stores the website's HTML code in a queue.
    Preconditions: The value returned by the creat_style_sheet function must be used for
    the style sheet.
    Postconditions: The website's HTML code in a queue.
    :return: The website's HTML code in a queue.
    """
    queue = cs_queue.make_empty_queue()
    arguments = len(sys.argv) - 1
    if arguments > 0:
        website_mode.create_website_data_structure(sys.argv, queue)
    else:
        cs_queue.enqueue(queue, "<!DOCTYPE html>")
        cs_queue.enqueue(queue, "<html>")
        cs_queue.enqueue(queue, "<head>")
        title, inputted_title = wizard_mode.create_title()
        cs_queue.enqueue(queue, title)
        cs_queue.enqueue(queue, create_style_sheet())
        cs_queue.enqueue(queue, "</head>")
        cs_queue.enqueue(queue, "<body>")
        wizard_mode.create_body(inputted_title, queue)
        cs_queue.enqueue(queue, "</body>")
        cs_queue.enqueue(queue, "</html>")

    return queue

def main():
    """
    Description: This function writes all of the code in the queue returned by create_website_data_structure
    into a file called index.html, which is stored in this program's directory.
    """
    queue = create_website_data_structure()
    arguments = len(sys.argv) - 1
    if arguments > 0:
        filename = sys.argv[1]
        filename = filename.replace(".txt", ".html")
        with open(filename, "w") as file:
            while queue.front != None:
                print(queue.front.contents, file=file)
                cs_queue.dequeue(queue)

    else:
        with open("index.html", "w") as file:
            while queue.front != None:
                print(queue.front.contents, file=file)
                cs_queue.dequeue(queue)

main()
"""
File: website_mode.py
Description: This program takes a text file and turns it into html code.
Language: Python 3.7.4
Author: Vishnu Muthuswamy
"""
import cs_queue
import html_builder


def create_website_data_structure(arguments, queue):
    """
    Description: This function creates a HTML data structure from a text file inputted.
    """
    if arguments == 1:
        cs_queue.enqueue(queue, "<!DOCTYPE html>")
        cs_queue.enqueue(queue, "<html>")
        cs_queue.enqueue(queue, "<head>")
        with open(arguments[1], "r") as file:
            line = file.readline()
            title = line
            title_in_html_head = "<title>" + "\n" + title + "\n" + "</title>"
            cs_queue.enqueue(queue, title_in_html_head)
            style_sheet = html_builder.create_style_sheet()
            cs_queue.enqueue(queue, style_sheet)
            cs_queue.enqueue(queue, "</head>")
            cs_queue.enqueue(queue, "<body>")
            title_in_html_body = "<h1>" + "\n" + title + "\n" + "</h1>"
            cs_queue.enqueue(queue, title_in_html_body)
            line = file.readline()
            while line == "!new_paragraph" or line == "\n":
                line = file.readline()
                if line[0: 7] == "!title":
                    line = line.split()
                    paragraph_title = ""
                    for index in range(1, len(line)):
                        paragraph_title += line[index]
                    paragraph_title_in_html = "<h2>" + paragraph_title + "</h2>"
                    cs_queue.enqueue(queue, paragraph_title_in_html)
                    line = file.readline()
                    paragraph = ""
                    while line != "!new_paragraph" or line[0: 7] != "!image" or line != "":
                        paragraph += line
                        line = file.readline()
                    if paragraph != "":
                        paragraph_in_html = "<p>" + "\n" + paragraph + "\n" + "</p>"
                        cs_queue.enqueue(queue, paragraph_in_html)
                    while line[0: 7] == "!image" or line == "\n":
                        line = line.split()
                        if len(line) == 3:
                            image_in_html = "<image src='" + line[1] + "' width='" + line[2] + "' class='center'>"
                            cs_queue.enqueue(queue, image_in_html)
                        elif len(line) == 1:
                            image_in_html = "<image src='" + line[1] + "' class='center'>"
                            cs_queue.enqueue(queue, image_in_html)
                        line = file.readline()
                else:
                    if line[0: 7] == "!title":
                        print("Error: missing !new_paragraph keyword before !title keyword.")
                        return None
                    elif len(line) > 0:
                        print("Error: missing !title keyword before the text on the current line.")
                        return None
                    elif line[0: 7] == "images":
                        print("Error: missing !image keyword.")
                        return None
                    elif line[0] == "!" and len(line) > 15:
                        print("Error: !new_paragraph should not have additional text on its line.")
                        return None

        cs_queue.enqueue(queue, "</body>")
        cs_queue.enqueue(queue, "</html>")

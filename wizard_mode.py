"""
File: wizard_mode.py
Description: This program takes user input to build a website.
Language: Python 3.7.4
Author: Vishnu Muthuswamy
"""


import cs_queue


def create_title():
    """
    Description: This function returns the title of the website according to user input.
    :return: User-defined title for website.
    """
    title = "<title>" + "\n"
    inputted_title = input("What is the title of your website? ")
    title += inputted_title + "\n" + "</title>"
    return title, inputted_title


def create_body(title, queue):
    """
    Description: This function creates the body of the website in a queue using user input.
    :return: User-defined queue for the body of the website.
    """
    title = "<h1>" + "\n" + title + "\n" + "</h1>"
    cs_queue.enqueue(queue, title)
    paragraph_title = "<h2>" + "\n"
    inputted_paragraph_title = input("Title of your paragraph: ")
    paragraph_title += inputted_paragraph_title + "\n" + "</h2>"
    cs_queue.enqueue(queue, paragraph_title)
    paragraph = "<p>" + "\n"
    inputted_paragraph = input("Content of your paragraph (single line)" + "\n")
    paragraph += inputted_paragraph + "\n" + "</p>"
    cs_queue.enqueue(queue, paragraph)
    response_for_image = input("Do you want to add an image? [yes] ")
    while response_for_image == "yes" or response_for_image is "":
        image = "<img src='"
        inputted_image = input("Image file name: ")
        image += inputted_image + "' width='30\%'>"
        cs_queue.enqueue(queue, image)
        response_for_image = input("Do you want to add another image? [yes] ")
    response_for_paragraph = input("Do you want to add another paragraph to your website? [yes] ")
    while response_for_paragraph == "yes" or response_for_paragraph is "":
        paragraph_title = "<h2>" + "\n"
        inputted_paragraph_title = input("Title of your paragraph: ")
        paragraph_title += inputted_paragraph_title + "\n" + "</h2>"
        cs_queue.enqueue(queue, paragraph_title)
        paragraph = "<p>" + "\n"
        inputted_paragraph = input("Content of your paragraph (single line)" + "\n")
        paragraph += inputted_paragraph + "\n" + "</p>"
        cs_queue.enqueue(queue, paragraph)
        response_for_image = input("Do you want to add an image? [yes] ")
        while response_for_image == "yes" or response_for_image is "":
            image = "<img src='"
            inputted_image = input("Image file name: ")
            image += inputted_image + "' class='center'>"
            cs_queue.enqueue(queue, image)
            response_for_image = input("Do you want to add another image? [yes] ")
        response_for_paragraph = input("Do you want to add another paragraph to your website? [yes] ")







    




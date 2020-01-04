"""
File: style_color_information.py
Description: This program assigns specific color settings for a website's style sheet using user input.
Language: Python 3.7.4
Author: Vishnu Muthuswamy
"""

import turtle

#Python colors sets for possible color names and hex values
colors = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen', 'lawngreen',
          'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen', 'chocolate',
          'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred', 'bisque',
          'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred', 'antiquewhite', 'royalblue', 'yellow', 'indigo',
          'lightcoral', 'darkslategrey', 'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki', 'darkviolet',
          'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise', 'lightyellow', 'grey', 'whitesmoke', 'blueviolet',
          'orchid', 'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen', 'gainsboro', 'darkorange',
          'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen', 'darkred', 'dimgray', 'floralwhite',
          'orangered', 'oldlace', 'darksalmon', 'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver',
          'tomato', 'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose',
          'lime', 'saddlebrown', 'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue',
          'darkgoldenrod', 'palevioletred', 'fuchsia', 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen',
          'aquamarine', 'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown', 'springgreen', 'purple',
          'olivedrab', 'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy', 'salmon', 'rebeccapurple',
          'darkmagenta', 'limegreen', 'deepskyblue', 'pink', 'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey',
          'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise', 'brown', 'thistle', 'lemonchiffon', 'peru',
          'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow', 'mediumturquoise', 'steelblue', 'lightgray',
          'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite', 'dodgerblue', 'greenyellow',
          'dimgrey', 'darkorchid'}
hex_letters = {'a', 'b', 'c', 'd', 'e', 'f'}
hex_numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def assign_background_color():
    """
    Description: This function creates the background color for a website using user input.
    :return: Background color of website.
    """
    print("Background Color")
    background_color = input("Choose the name of a color, or in format '#XXXXXX': ")
    while True:
        while True:
            if background_color.lower() not in colors:
                if background_color[0] is '#':
                    if background_color[1].lower() in hex_letters or background_color[1] in hex_numbers:
                        if background_color[2].lower() in hex_letters or background_color[2] in hex_numbers:
                            if background_color[3].lower() in hex_letters or background_color[3] in hex_numbers:
                                if background_color[4].lower() in hex_letters or background_color[4] in hex_numbers:
                                    if background_color[5].lower() in hex_letters or background_color[5] in hex_numbers:
                                        return background_color
                                    else:
                                        print("Illegal format")
                                        background_color = input("Choose the color name or #XXXXXX: ")
                                        break
                                else:
                                    print("Illegal format")
                                    background_color = input("Choose the color name or #XXXXXX: ")
                                    break
                            else:
                                print("Illegal format")
                                background_color = input("Choose the color name or #XXXXXX: ")
                                break
                        else:
                            print("Illegal format")
                            background_color = input("Choose the color name or #XXXXXX: ")
                            break
                    else:
                        print("Illegal format")
                        background_color = input("Choose the color name or #XXXXXX: ")
                        break
                else:
                    print("Illegal format")
                    background_color = input("Choose the color name or #XXXXXX: ")
                    break
            else:
                return background_color


def font_options():
    """
    Description: Returns user's font options for website.
    """
    turtle.hideturtle()
    turtle.up()
    turtle.write("Arial", font=("Arial", 14, "normal"))
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.write("Comic Sans MS", font=("Comic Sans MS", 14, "normal"))
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.write("Lucida Grande", font=("Lucida Grande", 14, "normal"))
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.write("Tahoma", font=("Tahoma", 14, "normal"))
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.write("Verdana", font=("Verdana", 14, "normal"))
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.write("Helvetica", font=("Helvetica", 14, "normal"))
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.write("Times New Roman", font=("Times New Roman", 14, "normal"))
    turtle.done()


def choose_text_font():
    """
    Description: Returns user's selection interface for paragraph text font.
    """
    font_choice = input("Choose a font by its number." + "\n" +
                   "0: Arial, size 14" + "\n" +
                   "1: Comic Sans MS, size 14" + "\n" +
                   "2: Lucida Grande, size 14" + "\n" +
                   "3: Tahoma, size 14" + "\n" +
                   "4: Verdana, size 14" + "\n" +
                   "5: Helvetica, size 14" + "\n" +
                   "6: Times New Roman, size 14" + "\n" +
                   ">> ")
    font_choice_numbers = {"0": "arial", "1": "comic sans ms" , "2": "lucida grande", "3": "tahoma", "4": "verdana",
                           "5": "helvetica", "6": "times new roman"}

    while True:
        if font_choice in font_choice_numbers:
            return font_choice_numbers[font_choice]
        else:
            print("Illegal format")
            font_choice = input("Choose a font by its number." + "\n" +
                                "0: Arial, size 14" + "\n" +
                                "1: Comic Sans MS, size 14" + "\n" +
                                "2: Lucida Grande, size 14" + "\n" +
                                "3: Tahoma, size 14" + "\n" +
                                "4: Verdana, size 14" + "\n" +
                                "5: Helvetica, size 14" + "\n" +
                                "6: Times New Roman, size 14" + "\n" +
                                ">> ")


def assign_text_font():
    """
    Description: Returns user's paragraph text font option.
    """
    print("You will now choose a font.")
    displayed_font_options = input("Do you want to see what the fonts look like? [yes] ")

    if displayed_font_options is "" or displayed_font_options.lower() == "yes":
        print("Close the window when you have made your choice.")
        font_options()
        font = choose_text_font()
        return font
    else:
        font = choose_text_font()
        return font


def assign_paragraph_text_color():
    """
    Description: Returns user's paragraph text color option.
    """
    print("Paragraph Text Color")
    paragraph_text_color = input("Choose the name of a color, or in format '#XXXXXX': ")
    while True:
        while True:
            if paragraph_text_color.lower() not in colors:
                if paragraph_text_color[0] is '#':
                    if paragraph_text_color[1].lower() in hex_letters or paragraph_text_color[1] in hex_numbers:
                        if paragraph_text_color[2].lower() in hex_letters or paragraph_text_color[2] in hex_numbers:
                            if paragraph_text_color[3].lower() in hex_letters or paragraph_text_color[3] in hex_numbers:
                                if paragraph_text_color[4].lower() in hex_letters or paragraph_text_color[4] in hex_numbers:
                                    if paragraph_text_color[5].lower() in hex_letters or paragraph_text_color[5] in hex_numbers:
                                        return paragraph_text_color
                                    else:
                                        print("Illegal format")
                                        paragraph_text_color = input("Choose the color name or #XXXXXX: ")
                                        break
                                else:
                                    print("Illegal format")
                                    paragraph_text_color = input("Choose the color name or #XXXXXX: ")
                                    break
                            else:
                                print("Illegal format")
                                paragraph_text_color = input("Choose the color name or #XXXXXX: ")
                                break
                        else:
                            print("Illegal format")
                            paragraph_text_color = input("Choose the color name or #XXXXXX: ")
                            break
                    else:
                        print("Illegal format")
                        paragraph_text_color = input("Choose the color name or #XXXXXX: ")
                        break
                else:
                    print("Illegal format")
                    paragraph_text_color = input("Choose the color name or #XXXXXX: ")
                    break
            else:
                return paragraph_text_color


def assign_heading_color():
    """
    Description: Returns user's heading color option.
    """
    print("Heading Color")
    heading_color = input("Choose the name of a color, or in format '#XXXXXX': ")
    while True:
        while True:
            if heading_color.lower() not in colors:
                if heading_color[0] is '#':
                    if heading_color[1].lower() in hex_letters or heading_color[1] in hex_numbers:
                        if heading_color[2].lower() in hex_letters or heading_color[2] in hex_numbers:
                            if heading_color[3].lower() in hex_letters or heading_color[3] in hex_numbers:
                                if heading_color[4].lower() in hex_letters or heading_color[4] in hex_numbers:
                                    if heading_color[5].lower() in hex_letters or heading_color[5] in hex_numbers:
                                        return heading_color
                                    else:
                                        print("Illegal format")
                                        heading_color = input("Choose the color name or #XXXXXX: ")
                                        break
                                else:
                                    print("Illegal format")
                                    heading_color = input("Choose the color name or #XXXXXX: ")
                                    break
                            else:
                                print("Illegal format")
                                heading_color = input("Choose the color name or #XXXXXX: ")
                                break
                        else:
                            print("Illegal format")
                            heading_color = input("Choose the color name or #XXXXXX: ")
                            break
                    else:
                        print("Illegal format")
                        heading_color = input("Choose the color name or #XXXXXX: ")
                        break
                else:
                    print("Illegal format")
                    heading_color = input("Choose the color name or #XXXXXX: ")
                    break
            else:
                return heading_color
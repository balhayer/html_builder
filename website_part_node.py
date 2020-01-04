"""
File: website_part_node.py
Description: The node used for the HTML data structure queue.
Language: Python 3.7.4
Author: Vishnu Muthuswamy
"""
from dataclasses import dataclass
from typing import Any, Union


@dataclass
class Node:
    contents: Any
    rest: Union[None, 'Node']

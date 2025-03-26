from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if re.search(r"#{1,6} .", block):
        return BlockType.HEADING
    elif re.search(r"^```.*```$", block):
        return BlockType.CODE
    elif re.search(r"^>", block):
        return BlockType.QUOTE
    elif re.search(r"^-\s", block):
        return BlockType.UNORDERED_LIST
    elif re.search(r"^\d+\.\s", block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    new_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block:  # Only append if non-empty after stripping
            new_blocks.append(block.strip())
    
    return new_blocks


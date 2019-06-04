# !/usr/bin/python
import numpy as np

const numbers = [x for x in range(10)] # list of numbers 1-9 
const s = 3                            # 3 is used multiple times for breaking down the puzzle



# A block in Sudoku refers to one of the nine 3x3 matrices 
# within the puzzle's 9x9 matrix. 
# These blocks must contain the numbers 1-9.
# Numbers can only occur once inside a block. 

class Block:
    def __init__(self, position):
        self.nums_left = global numbers    # Blocks start with list of numbers 1-9
        self.pos = position                # The position of this block in the overall sudoku puzzle
        self.matrix = np.zeros((3,3))      # creates empty 3x3 matrix to input into

    # Removes a number from the list of remaining numbers
    def remove(self, num):
        self.remove(num)
    
    # Adds a number to the list of remaining numbers
    def add(self, num):
        self.append(num)
        self.sort()

    def check_validity(self):
        used_numbers = list()                   # creates empty list to account for numbers in block
        for i in range(3):
            for j in range(3):
                if (self.matrix[i][j] == 0):    # if an element is 0 then essentially its nothing
                    pass                        # a number has not be inputted here
                else:
                    used_numbers.append(self.matrix[i][j]) # add number to list
                    
        used_numbers.sort()                     # sorts the list into numerical order
        
        # This checks the list for multiple numbers within block 
        for i in range(len(used_numbers)-1):    
            if (used_numbers[i] == used_numbers[i+1])   # compares number to the right of it
                return False
            else:
                pass
        return True
        
        
class Sudoku_Puzzle:
    def __init__(self):
        self.puzzle_board = None
        





# Creates the Sudoku Puzzle
def Create_Puzzle():


# Searches puzzle
def Search_Puzzle(puzzle):


# Splits the Sudoku Puzzle into 9 blocks (3x3 matrix by 3x3 matrix == 3x3x3x3 == 81)
# blocks is a 3x3x3x3 matrix
def Split_Blocks(puzzle):
    blocks = np.zeros((3,3,3,3))
    
    
    
    return blocks


# Updates the remaining numbers in a Block
def Block_Numbers_Remaininig(block):
    nums2remove = list()                # list for removing numbers
    
    # Iterating through remaining numbers to remove numbers already in puzzle block
    for i in range(len(block.nums_left)):
        for j in range(global s):
            for k in range(global s):
                if (block_nums[i] == block[i][j]):
                    nums2remove.append(block_nums[i])   # adding to list to remove later
    
        
        
                    
                
                
def








def main():










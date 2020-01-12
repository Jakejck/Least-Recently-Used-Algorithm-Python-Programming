
# LRU Instruction :

## How to use it 

You can use it in python or in a jupyternote book.

It is easy to use the Anconda environment.


## Explanation

### Design

Used data structure: **DoublyLinkedlist and Dictionary**.
    
Because the LRU cache need to delete the least used data while the datas in cache are over capacity, we build the doublylinkedlist to track the least used data.

In the logic of the doublylinkedlist, the least linked list will be the tail one. So if the datas are over capacity, we will delete the tail one.

### Time complexities

we used the dictionary to meet the purpose that the time of complexity is O(1) when looking up the value in the LRU cache.

### Space complexities 

Space complexities is O(2n) that 1n is stored for dictionary and 1n is stored for doublylinkedlist.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:15:36 2019

@author: jake
"""
class DoubleNode:
    def __init__(self,value = None):
        self.value  = value
        self.next = None
        self.previous = None
        
        
class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_element = 0 

    def append(self,value):
        if self.head is None:
            self.head =  DoubleNode(value)
            self.tail = self.head
            self.num_element +=1

        else:
            if self.lookup(value) is None:
                transition = self.head
                self.head = DoubleNode(value)
                transition.previous = self.head
                self.head.next = transition
                self.num_element +=1
            else:
                transition = self.lookup(value)
                if transition == self.tail:
                    self.tail = transition.previous
                    transition = self.head
                    self.head = DoubleNode(value)
                    transition.previous = self.head
                    self.head.next = transition
                elif transition == self.head:
                    self.head = transition
                else: 
                    transition.previous.next = transition.next
                    transition.next.previous = transition.previous
                    transition_2 = self.head
                    self.head = DoubleNode(value)
                    transition_2.previous = self.head
                    self.head.next = transition_2  


    def lookup(self,value):
        if self.head is None:
            return None
        else:
            transition = self.head
            while transition:
                if transition.value == value:
                    return transition
                    break
                transition = transition.next
            return None

    def del_tail(self):
       if self.head ==self.tail:
           self.head = None
           self.tail = None
       else:
           self.tail = self.tail.previous
       self.num_element -=1
       


class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.ddlist = DoublyLinkedlist()

    
    def get(self,key):
        if key in self.dict.keys():
            self.ddlist.append(self.dict[key])
            return self.dict[key]
        else:
            return -1

    def set(self,key,value):
        if self.capacity == 0 : 
            print ("can't perform operations on 0 capacity cache")
        else:
            if self.ddlist.num_element == self.capacity:
                tail_key = list(self.dict.keys())[list(self.dict.values()).index(self.ddlist.tail.value)]
                self.ddlist.del_tail()
                del self.dict[tail_key]
                self.ddlist.append(value)
                self.dict[key] = self.ddlist.head.value
            else:
                self.ddlist.append(value)
                self.dict[key] = self.ddlist.head.value
            
            

"""
Test the code in the below

"""

"""
First test case
"""
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 


"""
Second test case
"""

our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

"""
Third test case
"""

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some warning message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1


# -*- coding: utf-8 -*-
"""
Задача 4:
Реализуйте двусвязный список используя синтаксис языка Python. Вам необходимо создать класс (либо несколько классов), который (которые) будет (будут) представлять структуру данных - связный список.
Связный список — это набор элементов данных, называемых узлами. В односвязном списке каждый узел содержит значение и ссылку на следующий узел. В двусвязном списке каждый узел также содержит ссылку на предыдущий узел.
Реализуйте узел для хранения значения и указателей на следующий и предыдущий узлы. 
Затем реализуйте список, который содержит ссылки на первый и последний узел и предлагает интерфейс, подобный массиву, для добавления и удаления элементов, какие методы должны быть реализованы:
push() - записывает значение в конец списка
pop() - удаляет значение с конца списка
shift() - удаляет значение в начале списка
unshift() - записывает значение в начало списка
"""

class List:
    def __init__(self, value, prev=None, next=None):
        self.value = value  
        self.next = next    
        self.prev = prev    
    
    def __str__(self):
        return str(self.value) 
        
class DoublyLinkedList:
        first = None  
        last = None  
        length = 0

        def __str__(self):
            st = ''
            i = self.first
            while i:
                st += str(i) + ' ' 
                i = i.next
            return st.rstrip()
        
        def push(self, value):
            if self.first is None:
                l = List(value)
                self.first = l
                self.last = l
            else:
                l = List(value, prev=self.last)
                self.last.next = l
                self.last = l
            self.length += 1

        def pop(self):
            if self.last is None:  
                return None
            p = self.last
            if self.length == 1:  
                self.first = None
                self.last = None
            else:
                self.last = p.prev
                self.last.next = None
                p.prev = None
            self.length -= 1
            return p.value
        
        def shift(self):
            if self.first is None: 
                return None
            sh = self.first
            if self.length == 1: 
                self.first = None
                self.last = None
            else:
                self.first = sh.next
                self.first.prev = None
                sh.next = None  
            self.length -= 1
            return sh.value

        def unshift(self, value):
            n = List(value)
            if not self.first:  
                self.first = n
                self.last = n
            else:
                n.next = self.first
                self.first.prev = n
                self.first = n
            self.length += 1

"""
dll = DoublyLinkedList()
dll.push(1)
dll.push(2)
dll.push(3)
dll.pop() 
dll.pop() 
dll.unshift(0)
dll.shift()
print(dll)
"""

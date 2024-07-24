class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
   
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
   
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def sort_ascending(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            sorted_list.insert_sorted(current.data, ascending=True)
            current = current.next
        return sorted_list

    def sort_descending(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            sorted_list.insert_sorted(current.data, ascending=False)
            current = current.next
        return sorted_list

    def insert_sorted(self, data, ascending=True):
        new_node = Node(data)
        if not self.head or (ascending and self.head.data >= new_node.data) or (not ascending and self.head.data <= new_node.data):
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and ((ascending and current.next.data < new_node.data) or (not ascending and current.next.data > new_node.data)):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

ll = LinkedList()
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for number in numbers:
    ll.append(number)

print("Original List:", ll.traverse())

sorted_ll_asc = ll.sort_ascending()
print("Sorted List Ascending:", sorted_ll_asc.traverse())

sorted_ll_desc = ll.sort_descending()
print("Sorted List Descending:", sorted_ll_desc.traverse())

search_number = 5
is_present = ll.search(search_number)
print(f"Number {search_number} is present in the list: {is_present}")

search_number = 7
is_present = ll.search(search_number)
print(f"Number {search_number} is present in the list: {is_present}")